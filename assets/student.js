/* Shared student session + backend calls (used by the home page and the homework page). */
(function () {
  const KEY = 'gt_student_v1';
  const CACHE = 'gt_progress_v1';
  const cfg = window.GT_CONFIG || {};

  function get() { try { return JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { return null; } }
  function set(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }
  function clear() { try { localStorage.removeItem(KEY); localStorage.removeItem(CACHE); } catch (e) {} }
  function cachedProgress() { try { const p = JSON.parse(localStorage.getItem(CACHE) || 'null'), me = get(); return p && me && p.email === me.email ? p : null; } catch (e) { return null; } }
  function cacheProgress(p) { try { localStorage.setItem(CACHE, JSON.stringify(p)); } catch (e) {} }

  const online = () => !!cfg.api;

  /* Apps Script web apps accept "simple" requests only: POST with a text/plain body, no custom headers. */
  async function call(action, data, timeoutMs) {
    if (!online()) throw new Error('Hệ thống nộp bài chưa được kết nối.');
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), timeoutMs || 30000);
    try {
      const res = await fetch(cfg.api, {
        method: 'POST', body: JSON.stringify(Object.assign({ action }, data || {})),
        headers: { 'Content-Type': 'text/plain;charset=utf-8' }, redirect: 'follow', signal: ctrl.signal
      });
      const out = await res.json();
      if (!out.ok) throw new Error(out.error || 'Lỗi máy chủ');
      return out;
    } catch (e) {
      if (e.name === 'AbortError') throw new Error('Mạng chậm — vui lòng thử lại.');
      if (e instanceof TypeError) throw new Error('Không kết nối được máy chủ. Kiểm tra Internet rồi thử lại.');
      throw e;
    } finally { clearTimeout(t); }
  }

  async function login(name, email) {
    const out = await call('login', { name, email });
    set({ name: out.name, email: out.email });
    cacheProgress(out);
    return out;
  }
  async function progress() {
    const s = get(); if (!s) return null;
    const out = await call('progress', { email: s.email });
    cacheProgress(out);
    return out;
  }

  /* Login dialog shared by both pages. Resolves with the student, or null if closed. */
  function loginDialog(opts) {
    opts = opts || {};
    return new Promise(resolve => {
      const old = document.getElementById('gtLogin'); if (old) old.remove();
      const wrap = document.createElement('div');
      wrap.id = 'gtLogin';
      wrap.innerHTML = `
        <div class="gl-back"></div>
        <form class="gl-box" novalidate>
          <div class="gl-kick">Góc học viên</div>
          <h3>${opts.title || 'Đăng nhập để làm bài & theo dõi tiến độ'}</h3>
          <label>Họ và tên<input name="name" autocomplete="name" placeholder="VD: Nguyễn Minh An" required></label>
          <label>Email<input name="email" type="email" autocomplete="email" inputmode="email" placeholder="VD: an.nguyen@gmail.com" required></label>
          <div class="gl-err" hidden></div>
          <div class="gl-acts">
            ${opts.required ? '' : '<button type="button" class="gl-cancel">Để sau</button>'}
            <button type="submit" class="gl-ok">Bắt đầu →</button>
          </div>
        </form>`;
      document.body.appendChild(wrap);
      const f = wrap.querySelector('form'), err = wrap.querySelector('.gl-err'), ok = wrap.querySelector('.gl-ok');
      const prev = get(); if (prev) { f.name.value = prev.name; f.email.value = prev.email; }
      setTimeout(() => (f.name.value ? f.email : f.name).focus(), 50);
      const close = v => { wrap.remove(); resolve(v); };
      const cancel = wrap.querySelector('.gl-cancel'); if (cancel) cancel.onclick = () => close(null);
      if (!opts.required) wrap.querySelector('.gl-back').onclick = () => close(null);
      f.onsubmit = async e => {
        e.preventDefault();
        const name = f.name.value.replace(/\s+/g, ' ').trim(), email = f.email.value.trim().toLowerCase();
        err.hidden = true;
        if (name.length < 2) { err.textContent = 'Vui lòng nhập họ tên.'; err.hidden = false; return; }
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { err.textContent = 'Email chưa đúng định dạng.'; err.hidden = false; return; }
        if (!online()) { set({ name, email }); return close({ name, email, offline: true }); }
        ok.disabled = true; ok.textContent = 'Đang kết nối…';
        try { await login(name, email); close(get()); }
        catch (x) { err.textContent = x.message; err.hidden = false; ok.disabled = false; ok.textContent = 'Bắt đầu →'; }
      };
    });
  }

  const css = `
  #gtLogin{position:fixed;inset:0;z-index:100;display:flex;align-items:center;justify-content:center;padding:16px}
  #gtLogin .gl-back{position:absolute;inset:0;background:rgba(11,31,92,.55)}
  #gtLogin .gl-box{position:relative;width:100%;max-width:420px;background:#fff;border-radius:20px;padding:24px;box-shadow:0 20px 60px rgba(11,31,92,.3);display:flex;flex-direction:column;gap:12px;font-family:inherit}
  #gtLogin .gl-kick{font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:#1D4ED8}
  #gtLogin h3{font-size:22px;color:#0B1F5C;line-height:1.25}
  #gtLogin .gl-sub{font-size:14px;color:#5B6B8C}
  #gtLogin label{display:flex;flex-direction:column;gap:5px;font-size:13px;font-weight:800;color:#0B1F5C}
  #gtLogin input{height:46px;border:2px solid #E3E8F4;border-radius:12px;padding:0 14px;font:inherit;font-size:16px;color:#0B1F5C}
  #gtLogin input:focus{outline:none;border-color:#1D4ED8}
  #gtLogin .gl-err{background:#FEE2E2;color:#B91C1C;font-weight:700;font-size:14px;padding:9px 12px;border-radius:10px}
  #gtLogin .gl-acts{display:flex;gap:10px;justify-content:flex-end;margin-top:4px}
  #gtLogin button{font:inherit;font-weight:800;font-size:15px;border:none;border-radius:12px;padding:11px 18px;cursor:pointer}
  #gtLogin .gl-ok{background:#1D4ED8;color:#fff;box-shadow:0 3px 0 #163a9e}
  #gtLogin .gl-ok:disabled{opacity:.7}
  #gtLogin .gl-cancel{background:#F1F5FB;color:#0B1F5C}`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  window.GTStudent = { get, set, clear, call, login, progress, loginDialog, online, cachedProgress };
})();
