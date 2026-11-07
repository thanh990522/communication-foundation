/* =============================================================
   Student identity + progress logging + lesson lock (shared)
   Needs: assets/config.js (window.GT_CONFIG) — optional assets/sessions.js
   ============================================================= */
(function () {
  const K = 'gt_student', TEACHER = 'gt_teacher';
  const CFG = window.GT_CONFIG || {};
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  const get = () => { try { return JSON.parse(localStorage.getItem(K) || 'null'); } catch (e) { return null; } };
  const isTeacher = () => { try { return localStorage.getItem(TEACHER) === '1'; } catch (e) { return false; } };

  function css() {
    if (document.getElementById('gtcss')) return;
    const s = document.createElement('style'); s.id = 'gtcss';
    s.textContent = `
.gt-ov{position:fixed;inset:0;background:rgba(11,31,92,.55);backdrop-filter:blur(3px);z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px;font-family:'Be Vietnam Pro',system-ui,sans-serif}
.gt-box{background:#fff;border-radius:22px;max-width:440px;width:100%;padding:26px 24px;box-shadow:0 20px 60px rgba(11,31,92,.3);position:relative;overflow:hidden}
.gt-box::before{content:"";position:absolute;right:-60px;top:-60px;width:150px;height:150px;border-radius:50%;background:#FFC72C}
.gt-box h2{position:relative;font-size:24px;font-weight:900;color:#0B1F5C;margin:0 0 6px;line-height:1.2}
.gt-box p{position:relative;color:#5B6B8C;font-size:15px;margin:0 0 16px;line-height:1.5}
.gt-box label{display:block;font-weight:800;font-size:13px;color:#0B1F5C;margin:10px 0 5px;letter-spacing:.3px}
.gt-box input{width:100%;box-sizing:border-box;height:48px;border:2px solid #E3E8F4;border-radius:12px;padding:0 14px;font-size:17px;font-weight:700;color:#0B1F5C;font-family:inherit}
.gt-box input:focus{outline:none;border-color:#1D4ED8}
.gt-row{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap}
.gt-btn{flex:1;border:none;border-radius:12px;padding:13px 16px;font-weight:900;font-size:16px;cursor:pointer;font-family:inherit}
.gt-btn.go{background:#1D4ED8;color:#fff;box-shadow:0 4px 0 #163a9e}.gt-btn.skip{background:#EAF1FF;color:#1D4ED8;flex:0 0 auto}
.gt-err{color:#DC2626;font-weight:700;font-size:14px;min-height:18px;margin-top:6px}
.gt-lock{text-align:center}.gt-lock .ic{font-size:64px;line-height:1;margin-bottom:8px;position:relative}
.gt-me{display:inline-flex;align-items:center;gap:8px;background:#0B1F5C;color:#fff;border-radius:999px;padding:6px 8px 6px 14px;font-size:14px;font-weight:700;font-family:'Be Vietnam Pro',system-ui,sans-serif}
.gt-me b{color:#FFC72C}.gt-me button{background:#FFC72C;color:#0B1F5C;border:none;border-radius:999px;padding:4px 10px;font-weight:800;font-size:12px;cursor:pointer;font-family:inherit}`;
    document.head.appendChild(s);
  }

  function ask(opts) {
    opts = opts || {};
    return new Promise(res => {
      css(); const cur = get() || {};
      const ov = document.createElement('div'); ov.className = 'gt-ov';
      ov.innerHTML = `<div class="gt-box"><h2>${opts.title || '👋 Chào bạn!'}</h2><p>${opts.msg || 'Nhập <b>họ và tên</b> để lưu tiến độ học và kết quả homework của bạn.'}</p>
        <label>Họ và tên</label><input id="gtName" maxlength="60" autocomplete="name" value="${esc(cur.name || '')}" placeholder="VD: Nguyễn Thị Lan">
        <label>Lớp / nhóm (nếu có)</label><input id="gtCls" maxlength="30" value="${esc(cur.cls || '')}" placeholder="VD: GT246-K1">
        <div class="gt-err" id="gtErr"></div>
        <div class="gt-row">${opts.noSkip ? '' : '<button class="gt-btn skip" id="gtSkip">Để sau</button>'}<button class="gt-btn go" id="gtGo">Bắt đầu →</button></div></div>`;
      document.body.appendChild(ov);
      const n = ov.querySelector('#gtName'); setTimeout(() => n.focus(), 50);
      const done = v => { ov.remove(); res(v); };
      ov.querySelector('#gtGo').onclick = () => {
        const name = n.value.replace(/\s+/g, ' ').trim(), cls = ov.querySelector('#gtCls').value.trim();
        if (name.split(' ').length < 2 || name.length < 4) { ov.querySelector('#gtErr').textContent = 'Hãy nhập đầy đủ họ và tên.'; return; }
        const changed = cur.name && cur.name.toLowerCase() !== name.toLowerCase();
        const st = { id: changed || !cur.id ? 'st' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6) : cur.id, name, cls };
        try {
          if (changed) Object.keys(localStorage).filter(k => /^gt_hw_(best|draft)_/.test(k)).forEach(k => localStorage.removeItem(k));
          localStorage.setItem(K, JSON.stringify(st));
        } catch (e) {}
        log({ kind: 'join' }); done(st); renderMe();
      };
      n.onkeydown = ev => { if (ev.key === 'Enter') ov.querySelector('#gtGo').click(); };
      const sk = ov.querySelector('#gtSkip'); if (sk) sk.onclick = () => { try { sessionStorage.setItem('gt_skip', '1'); } catch (e) {} done(null); };
    });
  }

  function log(ev) {
    const st = get(); if (!st || !CFG.progressUrl) return;
    const body = JSON.stringify(Object.assign({ id: st.id, name: st.name, cls: st.cls || '', ua: /Mobi/.test(navigator.userAgent) ? 'mobile' : 'desktop' }, ev));
    try { fetch(CFG.progressUrl, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body, keepalive: true }); } catch (e) {}
  }

  function renderMe() {
    const el = document.getElementById('gtMe'); if (!el) return; css();
    const st = get();
    el.innerHTML = st ? `<span class="gt-me">👤 <b>${esc(st.name)}</b>${st.cls ? ' · ' + esc(st.cls) : ''}<button type="button" id="gtChange">Đổi</button></span>`
      : `<span class="gt-me">👤 Chưa nhập tên<button type="button" id="gtChange">Nhập tên</button></span>`;
    el.querySelector('#gtChange').onclick = () => ask({ title: st ? '✏️ Đổi tên' : '👋 Chào bạn!' });
  }

  function sessionOf(sid) { return (window.SESSIONS || []).find(s => s.id === sid); }

  /* lesson / homework page: block when the lesson is closed (teacher device is never blocked) */
  function guard(sid, home) {
    const s = sessionOf(sid); if (!s || s.status === 'live' || isTeacher()) return false;
    css(); const ov = document.createElement('div'); ov.className = 'gt-ov';
    ov.innerHTML = `<div class="gt-box gt-lock"><div class="ic">🔒</div><h2>Bài ${esc(sid)} chưa mở</h2><p>${esc(s.title || '')}<br>Bài học sẽ được mở theo lịch học. Hẹn gặp bạn sau nhé!</p><div class="gt-row"><a class="gt-btn go" style="text-decoration:none;text-align:center" href="${home}">← Tất cả bài học</a></div></div>`;
    document.body.appendChild(ov); return true;
  }

  /* lesson page: log one "lesson opened" per student per day */
  function lessonOpened(sid) {
    const st = get(); if (!st) return;
    const k = 'gt_seen_' + sid + '_' + new Date().toISOString().slice(0, 10);
    try { if (localStorage.getItem(k)) return; localStorage.setItem(k, '1'); } catch (e) {}
    log({ kind: 'lesson', sid });
  }

  async function requireName(msg) {
    if (get()) return get();
    return await ask({ title: '✍️ Nhập tên trước khi nộp bài', msg: msg || 'Kết quả sẽ được lưu với tên của bạn để giáo viên theo dõi tiến độ.', noSkip: true });
  }

  window.GT = { get, ask, log, renderMe, guard, lessonOpened, requireName, isTeacher };
})();
