# Avance del modelo en FlexSim

[TOC]

Registro del armado del modelo del Comedor Universitario UNC en FlexSim 2026, a partir de las capturas de esta carpeta. Sigue los pasos de la [guía](../GUIA_FLEXSIM.md) y se actualiza a medida que avanza el trabajo.

| Fecha | Qué se hizo | Guía |
|---|---|---|
| 29/09 | Modelo nuevo con unidades y hora de inicio | Sección 3 |
| 29/09 | Global Tables creadas y primer intento de importación | Sección 4 |
| 30/09 | Tablas importadas desde `inputs.xlsx` | Sección 4 |
| 30/09 | Recursos compartidos del Process Flow | Sección 7 |
| 30/09 | Actividades del inicio del día y del control del puesto | Sección 8 |
| 30/09 | Cambio de alcance: el modelo llega hasta el mostrador | Sección 20 |
| 09/10 | Llegadas, fila de caja y validación probadas | Sección 9 |
| 14/10 | Servicio con 3 personas, menú vegetariano y 17,3 s por ración | [GUIA_MODIFICACIONES](../GUIA_MODIFICACIONES.md) |
| 14/10 | Escena 3D: importación del dibujo de SketchUp | Aparte |

---

## 1. Modelo nuevo (29/09)

Se creó el modelo en **FlexSim 2026 for Education**, la versión de la licencia de la cátedra. En la ventana *Model Units* se eligió tiempo en segundos, longitud en metros y hora de inicio a las **11:40**: el reloj del modelo arranca cuando empieza a formarse la cola previa (S09).

![Ventana Model Units con Time Units en Seconds, Length Units en Meters y Model Start Time 11:40:00 del 30/09/2026](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-01.png)

La parada se configuró a las **16:00**, es decir, `t = 15600` s desde las 11:40. Se ve en la barra de simulación de la captura siguiente: *Run Time* va de 11:40:00 [0.00] a 16:00:00 [15600.00].

---

## 2. Tablas del modelo (29/09)

Las tablas de entrada se crean desde **Toolbox > + > Global Table**, una por cada hoja de `inputs.xlsx` y con el mismo nombre.

![Menú + del Toolbox desplegado, con la opción Global Table resaltada](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-02.png)

Primero se creó `TasaLlegadas_Pico`, vacía, con 16 filas y 8 columnas. También se crearon las tablas del parámetro del escenario (*Model Parameter Tables*) y de indicadores (*Performance Measure Tables*).

![Global Table TasaLlegadas_Pico vacía, de 16 filas por 8 columnas, con la barra de simulación de 11:40 a 16:00](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-03.png)

---

## 3. Importación desde Excel (29 y 30/09)

### Primer intento

El primer intento no importó nada. En la captura se ven las causas: *Starting Row*, *Starting Column*, *Total Rows* y *Total Columns* estaban en 0, y *Excel Workbook* tenía solo el nombre del archivo, sin la ruta completa. Además, quedó un Excel abierto en segundo plano que bloqueaba `inputs.xlsx`, y hubo que cerrarlo desde el Administrador de tareas.

![Excel Interface con la línea de TasaLlegadas_Pico: Starting Row, Starting Column, Total Rows y Total Columns en 0, y Data Preview vacío](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-04.png)

Aprendido en el camino: con *Use Column Headers* tildado, *Starting Row* y *Starting Column* van en **1**.

### Tablas importadas

Con esa configuración, las tablas se importaron. Por ejemplo, `TasaLlegadas_Bajo`:

![Global Table TasaLlegadas_Bajo importada, con las franjas como encabezados de fila desde 12:00 hasta 14:20 y columnas Inicio_s, Fin_s, Estudiantes, BecasNutrirse, BecasPersonal, Personal y Total](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-05.png)

> **A corregir.** La tabla termina en `14:20`: **falta la última franja** (`14:30`, con Total = 4,66). Tiene 15 filas y deberían ser 16. Con *Starting Row* = 1, *Total Rows* cuenta también la fila de encabezados, así que hay que poner **filas de datos + 1** (17 en las tablas de llegadas). Esto vale para **todas** las tablas: si no, a cada una le falta su última fila.
>
> Además, la columna `Franja` quedó como encabezado de fila, porque *Use Row Headers* está tildado. En estas dos tablas no afecta, pero en `ColaPrevia` y `MixTipos` el código busca por nombre la primera columna (`Perfil`, `Grupo`), y si queda como encabezado de fila el modelo falla. Conviene **destildar *Use Row Headers* en todas las líneas**.

---

## 4. Recursos del Process Flow (30/09)

En el Process Flow `Comedor` se crearon los cuatro recursos compartidos: `PuestosValidacion`, `LineaVegetariana`, `LineaNoVegetariana` y `Asientos`, con *Reference* = **Numeric**.

![Los cuatro recursos del Process Flow Comedor y el panel Properties de PuestosValidacion con Reference Numeric y Count 1](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-06.png)

> Con el cambio de alcance (sección 6 de este documento), estos recursos cambian: `LineaVegetariana`, `LineaNoVegetariana` y `Asientos` pasan a ser `PuestoViandas`, `EspacioFilaServicio` y `ServicioComida`.

En esta captura, `PuestosValidacion` todavía tiene *Count* = 1. Después se cambió por la expresión que lee `PuestosBase + PuestosExtra` de la tabla `Escenarios`. También hubo que volver a elegir *Numeric* de la lista, porque escrito a mano daba el error *Undefined variable Numeric* al hacer Reset.

---

## 5. Inicio del día y control del puesto (30/09)

Se agregaron las actividades de la sección 8 de la guía. La primera en configurarse fue `Bloquear puestos base`, un *Acquire Resource* que ya apunta a `PuestosValidacion` (la línea azul que los une).

![Process Flow con Bloquear puestos base unido a PuestosValidacion por una línea azul, y las actividades Inicio del dia, Preparar el dia, Crear cola previa, Crear control extra, Hasta la apertura, Abrir puestos base y Fin del control sueltas](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-07.png)

Ya están creadas las 14 actividades de las dos columnas: las 8 del inicio del día y las 6 del puesto extra.

![Process Flow Comedor con las 14 actividades de la sección 8 creadas pero sueltas, sin flechas entre ellas, junto a los cuatro recursos](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/avance-08.png)

> **A corregir.** Las actividades están **sueltas**: todavía no hay flechas entre ellas, así que los tokens no pasarían de una a otra. Hay que ordenarlas en dos columnas y conectarlas. Para eso se arrastra cada una y se suelta pegada debajo de la anterior, o se tira una flecha desde el borde de una a la siguiente.
>
> - **Columna 1:** Inicio del dia → Preparar el dia → Crear cola previa → Crear control extra → Bloquear puestos base → Hasta la apertura → Abrir puestos base → Fin del control
> - **Columna 2:** Bloquear puesto extra → Hasta que abre el extra → Abrir puesto extra → Hasta que cierra el extra → Cerrar puesto extra → Puesto extra cerrado
>
> La columna 2 no recibe ninguna flecha desde arriba: sus tokens llegan desde `Crear control extra`, por el *Destination* elegido con el gotero.

---

## 6. Cambio de alcance (30/09)

Al subir el avance al repositorio apareció un cambio del 23/09 que no estaba en esta copia: **el sistema llega hasta el mostrador** (D02 revisada). El salón y el retiro para llevar quedan fuera, y el menú solo se distingue por ser con o sin TACC. En su lugar entran:

- **Retiro de varias raciones por persona (S21):** una persona puede presentar varios DNI. Cada DNI suma tiempo en la caja y cada ración suma tiempo en el mostrador.
- **Fila de servicio y mostrador:** 2 personas sirviendo (S22) y una fila entre la caja y el mostrador. Si esa fila se llena, bloquea la caja (S23, capacidad pendiente).
- **Escenarios nuevos:** E4 separa la fila de viandas de la general (D06) y E5 suma una tercera persona en el servicio.

Esto responde al pedido de la cátedra: ver si al mejorar la caja la cola se corre al mostrador. La réplica en Python lo confirma. Con 2 puestos, la cola del mostrador pasa de unas 4 a unas 24 personas en el pico; con 3 personas sirviendo, baja a unas 6.

Para no pisar el cambio, se regeneraron `inputs.xlsx`, la guía y la réplica. Los supuestos de la versión anterior que siguen valiendo cambiaron de número: factor QR (S24), demora de apertura (S25) e interrupción del 18/8 (S26).

**Qué se conserva del modelo:** la configuración (sección 1 de este documento), la importación, el parámetro `Escenario`, `PuestosValidacion` y las actividades de la sección 8 de la guía. **Qué cambia:** las tablas de entrada y de salida, tres recursos y una tercera columna de control para el puesto de viandas. El detalle está en la sección 20 de la guía.

---

## 7. Parámetro `Escenario` (07/10)

Se creó la tabla de parámetros del modelo con un único parámetro, `Escenario`: un entero de 1 a 12 que indica qué fila de la tabla `Escenarios` usa la corrida. Queda en 1 (`E0_Pico`) para las pruebas. Además de *Type* = Integer y los límites *Lower Bound* = 1 y *Upper Bound* = 12, tiene el *Reference* apuntando a `/Tools/GlobalTables/Escenarios`, que permite elegir la fila desde la tabla.

![Panel del parámetro Escenario con valor 1, Type Integer, Lower Bound 1, Upper Bound 12 y Reference /Tools/GlobalTables/Escenarios](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/Captura%20parametro%20Escenario.png)

---

## 8. Las tres columnas conectadas (07/10)

Ya están conectadas las 3 columnas de la sección 8, con `Crear control viandas` incluido. Las columnas 2 y 3 no reciben flecha desde arriba, porque sus tokens llegan por el *Destination* de los *Create Tokens*.

![Process Flow Comedor con las tres columnas de actividades unidas por flechas: inicio del día, puesto extra y puesto de viandas](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/Captura%203%20columnas%20conectadas.png)

Con `PuestosValidacion` seleccionado, las líneas azules llegan a las tres actividades que lo toman: `Bloquear puestos base`, `Bloquear puesto extra` y `Cerrar puesto extra`. Los *Release* no aparecen unidos al recurso porque liberan lo guardado en la label del token (`token.bloqueo`). Por eso `PuestoViandas` muestra una sola línea, la de `Bloquear puesto viandas`. Es lo esperado.

![Process Flow con PuestosValidacion seleccionado y tres líneas azules hacia Bloquear puestos base, Bloquear puesto extra y Cerrar puesto extra; EspacioFilaServicio, PuestoViandas y ServicioComida arriba sin conexiones](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/Captura%20recursos%20y%20bloqueos.png)

> **Falta.** Completar los campos de cada actividad (sección 8 de la guía), con el *Destination* de `Crear control extra` y `Crear control viandas` elegido con el gotero, y hacer Reset.

---

## 9. Etapa A probada: llegadas, fila de caja y validación (09/10)

Con las tablas reimportadas y las llegadas conectadas, el modelo corre de punta a punta hasta la validación. En el camino aparecieron dos errores que conviene dejar anotados.

**Error 1: tablas mal importadas.** `ColaPrevia` no traía la columna `Perfil` y la *System Console* repetía *Perfil is not a valid column name*. Se resolvió reimportando todas las tablas con *Use Row Headers* destildado y *Total Rows* = filas de datos + 1.

**Error 2: los dos `Grupo` no estaban conectados a `Asignar tipo y raciones`.** Los tokens salían del Custom Code y se quedaban parados, con las tablas de salida vacías.

**Error 3: la cola previa no llegaba antes de abrir.** El *Delay Time* de `Llega entre 11:40 y 12:00` decía `exponential(...)` y no `uniform(0, 1200, getstream(activity))`. A las 11:59:50 todavía había 25 tokens en el Delay y solo 40 esperando en la fila; con la corrección la cola máxima de la caja dio 70 personas.

![Process Flow a las 11:59:50 con 25 tokens todavía en el Delay de la cola previa, 40 esperando en Esperar en la fila y PuestosValidacion con 1 unidad tomada por el control](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/Captura%20cola%20previa%20a%20las%2011-59.png)

El recurso `PuestosValidacion` muestra una unidad tomada (el token de control, en verde) y las personas esperando (en rojo): el bloqueo hasta la apertura funciona.

**Resultado de la corrida de E0_Pico.** La cola máxima en la caja es de 70 personas (objetivo S10: 60 a 70; la réplica da 71). Las raciones por franja de 10 minutos, desde las 12:00 hasta las 14:40, siguen la curva real: 106, 145, 135, 122, 108, 96, 122, 116, 132, 97, 69, 84, 70, 83, 49 y 5.

![Tabla Salida_Franjas con 16 filas de raciones validadas por franja de 10 minutos, de 106 en la primera a 5 en la última](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/Captura%20raciones%20por%20franja%20E0.png)

`Salida_Personas` queda solo con la fila `plantilla`, porque se llena con `Registrar y salir` (sección 15 de la guía), que todavía no está armada.

---

## 10. Servicio con 3 personas y menú vegetariano (14/10)

Se aplicó la [guía de modificaciones](../GUIA_MODIFICACIONES.md). Ya no hay fila de viandas: la columna 3 completa y el Decide `¿Que fila?` se borraron, y todas las personas pasan por `Esperar en la fila`. Los recursos son `PuestosValidacion`, `PuestoVeg` (antes `PuestoViandas`), `EspacioFilaServicio` y `ServicioComida`.

![Process Flow Comedor completo: inicio del día, puesto extra y el circuito de la persona con el Decide ¿Es Vegetariano? y el Decide ¿Usó el puesto vegetariano?](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/processflow-servicio-veg.png)

El tramo del servicio, ampliado. Los conectores se llaman `veg` y `general` en el primer Decide, y `si` y `no` en el segundo. Quien es vegetariano toma primero `PuestoVeg` y después una de las tres personas (`ServicioComida`); al terminar libera el servidor y, solo si usó el puesto vegetariano, lo libera también.

![Tramo del servicio: ¿Es Vegetariano? con las ramas veg y general, Esperar Servidor, Servir raciones, Liberar servidor y ¿Usó el puesto vegetariano? con las ramas si y no](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/servicio-decide-veg.png)

## 11. Tiempo de servicio de 15 a 20 s (14/10)

El mostrador con 3 personas y 21 s por ración no alcanzaba para el ritmo de la caja (unas 514 raciones por hora contra más de 900), y generaba una cola de servicio que no coincide con lo observado. El grupo asumió **15 a 20 s por ración**. En `TiemposServicio`, `ServicioRacion` quedó con `Scale` = 17,3 y `Shape` = 0,09: mediana 17,3 s y media 17,4 s. La validación sigue en 3,34 s de mediana (3,77 s de media).

![Tabla TiemposServicio con Validacion en Scale 3,34 y Shape 0,49, y ServicioRacion en Scale 17,30 y Shape 0,09, con mediana 17,30 y media 17,40](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/tiempos-servicio-17-3.png)

El razonamiento completo está en [EXPLICACION.md](../EXPLICACION.md).

## 12. Primera corrida de E0_Pico con el servicio (14/10)

`Salida_Dia` de la corrida con `Escenario` = 1:

![Tabla Salida_Dia con Apertura_s 1314,50, EnFilaCaja 0, ColaCajaMax 66, EnFilaServicio 0 y ColaServicioMax 131](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/salida-dia-e0.png)

| Indicador | FlexSim (una corrida) | Réplica de Python (media de 30) | Objetivo |
|---|---|---|---|
| `ColaCajaMax` | 66 | 71 | 60 a 70 (S10) |
| `ColaServicioMax` | 131 | 158 | Entre 120 y 200 (guía) |

Las dos colas caen en el rango esperado y la cola de la caja coincide con la observada. Es una sola corrida: la comparación formal con réplicas y con los registros reales la hace `analisis/validar_modelo.py`, con las salidas exportadas. Que `EnFilaCaja` y `EnFilaServicio` terminen en 0 indica que el día cerró sin gente en cola.

---

## 13. Escena 3D (14/10)

Se empezó la escena 3D. El primer paso fue **importar el dibujo hecho en SketchUp** (`3d/comedor-v00.skp`, exportado a `comedor-v00.dae`): el salón con seis mesas largas con sillas, en dos grupos de tres, y al fondo dos ambientes separados por un muro, donde van el mostrador y la cocina. Todavía es solo la geometría: no hay objetos de FlexSim ni personas, y los puestos no están conectados al Process Flow.

![Vista de la escena 3D en FlexSim con el comedor importado desde SketchUp: seis mesas largas con sillas y, al fondo, dos ambientes separados por un muro](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/flexsim/capturas/escena3d-importada.png)

## Próximos pasos

1. Exportar las tres tablas de salida a `flexsim/salidas.xlsx` y correr `python analisis/validar_modelo.py --escenario E0_Pico`.
2. Correr el escenario base con 10 a 12 s por ración como análisis de sensibilidad, y E4 y E5 (4 personas sirviendo).
3. Pedirle al referente que cronometre solo el servicio y estime la caminata entre la caja y el mostrador. Con eso se cierra S15.
4. Confirmar el 12 % de menú vegetariano (S27) y el espacio de la fila de servicio (S23).
5. Seguir con la escena 3D: ubicar el puesto de validación y el mostrador sobre el dibujo y ver si conviene animar a las personas.
