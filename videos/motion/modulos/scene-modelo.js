const { seg, eo, eio, lerp, clamp } = kit;

// Las tomas reales del modelo. Primero el salon entero en el pico; despues, una caja contra dos cajas.
const CORTE = 8.6;

kit.scene('modelo', {
  init(kit) {
    kit.css('.modelo-marco { position:absolute; overflow:hidden; background:var(--panel) }' +
      '.modelo-marco video { position:absolute; left:0; top:0; width:100%; height:100%; object-fit:cover; display:block }' +
      '.modelo-par { border:2px solid var(--borde); border-radius:12px }' +
      '.modelo-pie { position:absolute; left:0; right:0; bottom:0; height:116px; background:var(--vidrio) }' +
      '.modelo-nota { position:absolute; left:120px; bottom:42px }' +
      '.modelo-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:60px; font-weight:700; margin:0; line-height:1.06 }' +
      '.modelo-velo { position:absolute; left:0; top:0; width:1920px; height:420px; background:linear-gradient(color-mix(in srgb, var(--ground) 82%, transparent), transparent) }');
    this.vSalon = kit.video('cola-mostrador-1caja.mp4');
    this.vUna = kit.video('caja-1caja.mp4');
    this.vDos = kit.video('cajas-2cajas.mp4');
    kit.stage.append(kit.h('<div class="ground">' +
      '<div class="modelo-marco modelo-salon" style="left:0; top:0; width:1920px; height:1080px"></div>' +
      '<div class="modelo-marco modelo-par modelo-izq" style="left:120px; top:318px; width:816px; height:459px"></div>' +
      '<div class="modelo-marco modelo-par modelo-der" style="left:984px; top:318px; width:816px; height:459px"></div>' +
      '<div class="modelo-velo"></div>' +
      '<div class="edge"></div>' +
      '<div class="modelo-pie"></div>' +
      '<div class="words" style="left:120px; top:108px; width:1180px; gap:10px">' +
      '<h2 class="modelo-titulo">As&iacute; se ve el modelo corriendo</h2>' +
      '<p class="sub modelo-sub">El sal&oacute;n en la hora pico, con un solo puesto de caja</p></div>' +
      '<div class="etiqueta modelo-rot-izq" style="left:120px; top:806px">Un puesto de caja</div>' +
      '<div class="etiqueta modelo-rot-der" style="left:984px; top:806px">Dos puestos de caja</div>' +
      '<div class="pendiente modelo-nota">ANIMACI&Oacute;N ILUSTRATIVA DE UN ESCENARIO M&Aacute;S EXIGENTE QUE EL MEDIDO</div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.salon = q('.modelo-salon');
    this.izq = q('.modelo-izq');
    this.der = q('.modelo-der');
    this.salon.append(this.vSalon);
    this.izq.append(this.vUna);
    this.der.append(this.vDos);
    Object.assign(this, {
      velo: q('.modelo-velo'), pie: q('.modelo-pie'), nota: q('.modelo-nota'),
      titulo: q('.modelo-titulo'), sub: q('.modelo-sub'),
      rotIzq: q('.modelo-rot-izq'), rotDer: q('.modelo-rot-der'),
    });
  },
  render(t) {
    const abre = eo(seg(t, CORTE, CORTE + 0.7));
    const entra = eio(seg(t, CORTE, CORTE + 0.9));
    this.salon.style.opacity = 1 - abre;
    this.salon.style.transform = 'scale(' + lerp(1, 1.05, eio(seg(t, 0, CORTE))).toFixed(4) + ')';
    kit.seek(this.vSalon, clamp(37 + t, 0, 53.4));
    this.izq.style.opacity = abre;
    this.der.style.opacity = abre;
    this.izq.style.transform = 'translateY(' + lerp(30, 0, entra).toFixed(1) + 'px)';
    this.der.style.transform = 'translateY(' + lerp(30, 0, eio(seg(t, CORTE + 0.2, CORTE + 1.1))).toFixed(1) + 'px)';
    kit.seek(this.vUna, clamp(2 + (t - CORTE), 0, 15.6));
    kit.seek(this.vDos, clamp(0.4 + (t - CORTE), 0, 8.6));
    this.titulo.style.opacity = eo(seg(t, -0.3, 0.6));
    this.sub.style.opacity = eo(seg(t, 0.8, 1.4)) * (1 - abre);
    this.velo.style.opacity = 0.9 - 0.25 * abre;
    this.pie.style.opacity = eo(seg(t, 0.9, 1.7));
    this.nota.style.opacity = eo(seg(t, 1.3, 2.1)) * 0.92;
    this.rotIzq.style.opacity = eo(seg(t, CORTE + 0.6, CORTE + 1.2));
    this.rotDer.style.opacity = eo(seg(t, CORTE + 0.9, CORTE + 1.5));
  },
});
