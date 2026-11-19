/* BookedOrion hero 3D scene (Three.js module). Decorative only: aria-hidden canvas behind the hero. */
const d = document.documentElement;
const hero = document.querySelector('.hero');
if (d.dataset.m3 && d.dataset.m3 !== 'off' && d.dataset.m3gl !== 'none' && hero) {
  const THREE = await import('three');
  const { RoundedBoxGeometry } = await import('three/addons/geometries/RoundedBoxGeometry.js');
  const { RoomEnvironment } = await import('three/addons/environments/RoomEnvironment.js');

  const full = d.dataset.m3 === 'full';
  const mobile = !matchMedia('(min-width: 901px)').matches;
  const canvas = document.createElement('canvas');
  canvas.id = 'hero3d'; canvas.setAttribute('aria-hidden', 'true');
  hero.prepend(canvas);

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: !mobile, alpha: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(devicePixelRatio, mobile ? 1.5 : 1.75));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
  renderer.setClearColor(0x000000, 0);
  const scene = new THREE.Scene();
  const pm = new THREE.PMREMGenerator(renderer);
  scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
  const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 80);

  const C = { indigo: 0x3f37c9, indigoDk: 0x332ca8, night: 0x1d1b4b, mint: 0x2bd9a0, mintDk: 0x0a7a55, line: 0xe4e6ee };
  const M = {
    indigo: new THREE.MeshPhysicalMaterial({ color: C.indigo, roughness: 0.25, metalness: 0.2, clearcoat: 1, clearcoatRoughness: 0.15 }),
    mint: new THREE.MeshPhysicalMaterial({ color: C.mint, roughness: 0.2, metalness: 0.1, clearcoat: 1, clearcoatRoughness: 0.1, emissive: C.mint, emissiveIntensity: 0.15 }),
    white: new THREE.MeshPhysicalMaterial({ color: 0xffffff, roughness: 0.3, metalness: 0, clearcoat: 0.6 }),
    night: new THREE.MeshPhysicalMaterial({ color: C.night, roughness: 0.35, metalness: 0.4, clearcoat: 0.8 }),
    glass: new THREE.MeshPhysicalMaterial({ color: 0xdcd9ff, roughness: 0.05, transmission: 0.95, thickness: 0.8, ior: 1.45, transparent: true }),
  };

  function labelTexture(draw, w = 512, h = 256) {
    const c = document.createElement('canvas'); c.width = w; c.height = h; const x = c.getContext('2d'); draw(x, w, h);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t;
  }
  const FONT = '"Plus Jakarta Sans", system-ui, sans-serif';

  /* 1. BookedOrion mark: mint ring + white check, glossy */
  const mark = new THREE.Group();
  mark.add(new THREE.Mesh(new THREE.TorusGeometry(1, 0.26, 32, 96), M.mint));
  const checkPath = new THREE.CatmullRomCurve3([new THREE.Vector3(-0.42, 0.02, 0), new THREE.Vector3(-0.12, -0.3, 0), new THREE.Vector3(0.5, 0.42, 0)], false, 'catmullrom', 0.0);
  const check = new THREE.Mesh(new THREE.TubeGeometry(checkPath, 48, 0.13, 16), M.night);
  const capG = new THREE.SphereGeometry(0.13, 20, 20);
  [checkPath.points[0], checkPath.points[2]].forEach(p => { const s = new THREE.Mesh(capG, M.night); s.position.copy(p); check.add(s); });
  mark.add(check);

  /* 2. booked-visit card */
  const cal = new THREE.Group();
  const calBody = new THREE.Mesh(new RoundedBoxGeometry(2.3, 1.25, 0.16, 4, 0.12), M.white);
  const calFace = new THREE.Mesh(new THREE.PlaneGeometry(2.14, 1.1), new THREE.MeshBasicMaterial({ transparent: true, map: labelTexture((x, w, h) => {
    x.fillStyle = '#E6F7F0'; x.beginPath(); x.roundRect(18, 30, 150, 196, 22); x.fill();
    x.fillStyle = '#0A7A55'; x.font = `800 40px ${FONT}`; x.textAlign = 'center'; x.fillText('WED', 93, 118);
    x.font = `800 64px ${FONT}`; x.fillText('8', 93, 190);
    x.textAlign = 'left'; x.fillStyle = '#15133A'; x.font = `800 46px ${FONT}`; x.fillText('Visit booked', 196, 100);
    x.fillStyle = '#55576F'; x.font = `600 32px ${FONT}`; x.fillText('8:00–10:00 AM', 196, 150); x.fillText('AC repair', 196, 194);
  }) }));
  calFace.position.z = 0.081; cal.add(calBody, calFace);

  /* 3. text bubble to the owner */
  const sms = new THREE.Group();
  const smsBody = new THREE.Mesh(new RoundedBoxGeometry(2.2, 0.9, 0.14, 4, 0.2), M.indigo);
  const tail = new THREE.Mesh(new THREE.ConeGeometry(0.16, 0.34, 3), M.indigo); tail.position.set(-0.78, -0.5, 0); tail.rotation.z = Math.PI * 0.85;
  const smsFace = new THREE.Mesh(new THREE.PlaneGeometry(2.0, 0.78), new THREE.MeshBasicMaterial({ transparent: true, map: labelTexture((x, w, h) => {
    x.fillStyle = '#FFFFFF'; x.font = `800 44px ${FONT}`; x.fillText('New job booked ✓', 26, 92);
    x.fillStyle = 'rgba(255,255,255,.78)'; x.font = `600 30px ${FONT}`; x.fillText('Maria G. · Wed 8–10 AM', 26, 152);
  }, 512, 200) }));
  smsFace.position.z = 0.071; sms.add(smsBody, tail, smsFace);

  /* 4. voice bars (Molly talking) */
  const voice = new THREE.Group(); const barG = new RoundedBoxGeometry(0.22, 1, 0.22, 3, 0.1); const bars = [];
  for (let i = 0; i < 7; i++) { const b = new THREE.Mesh(barG, i % 2 ? M.indigo : M.mint); b.position.x = (i - 3) * 0.34; voice.add(b); bars.push(b); }

  /* 5. call pulse rings */
  const rings = []; const ringMat = new THREE.MeshBasicMaterial({ color: C.mint, transparent: true, side: THREE.DoubleSide, depthWrite: false });
  const pulse = new THREE.Group();
  for (let i = 0; i < 3; i++) { const r = new THREE.Mesh(new THREE.RingGeometry(0.95, 1.0, 96), ringMat.clone()); pulse.add(r); rings.push(r); }
  const phone = new THREE.Mesh(new RoundedBoxGeometry(0.62, 1.15, 0.12, 4, 0.12), M.night);
  const scr = new THREE.Mesh(new THREE.PlaneGeometry(0.5, 0.95), new THREE.MeshBasicMaterial({ map: labelTexture((x, w, h) => {
    const g = x.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#3F37C9'); g.addColorStop(1, '#1D1B4B'); x.fillStyle = g; x.fillRect(0, 0, w, h);
    x.fillStyle = '#2BD9A0'; x.beginPath(); x.arc(w / 2, h * 0.78, 34, 0, 7); x.fill();
    x.fillStyle = '#fff'; x.textAlign = 'center'; x.font = `800 34px ${FONT}`; x.fillText('Molly', w / 2, h * 0.28); x.font = `600 22px ${FONT}`; x.fillStyle = 'rgba(255,255,255,.75)'; x.fillText('answering…', w / 2, h * 0.36);
  }, 256, 480) }));
  scr.position.z = 0.061; phone.add(scr); pulse.add(phone);

  /* 6. Orion constellation + star dust */
  const stars = new THREE.Group();
  const orion = [[-1.6, 2.2], [1.3, 2.0], [-0.45, 0.15], [0, 0], [0.45, -0.15], [-1.2, -2.2], [1.5, -2.0]];
  const starMat = new THREE.MeshBasicMaterial({ color: C.indigo });
  orion.forEach(([x, y], i) => { const s = new THREE.Mesh(new THREE.IcosahedronGeometry(i === 0 ? 0.11 : 0.08, 2), i === 0 ? new THREE.MeshBasicMaterial({ color: C.mint }) : starMat); s.position.set(x, y, 0); stars.add(s); });
  const links = [[0, 2], [1, 4], [2, 3], [3, 4], [2, 5], [4, 6], [0, 1]];
  const lg = new THREE.BufferGeometry().setFromPoints(links.flatMap(([a, b]) => [new THREE.Vector3(...orion[a], 0), new THREE.Vector3(...orion[b], 0)]));
  stars.add(new THREE.LineSegments(lg, new THREE.LineBasicMaterial({ color: C.indigo, transparent: true, opacity: 0.22 })));
  const N = mobile ? 160 : 420, pos = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) { pos[i * 3] = (Math.random() - 0.5) * 26; pos[i * 3 + 1] = (Math.random() - 0.5) * 14; pos[i * 3 + 2] = -Math.random() * 22 + 4; }
  const dg = new THREE.BufferGeometry(); dg.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const dotTex = labelTexture((x, w, h) => { const g = x.createRadialGradient(32, 32, 0, 32, 32, 32); g.addColorStop(0, 'rgba(63,55,201,1)'); g.addColorStop(1, 'rgba(63,55,201,0)'); x.fillStyle = g; x.fillRect(0, 0, 64, 64); }, 64, 64);
  const dust = new THREE.Points(dg, new THREE.PointsMaterial({ size: mobile ? 0.05 : 0.07, map: dotTex, transparent: true, opacity: mobile ? 0.35 : 0.55, depthWrite: false }));
  scene.add(dust);

  const objs = [mark, cal, sms, voice, pulse, stars];
  objs.forEach(o => scene.add(o));

  /* layout: objects sit around the console (right column); recomputed on resize */
  const home = new Map();
  function layout() {
    const w = hero.clientWidth, h = hero.clientHeight;
    renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix();
    const dist = 12, vh = 2 * dist * Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)), vw = vh * camera.aspect;
    const con = hero.querySelector('.console'); const hr = hero.getBoundingClientRect(); const cr = con ? con.getBoundingClientRect() : null;
    const toWorld = (px, py) => [(px / w - 0.5) * vw, -(py / h - 0.5) * vh];
    let L;
    if (!mobile && cr) {
      const [cx, cy] = toWorld(cr.left - hr.left + cr.width / 2, cr.top - hr.top + cr.height / 2);
      const cw = cr.width / w * vw, ch = cr.height / h * vh;
      L = {
        mark: [cx - cw / 2 - 0.35, cy + ch * 0.18, -0.9, 0.82],
        cal: [cx + cw / 2 - 0.55, cy - ch / 2 + 0.05, 0.5, 0.68],
        sms: [cx + cw / 2 + 0.15, cy + ch * 0.3, -1.6, 0.72],
        voice: [cx - cw / 2 - 0.55, cy - ch / 2 + 0.2, -1.2, 0.78],
        pulse: [cx + cw * 0.05, cy + ch / 2 + 0.45, -3.5, 0.85],
        stars: [cx - cw * 0.2, cy, -9, 1.6],
      };
    } else {
      L = {
        mark: [0, 0, -40, 0.001], cal: [0, 0, -40, 0.001], sms: [0, 0, -40, 0.001],
        voice: [0, 0, -40, 0.001], pulse: [0, 0, -40, 0.001], stars: [0, 0, -40, 0.001],
      };
    }
    [['mark', mark], ['cal', cal], ['sms', sms], ['voice', voice], ['pulse', pulse], ['stars', stars]].forEach(([k, o]) => {
      const [x, y, z, s] = L[k]; o.position.set(x, y, z); o.scale.setScalar(s); home.set(o, { x, y, z, ph: Math.random() * 6 });
    });
  }
  camera.position.set(0, 0, 12);

  scene.add(new THREE.HemisphereLight(0xffffff, 0xe6e4ff, 1.2));
  const key = new THREE.DirectionalLight(0xffffff, 2.2); key.position.set(-4, 6, 8); scene.add(key);
  const rim = new THREE.PointLight(C.mint, 25, 20, 1.5); rim.position.set(6, -2, 4); scene.add(rim);
  const rim2 = new THREE.PointLight(C.indigo, 30, 20, 1.5); rim2.position.set(-6, 3, 3); scene.add(rim2);

  /* scroll: camera flies forward through the scene as the hero leaves the screen */
  const qs = new URLSearchParams(location.search);
  const st = { p: 0 }, mouse = { x: 0, y: 0, sx: 0, sy: 0 };
  if (full) addEventListener('pointermove', e => { mouse.x = e.clientX / innerWidth - 0.5; mouse.y = e.clientY / innerHeight - 0.5; });
  let visible = true, running = true;
  new IntersectionObserver(es => { visible = es[0].isIntersecting; }).observe(hero);
  document.addEventListener('visibilitychange', () => { running = !document.hidden; });
  const clock = new THREE.Clock();
  function frame() {
    if (!running || !visible) { clock.getDelta(); return; }
    const dt = Math.min(clock.getDelta(), 0.05), t = clock.elapsedTime;
    const target = qs.has('p') ? +qs.get('p') : Math.min(1, Math.max(0, scrollY / hero.offsetHeight));
    st.p += (target - st.p) * 0.1;
    mouse.sx += (mouse.x - mouse.sx) * 0.05; mouse.sy += (mouse.y - mouse.sy) * 0.05;
    camera.position.set(mouse.sx * 0.9, -mouse.sy * 0.6 - st.p * 1.2, 12 - st.p * (full ? 13 : 8));
    camera.lookAt(mouse.sx * 0.3, -st.p * 1.5, -6);
    objs.forEach((o, i) => {
      const h = home.get(o); if (!h) return;
      const spread = st.p * (full ? 2.2 : 1.2);
      o.position.x = h.x * (1 + spread * 0.35); o.position.y = h.y + Math.sin(t * 0.9 + h.ph) * 0.12 + (h.y > 0 ? spread : -spread) * 0.6; o.position.z = h.z;
      o.visible = o.position.distanceTo(camera.position) > 1.8;
    });
    mark.rotation.set(Math.sin(t * 0.6) * 0.25 + mouse.sy * 0.4, t * 0.5 + mouse.sx * 0.8, 0);
    cal.rotation.set(-0.15 + Math.sin(t * 0.7) * 0.08, -0.45 + Math.sin(t * 0.5) * 0.12 + mouse.sx * 0.4, 0.06);
    sms.rotation.set(0.1, 0.35 + Math.sin(t * 0.6 + 1) * 0.12 + mouse.sx * 0.4, -0.05);
    voice.rotation.set(0.2, 0.5 + mouse.sx * 0.5, 0);
    bars.forEach((b, i) => { b.scale.y = 0.35 + Math.abs(Math.sin(t * 3.2 + i * 0.75)) * (i === 3 ? 1.4 : 1.0); });
    pulse.rotation.set(0, -0.3 + mouse.sx * 0.4, 0);
    rings.forEach((r, i) => { const k = ((t * 0.55 + i / 3) % 1); r.scale.setScalar(0.6 + k * 1.6); r.material.opacity = (1 - k) * 0.5; });
    phone.rotation.z = Math.sin(t * 9) * 0.04 * (Math.sin(t * 1.3) > 0.4 ? 1 : 0);
    stars.rotation.set(0, Math.sin(t * 0.1) * 0.15 + mouse.sx * 0.2, Math.sin(t * 0.07) * 0.05);
    dust.rotation.y = t * 0.01;
    renderer.render(scene, camera);
  }
  const ready = () => { layout(); canvas.classList.add('ready'); window.__m3gl = true; };
  addEventListener('resize', layout);
  if (document.readyState === 'complete') ready(); else addEventListener('load', ready);
  setTimeout(layout, 1600); // after the console intro animation
  renderer.setAnimationLoop(frame);
}
