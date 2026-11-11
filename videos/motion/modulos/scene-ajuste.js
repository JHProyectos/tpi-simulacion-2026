const { seg, eo, eio, lerp } = kit;

// Bondad de ajuste de las llegadas: las seis franjas del turno contra un reparto
// parejo. Los numeros salen de la seccion 7.1 de entregas/entrega-final/INFORME.md.
// Los segundos salen de la transcripcion por palabra de
// videos/audios/jonatan/jonatan-e10-ajuste.wav.
const FRANJAS = [['12:00', 304], ['12:30', 236], ['13:00', 276], ['13:30', 191], ['14:00', 163], ['14:30', 5]];
const ESPERADAS = 195.83;
const BASE_Y = 872, X0 = 196, PASO = 162, ANCHO = 112, ESCALA = 1.625;
// Las dos franjas que la voz nombra: la primera media hora y la ultima.
const DESTACADAS = [[0, 20.1], [5, 22.8]];
// Cada renglon de la placa, con el segundo en que Jonatan lo dice.
const PLACA = [
  [7.5, 'Raciones del d&iacute;a', '1.175'],
  [15.1, '&chi;&sup2; calculado', '292,39'],
  [17.4, '&chi;&sup2; cr&iacute;tico &middot; 5 g.l. &middot; &alpha; = 0,05', '11,07'],
];

kit.scene('ajuste', {
  init(kit) {
    kit.css('.ajuste-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:68px; font-weight:700; line-height:1.06; margin:0; color:var(--tinta) }' +
      '.ajuste-caja { position:absolute; left:1250px; top:330px; width:520px }' +
      '.ajuste-fila { display:flex; justify-content:space-between; align-items:baseline; gap:24px; padding:17px 0; border-top:1px solid var(--borde) }' +
      '.ajuste-valor { font-family:var(--mono, ui-monospace, monospace); font-variant-numeric:tabular-nums; font-size:48px; font-weight:700; color:var(--tinta); line-height:1 }' +
      '.ajuste-sello { font-family:var(--mono, ui-monospace, monospace); font-size:34px; letter-spacing:.09em; color:var(--marca-texto); margin-top:26px }' +
      '.ajuste-remate { font-size:30px; color:var(--tenue); margin-top:10px; line-height:1.3 }' +
      '.ajuste-pie { position:absolute; left:196px; top:946px; width:1000px; font-size:32px; color:var(--tinta); line-height:1.3 }' +
      '.ajuste-fuente { position:absolute; left:1250px; top:966px }');
    const barras = FRANJAS.map((f, i) => {
      const x = X0 + i * PASO;
      return '<g class="ajuste-barra">' +
        '<rect class="ajuste-cuerpo" x="' + x + '" y="' + BASE_Y + '" width="' + ANCHO + '" height="0" rx="4" style="fill:var(--linea)"/>' +
        '<rect class="ajuste-foco" x="' + x + '" y="' + BASE_Y + '" width="' + ANCHO + '" height="0" rx="4" style="fill:var(--marca);opacity:0"/>' +
        '<text class="ajuste-cifra" x="' + (x + ANCHO / 2) + '" y="' + (BASE_Y - 16) + '" text-anchor="middle" style="fill:var(--tinta);font-size:36px;font-weight:700;font-family:var(--mono, ui-monospace, monospace)">' + f[1] + '</text>' +
        '<text x="' + (x + ANCHO / 2) + '" y="918" text-anchor="middle" style="fill:var(--tenue);font-size:28px;font-family:var(--mono, ui-monospace, monospace)">' + f[0] + '</text></g>';
    }).join('');
    const yEsp = (BASE_Y - ESPERADAS * ESCALA).toFixed(1);
    const filas = PLACA.map((p) => '<div class="ajuste-fila"><span class="rotulo">' + p[1] + '</span>' +
      '<span class="ajuste-valor">' + p[2] + '</span></div>').join('');
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
      '<svg class="art ajuste-grilla" viewBox="0 0 1920 1080">' + W.tramas('ajuste') + '</svg>' +
      '<svg class="art" viewBox="0 0 1920 1080">' +
      '<path class="ajuste-eje" d="M' + (X0 - 40) + ' 352 V' + BASE_Y + ' H1160" style="fill:none;stroke:var(--borde);stroke-width:3"/>' +
      barras +
      '<g class="ajuste-esperadas"><path d="M' + (X0 - 40) + ' ' + yEsp + ' H1160" style="fill:none;stroke:var(--marca);stroke-width:3;stroke-dasharray:14 12"/>' +
      '<text x="1160" y="' + (Number(yEsp) - 18) + '" text-anchor="end" style="fill:var(--marca-texto);font-size:27px;letter-spacing:.04em">reparto parejo &middot; 196 por franja</text></g>' +
      '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words ajuste-cab" style="left:196px; top:150px; width:980px; gap:14px">' +
      '<h2 class="ajuste-titulo">&iquest;La gente llega pareja a lo largo del turno?</h2>' +
      '<p class="sub ajuste-sub">Raciones consumidas el 1 de julio de 2026, un d&iacute;a de perfil pico, en seis franjas de media hora.</p></div>' +
      '<div class="ajuste-caja"><div class="ajuste-filas">' + filas + '</div>' +
      '<p class="ajuste-sello">SE RECHAZA H&#8320;</p>' +
      '<p class="ajuste-remate">Las llegadas no se reparten parejo: la demanda se concentra al principio del turno.</p></div>' +
      '<p class="ajuste-pie">Por eso el modelo no usa una tasa &uacute;nica: usa una por franja de diez minutos y por grupo.</p>' +
      '<div class="etiqueta ajuste-fuente">Registros de reservas &middot; <span class="num">1.175</span> raciones</div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.ajuste-grilla');
    this.titulo = q('.ajuste-titulo');
    this.sub = q('.ajuste-sub');
    this.eje = q('.ajuste-eje');
    this.esperadas = q('.ajuste-esperadas');
    this.cuerpos = Array.from(kit.stage.querySelectorAll('.ajuste-cuerpo'));
    this.focos = Array.from(kit.stage.querySelectorAll('.ajuste-foco'));
    this.cifras = Array.from(kit.stage.querySelectorAll('.ajuste-cifra'));
    this.filas = Array.from(kit.stage.querySelectorAll('.ajuste-fila'));
    this.sello = q('.ajuste-sello');
    this.remate = q('.ajuste-remate');
    this.pie = q('.ajuste-pie');
    this.fuente = q('.ajuste-fuente');
  },
  render(t) {
    const push = eio(seg(t, 0, 33));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.02, push) + ')';
    this.titulo.style.opacity = eo(seg(t, 0, 0.9));
    this.sub.style.opacity = eo(seg(t, 4.8, 5.8));
    this.eje.style.opacity = eo(seg(t, 8.4, 9.4));
    FRANJAS.forEach((f, i) => {
      const t0 = 9.9 + i * 0.28;
      const a = eio(seg(t, t0, t0 + 0.6));
      const h = f[1] * ESCALA * a;
      const y = (BASE_Y - h).toFixed(1);
      this.cuerpos[i].setAttribute('y', y);
      this.cuerpos[i].setAttribute('height', h.toFixed(1));
      this.focos[i].setAttribute('y', y);
      this.focos[i].setAttribute('height', h.toFixed(1));
      this.cifras[i].setAttribute('y', (BASE_Y - h - 16).toFixed(1));
      this.cifras[i].style.opacity = eo(seg(t, t0 + 0.5, t0 + 1.1));
    });
    DESTACADAS.forEach((d) => { this.focos[d[0]].style.opacity = eo(seg(t, d[1], d[1] + 0.7)); });
    this.esperadas.style.opacity = eo(seg(t, 12, 13));
    this.filas.forEach((el, i) => {
      const a = eo(seg(t, PLACA[i][0], PLACA[i][0] + 0.6));
      el.style.opacity = a;
      el.style.transform = 'translateX(' + lerp(30, 0, a) + 'px)';
    });
    this.sello.style.opacity = eo(seg(t, 18.1, 18.8));
    this.remate.style.opacity = eo(seg(t, 19.2, 20.1));
    this.pie.style.opacity = eo(seg(t, 25.1, 26));
    this.fuente.style.opacity = eo(seg(t, 30, 30.9)) * 0.9;
  },
});
