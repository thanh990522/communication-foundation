// Runs backend/Code.gs unchanged inside Node with in-memory fakes of the Google services,
// and serves it over HTTP like an Apps Script web app. For local testing only.
//   node backend/test/mock-server.js [port]
const fs = require('fs'), path = require('path'), vm = require('vm'), http = require('http'), crypto = require('crypto');

function makeSheet(name) {
  const data = []; // 2D array, row 0 = row 1
  const sh = {
    name, data,
    getRange(r, c, nr = 1, nc = 1) {
      return {
        setValues(v) { for (let i = 0; i < nr; i++) { data[r - 1 + i] = data[r - 1 + i] || []; for (let j = 0; j < nc; j++) data[r - 1 + i][c - 1 + j] = v[i][j]; } return this; },
        setValue(v) { data[r - 1] = data[r - 1] || []; data[r - 1][c - 1] = v; return this; },
        getValues() { const out = []; for (let i = 0; i < nr; i++) { const row = []; for (let j = 0; j < nc; j++) { const v = (data[r - 1 + i] || [])[c - 1 + j]; row.push(v === undefined ? '' : v); } out.push(row); } return out; },
        setFontWeight() { return this; }
      };
    },
    getLastRow() { return data.length; },
    appendRow(row) { data.push(row.slice()); },
    setFrozenRows() {}
  };
  return sh;
}
const sheets = {};
const files = [];
const SpreadsheetApp = { getActiveSpreadsheet: () => ({
  getSheetByName: n => sheets[n] || null,
  insertSheet: n => (sheets[n] = makeSheet(n))
}) };
function folder(name) {
  const subs = {};
  return { name,
    getFoldersByName: n => { let done = !subs[n]; return { hasNext: () => !done, next: () => { done = true; return subs[n]; } }; },
    createFolder: n => (subs[n] = folder(n)),
    createFile: blob => { const f = { url: `https://drive.mock/${name}/${blob.name}`, size: blob.bytes.length, name: blob.name }; files.push(f); return { getUrl: () => f.url }; }
  };
}
const roots = {};
const DriveApp = {
  getFoldersByName: n => { let done = !roots[n]; return { hasNext: () => !done, next: () => { done = true; return roots[n]; } }; },
  createFolder: n => (roots[n] = folder(n))
};
const Utilities = {
  DigestAlgorithm: { SHA_256: 'sha256' }, Charset: { UTF_8: 'utf8' },
  computeDigest: (alg, s) => Array.from(crypto.createHash('sha256').update(s, 'utf8').digest()).map(b => (b > 127 ? b - 256 : b)),
  base64Decode: s => Array.from(Buffer.from(s, 'base64')),
  newBlob: (bytes, mime, name) => ({ bytes, mime, name }),
  formatDate: d => d.toISOString().slice(0, 16).replace(/[-:T]/g, '')
};
let lastOutput = null;
const ContentService = { MimeType: { JSON: 'json' }, createTextOutput: t => ({ setMimeType() { lastOutput = t; return t; } }) };
const LockService = { getScriptLock: () => ({ waitLock() {}, releaseLock() {} }) };
const Logger = { log: () => {} };

const ctx = vm.createContext({ SpreadsheetApp, DriveApp, Utilities, ContentService, LockService, Logger, JSON, Date, Math, String, Number, Array, Object, isNaN, console });
vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'Code.gs'), 'utf8'), ctx);

const port = +process.argv[2] || 8790;
http.createServer((req, res) => {
  const cors = { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' };
  const url = new URL(req.url, 'http://x');
  if (url.pathname === '/__state') { res.writeHead(200, cors); return res.end(JSON.stringify({ sheets: Object.fromEntries(Object.entries(sheets).map(([k, v]) => [k, v.data])), files })); }
  if (url.pathname === '/__addHomework') { sheets.Homework.appendRow(JSON.parse(decodeURIComponent(url.searchParams.get('row')))); res.writeHead(200, cors); return res.end('{}'); }
  if (url.pathname === '/__grade') { const r = sheets.Submissions.data[+url.searchParams.get('row')]; r[10] = 'Đã chấm'; r[11] = url.searchParams.get('score'); r[12] = url.searchParams.get('fb'); res.writeHead(200, cors); return res.end('{}'); }
  if (req.method === 'OPTIONS') { res.writeHead(405); return res.end(); } // real Apps Script has no preflight support
  let body = '';
  req.on('data', c => body += c);
  req.on('end', () => {
    if (req.method === 'POST') ctx.doPost({ postData: { contents: body } });
    else ctx.doGet({ parameter: Object.fromEntries(url.searchParams) });
    res.writeHead(200, cors); res.end(lastOutput);
  });
}).listen(port, () => console.log('mock Apps Script on', port));
