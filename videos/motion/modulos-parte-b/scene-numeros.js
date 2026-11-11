const { seg, eo, eio, lerp } = kit;

// Primera mitad de la escena 6: la placa del escenario base, con los numeros del Experimenter.
// Las dos colas son las que sostienen el resto del video, asi que al final quedan solas encendidas.
const TARJETAS = [
  ['Espera m&aacute;xima en la caja', '4,9 min', '&plusmn; 0,2', 0],
  ['Cola m&aacute;xima en la caja', '71 personas', '&plusmn; 3', 0],
  ['Tiempo total medio', '68 s', '&plusmn; 5 s', 0],
  ['Cola m&aacute;xima en el mostrador', '5 personas', '', 0],
  ['Utilizaci&oacute;n de la caja', '63 %', '', 0.63],
  ['Correlaci&oacute;n con lo real', '0,95', '', 0],
];
const CLAVE = [1, 3];

kit.scene('numeros', {
  init(kit) {
    kit.css('.numeros-t { position:absolute; width:420px }' +
      '.numeros-barra { height:10px; border-radius:5px; background:var(--hueco); overflow:hidden; margin-top:8px }' +
      '.numeros-relleno { display:block; height:100%; background:var(--marca); transform-origin:left center }' +
      '.numeros-ic { font-family:var(--mono, ui-monospace, monospace); font-size:25px; color:var(--tenue); letter-spacing:.04em }' +
      '.numeros-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:64px; font-weight:700; margin:0; line-height:1.06 }');
    const col = [260, 760, 1260], fila = [360, 654];
    const tarjetas = TARJETAS.map((c, i) => '<div class="tarjeta numeros-t" style="left:' + col[i % 3] + 'px; top:' + fila[Math.floor(i / 3)] + 'px">' +
      '<span class="rotulo">' + c[0] + '</span><span class="dato">' + c[1] + '</span>' +
      (c[2] ? '<span class="numeros-ic">' + c[2] + '</span>' : '') +
      (c[3] ? '<span class="numeros-barra"><span class="numeros-relleno"></span></span>' : '') + '</div>').join('');
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
      W.foto(kit, 'amb-mostrador.webp', 'ambiente', 'left:0; top:0; width:1920px; height:1080px') +
      '<svg class="art numeros-grilla" viewBox="0 0 1920 1080">' + W.tramas('numeros') + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words numeros-cab" style="left:260px; top:144px; width:1280px; gap:12px">' +
      '<h2 class="numeros-titulo">Resultados del escenario base</h2>' +
      '<p class="sub numeros-sub">E0 &middot; 1 puesto de caja y 3 personas sirviendo &middot; 30 r&eacute;plicas</p></div>' +
      tarjetas +
      '<p class="pendiente numeros-nota" style="position:absolute; left:260px; bottom:96px">30 R&Eacute;PLICAS &middot; PERFIL PICO &middot; INTERVALOS AL 95 %</p></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.numeros-grilla');
    this.titulo = q('.numeros-titulo');
    this.sub = q('.numeros-sub');
    this.nota = q('.numeros-nota');
    this.tarjetas = Array.from(kit.stage.querySelectorAll('.numeros-t'));
    this.barras = this.tarjetas.map((el) => el.querySelector('.numeros-relleno'));
    this.t0 = 1.4;
    this.paso = 1.7;
  },
  render(t) {
    const push = eio(seg(t, 0, 15));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.018, push) + ')';
    this.titulo.style.opacity = eo(seg(t, -0.3, 0.6));
    this.sub.style.opacity = eo(seg(t, 0.7, 1.4));
    this.nota.style.opacity = eo(seg(t, 1.6, 2.3)) * 0.9;
    // Cuando la voz termina se apaga lo demas y quedan las dos colas, 71 contra 5.
    const foco = eo(seg(t, 11.8, 13.3));
    this.tarjetas.forEach((el, i) => {
      const a = eo(seg(t, this.t0 + i * this.paso, this.t0 + i * this.paso + 0.55));
      const clave = CLAVE.indexOf(i) >= 0;
      el.style.opacity = a * (clave ? 1 : lerp(1, 0.32, foco));
      el.style.transform = 'translateY(' + lerp(26, 0, a) + 'px) scale(' + (clave ? lerp(1, 1.045, foco) : 1).toFixed(3) + ')';
      const barra = this.barras[i];
      if (barra) barra.style.transform = 'scaleX(' + (TARJETAS[i][3] * eio(seg(t, this.t0 + i * this.paso + 0.4, this.t0 + i * this.paso + 1.5))).toFixed(3) + ')';
    });
  },
});
