const { seg, eo, eio, lerp, TextFx } = kit;

// Vuelve la pregunta, mas chica, y debajo queda el lugar de la respuesta. No se escribe hasta tener los resultados.
kit.scene('respuesta', {
  init(kit) {
    kit.css('.respuesta-pregunta { font-size:40px; line-height:1.3; color:var(--tenue); margin:0 }' +
      '.respuesta-regla { position:absolute; left:300px; top:368px; width:1320px; height:2px; background:var(--borde); transform-origin:left center }' +
      '.respuesta-caja { position:absolute; left:300px; top:428px; width:1320px; height:236px; box-sizing:border-box; border:2px dashed var(--borde); border-radius:12px; display:flex; align-items:center; justify-content:center; transform-origin:center }' +
      '.respuesta-falta { font-family:var(--mono, ui-monospace, monospace); font-size:34px; letter-spacing:.1em; color:var(--marca); text-align:center }' +
      '.respuesta-plano { transform-origin:960px 540px; opacity:.12 }');
    kit.stage.append(kit.h('<div class="ground">' +
      W.foto(kit, 'amb-caja.webp', 'ambiente', 'left:0; top:0; width:1920px; height:1080px') +
      '<svg class="art respuesta-grilla" viewBox="0 0 1920 1080">' + W.tramas('respuesta') + '</svg>' +
      '<svg class="art respuesta-plano" viewBox="0 0 1920 1080">' + '' + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words" style="left:300px; top:168px; width:1320px; gap:14px">' +
      '<p class="rotulo respuesta-rotulo">La pregunta del principio</p>' +
      '<p class="respuesta-pregunta">&iquest;Qu&eacute; combinaci&oacute;n de puestos de validaci&oacute;n y personas en el servicio reduce el tiempo total en el pico, sin trasladar la cola al mostrador?</p></div>' +
      '<div class="respuesta-regla"></div>' +
      '<div class="respuesta-caja"><span class="respuesta-falta">LA RESPUESTA SE ESCRIBE CUANDO EST&Eacute;N LOS SEIS ESCENARIOS</span></div>' +
      '<div class="words" style="left:300px; top:716px; width:1320px; gap:16px">' +
      '<p class="sub respuesta-d1">Lo &uacute;nico medido hasta ahora es el escenario base: la caja al 63 % y el servicio al 94 %.</p>' +
      '<p class="sub respuesta-d2">L&iacute;mite del estudio: el tiempo de servicio por raci&oacute;n no se pudo cronometrar y queda como supuesto.</p></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    Object.assign(this, {
      grilla: q('.respuesta-grilla'), plano: q('.respuesta-plano'), rotulo: q('.respuesta-rotulo'),
      pregunta: q('.respuesta-pregunta'), regla: q('.respuesta-regla'), caja: q('.respuesta-caja'),
      falta: q('.respuesta-falta'), d1: q('.respuesta-d1'), d2: q('.respuesta-d2'),
    });
  },
  render(t) {
    const push = eio(seg(t, 0, 16));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.014, push) + ')';
    this.plano.style.transform = 'scale(' + lerp(1, 1.04, push) + ')';
    this.rotulo.style.opacity = eo(seg(t, -0.3, 0.5));
    TextFx.fadeFromRight(this.pregunta, t, 0.3, { stagger: 0.09, dur: 0.5, dx: 20 });
    this.regla.style.transform = 'scaleX(' + eio(seg(t, 3.4, 4.2)).toFixed(3) + ')';
    const entra = eo(seg(t, 4.3, 5.1));
    this.caja.style.opacity = entra;
    this.caja.style.transform = 'scale(' + lerp(0.97, 1, entra).toFixed(3) + ')';
    this.falta.style.opacity = eo(seg(t, 5, 5.6)) * (0.66 + 0.24 * Math.sin(t * 1.5));
    this.d1.style.opacity = eo(seg(t, 6.6, 7.3));
    this.d2.style.opacity = eo(seg(t, 8.2, 8.9));
  },
});
