const { seg, eo, eio, lerp, TextFx } = kit;

// Cierre de la escena 6: la cola que ya esta antes de que abra la caja.
// Las dos franjas son lo que se observa en el comedor; el modelo cae adentro de las dos.
const X0 = 300, ANCHO = 1320;
const BLOQUES = [
  { rot: 'Personas esperando cuando abre la caja', tope: 100, desde: 60, hasta: 70, top: 352, escala: ['0', '50', '100'], marca: 65, marcaTxt: 'modelo &middot; 65', cls: 'antes-b1' },
  { rot: 'Espera de quien llega antes de abrir', tope: 20, desde: 10, hasta: 15, top: 548, escala: ['0', '10 min', '20 min'], marca: 0, marcaTxt: '', cls: 'antes-b2' },
];
const enX = (v, tope) => X0 + ANCHO * (v / tope);

kit.scene('antes', {
  init(kit) {
    kit.css('.antes-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:58px; font-weight:700; margin:0; line-height:1.06 }' +
      '.antes-rot { position:absolute; font-size:32px; color:var(--second) }' +
      '.antes-pista { position:absolute; height:26px; border-radius:13px; background:var(--hueco) }' +
      '.antes-banda { position:absolute; height:26px; border-radius:13px; background:var(--main); transform-origin:left center }' +
      '.antes-marca { position:absolute; width:5px; height:52px; border-radius:3px; background:var(--marca) }' +
      '.antes-mtxt { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-size:27px; color:var(--marca-texto); letter-spacing:.04em; white-space:nowrap }' +
      '.antes-esc { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-size:25px; color:var(--tenue) }' +
      '.antes-rango { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-size:27px; color:var(--second); letter-spacing:.04em; white-space:nowrap }' +
      '.antes-words .line { font-size:62px }');
    const bloques = BLOQUES.map((b) => {
      const x1 = enX(b.desde, b.tope), x2 = enX(b.hasta, b.tope);
      return '<div class="antes-rot" style="left:' + X0 + 'px; top:' + b.top + 'px">' + b.rot + '</div>' +
        '<div class="antes-pista" style="left:' + X0 + 'px; top:' + (b.top + 54) + 'px; width:' + ANCHO + 'px"></div>' +
        '<div class="antes-banda ' + b.cls + '" style="left:' + x1.toFixed(1) + 'px; top:' + (b.top + 54) + 'px; width:' + (x2 - x1).toFixed(1) + 'px"></div>' +
        '<div class="antes-rango ' + b.cls + '-r" style="left:' + x1.toFixed(1) + 'px; top:' + (b.top + 92) + 'px">' + b.desde + ' a ' + b.hasta + '</div>' +
        (b.marca ? '<div class="antes-marca ' + b.cls + '-m" style="left:' + enX(b.marca, b.tope).toFixed(1) + 'px; top:' + (b.top + 41) + 'px"></div>' +
          '<div class="antes-mtxt ' + b.cls + '-mt" style="left:' + (enX(b.marca, b.tope) + 18).toFixed(1) + 'px; top:' + (b.top + 8) + 'px">' + b.marcaTxt + '</div>' : '') +
        b.escala.map((e, i) => '<div class="antes-esc" style="left:' + (X0 + ANCHO * (i / 2) - (i === 2 ? 70 : 0)).toFixed(0) + 'px; top:' + (b.top + 92) + 'px">' + e + '</div>').join('');
    }).join('');
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
      W.foto(kit, 'amb-aerea.webp', 'ambiente', 'left:0; top:0; width:1920px; height:1080px') +
      '<svg class="art antes-grilla" viewBox="0 0 1920 1080">' + W.tramas('antes') + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words" style="left:300px; top:142px; width:1280px; gap:10px">' +
      '<h2 class="antes-titulo">La fila ya est&aacute; antes de que abra la caja</h2>' +
      '<p class="sub antes-sub">La franja azul es lo que se observa en el comedor</p></div>' +
      bloques +
      '<div class="words antes-words" style="left:300px; bottom:84px; width:1340px">' +
      '<h2 class="line">El modelo cae dentro de las dos.</h2></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    Object.assign(this, {
      grilla: q('.antes-grilla'), titulo: q('.antes-titulo'), sub: q('.antes-sub'), linea: q('.line'),
      bandas: BLOQUES.map((b) => q('.' + b.cls)),
      rangos: BLOQUES.map((b) => q('.' + b.cls + '-r')),
      marca: q('.antes-b1-m'), marcaTxt: q('.antes-b1-mt'),
      rots: Array.from(kit.stage.querySelectorAll('.antes-rot')),
      pistas: Array.from(kit.stage.querySelectorAll('.antes-pista')),
      escalas: Array.from(kit.stage.querySelectorAll('.antes-esc')),
    });
  },
  render(t) {
    const push = eio(seg(t, 0, 12));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.014, push) + ')';
    this.titulo.style.opacity = eo(seg(t, -0.4, 0.6));
    this.sub.style.opacity = eo(seg(t, 0.7, 1.4));
    this.pistas.forEach((el, i) => { el.style.opacity = eo(seg(t, 0.4 + i * 0.5, 1.1 + i * 0.5)) * 0.8; });
    this.rots.forEach((el, i) => { el.style.opacity = eo(seg(t, 0.6 + i * 0.5, 1.2 + i * 0.5)); });
    this.escalas.forEach((el, i) => { el.style.opacity = eo(seg(t, 1 + Math.floor(i / 3) * 0.5 + (i % 3) * 0.14, 1.5 + Math.floor(i / 3) * 0.5 + (i % 3) * 0.14)) * 0.85; });
    // Cada franja crece desde su borde izquierdo, una y despues la otra.
    this.bandas.forEach((el, i) => {
      const a = eio(seg(t, 5 + i * 2, 6.4 + i * 2));
      el.style.transform = 'scaleX(' + a.toFixed(3) + ')';
      this.rangos[i].style.opacity = eo(seg(t, 6.3 + i * 2, 6.9 + i * 2));
    });
    const m = eo(seg(t, 6.8, 7.4));
    this.marca.style.opacity = m;
    this.marca.style.transform = 'scaleY(' + lerp(0.4, 1, eio(seg(t, 6.8, 7.6))).toFixed(3) + ')';
    this.marcaTxt.style.opacity = eo(seg(t, 7.2, 7.8));
    TextFx.fadeFromRight(this.linea, t, 9.9, { stagger: 0.12, dur: 0.6, dx: 28 });
  },
});
