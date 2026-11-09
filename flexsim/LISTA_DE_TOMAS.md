# Lista de tomas para el video (OBS)

[TOC]

El tiempo del modelo es en segundos y el 0 equivale a las 11:40. Todas las horas salen de `replay.xlsx` (`--ritmo 3 --inicio 900 --cola-pre 50 --cola-max 100`).

## Preparación

- [ ] Vista 3D en pantalla completa (F11), con **Show Nothing** en View Style para ocultar los nombres.
- [ ] OBS: captura de ventana, 1920×1080 (o 2560×1440 para poder hacer zoom en el editor), 30 o 60 fps, formato MKV.
- [ ] Run Speed bajado hasta que se vea fluido. Si se traba, se acelera en el editor.
- [ ] Para llegar a cada toma: Reset, poner el tiempo de parada en el segundo de inicio y Fast Forward hasta ahí. Después ubicá la cámara, empezá a grabar en OBS y dale Run.

## Tomas

| N.º | Toma | Modelo (s) | Hora | Duración sugerida | Cámara | Qué mostrar |
|---|---|---|---|---|---|---|
| 1 | Llegada | 900 a 1314 | 11:55 a 12:01:54 | 15 s (acelerada) | Alta y abierta, sobre la puerta | Entra la gente y se arma la fila de la caja antes de abrir |
| 2 | Apertura de la caja | 1314 a 1400 | 12:01:54 a 12:03:20 | 10 s | Cerca de la caja, a la altura de la gente | La fila arranca a avanzar y se valida la primera persona |
| 3 | La fila crece | 1400 a 2100 | 12:03:20 a 12:15 | 15 s (acelerada) | Plano general, zoom lento hacia atrás (efecto dron) | La fila llega a 100 personas |
| 4 | Mostrador | 2100 a 2400 | 12:15 a 12:20 | 15 s | Cerca de los 4 puestos | Las personas toman la bandeja y las sirven |
| 5 | Camino a la salida | cualquiera | cualquiera | 8 s | Siguiendo a una persona | Sale con la bandeja |
| 6 | Cierre | 8300 a 8484 | 13:58 a 14:01 | 10 s | Alta y abierta | La sala se vacía |

## Epígrafes (agregar en el editor)

- Toma 1: "11:55, empiezan a llegar los comensales".
- Toma 2: "12:01, abre la caja: ya hay 50 personas esperando".
- Toma 3: "La fila crece hasta 100 personas".
- Toma 4: "Los 4 puestos del mostrador sirven en paralelo".
- Toma 6: "14:01, sale el último comensal".
- Pie fijo en todo el video: "Animación ilustrativa de un escenario más exigente que el medido".

## Consejos

- Grabá **dos o tres versiones** de cada toma con cámara distinta y elegí la mejor.
- Para el efecto dron en la toma 3: empezá cerca y alejá despacio, o grabá abierto y aplicá un zoom lento en el editor.
- Los **segundos exactos** de cada toma pueden correrse unos segundos, porque la hora que ves en el modelo depende del paso de simulación.
- Si en la toma 4 algún puesto no muestra la bandeja, revisá la actividad **Tomar-bandeja**.

---

## Guión de edición con las dos grabaciones

Archivos: `videos/una-caja.mkv` y `videos/dos-cajas.mkv`. Los datos de los números de pantalla (esperas, colas) salen del modelo completo medido, no de esta animación.

| Bloque | Qué se ve | Duración sugerida | Texto en pantalla |
|---|---|---|---|
| 1. Presentación | Plano general de la sala (toma 1 de una caja, acelerada) | 8 s | "Comedor Universitario UNC: la fila de la caja" |
| 2. Una caja | Tomas 2 y 3 de `una-caja.mkv` (apertura y fila que crece) | 20 s | "12:02: abre la caja y ya hay 50 personas esperando" |
| 3. El mostrador | Toma 4 de `una-caja.mkv` (bandejas, 3 puestos) | 12 s | "Los puestos del mostrador sirven en paralelo" |
| 4. Dos cajas | Mismas tomas 2 y 3 de `dos-cajas.mkv` | 20 s | "Con 2 puestos de validación, la fila se mueve más rápido" |
| 5. Dónde se traba ahora | Fila de servicio llena en `dos-cajas.mkv` | 10 s | "El cuello de botella pasa al mostrador" |
| 6. Cierre | Toma 6 de ambos, lado a lado o una después de la otra | 10 s | "Una caja: sale el último a las 14:01. Dos cajas: a las 13:23" |

Duración total: ~80 s. Ajustá los números del último bloque a los que mida el modelo licenciado.

Notas:
- El texto del último bloque (14:01 y 13:23) es de **esta animación** (replay con `--ritmo 3`). Si en el informe ponés otros resultados, usá esos.
- Pie en todo el video: "Animación ilustrativa de un escenario más exigente que el medido".
- Poné la misma cámara en ambas versiones para que se pueda comparar.
