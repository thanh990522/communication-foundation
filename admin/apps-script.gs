/**
 * GIAO TIẾP 246 — Progress tracker (Google Apps Script)
 * 1) Đổi ADMIN_KEY bên dưới thành mật khẩu của bạn.
 * 2) Deploy → New deployment → Web app · Execute as: Me · Who has access: Anyone.
 * 3) Copy Web app URL → dán vào trang Admin → Cài đặt.
 */
const ADMIN_KEY = 'doi-mat-khau-nay';   // ← đổi thành mật khẩu riêng của bạn
const SHEET = 'Progress';

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let s = ss.getSheetByName(SHEET);
  if (!s) {
    s = ss.insertSheet(SHEET);
    s.appendRow(['Time', 'Student ID', 'Name', 'Class', 'Session', 'Kind', 'Score %', 'Passed', 'Device']);
    s.setFrozenRows(1);
  }
  return s;
}

function clean_(v, n) {            // plain text only, no formulas
  v = String(v == null ? '' : v).slice(0, n);
  return /^[=+\-@]/.test(v) ? "'" + v : v;
}

function doPost(e) {
  try {
    const d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    if (!d.id || !d.name) return out_({ ok: false });
    const lock = LockService.getScriptLock(); lock.waitLock(5000);
    sheet_().appendRow([new Date(), clean_(d.id, 40), clean_(d.name, 60), clean_(d.cls, 30), clean_(d.sid, 6),
      clean_(d.kind, 20), d.pct == null || d.pct === '' ? '' : Number(d.pct),
      d.passed === true ? 'yes' : d.passed === false ? 'no' : '', clean_(d.ua, 10)]);
    lock.releaseLock();
    return out_({ ok: true });
  } catch (err) { return out_({ ok: false, error: String(err) }); }
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.ping) return out_({ ok: true, ping: true });
  if (p.key !== ADMIN_KEY) return out_({ ok: false, error: 'wrong key' });
  const v = sheet_().getDataRange().getValues(); v.shift();
  return out_({ ok: true, rows: v.map(r => ({ t: r[0], id: r[1], name: r[2], cls: r[3], sid: r[4], kind: r[5], pct: r[6], passed: r[7] })) });
}

function out_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
