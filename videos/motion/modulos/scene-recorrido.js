const { seg, eo, eio, lerp } = kit;

// El recorrido, marcado sobre la ilustracion del modelo. Los rotulos del puesto y de la fila
// ya vienen en la imagen, asi que aca solo se traza el camino y la persona que lo hace.
const D_FILA = 'M218 685 Q375 630 529 572 Q645 538 741 506 Q845 465 926 414 Q1015 365 1085 299';
const FIN = [1085, 299];

kit.scene('recorrido', {
  init(kit) {
    kit.css('.recorrido-foto { transform-origin:50% 46% }' +
      '.recorrido-fila { fill:none; stroke:var(--marca); stroke-width:9; stroke-linecap:round }' +
      '.recorrido-nota { position:absolute; right:104px; bottom:52px }');
    kit.stage.append(kit.h('<div class="ground">' +
      W.foto(kit, 'fila-render.webp', 'recorrido-foto', 'left:0; top:63px; width:1920px; height:953px') +
      '<svg class="art recorrido-marcas" viewBox="0 0 1920 1080">' +
      '<path class="recorrido-fila" d="' + D_FILA + '"/>' +
      '<g class="recorrido-fin"><circle cx="' + FIN[0] + '" cy="' + FIN[1] + '" r="44" style="fill:none;stroke:var(--marca);stroke-width:5"/></g>' +
      '<g class="recorrido-yo"><circle r="26" style="fill:var(--second);opacity:.2"/><circle r="14" style="fill:var(--second)"/></g></svg>' +
      '<div class="edge"></div>' +
      '<div class="pendiente recorrido-nota">ILUSTRACI&Oacute;N A PARTIR DEL MODELO &middot; NO ES UNA CAPTURA DE FLEXSIM</div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.foto = q('.recorrido-foto');
    this.fila = q('.recorrido-fila');
    this.fin = q('.recorrido-fin');
    this.yo = q('.recorrido-yo');
    this.nota = q('.recorrido-nota');
    // El largo del trazo se mide una sola vez, para revelarlo con el guion de la linea.
    this.largo = this.fila.getTotalLength();
    this.fila.style.strokeDasharray = this.largo + ' ' + this.largo;
    // Puntos del trazo, muestreados aca: en cada cuadro la persona sale de t y de esta lista.
    this.puntos = Array.from({ length: 121 }, (_, i) => {
      const p = this.fila.getPointAtLength((i / 120) * this.largo);
      return [p.x, p.y];
    });
  },
  render(t) {
    const push = eio(seg(t, 0, 29));
    this.foto.style.transform = 'scale(' + lerp(1.005, 1.052, push).toFixed(4) + ')';
    const traza = eio(seg(t, 2.8, 9.6));
    this.fila.style.strokeDashoffset = (this.largo * (1 - traza)).toFixed(1);
    this.fila.style.opacity = eo(seg(t, 2.6, 3.8)) * 0.92;
    // La persona sube por la fila y frena donde la fila termina.
    const p = eio(seg(t, 4.4, 15.2));
    const i = Math.min(119, Math.floor(p * 120)), f = p * 120 - i;
    const a = this.puntos[i], b = this.puntos[i + 1];
    this.yo.setAttribute('transform', 'translate(' + lerp(a[0], b[0], f).toFixed(1) + ' ' + lerp(a[1], b[1], f).toFixed(1) + ')');
    this.yo.style.opacity = eo(seg(t, 4, 5)) * (1 - eo(seg(t, 18.8, 20.8)));
    const abre = eo(seg(t, 13.2, 14.8));
    this.fin.style.opacity = abre * (0.6 + 0.3 * Math.sin((t - 13.2) * 2.4));
    this.fin.style.transform = 'scale(' + lerp(1.3, 1, abre).toFixed(3) + ')';
    this.fin.style.transformOrigin = FIN[0] + 'px ' + FIN[1] + 'px';
    this.nota.style.opacity = eo(seg(t, 9.2, 10.8)) * 0.85;
  },
});
