# Storyboard · Parte C del video

[TOC]

## Qué cubre

Escenas 7, 8 y 9 del guion, de 6:30 a 12:20. Es el bloque más largo: **2:47 de locución** en diez archivos. El film suma unos **193 segundos**, bien por debajo del tope de 300 que pone Motion.

| Escena del guion | Audio | Dura |
|---|---|---|
| 7 Introducción | `juan-e07-a.ogg` | 9,4 s |
| 7 E1 | `jonatan/jonatan-e07-e1.wav` | 16,6 s |
| 7 E2 | `juan-e07-b.ogg` | 11,6 s |
| 7 E3 | `jonatan/jonatan-e07-e3.wav` | 15,2 s |
| 7 E4 | `juan-e07-c.ogg` | 10,3 s |
| 7 E5 | `jonatan/jonatan-e07-e5.wav` | 15,1 s |
| 8 Comparación | `jonatan/jonatan-e08.wav` | 45,3 s |
| 9 Conclusión (Juan) | `juan-e09.ogg` | 25,2 s |
| 9 Conclusión (Jonatan) | `jonatan/jonatan-e09.wav` | 18,4 s |

## Antes de empezar

Vale lo mismo que para la Parte B: se crea desde el tipo **Motion**, se copian `base.css`, `shared.js` y `scenes.json` desde `videos/motion/modulos/`, y se arranca con la paleta clara que la Parte A tiene puesta a mano (fondo `#f6f3ec`, azul `#1f5673`, tinta `#22282e`, acento `#d1603d`).

Assets que usa esta parte: `cajas-2cajas.mp4`, `amb-servicio.webp`, `amb-bandejas.webp`, `amb-caja.webp` y `sala.webp`.

Los módulos que sirven de base son `scene-cambios.js`, `scene-comparar.js`, `scene-respuesta.js` y `scene-cierre.js`, todos con el armazón hecho y los datos vacíos.

## Las once escenas

### 1 · `cambios` — 20 s

Entra la lista de los cinco escenarios, una ficha por vez, sin resultados todavía. Se parte de `scene-cambios.js`, que ya hace exactamente esto; lo que se saca son los cinco chips de `RESULTADO PENDIENTE` y el pie de «E4 y E5: definición a confirmar», porque las definiciones ya están cerradas.

| | Cambio |
|---|---|
| E1 | Dos puestos de caja |
| E2 | Dos puestos de caja hasta las 13:30 |
| E3 | Validación por QR |
| E4 | Cuatro personas sirviendo |
| E5 | Dos puestos de caja y cuatro personas sirviendo |

### 2 a 6 · una escena por escenario

Las cinco son la misma plantilla, para que se lean de un vistazo: arriba el nombre del escenario, al medio dos cifras que cambian de un número al otro, abajo una frase de remate. La cifra que mejora va en el color de acento.

| Escena | Dura | Cifras | Remate |
|---|---|---|---|
| `e1` | 18 s | Caja 4,9 → **2,4 min** · Mostrador 5 → **31** | La cola no desaparece: se muda al mostrador |
| `e2` | 13 s | Igual que E1 | El pico es lo único que pesa |
| `e3` | 16 s | Caja 4,9 → **2,9 min** · Mostrador 5 → **23** | El QR acorta la validación, no la elimina |
| `e4` | 11 s | Caja 4,9 → **4,9 min** · Mostrador 5 → **3** | Reforzar el mostrador solo no mueve la aguja |
| `e5` | 16 s | Caja 4,9 → **2,4 min** · Mostrador 5 → **16** | Las dos cosas juntas |

En `e1` conviene meter `cajas-2cajas.mp4` de fondo, al 30 % como las escenas de ambiente de la Parte A. En `e4`, `amb-servicio.webp`.

`e4` es la escena bisagra del video: es la que prueba que el cuello de botella está en la caja. Vale dejarla un segundo más en negro antes de cortar.

### 7 · `comparar` — 30 s

Escena 8. Las barras de `scene-comparar.js`, que están dibujadas pero sin medir. El dato es el tiempo total medio en segundos, con el intervalo al 95 % como bigote.

```grafico
tipo: barras
titulo: Tiempo total medio en el pico
unidad: s
min: 0

Escenario, Tiempo total
E0, 68
E1, 59
E2, 59
E3, 58
E4, 68
E5, 55
```

Los intervalos para los bigotes: E0 63–74, E1 54–63, E2 55–64, E3 53–62, E4 62–73, E5 52–59.

Las barras entran de izquierda a derecha y la de E5 queda en el color de acento. Pie: «30 réplicas por escenario, con las mismas personas en todos».

### 8 · `pendiente` — 16 s

El segundo gráfico de la escena 8: la cola máxima en el mostrador, que es el costo escondido de abrir la segunda caja.

```grafico
tipo: barras
titulo: Cola máxima en el mostrador
unidad: personas
min: 0

Escenario, Cola máxima
E0, 5
E1, 31
E2, 31
E3, 23
E4, 3
E5, 16
```

Puesto al lado del gráfico anterior se ve el argumento completo: E1 es casi tan rápido como E5 pero deja 31 personas esperando en el mostrador.

### 9 · `respuesta` — 26 s

Escena 9, la parte de Juan. Vuelve la pregunta de la Parte A achicada arriba, y debajo se escribe la respuesta, que hoy está en blanco en `scene-respuesta.js`:

> **Dos puestos de validación en el pico y cuatro personas sirviendo.**

Debajo, tres renglones que entran de a uno mientras Juan los dice:

- 68 s → **55 s** · 13 segundos menos, un 19 %
- Abrir solo la segunda caja muda la cola al mostrador: 5 → 31
- Reforzar solo el mostrador no cambia nada: el cuello está en la caja

Cierra con la recomendación horaria: segundo puesto **de 12:00 a 13:30** y una persona más en el mostrador en esa franja.

### 10 · `limites` — 19 s

El cierre de Jonatan, que es el que da honestidad al trabajo. Dos renglones sobre `amb-caja.webp` al 30 %:

- Ningún escenario cambia la espera de quienes llegan antes de la apertura.
- El tiempo de servicio por ración es un supuesto: no se pudo cronometrar.

### 11 · `cierre` — 8 s

`scene-cierre.js` tal cual, que ya tiene los nombres y «Simulación · 2026».

## Lo que falta resolver

`flexsim/DATOS_VIDEO.md` marca una contradicción sin cerrar: la corrida validada da 7,7 min de espera y 131 personas de cola en el mostrador, y el Experimenter da 0,016 min y 4,8. El archivo pide revisar la tabla `TiemposServicio` de `comedor_unc_3.fsm`, fila 2, Scale 17,3, antes de cerrar el video.

Toda esta parte está escrita con los números del Experimenter, que son los que ya quedaron grabados en la voz de Juan. Si al revisar el `.fsm` resulta que el Experimenter corrió con un servicio más rápido que el real, no alcanza con cambiar las placas: hay que regrabar.
