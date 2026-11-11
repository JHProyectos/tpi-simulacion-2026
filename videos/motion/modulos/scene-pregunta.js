const { seg, eo, eio, lerp, TextFx } = kit;

kit.scene('pregunta', {
  init(kit) {
    kit.css('.pregunta-plano { transform-origin:960px 520px }' +
      '.pregunta-words .line { font-size:64px; line-height:1.24; font-weight:600 }' +
      '.pregunta-regla { position:absolute; left:210px; top:286px; width:150px; height:6px; background:var(--marca); transform-origin:left center }');
    kit.stage.append(kit.h('<div class="ground">' +
      W.foto(kit, 'amb-aerea.webp', 'ambiente', 'left:0; top:0; width:1920px; height:1080px') +
      '<svg class="art pregunta-grilla" viewBox="0 0 1920 1080">' + W.tramas('pregunta') + '</svg>' +
      '<svg class="art pregunta-plano" viewBox="0 0 1920 1080">' + '' + '</svg>' +
      '<div class="calm pregunta-velo"></div><div class="edge"></div>' +
      '<div class="pregunta-regla"></div>' +
      '<div class="words pregunta-words" style="left:210px; top:346px; width:1500px">' +
      '<p class="sub pregunta-rotulo">La pregunta de estudio</p>' +
      '<h2 class="line">&iquest;Qu&eacute; combinaci&oacute;n de puestos de validaci&oacute;n y personas en el servicio reduce el tiempo total en el pico, sin trasladar la cola al mostrador?</h2>' +
      '</div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.pregunta-grilla');
    this.plano = q('.pregunta-plano');
    this.velo = q('.pregunta-velo');
    this.regla = q('.pregunta-regla');
    this.rotulo = q('.pregunta-rotulo');
    this.linea = q('.line');
  },
  render(t) {
    const push = eio(seg(t, 0, 34));
    this.grilla.style.transform = 'scale(' + lerp(1.014, 1.03, push) + ')';
    this.plano.style.transform = 'scale(' + lerp(1.042, 1.08, push) + ') translateY(' + lerp(0, -26, push) + 'px)';
    this.velo.style.opacity = eo(seg(t, 0, 2.8));
    this.regla.style.transform = 'scaleX(' + eo(seg(t, 1.5, 2.8)) + ')';
    this.rotulo.style.opacity = eo(seg(t, 1.9, 3.2));
    TextFx.fadeFromRight(this.linea, t, 2.8, { stagger: 0.45, dur: 0.6, dx: 26 });
  },
});
