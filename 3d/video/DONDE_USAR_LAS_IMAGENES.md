# Dónde usar las imágenes 3D en el video

[TOC]

Propuesta de uso de las tomas renderizadas en Blender (`3d/video/`, 1920×1080), según las escenas de `entregas/entrega-final/GUION.md`. El número del archivo es el orden en que se armaron las tomas, **no** el número de escena.

## Resumen

| Archivo | Qué muestra | Escena principal | También sirve en |
|---|---|---|---|
| `00_vista-lineas` | Misma vista que la 01, dibujada en líneas sobre fondo casi blanco, con el cartel en rojo | 0 (placa de apertura) | Portada y separadores |
| `01_vista-general` | Sala desde la entrada, hacia el mostrador y el cartel rojo | 0 (apertura, fundido final) | 3 (escenario base) |
| `02_aerea` | Vista aérea sin techo: mesas, fila y mostrador | 3 (escenario base) | 4 (renderizado 3D) |
| `04_fila-de-caja` | Pasillo de la fila, con la caja al fondo | 4 (la fila de caja) | 5 (apertura de la caja) |
| `06_fila-de-servicio` | Zona previa al mostrador, donde se acumula la fila de servicio | 5 (cuello de botella) | 7 |
| `07a_mostrador-medio` | Mostrador en plano medio | 4 (el mostrador) | 5 |
| `07b_mostrador-completo` | Mostrador completo, con todos los puestos | 5 (servicio en paralelo) | 6, 7 |
| `08_recorrido-cenital` | Vista cenital del recorrido completo | 4 (recorrido 3D) | 3 |

## Escena por escena

### Escena 0 · Apertura (0:00 – 0:15)

- El guion pide una placa con los apellidos y, al final, un fundido a una foto o al plano 3D.
- Usar `00_vista-lineas` como fondo de la placa con los apellidos: se reconoce el comedor sin competir con el texto.
- Para el fundido final, pasar de `00_vista-lineas` a `01_vista-general` (misma cámara, así el cambio se ve como si el dibujo "tomara color").
- El cartel rojo "Comedor Universitario" se ve en esta toma: sirve como identidad visual.

### Escena 3 · Escenario base (1:45 – 3:15)

- `02_aerea` mientras se explican las cuatro etapas (fila, caja, servicio, mesas).
- `01_vista-general` para mostrar la escala de la sala.

### Escena 4 · Renderizado 3D (3:15 – 3:45), opcional

El guion pide un recorrido por: entrada, fila de caja, puesto, fila de servicio y mostrador. Con imágenes fijas se arma con zooms lentos y las etiquetas en negrita del texto sobre cada sector.

1. `01_vista-general`: la sala completa.
2. `04_fila-de-caja`: «acá se forma la fila de caja».
3. `08_recorrido-cenital`: «el puesto de validación» y el camino hacia el mostrador.
4. `07a_mostrador-medio` → `07b_mostrador-completo`: «la gente avanza hacia el mostrador».

Es la primera escena a recortar si el video se pasa de tiempo.

### Escena 5 · Ejecución del escenario base (3:45 – 5:15)

- El protagonista es `una-caja.mkv`. Las imágenes fijas sólo sirven de transición o para reforzar:
  - `04_fila-de-caja` antes de la toma 2 (abre la caja).
  - `06_fila-de-servicio` y `07b_mostrador-completo` junto a la frase «el cuello de botella está en el mostrador».

### Escenas 6, 7 y 8

- Las imágenes 3D no son la base de estas escenas (son resultados y gráficos).
- Opcional: `07b_mostrador-completo` como fondo tenue de la escena 7 cuando se habla de sumar puestos en el mostrador.

## Avisos

- Las imágenes son del modelo visual, no de la corrida medida: en pantalla va el pie «Animación ilustrativa».
- No nombrar a la organización: el cartel dice sólo "Comedor Universitario".
- Si se pasan por una IA para dar realismo, conservar el cartel en rojo y la disposición de las mesas.
