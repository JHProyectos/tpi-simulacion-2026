# Cámara en FlexSim y corridas de escenarios

[TOC]

Dos partes independientes: **A**, la cámara y la grabación del video desde FlexSim; **B**, las corridas del Experimenter. Los nombres de menús y campos salen de `program/translations/en-US.csv` de FlexSim 2026 (confirmados como texto de la interfaz). Lo que se deduce y hay que mirar en pantalla va marcado con †.

## A. Movimiento de cámara y grabación

### A.1 Qué herramientas hay

Con licencia ya no hace falta OBS: FlexSim trae dos herramientas en **Toolbox > + > Visual**:

- **Fly Path** (*Presentation Builder*): una ruta de cámara con keyframes, que se puede reproducir y editar en una línea de tiempo.
- **Video Recorder**: corre el modelo entre dos tiempos, a la velocidad que elijas, sigue un Fly Path y escribe el video (H.264, 1920×1080).

Ventaja sobre OBS: la toma queda **repetible**. Si cambia el modelo, se vuelve a grabar con la misma cámara, y la cámara de `una-caja` y `dos-cajas` puede ser exactamente la misma.

### A.2 Crear un Fly Path por toma

1. Abrí el modelo de animación (`comedor_visual_2.fsm`) y dejá a la vista la vista 3D en perspectiva.
2. **Toolbox > + > Visual > Fly Path**. Se abre *Presentation Builder*.
3. Panel *Flypaths*, botón **+** (*Add a new flypath*). Ponele nombre con el lápiz: `T1_Llegada`, `T2_Apertura`, etc. (una ruta por toma de `LISTA_DE_TOMAS.md`).
4. Con el mouse, dejá la cámara en el **encuadre inicial** de la toma y apretá **Add** (*Add a keyframe*, `Ctrl+Shift+D`).
5. Movela al encuadre siguiente y agregá otro keyframe. Con *AutoKeyframe* tildado, se crea uno solo cada vez que movés la vista.
6. En la línea de tiempo arrastrá los keyframes para fijar **cuándo** llega la cámara a cada encuadre. *Zoom to fit* ajusta la escala.
7. Probalo con **Run**. *Active Update* hace que la vista 3D siga la línea de tiempo mientras la arrastrás. *Loop* repite la reproducción.

**Ajuste fino.** En el panel de ubicación de la cámara hay seis números: **X**, **Y**, **Rad**, **RX**, **RY**, **RZ**. Por el nombre son un punto de foco (X, Y), la distancia (Rad) y los giros†. Sirven para que el *zoom hacia atrás* sea exacto: mantené X, Y y los giros, y subí solo **Rad** entre el primer y el último keyframe.

### A.3 Qué cámara para cada toma

| Toma | Movimiento | Cómo armarlo |
|---|---|---|
| 1 Llegada | Alta y abierta sobre la puerta, bajando de a poco | 2 keyframes: alto y lejos, y más bajo y cerca |
| 2 Apertura de la caja | A la altura de la gente, casi quieta | 2 keyframes muy parecidos, con un giro (RZ) de pocos grados |
| 3 La fila crece | Efecto dron: empieza cerca y se aleja | Mismo X, Y y giros; **Rad** chico al principio, grande al final |
| 4 Mostrador | Cerca de los 4 puestos, con un paneo lento | 2 keyframes con distinto RZ |
| 5 Camino a la salida | Recorrido por el pasillo | Un keyframe por tramo. No hay una opción de "seguir a una persona" en el panel† |
| 6 Cierre | Alta y abierta | 1 o 2 keyframes |

Los números exactos dependen de la escena. Armá cada keyframe con el mouse y mirá después qué quedó en X, Y y Rad. Después podés repetirlo en la otra grabación.

### A.4 Grabar con el Video Recorder

1. **Toolbox > + > Visual > Video Recorder**.
2. Pestaña **Output**. En *Output Files*, **Add** (*Add output file*) para crear un archivo por toma, por ejemplo `T3_FilaCrece.mp4`.
3. A la derecha de cada archivo:
   - *File Path*: carpeta de salida (botón de examinar).
   - *Codec*: **H.264**.
   - *FPS*: 30 (o 60 si la máquina aguanta).
   - *Size*: 1920 × 1080.
4. Elegí **Use Basic Sequence** y completá:
   - *Start* y *End*: tiempo de modelo en segundos (los de la columna "Modelo (s)" de `LISTA_DE_TOMAS.md`).
   - *Speed*: segundos de modelo por segundo real. *Duration*: duración en el video (hh:mm:ss). Los dos están ligados: al cambiar uno se recalcula el otro†.
   - *Flypath*: la ruta de esa toma.
   - *View*: **pick** y tocás la vista 3D.
   - *Preview*: ver la grabación mientras corre (desactivalo si va lento).
5. Tocá **Record**.

Velocidad que sale de cada duración sugerida (modelo ÷ duración del video):

| Toma | Start – End (s) | Duración | Speed (s de modelo por s de video) |
|---|---|---|---|
| 1 Llegada | 900 – 1314 | 15 s | 27,6 |
| 2 Apertura | 1314 – 1400 | 10 s | 8,6 |
| 3 La fila crece | 1400 – 2100 | 15 s | 46,7 |
| 4 Mostrador | 2100 – 2400 | 15 s | 20 |
| 6 Cierre | 8300 – 8484 | 10 s | 18,4 |

Dos cosas a probar con una toma corta antes de grabar todas†:

- Si el recorder **avanza solo hasta *Start*** sin grabar, o hay que dejar el modelo parado en ese tiempo (como se hacía con Fast Forward). Si hace falta, usá el procedimiento de `LISTA_DE_TOMAS.md`.
- Si en el Fly Path hay que tildar **Use Model Time** (*Match the flypath time to the model time*). Con eso tildado, los keyframes se ubican en **segundos de modelo** y la cámara queda sincronizada con la fila; sin eso, quedan en tiempo del video†.

### A.5 Un solo archivo con varias tomas

En vez de *Use Basic Sequence* podés tildar **Use Shared Sequences**. Cada secuencia tiene nombre, *Start*, *End*, *Speed*, *Duration* y **capas** (*Layers*) de tipo **Color** o **View**, cada una con su Fly Path y una *Opacity* animable con keyframes. Con eso se pueden hacer **fundidos** entre tomas (una capa de color que sube y baja) sin ir al editor. Las capas no admiten texto: **los epígrafes y el pie fijo se agregan en el editor**.

### A.6 Problemas posibles

| Problema | Qué mirar |
|---|---|
| El video sale más corto o más largo | *Speed* y *Duration* están ligados: tocaste uno después del otro |
| La cámara salta al empezar | El primer keyframe no está en el tiempo 0 de la línea |
| Se ve la interfaz o los nombres de los objetos | Mismo ajuste que en la lista de tomas: *Show Nothing* en View Style |
| Grabación a tirones | Desactivá *Preview* y bajá el FPS a 30 |

## B. Corridas de los escenarios

### B.1 Antes de empezar

- [ ] El modelo que se corre es el **lógico** (`comedor_unc_3.fsm` o el último con la lógica completa). Las personas 3D son solo visuales y **no tienen que cambiar ningún resultado**: comparalo con `E0_Pico` y la misma semilla antes y después.
- [ ] Un modelo con muchas Person corre más lento. Si las corridas tardan, usá la copia sin la parte 3D para el Experimenter.
- [ ] Están creadas las **Performance Measures** de `GUIA_FLEXSIM.md` sección 16: tiempo total medio, espera máxima en la caja, espera media en el servicio, tiempo con la caja bloqueada, utilización de la caja, cola máxima en la caja, cola máxima en el servicio y personas del día.
- [ ] El parámetro del modelo `Escenario` existe, y el escenario se lee de la tabla `Escenarios` (12 filas, `E0_Pico` a `E5_Bajo`).
- [ ] Comprobá que `Table("Salida_Personas")` arranque vacía en cada réplica (corrés dos réplicas seguidas y mirá que la cantidad de filas no se acumule). Si se acumula, las medidas salen mal†.

### B.2 Corrida piloto

Antes de lanzar las 360 réplicas (12 escenarios × 30):

1. Configurá el job con **5 réplicas** y solo `E0_Pico` y `E1_Pico`.
2. Mirá cuánto tarda una réplica. Estimación del total: `tiempo por réplica × 360 ÷ núcleos usados`†.
3. Comparalas con la tabla de la sección 17 de `GUIA_FLEXSIM.md` (la réplica en Python). Con 5 réplicas no van a coincidir exactas, pero tienen que estar cerca: E0 con cola máx. de la caja ≈ 71 y cola del servicio ≈ 4; E1 con cola del servicio ≈ 24.
4. Si algo se aleja mucho, revisalo ahora: es más barato que tirar 360 réplicas.

### B.3 Corrida completa

Mismo job (`GUIA_FLEXSIM.md`, sección 16):

1. **Statistics > Experimenter...**
2. Job **Experiment** con el parámetro `Escenario` y los 12 escenarios.
3. *Warmup Time* **0**, *Stop Time* **15600**, *Replications per Scenario* **30** (el plan pide 20 a 30).
4. Pestaña **Run** y **Run**. Dejá la compu sin hacer otras cosas pesadas, y con el modelo sin animación.
5. **View Results**:
   - *Scenario Comparison* para ver todo junto.
   - *Data Summary* con el intervalo de confianza al **95 %**.
   - *Raw Data* tiene el valor de cada réplica: es lo que se exporta para procesar.

### B.4 Lo que se lleva al informe

- La tabla de medias con su intervalo para cada indicador y los 12 escenarios.
- Las comparaciones que pide el plan (Fase 7): **E1 contra E5** en tiempo total y **E4 contra E1** por tipo de cliente.
- Cuántas réplicas hacen falta si el intervalo es ancho: $n \approx (t\,s/h)^2$ de la sección 16.
- Si cambia el supuesto de tiempo de servicio, hay que **volver a correr todo**; los resultados viejos no valen. Usá *Delete Results File* para no mezclar.

### B.5 Orden recomendado

1. Corrida piloto (B.2).
2. Corrida completa (B.3) y exportar *Raw Data*.
3. Procesar los resultados con intervalos y gráficos (lo hago yo sobre el *Raw Data* exportado).
4. Recién entonces grabar el video (parte A) con el modelo final.
