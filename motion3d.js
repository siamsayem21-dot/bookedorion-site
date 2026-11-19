/* BookedOrion 3D motion layer: GSAP part (classic script, runs after GSAP loads). */
(function () {
  var d = document.documentElement;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = matchMedia('(hover:hover) and (pointer:fine)').matches;
  var wide = matchMedia('(min-width: 901px)').matches;
  var gl = false; try { gl = !!document.createElement('canvas').getContext('webgl2'); } catch (e) {}
  d.dataset.m3 = reduce ? 'off' : (wide && finePointer ? 'full' : 'lite');
  if (!gl) d.dataset.m3gl = 'none';
  if (reduce) return;
  d.classList.add('m3-on');

  // safety net: never leave anything hidden if a library fails
  setTimeout(function () {
    document.querySelectorAll('[data-m3-fly]').forEach(function (e) {
      if (+getComputedStyle(e).opacity < 0.05) { e.style.opacity = 1; e.style.transform = 'none'; }
    });
  }, 2600);

  function splitWords(h) {
    h.setAttribute('aria-label', h.textContent.replace(/\s+/g, ' ').trim());
    (function walk(node) {
      Array.from(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3 && n.textContent.trim()) {
          var f = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (w) {
            if (!w) return;
            if (/^\s+$/.test(w)) { f.appendChild(document.createTextNode(' ')); return; }
            var s = document.createElement('span'); s.className = 'w'; s.setAttribute('aria-hidden', 'true');
            var t = document.createElement('span'); t.textContent = w; s.appendChild(t); f.appendChild(s);
          });
          n.replaceWith(f);
        } else if (n.nodeType === 1 && n.tagName !== 'BR' && n.tagName !== 'SVG') walk(n);
      });
    })(h);
    h.classList.add('m3-split');
  }

  // mark elements before first paint of JS-driven state
  var FLY = ['.vs-col', '.mc', '.flw', '.emerg', '.rv-two', '.rv-console', '.demo-r', '.cap-col', '.works', '.pl', '.cv', '.ao-inc', '.ao-r', '.final'];
  document.addEventListener('DOMContentLoaded', function () {
    FLY.forEach(function (s) { document.querySelectorAll('main ' + s).forEach(function (e) { e.setAttribute('data-m3-fly', ''); if (e.parentElement) e.parentElement.classList.add('m3-depth'); }); });
    ['.vs-col', '.flw', '.cap-col', '.pl', '.ao-inc', '.ao-r', '.mc'].forEach(function (s) { document.querySelectorAll('main ' + s).forEach(function (e) { e.setAttribute('data-m3-tilt', ''); }); });
    document.querySelectorAll('main h1, main h2').forEach(splitWords);

    if (!window.gsap || !window.ScrollTrigger) return;
    gsap.registerPlugin(ScrollTrigger);
    var full = d.dataset.m3 === 'full';

    // smooth scroll (desktop with a mouse only)
    if (full && window.Lenis) {
      var lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
      window.__lenis = lenis;
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
      gsap.ticker.lagSmoothing(0);
      document.querySelectorAll('a[href^="#"]').forEach(function (a) {
        a.addEventListener('click', function (e) {
          var id = a.getAttribute('href');
          if (id.length > 1 && document.querySelector(id)) { e.preventDefault(); lenis.scrollTo(id, { offset: -80 }); }
        });
      });
    }

    // scroll progress bar
    var bar = document.createElement('div'); bar.className = 'm3-progress'; bar.setAttribute('aria-hidden', 'true'); document.body.appendChild(bar);
    gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: 0.3 } });

    // hero intro (one timeline)
    var tl = gsap.timeline({ defaults: { ease: 'power4.out' } });
    tl.from('.hero .kicker', { y: 14, opacity: 0, duration: 0.6 })
      .from('.hero h1 .w>span', { yPercent: 110, rotateX: -80, opacity: 0, stagger: 0.05, duration: 0.95 }, '-=0.35')
      .from('.hero-lede, .hero-cta, .hero-facts, .hero-call', { y: 18, opacity: 0, stagger: 0.08, duration: 0.7 }, '-=0.6')
      .from('.hero .console', { z: -400, rotateY: -30, rotateX: 12, opacity: 0, duration: 1.3, ease: 'power3.out' }, 0.25)
      .from('.hero .con-steps > li', { x: 24, opacity: 0, stagger: 0.12, duration: 0.6, ease: 'power3.out' }, 0.9);
    window.__m3tl = tl;

    // hero console: resting 3D tilt, follows the mouse, recedes as you scroll away
    var con = document.querySelector('.hero .console');
    if (con && full) {
      gsap.set(con, { rotateY: -12, rotateX: 5, transformPerspective: 1400 });
      var rx = gsap.quickTo(con, 'rotateX', { duration: 0.8, ease: 'power3' });
      var ry = gsap.quickTo(con, 'rotateY', { duration: 0.8, ease: 'power3' });
      document.querySelector('.hero').addEventListener('pointermove', function (e) {
        ry(-12 + (e.clientX / innerWidth - 0.5) * 14); rx(5 - (e.clientY / innerHeight - 0.5) * 10);
      });
      gsap.to(con, { z: -380, rotateX: 26, opacity: 0.15, ease: 'none', immediateRender: false,
        scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 0.8 } });
      gsap.to('.hero-copy', { y: -80, opacity: 0.2, ease: 'none',
        scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 0.8 } });
    }

    // section headings: words flip up
    gsap.utils.toArray('main h2').forEach(function (h) {
      gsap.from(h.querySelectorAll('.w>span'), { yPercent: 105, rotateX: -75, opacity: 0, stagger: 0.04, duration: 0.85, ease: 'power4.out',
        scrollTrigger: { trigger: h, start: 'top 88%', once: true } });
    });

    // cards fly in from depth; on desktop they fall back as you pass
    gsap.utils.toArray('[data-m3-fly]').forEach(function (c, i) {
      var isPlan = c.matches('.pl, .ao-inc, .ao-r, .cv, .final');
      if (full) {
        gsap.fromTo(c, { z: -560, rotateX: 20, rotateY: (i % 2 ? 1 : -1) * 8, opacity: 0 },
          { z: 0, rotateX: 0, rotateY: 0, opacity: 1, ease: 'power2.out',
            scrollTrigger: { trigger: c, start: 'top 100%', end: 'top 64%', scrub: 0.8 } });
        if (!isPlan) gsap.to(c, { z: -200, rotateX: -8, opacity: 0.35, ease: 'none', immediateRender: false,
          scrollTrigger: { trigger: c, start: 'bottom 28%', end: 'bottom -12%', scrub: 0.8 } });
      } else {
        gsap.fromTo(c, { y: 40, rotateX: 12, opacity: 0, transformPerspective: 900 },
          { y: 0, rotateX: 0, opacity: 1, duration: 0.9, ease: 'power3.out', scrollTrigger: { trigger: c, start: 'top 90%', once: true } });
      }
    });

    // 3D tilt with glare + magnetic buttons (mouse only)
    if (finePointer) {
      document.querySelectorAll('[data-m3-tilt]').forEach(function (el) {
        var rX = gsap.quickTo(el, 'rotationX', { duration: 0.5, ease: 'power3' }), rY = gsap.quickTo(el, 'rotationY', { duration: 0.5, ease: 'power3' });
        gsap.set(el, { transformPerspective: 900 });
        el.addEventListener('pointermove', function (e) {
          var r = el.getBoundingClientRect(), px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
          rY((px - 0.5) * 8); rX(-(py - 0.5) * 8);
          el.style.setProperty('--mx', px * 100 + '%'); el.style.setProperty('--my', py * 100 + '%');
        });
        el.addEventListener('pointerleave', function () { rX(0); rY(0); });
      });
      document.querySelectorAll('main .b-lg, .final .b').forEach(function (b) {
        var x = gsap.quickTo(b, 'x', { duration: 0.45, ease: 'power3' }), y = gsap.quickTo(b, 'y', { duration: 0.45, ease: 'power3' });
        b.addEventListener('pointermove', function (e) { var r = b.getBoundingClientRect(); x((e.clientX - r.left - r.width / 2) * 0.2); y((e.clientY - r.top - r.height / 2) * 0.3); });
        b.addEventListener('pointerleave', function () { x(0); y(0); });
      });
    }

    addEventListener('load', function () { ScrollTrigger.refresh(); });
  });
})();
