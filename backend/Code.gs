/**
 * TIẾNG ANH GIAO TIẾP FOUNDATION — Homework backend (Google Apps Script)
 * --------------------------------------------------------------------
 * Gắn vào 1 Google Sheet (Tiện ích mở rộng → Apps Script), dán toàn bộ file này,
 * rồi Deploy → New deployment → Web app (Execute as: Me · Who has access: Anyone).
 *
 * Các tab được tạo tự động ở lần chạy đầu:
 *   Students     — danh sách học viên (tự đăng ký bằng tên + email)
 *   Submissions  — mỗi lần nộp bài là 1 dòng; thầy chấm ở cột "Teacher score" / "Teacher feedback" / "Status"
 *   Homework     — thầy tự thêm / sửa câu hỏi cho từng buổi (tuỳ chọn)
 * File voice note được lưu trong Google Drive, thư mục "GIAO TIEP FOUNDATION - Voice notes".
 */

var VERSION = 1;
var VOICE_FOLDER = 'GIAO TIEP FOUNDATION - Voice notes';
var MAX_VOICE_BYTES = 15 * 1024 * 1024;

var HEADERS = {
  Students: ['Email', 'Name', 'First seen', 'Last seen'],
  Submissions: ['Timestamp', 'Email', 'Name', 'Session', 'Attempt', 'Auto score', 'Auto max', 'Auto %',
                'Written answers', 'Voice notes', 'Status', 'Teacher score', 'Teacher feedback', 'Details (JSON)'],
  Homework: ['Session', 'QID', 'Section', 'Type', 'Prompt', 'Options (a | b | c)', 'Answer (đáp án | đáp án khác)',
             'Audio URL', 'Points', 'Active']
};
var PASS_PCT = 80;
var STATUS_PASSED = 'Đạt';
var STATUS_FAILED = 'Chưa đạt - làm lại';
var STATUS_GRADED = 'Đã chấm';

/* ------------------------------------------------------------------ entry points */
function doGet(e) { return handle_((e && e.parameter) || {}); }
function doPost(e) {
  var p = {};
  try { p = JSON.parse((e && e.postData && e.postData.contents) || '{}'); } catch (err) { p = {}; }
  return handle_(p);
}

function handle_(p) {
  try {
    ensureSheets_();
    var out;
    switch (String(p.action || '')) {
      case 'ping': out = { version: VERSION }; break;
      case 'login': out = login_(p); break;
      case 'progress': out = progress_(p); break;
      case 'homework': out = homework_(p); break;
      case 'submit': out = submit_(p); break;
      default: throw new Error('Unknown action');
    }
    out.ok = true;
    return json_(out);
  } catch (err) {
    return json_({ ok: false, error: String((err && err.message) || err) });
  }
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/* ------------------------------------------------------------------ helpers */
function ss_() { return SpreadsheetApp.getActiveSpreadsheet(); }

function ensureSheets_() {
  var ss = ss_();
  Object.keys(HEADERS).forEach(function (name) {
    var sh = ss.getSheetByName(name);
    if (!sh) {
      sh = ss.insertSheet(name);
      sh.getRange(1, 1, 1, HEADERS[name].length).setValues([HEADERS[name]]).setFontWeight('bold');
      sh.setFrozenRows(1);
      if (name === 'Homework') {
        sh.getRange(2, 1, 1, HEADERS[name].length).setValues([[
          'S01', 'T1', 'Thêm của thầy', 'mcq', 'Ví dụ: Which letter sounds like "see"?', 'A | B | F', 'B', '', 1, 'no'
        ]]);
      }
    }
  });
}

function cleanEmail_(email) {
  var e = String(email || '').trim().toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e)) throw new Error('Email không hợp lệ');
  return e;
}
function cleanName_(name) {
  var n = String(name || '').replace(/\s+/g, ' ').trim();
  if (n.length < 2) throw new Error('Vui lòng nhập họ tên');
  return n.slice(0, 80);
}
function rows_(name) {
  var sh = ss_().getSheetByName(name);
  var last = sh.getLastRow();
  if (last < 2) return [];
  return sh.getRange(2, 1, last - 1, HEADERS[name].length).getValues();
}
function norm_(s) { return String(s == null ? '' : s).toLowerCase().replace(/[\s\-–—]+/g, ''); }
function sha256Hex_(s) {
  var bytes = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, s, Utilities.Charset.UTF_8);
  return bytes.map(function (b) { var v = (b < 0 ? b + 256 : b).toString(16); return v.length === 1 ? '0' + v : v; }).join('');
}
function iso_(d) { return d instanceof Date ? d.toISOString() : String(d || ''); }

/* ------------------------------------------------------------------ actions */
function login_(p) {
  var email = cleanEmail_(p.email), name = cleanName_(p.name);
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var sh = ss_().getSheetByName('Students');
    var data = rows_('Students'), now = new Date(), found = -1;
    for (var i = 0; i < data.length; i++) if (String(data[i][0]).toLowerCase() === email) { found = i; break; }
    if (found >= 0) {
      sh.getRange(found + 2, 2).setValue(name);
      sh.getRange(found + 2, 4).setValue(now);
    } else {
      sh.appendRow([email, name, now, now]);
    }
  } finally { lock.releaseLock(); }
  var pr = progress_({ email: email });
  pr.name = name;
  return pr;
}

function progress_(p) {
  var email = cleanEmail_(p.email);
  var data = rows_('Submissions'), by = {};
  data.forEach(function (r) {
    if (String(r[1]).toLowerCase() !== email) return;
    var s = String(r[3]);
    var o = by[s] || (by[s] = { session: s, attempts: 0, bestPct: null, passed: false, lastAt: '', status: '', teacherScore: '', feedback: '', voice: 0 });
    o.attempts++;
    var pct = r[7] === '' ? null : Number(r[7]);
    if (pct != null && !isNaN(pct) && (o.bestPct == null || pct > o.bestPct)) o.bestPct = pct;
    if (pct != null && pct >= PASS_PCT) o.passed = true;
    o.lastAt = iso_(r[0]);
    if (r[10]) o.status = String(r[10]);
    if (r[11] !== '' && r[11] != null) o.teacherScore = String(r[11]);
    if (r[12]) o.feedback = String(r[12]);
    if (r[9]) o.voice += String(r[9]).split('\n').filter(String).length;
  });
  var list = Object.keys(by).sort().map(function (k) { return by[k]; });
  return { email: email, sessions: list };
}

function homework_(p) {
  var session = String(p.session || '').toUpperCase();
  if (!/^S\d{2}$/.test(session)) throw new Error('Session không hợp lệ');
  var items = [];
  rows_('Homework').forEach(function (r) {
    if (String(r[0]).toUpperCase() !== session) return;
    if (norm_(r[9]) === 'no' || norm_(r[9]) === 'không') return;
    var qid = String(r[1] || '').trim();
    if (!qid) return;
    var type = String(r[3] || 'mcq').trim();
    var options = String(r[5] || '').split('|').map(function (x) { return x.trim(); }).filter(String);
    var answers = String(r[6] || '').split('|').map(function (x) { return x.trim(); }).filter(String);
    items.push({
      id: qid, section: String(r[2] || 'Thêm của thầy'), type: type, prompt: String(r[4] || ''),
      options: options, audio: String(r[7] || ''), points: Number(r[8]) || 1,
      ah: answers.map(function (a) { return sha256Hex_(session + '|' + qid + '|' + norm_(a)); })
    });
  });
  return { session: session, items: items };
}

function submit_(p) {
  var email = cleanEmail_(p.email), name = cleanName_(p.name);
  var session = String(p.session || '').toUpperCase();
  if (!/^S\d{2}$/.test(session)) throw new Error('Session không hợp lệ');
  var voice = Array.isArray(p.voice) ? p.voice : [];
  var links = [];
  if (voice.length) {
    var folder = folder_(session);
    voice.forEach(function (v) {
      var bytes = Utilities.base64Decode(String(v.b64 || ''));
      if (!bytes.length) return;
      if (bytes.length > MAX_VOICE_BYTES) throw new Error('File ghi âm quá lớn (tối đa 15 MB)');
      var ext = String(v.ext || 'webm').replace(/[^a-z0-9]/gi, '').slice(0, 5) || 'webm';
      var stamp = Utilities.formatDate(new Date(), 'Asia/Ho_Chi_Minh', 'yyyyMMdd-HHmm');
      var fname = session + '_' + name.replace(/[^\wÀ-ỹ ]/g, '').replace(/\s+/g, '-') + '_' + String(v.qid || 'voice') + '_' + stamp + '.' + ext;
      var file = folder.createFile(Utilities.newBlob(bytes, String(v.mime || 'audio/webm'), fname));
      links.push(String(v.qid || 'voice') + ': ' + file.getUrl());
    });
  }
  var written = (Array.isArray(p.written) ? p.written : []).map(function (w) {
    return '[' + String(w.qid) + '] ' + String(w.prompt || '').slice(0, 80) + '\n' + String(w.text || '');
  }).join('\n\n');
  var autoScore = Number(p.autoScore) || 0, autoMax = Number(p.autoMax) || 0;
  var pct = autoMax ? Math.round(autoScore / autoMax * 100) : '';

  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  var attempt = 1;
  try {
    rows_('Submissions').forEach(function (r) {
      if (String(r[1]).toLowerCase() === email && String(r[3]) === session) attempt++;
    });
    ss_().getSheetByName('Submissions').appendRow([
      new Date(), email, name, session, attempt, autoScore, autoMax, pct,
      written, links.join('\n'), (pct !== '' && pct >= PASS_PCT) ? STATUS_PASSED : STATUS_FAILED, '', '',
      JSON.stringify(p.details || {}).slice(0, 45000)
    ]);
    // keep the student list fresh
    var st = rows_('Students'), seen = false;
    for (var i = 0; i < st.length; i++) if (String(st[i][0]).toLowerCase() === email) {
      ss_().getSheetByName('Students').getRange(i + 2, 4).setValue(new Date()); seen = true; break;
    }
    if (!seen) ss_().getSheetByName('Students').appendRow([email, name, new Date(), new Date()]);
  } finally { lock.releaseLock(); }
  return { attempt: attempt, voiceLinks: links.length, pct: pct, passed: pct !== '' && pct >= PASS_PCT };
}

function folder_(session) {
  var it = DriveApp.getFoldersByName(VOICE_FOLDER);
  var root = it.hasNext() ? it.next() : DriveApp.createFolder(VOICE_FOLDER);
  var sub = root.getFoldersByName(session);
  return sub.hasNext() ? sub.next() : root.createFolder(session);
}

/** Chạy 1 lần trong trình soạn thảo (nút ▶ Run) để cấp quyền và tạo sẵn các tab. */
function setup() {
  ensureSheets_();
  folder_('S01');
  Logger.log('Đã sẵn sàng. Tiếp theo: Deploy → New deployment → Web app.');
}
