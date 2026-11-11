const { seg, eo, eio, lerp } = kit;

// Los cinco escenarios alternativos. El resultado de cada uno queda como hueco: el Experimenter todavia no corrio.
const ESCENARIOS = [
  ['E1', 'Dos puestos de caja todo el turno'],
  ['E2', 'Dos puestos solo en el pico, de 12:00 a 13:30'],
  ['E3', 'Validaci&oacute;n por c&oacute;digo QR: 60 % del tiempo del DNI'],
  ['E4', 'Un puesto de caja y cuatro personas sirviendo'],
  ['E5', 'Dos puestos y cuatro personas sirviendo'],
];

kit.scene('cambios', {
  init(kit) {
    kit.css('.cambios-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:62px; font-weight:700; margin:0; line-height:1.06 }' +
      '.cambios-fila { position:absolute; left:300px; width:1320px; display:flex; align-items:center; gap:30px; padding:20px 28px; box-sizing:border-box; background:var(--panel); border:1px solid var(--borde); border-radius:10px }' +
      '.cambios-cod { font-family:var(--mono, ui-monospace, monospace); font-size:44px; font-weight:700; color:var(--marca); flex:none; min-width:76px }' +
      '.cambios-desc { font-size:34px; flex:1; color:var(--second) }' +
      '.cambios-hueco { font-family:var(--mono, ui-monospace, monospace); font-size:26px; color:var(--marca); letter-spacing:.08em; border:1px dashed var(--borde); border-radius:6px; padding:9px 18px; flex:none }' +
      '.cambios-plano { transform-origin:960px 540px; opacity:.16 }');
    const filas = ESCENARIOS.map((e, i) => '<div class="cambios-fila" style="top:' + (344 + i * 104) + 'px">' +
      '<span class="cambios-cod">' + e[0] + '</span><span class="cambios-desc">' + e[1] + '</span>' +
      '<span class="cambios-hueco">RESULTADO PENDIENTE</span></div>').join('');
    kit.stage.append(kit.h('<div class="ground">' +
      W.foto(kit, 'amb-servicio.webp', 'ambiente', 'left:0; top:0; width:1920px; height:1080px') +
      '<svg class="art cambios-grilla" viewBox="0 0 1920 1080">' + W.tramas('cambios') + '</svg>' +
      '<svg class="art cambios-plano" viewBox="0 0 1920 1080">' + '' + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words" style="left:300px; top:168px; width:1300px; gap:8px">' +
      '<h2 class="cambios-titulo">Cinco cambios sobre la base</h2>' +
      '<p class="sub cambios-sub">En cada uno se modifica una sola cosa, as&iacute; se sabe qu&eacute; causa la diferencia.</p></div>' +
      filas +
      '<div class="pendiente cambios-nota" style="position:absolute; left:300px; top:898px">E4 Y E5: DEFINICI&Oacute;N A CONFIRMAR CONTRA LA TABLA DE ESCENARIOS</div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.cambios-grilla');
    this.plano = q('.cambios-plano');
    this.titulo = q('.cambios-titulo');
    this.sub = q('.cambios-sub');
    this.nota = q('.cambios-nota');
    this.filas = Array.from(kit.stage.querySelectorAll('.cambios-fila'));
    this.huecos = this.filas.map((el) => el.querySelector('.cambios-hueco'));
    this.t0 = 2.2;
    this.paso = 2.6;
  },
  render(t) {
    const push = eio(seg(t, 0, 27));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.016, push) + ')';
    this.plano.style.transform = 'scale(' + lerp(1, 1.05, push) + ')';
    this.titulo.style.opacity = eo(seg(t, -0.3, 0.6));
    this.sub.style.opacity = eo(seg(t, 0.7, 1.3));
    this.filas.forEach((el, i) => {
      const t0 = this.t0 + i * this.paso, a = eo(seg(t, t0, t0 + 0.55));
      el.style.opacity = a;
      el.style.transform = 'translateX(' + lerp(44, 0, a) + 'px)';
      this.huecos[i].style.opacity = eo(seg(t, t0 + 0.5, t0 + 1.1)) * (0.68 + 0.2 * Math.sin((t - t0) * 1.5));
    });
    this.nota.style.opacity = eo(seg(t, 16.2, 17.3)) * 0.9;
  },
});
