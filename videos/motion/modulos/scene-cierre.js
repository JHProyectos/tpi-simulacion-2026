const { seg, eo, eio, lerp } = kit;

// Placa final: el salon vuelve, mas cerca y muy apagado, y queda el nombre del trabajo.
kit.scene('cierre', {
  init(kit) {
    kit.css('.cierre-foto { transform-origin:66% 42% }' +
      '.cierre-words .line { font-size:96px }' +
      '.cierre-regla { position:absolute; left:300px; top:404px; width:170px; height:7px; background:var(--marca); transform-origin:left center }');
    kit.stage.append(kit.h('<div class="ground">' +
      W.foto(kit, 'sala.webp', 'cierre-foto', 'left:0; top:0; width:1920px; height:1080px') +
      '<div class="calm cierre-velo"></div><div class="edge"></div>' +
      '<div class="cierre-regla"></div>' +
      '<div class="words cierre-words" style="left:300px; top:462px; width:1200px; gap:18px">' +
      '<h2 class="line">Simulaci&oacute;n 2026</h2>' +
      '<p class="sub cierre-sub">Trabajo integrador: la fila de un comedor universitario</p>' +
      '<p class="sub cierre-falta">Jonatan Harbertz &middot; Juan Ch&aacute;vez</p></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.foto = q('.cierre-foto');
    this.velo = q('.cierre-velo');
    this.regla = q('.cierre-regla');
    this.linea = q('.line');
    this.sub = q('.cierre-sub');
    this.falta = q('.cierre-falta');
  },
  render(t) {
    const push = eio(seg(t, 0, 8));
    this.foto.style.transform = 'scale(' + lerp(1.16, 1.22, push).toFixed(4) + ')';
    this.velo.style.opacity = lerp(0.84, 0.92, push);
    this.regla.style.transform = 'scaleX(' + eo(seg(t, -0.2, 0.7)).toFixed(3) + ')';
    this.linea.style.opacity = eo(seg(t, -0.3, 0.7));
    this.linea.style.transform = 'translateY(' + lerp(16, 0, eo(seg(t, -0.3, 0.9))) + 'px)';
    this.sub.style.opacity = eo(seg(t, 0.8, 1.5));
    this.falta.style.opacity = eo(seg(t, 1.6, 2.2));
  },
});
