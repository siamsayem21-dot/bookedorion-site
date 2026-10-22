(function () {
  function el(id) { return document.getElementById(id); }

  /* ---------- sample call demo ---------- */
  var state = { scene: 0, company: '', calls: 8, ticket: 350, rate: 40 };
  function company() { return (state.company || '').trim() || 'ABC Heating & Air'; }
  function scenes() {
    var c = company();
    return [
      { label: 'AC not cooling', outcome: 'Job booked · Wed 8:00 AM · owner texted', lines: [
        ['c', 'Caller:', 'Hi, my AC is running but blowing warm air.'],
        ['m', 'Molly:', 'Sorry about that. I’m Molly, the AI assistant for ' + c + '. Can I get your name and address?'],
        ['c', 'Caller:', 'Maria, 214 Oak Lane, Plano.'],
        ['m', 'Molly:', 'Thanks, Maria. I have Wednesday 8 to 10 AM open. Does that work?']
      ]},
      { label: 'Gas smell (emergency)', outcome: 'Owner called right away · caller told to get outside', lines: [
        ['c', 'Caller:', 'I smell gas near my furnace.'],
        ['m', 'Molly:', 'Please leave the house now and call 911 or your gas company from outside.'],
        ['m', 'Molly:', 'I’m calling the owner right now so a technician can reach you.'],
        ['c', 'Caller:', 'Okay, we’re outside.']
      ]},
      { label: 'Price question', outcome: 'Diagnostic visit booked · Thu 1:00 PM', lines: [
        ['c', 'Caller:', 'How much do you charge to come look at my unit?'],
        ['m', 'Molly:', 'Our diagnostic visit has a flat fee, paid to the technician on site.'],
        ['c', 'Caller:', 'That’s fine. Can someone come Thursday?'],
        ['m', 'Molly:', 'Yes. I have 1 PM open. Shall I book it?']
      ]}
    ];
  }
  function renderDemo() {
    var tabs = el('tabs'), lines = el('lines'); if (!tabs || !lines) return;
    var sc = scenes(), cur = sc[state.scene];
    el('bizShown').textContent = company();
    tabs.textContent = '';
    sc.forEach(function (s, i) {
      var b = document.createElement('button');
      b.type = 'button'; b.setAttribute('role', 'tab');
      b.setAttribute('aria-selected', i === state.scene ? 'true' : 'false');
      b.textContent = s.label;
      b.addEventListener('click', function () { state.scene = i; renderDemo(); });
      tabs.appendChild(b);
    });
    lines.textContent = '';
    cur.lines.forEach(function (l) {
      var d = document.createElement('div');
      d.className = 'ln ' + (l[0] === 'm' ? 'ln-m' : 'ln-c');
      var w = document.createElement('b'); w.textContent = l[1];
      d.appendChild(w); d.appendChild(document.createTextNode(l[2]));
      lines.appendChild(d);
    });
    el('outcome').textContent = cur.outcome;
  }
  var biz = el('biz');
  if (biz) biz.addEventListener('input', function (e) { state.company = e.target.value; renderDemo(); });

  /* ---------- calculator ---------- */
  function fmt(n) { return n.toLocaleString('en-US'); }
  function renderCalc() {
    if (!el('monthly')) return;
    var m = Math.round(state.calls * 4.33 * (state.rate / 100) * state.ticket);
    el('callsV').textContent = state.calls; el('ticketV').textContent = fmt(state.ticket); el('rateV').textContent = state.rate;
    el('monthly').textContent = fmt(m); el('yearly').textContent = fmt(m * 12);
  }
  ['calls', 'ticket', 'rate'].forEach(function (k) {
    var i = el(k); if (i) i.addEventListener('input', function (e) { state[k] = Number(e.target.value); renderCalc(); });
  });

  /* ---------- plan finder ---------- */
  var fb = [].slice.call(document.querySelectorAll('.finder button')), pls = [].slice.call(document.querySelectorAll('.pl'));
  fb.forEach(function (b) {
    b.addEventListener('click', function () {
      var k = b.getAttribute('data-plan');
      fb.forEach(function (x) { x.classList.toggle('on', x === b); x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      pls.forEach(function (p) { p.classList.toggle('is-rec', p.getAttribute('data-plan') === k); });
    });
  });

  /* ---------- pilot form ---------- */
  var form = el('pilotForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = el('f-name'), co = el('f-company'), em = el('f-email'), ph = el('f-phone');
      var bad = [];
      [name, co].forEach(function (f) { var v = !f.value.trim(); f.setAttribute('aria-invalid', v ? 'true' : 'false'); if (v) bad.push(f); });
      var emOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value.trim());
      em.setAttribute('aria-invalid', emOk ? 'false' : 'true'); if (!emOk) bad.push(em);
      var fe = el('fieldErr');
      if (bad.length) { fe.textContent = 'Please add your name, company and a valid email.'; fe.hidden = false; bad[0].focus(); return; }
      fe.hidden = true;
      var t = 'Free pilot request\nName: ' + name.value.trim() + '\nCompany: ' + co.value.trim() + '\nEmail: ' + em.value.trim() + '\nPhone: ' + ph.value.trim();
      var btn = el('f-submit'); btn.disabled = true; btn.textContent = 'Sending…'; el('formErr').hidden = true;
      fetch('https://api.web3forms.com/submit', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ access_key: 'd2b56b26-ace6-4f6d-a1ac-23340b566c8b', subject: 'New pilot request: ' + co.value.trim(), from_name: 'BookedOrion website',
          name: name.value.trim(), company: co.value.trim(), email: em.value.trim(), phone: ph.value.trim(), replyto: em.value.trim(), botcheck: el('f-bot').checked }) })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (d && d.success) { el('formOk').hidden = false; btn.hidden = true; [name, co, em, ph].forEach(function (f) { f.disabled = true; }); }
          else { throw new Error((d && d.message) || 'failed'); }
        })
        .catch(function () {
          btn.disabled = false; btn.textContent = 'Start my free pilot';
          el('formErr').textContent = 'We couldn’t send that just now. Please email the details below instead.'; el('formErr').hidden = false;
          el('formText').textContent = t; el('formDone').hidden = false;
        });
    });
    el('copyBtn').addEventListener('click', function () {
      var b = this, t = el('formText').textContent;
      function sel() { var r = document.createRange(); r.selectNodeContents(el('formText')); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }
      try { navigator.clipboard.writeText(t).then(function () { b.textContent = 'Copied'; }, sel); } catch (_) { sel(); }
    });
  }

  /* ---------- mobile quick actions ---------- */
  var bar = document.querySelector('.mcta'), hero = el('top'), start = el('start');
  function onScroll() {
    if (!bar || !hero) return;
    var past = hero.getBoundingClientRect().bottom < 0;
    var atForm = start && start.getBoundingClientRect().top < innerHeight && start.getBoundingClientRect().bottom > 0;
    bar.classList.toggle('on', past && !atForm);
  }
  addEventListener('scroll', onScroll, { passive: true });

  renderDemo(); renderCalc(); onScroll();
})();
