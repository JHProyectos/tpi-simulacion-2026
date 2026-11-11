const { seg, eo, eio, lerp, clamp, TextFx } = kit;

// Abre con el clip de apertura: el salon dibujado en lineas que se pasa a color.
const COLOR = 13;

kit.scene('abrir', {
  init(kit) {
    kit.css('.abrir-marco { position:absolute; left:0; top:0; width:1920px; height:1080px; overflow:hidden; background:var(--panel) }' +
      '.abrir-marco video { position:absolute; left:0; top:0; width:100%; height:100%; object-fit:cover; display:block }' +
      '.abrir-velo { position:absolute; left:0; bottom:0; width:80%; height:70%; background:radial-gradient(100% 100% at 0 100%, color-mix(in srgb, var(--ground) 97%, transparent) 54%, transparent) }' +
      '.abrir-words .line { font-size:82px }' +
      '.abrir-firma { margin-top:6px }' +
      '.abrir-sello { position:absolute; right:112px; top:104px }');
    this.vApertura = kit.video('apertura.mp4');
    kit.stage.append(kit.h('<div class="ground">' +
      '<div class="abrir-marco"></div>' +
      '<div class="abrir-velo"></div><div class="edge"></div>' +
      '<div class="etiqueta abrir-sello">Modelo 3D del sal&oacute;n</div>' +
      '<div class="words abrir-words" style="left:140px; bottom:120px; width:900px">' +
      '<h2 class="line">La fila de un comedor universitario</h2>' +
      '<p class="sub abrir-sub">Trabajo integrador de Simulaci&oacute;n &middot; 2026</p>' +
      '<p class="sub abrir-firma">Jonatan Harbertz &middot; Juan Ch&aacute;vez</p></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.marco = q('.abrir-marco');
    this.marco.append(this.vApertura);
    this.velo = q('.abrir-velo');
    this.sello = q('.abrir-sello');
    this.linea = q('.line');
    this.sub = q('.abrir-sub');
    this.firma = q('.abrir-firma');
  },
  render(t) {
    kit.seek(this.vApertura, clamp(t, 0, 15.9));
    this.velo.style.opacity = (lerp(0.6, 0.93, eo(seg(t, 0, 1.6))) * lerp(1, 1.05, eio(seg(t, COLOR - 3, COLOR)))).toFixed(3);
    this.sello.style.opacity = eo(seg(t, 8.1, 8.9)) * 0.88;
    TextFx.fadeFromRight(this.linea, t, 5.4, { stagger: 0.12, dur: 0.55, dx: 30 });
    this.sub.style.opacity = eo(seg(t, 3.3, 3.9));
    this.firma.style.opacity = eo(seg(t, 0.7, 1.3));
  },
});
