/* Quiet motion for the home page: one entrance, small scroll reveals, a gentle tilt on the hero call log.
   No libraries. Everything is visible without JS or with reduced motion. */
(function () {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var d = document.documentElement;
  d.classList.add('js-motion');
  var show = function () { d.classList.add('loaded'); };
  setTimeout(function () { document.querySelectorAll('[data-rise]').forEach(function (e) { e.classList.add('in'); }); show(); }, 2500);
  document.addEventListener('DOMContentLoaded', function () {
    requestAnimationFrame(function () { requestAnimationFrame(show); });
    var targets = document.querySelectorAll('main section:not(.hero) .wrap > *');
    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    targets.forEach(function (t) { if (t.getBoundingClientRect().top > innerHeight) { t.setAttribute('data-rise', ''); io.observe(t); } });
    // gentle tilt that follows the pointer (desktop, mouse only)
    var vis = document.querySelector('.hero-vis'), con = vis && vis.querySelector('.console'), tk = vis && vis.querySelector('.ticket');
    if (!vis || !matchMedia('(hover:hover) and (pointer:fine) and (min-width:1001px)').matches) return;
    var hero = document.querySelector('.hero'), raf = 0, px = 0, py = 0;
    hero.addEventListener('pointermove', function (e) {
      px = e.clientX / innerWidth - 0.5; py = e.clientY / innerHeight - 0.5;
      if (raf) return;
      raf = requestAnimationFrame(function () {
        raf = 0;
        con.style.transform = 'rotateY(' + (-7 + px * 4).toFixed(2) + 'deg) rotateX(' + (3 - py * 3).toFixed(2) + 'deg)';
        if (tk) tk.style.transform = 'rotate(-5deg) rotateX(8deg) translate(' + (px * -6).toFixed(1) + 'px,' + (py * -4).toFixed(1) + 'px)';
      });
    });
    hero.addEventListener('pointerleave', function () { con.style.transform = ''; if (tk) tk.style.transform = ''; });
  });
})();
