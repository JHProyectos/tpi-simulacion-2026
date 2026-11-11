const { seg, eo, eio, lerp } = kit;

// Los seis numeros medidos del escenario base. El cuarto y el quinto son los que sostienen la conclusion.
const TARJETAS = [
  ['Espera en la cola previa', '13 min', 0],
  ['Espera en la caja', '< 1 min', 0],
  ['Espera en el mostrador', '8 min', 0],
  ['Utilizaci&oacute;n de la caja', '63 %', 0.63],
  ['Utilizaci&oacute;n del servicio', '94 %', 0.94],
  ['Correlaci&oacute;n con lo real', '0,95', 0],
];
const CLAVE = [3, 4];

kit.scene('numeros', {
  init(kit) {
    kit.css('.numeros-t { position:absolute; width:420px }' +
      '.numeros-barra { height:10px; border-radius:5px; background:var(--hueco); overflow:hidden; margin-top:8px }' +
      '.numeros-relleno { display:block; height:100%; background:var(--marca); transform-origin:left center }' +
      '.numeros-plano { transform-origin:960px 540px; opacity:.2 }');
    const col = [260, 760, 1260], fila = [322, 616];
    const tarjetas = TARJETAS.map((c, i) => '<div class="tarjeta numeros-t" style="left:' + col[i % 3] + 'px; top:' + fila[Math.floor(i / 3)] + 'px">' +
      '<span class="rotulo">' + c[0] + '</span><span class="dato">' + c[1] + '</span>' +
      (c[2] ? '<span class="numeros-barra"><span class="numeros-relleno"></span></span>' : '') + '</div>').join('');
    kit.stage.append(kit.h('<div class="ground">' +
      W.foto(kit, 'amb-mostrador.webp', 'ambiente', 'left:0; top:0; width:1920px; height:1080px') +
      '<svg class="art numeros-grilla" viewBox="0 0 1920 1080">' + W.tramas('numeros') + '</svg>' +
      '<svg class="art numeros-plano" viewBox="0 0 1920 1080">' + '' + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words numeros-cab" style="left:260px; top:150px; width:1200px; gap:10px">' +
      '<h2 class="numeros-titulo">Resultados del escenario base</h2>' +
      '<p class="pendiente numeros-nota">1 CORRIDA MEDIDA &middot; FALTAN LAS 30 R&Eacute;PLICAS DEL EXPERIMENTER</p></div>' +
      tarjetas + '</div>'));
    kit.css('.numeros-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:64px; font-weight:700; margin:0; line-height:1.06 }');
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.numeros-grilla');
    this.plano = q('.numeros-plano');
    this.titulo = q('.numeros-titulo');
    this.nota = q('.numeros-nota');
    this.tarjetas = Array.from(kit.stage.querySelectorAll('.numeros-t'));
    this.barras = this.tarjetas.map((el) => el.querySelector('.numeros-relleno'));
    this.t0 = 2.25;
    this.paso = 2.25;
  },
  render(t) {
    const push = eio(seg(t, 0, 39));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.018, push) + ')';
    this.plano.style.transform = 'scale(' + lerp(1, 1.05, push) + ')';
    this.titulo.style.opacity = eo(seg(t, -0.3, 0.6));
    this.nota.style.opacity = eo(seg(t, 0.8, 1.4)) * 0.9;
    // Pasados los 22 s, lo que no es utilizacion se apaga y quedan los dos numeros que importan.
    const foco = eo(seg(t, 22.5, 24.6));
    this.tarjetas.forEach((el, i) => {
      const a = eo(seg(t, this.t0 + i * this.paso, this.t0 + i * this.paso + 0.55));
      const clave = CLAVE.indexOf(i) >= 0;
      el.style.opacity = a * (clave ? 1 : lerp(1, 0.38, foco));
      el.style.transform = 'translateY(' + lerp(26, 0, a) + 'px) scale(' + (clave ? lerp(1, 1.035, foco) : 1).toFixed(3) + ')';
      const barra = this.barras[i];
      if (barra) barra.style.transform = 'scaleX(' + (TARJETAS[i][2] * eio(seg(t, this.t0 + i * this.paso + 0.4, this.t0 + i * this.paso + 1.5))).toFixed(3) + ')';
    });
  },
});
