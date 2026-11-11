// El comedor universitario visto desde arriba, como un plano tecnico sobre una mesa de dibujo.
// Todas las escenas encuadran este mismo plano; ninguna lo vuelve a dibujar.
window.W = {
  // Una imagen real del modelo, encuadrada en una caja de la escena.
  foto(kit, nombre, cls, estilo) {
    return '<div class="foto ' + cls + '" style="' + estilo + '"><img src="' + kit.assets.url(nombre) + '" alt=""></div>';
  },
  // El recorrido de una persona: puerta, fila de caja, caja, fila de servicio, mostrador y salida al salon.
  RUTA: [[330, 1030], [330, 905], [1390, 905], [1560, 905], [1560, 350], [1180, 350], [860, 350], [860, 640]],
  _L: null,
  largos() {
    if (!this._L) {
      const P = this.RUTA, L = [0];
      for (let i = 1; i < P.length; i++) L.push(L[i - 1] + Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]));
      this._L = L;
    }
    return this._L;
  },
  // Punto del recorrido en la fraccion p: cualquier persona se ubica desde t, sin guardar nada.
  enRuta(p) {
    const P = this.RUTA, L = this.largos(), tot = L[L.length - 1], d = Math.max(0, Math.min(1, p)) * tot;
    let i = 1;
    while (i < L.length - 1 && L[i] < d) i++;
    const f = (d - L[i - 1]) / (L[i] - L[i - 1] || 1);
    return [P[i - 1][0] + (P[i][0] - P[i - 1][0]) * f, P[i - 1][1] + (P[i][1] - P[i - 1][1]) * f];
  },
  rutaD() { return this.RUTA.map((p, i) => (i ? 'L' : 'M') + p[0] + ' ' + p[1]).join(' '); },
  // La grilla de la mesa de dibujo y la trama de la cocina: dos patrones, no cientos de lineas.
  tramas(id) {
    return '<defs><pattern id="' + id + '-g" width="60" height="60" patternUnits="userSpaceOnUse">' +
      '<path d="M60 0 V60 M0 60 H60" style="fill:none;stroke:var(--grilla);stroke-width:1"/></pattern>' +
      '<pattern id="' + id + '-h" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">' +
      '<path d="M0 0 V16" style="fill:none;stroke:var(--borde);stroke-width:2"/></pattern></defs>' +
      '<rect class="grilla" width="1920" height="1080" fill="url(#' + id + '-g)"/>';
  },
  // El salon: muros con el hueco de la puerta, la cocina tramada, el mostrador, la caja y las mesas largas.
  // Los muros y el mostrador estan desde el primer cuadro; lo que se dibuja solo son las mesas y la cocina.
  plano(kit, id) {
    let mesas = '';
    for (let g = 0; g < 2; g++) for (let f = 0; f < 3; f++) {
      const x = 300 + g * 660, y = 470 + f * 130;
      mesas += '<g class="mesa"><rect x="' + x + '" y="' + y + '" width="560" height="56" rx="6" style="fill:var(--panel);stroke:var(--linea);stroke-width:2"/>';
      for (let s = 0; s < 9; s++) {
        const cx = x + 40 + s * 60;
        mesas += '<circle cx="' + cx + '" cy="' + (y - 17) + '" r="11" style="fill:none;stroke:var(--borde);stroke-width:2"/>' +
          '<circle cx="' + cx + '" cy="' + (y + 73) + '" r="11" style="fill:none;stroke:var(--borde);stroke-width:2"/>';
      }
      mesas += '</g>';
    }
    return '<g class="salon">' +
      '<rect x="240" y="120" width="1440" height="840" style="fill:color-mix(in srgb, var(--ground) 94%, var(--main))"/>' +
      '<g class="cocina"><rect x="260" y="140" width="380" height="160" fill="url(#' + id + '-h)"/>' +
      '<rect x="260" y="140" width="380" height="160" style="fill:none;stroke:var(--linea);stroke-width:3"/></g>' +
      '<g class="mostrador"><rect x="700" y="212" width="780" height="62" rx="5" style="fill:var(--main)"/>' +
      '<path d="M700 282 H1480" style="fill:none;stroke:var(--linea);stroke-width:3;stroke-dasharray:14 12"/></g>' +
      '<g class="caja"><rect x="1378" y="868" width="124" height="72" rx="5" style="fill:var(--main)"/>' +
      '<rect x="1396" y="886" width="44" height="30" rx="3" style="fill:var(--ground)"/></g>' +
      mesas +
      '<path class="muros" d="M300 960 H240 V120 H1680 V960 H430" style="fill:none;stroke:var(--second);stroke-width:6;stroke-linejoin:round"/>' +
      '<path class="guia" d="' + this.rutaD() + '" style="fill:none;stroke:var(--borde);stroke-width:3;stroke-dasharray:10 14"/></g>';
  },
  // Una persona en el plano: un punto con un halo tenue, del tamanio justo para leerse de lejos.
  persona(cls, destacada) {
    return '<g class="' + cls + '"><circle r="20" style="fill:' + (destacada ? 'var(--marca)' : 'var(--second)') + ';opacity:.16"/>' +
      '<circle r="11" style="fill:' + (destacada ? 'var(--marca)' : 'var(--second)') + '"/></g>';
  },
  // Una hilera de personas sobre un tramo de la ruta. Cada una sale de su propia semilla y de t.
  hilera(kit, cls, n, desde, hasta, seed) {
    const r = kit.rng(seed), gente = Array.from({ length: n }, (_, i) => ({ p: desde + (hasta - desde) * (i / Math.max(1, n - 1)), j: (r() - 0.5) * 26, f: 0.5 + r() * 0.9, at: r() * 6 }));
    const self = this;
    return {
      markup: '<g class="' + cls + '">' + gente.map(() => self.persona('', false)).join('') + '</g>',
      bind(g) { gente.forEach((p, i) => { p.el = g.children[i]; }); },
      // avance: 0 la fila esta quieta, 1 la fila ya se vacio hacia la caja.
      render(t, avance, visibles) {
        gente.forEach((p, i) => {
          const salio = visibles !== undefined && i >= visibles;
          const q = Math.min(1, Math.max(0, p.p + avance * (hasta - p.p)));
          const xy = self.enRuta(q);
          p.el.setAttribute('transform', 'translate(' + (xy[0] + p.j * 0.3).toFixed(1) + ' ' + (xy[1] + p.j + Math.sin(t * p.f + p.at) * 2).toFixed(1) + ')');
          p.el.style.opacity = salio ? 0 : 1;
        });
      },
    };
  },
};
