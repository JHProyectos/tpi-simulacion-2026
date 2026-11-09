# Guía paso a paso: personas y servicios en el comedor 3D

[TOC]

Esta guía lleva a la práctica `GUIA_PERSONAS_3D.md` sobre el modelo nuevo (`comedor_unc_2.fsm` con la Shape del comedor hecho en Blender). Las posiciones salen de `UBICACIONES_3D.md`. El orden es el de la guía original, con cada fase probada antes de pasar a la siguiente.

> **Sin licencia completa:** FlexSim limita el Process Flow a 35 actividades y esta guía llega a más. En ese caso, para la animación seguí `GUIA_MODELO_VISUAL_3D.md` (modelo aparte que reproduce una corrida real). Esta guía queda para una máquina con licencia.

Los pasos marcados con **†** no pude verificarlos en la documentación (la ayuda online de FlexSim 2026 no carga): si un nombre o un campo no coincide, mandame una captura de esa ventana y lo ajusto. Usá FlexSim **en inglés**.

## 0. Antes de empezar

### 0.0 Dónde está cada cosa en FlexSim

En toda la guía uso estos nombres. Esta es la tabla para encontrarlos:

| Qué | Dónde está |
|---|---|
| **Menú superior** | La barra de arriba de todo: **File, Edit, View, Build, Statistics, Debug, Help** |
| **Guardar, guardar como** | **File > Save** (`Ctrl+S`) y **File > Save As...** |
| **Deshacer** | **Edit > Undo** (`Ctrl+Z`) |
| **Configuración del modelo** | **Edit > Model Settings** (unidades, cantidad de *streams* aleatorios) |
| **Barra de simulación** | Arriba de la vista central: botones **Reset**, **Run**, **Stop**, **Fast Forward**, **Skip**, **Step**, el reloj **Run Time** y el deslizador **Run Speed** |
| **Biblioteca (Library)** | Panel de la izquierda, con los grupos **Fixed Resources**, **Visual**, **People**, etc. Si no se ve: **View > Drag-Drop Library** |
| **Toolbox** | Panel con el botón **+** para crear tablas, Process Flows y parámetros. Si no se ve: **View > Toolbox** |
| **Panel de propiedades (Properties)** | Se abre al hacer **doble clic** sobre un objeto o una actividad. Si no aparece: **View > Properties** |
| **Árbol del modelo (Model Tree)** | **View > Model Tree**. Lista todos los objetos por nombre, sin tener que tocarlos en la vista 3D |
| **Pestañas de la vista central** | La fila de pestañas sobre la vista 3D: cada Process Flow, cada tabla y la vista 3D tienen la suya |
| **Mensajes de error** | **Debug > Output Console** |
| **Experimenter** | **Statistics > Experimenter** |
| **Tablas de entrada y de salida con Excel** | **Toolbox > Excel Import/Export** (pestañas **Import** y **Export**) |

Si un panel desapareció, casi siempre se recupera desde el menú **View**.

### 0.1 Qué tenés que tener

- [ ] `comedor_unc_2.fsm` abierto, con la Shape del comedor puesta en X = 8,24 · Y = −47,75 · Z = 0
- [ ] El defecto del menú vegetariano corregido (`AYUDA_IA.md`, sección 5)
- [ ] Los archivos del DAE y sus texturas juntos en una carpeta (se ve el damero en el piso)
- [ ] El modelo **funcionando sin 3D**: corre E0_Pico y las tablas de salida se llenan

### 0.2 Copia de seguridad

1. Menú superior: **File > Save As...**. Se abre el explorador de archivos.
2. Guardá una copia como `comedor_unc_2_antes3d.fsm` en la misma carpeta (`flexsim/`).
3. Ojo: después de **Save As**, el modelo abierto pasa a ser la copia. Volvé al de trabajo con **File > Open Model...** y elegí `comedor_unc_2.fsm` (o **File > Recent Models**).

Si algo sale mal más adelante, abrís `comedor_unc_2_antes3d.fsm`.

### 0.3 Corrida de referencia

**Sobre la semilla.** FlexSim no te muestra un número de semilla para anotar. Para que dos corridas den lo mismo se usa la opción **Repeat Random Streams**: con esa opción activa, cada **Reset** reinicia los generadores aleatorios en el mismo punto y el modelo da siempre el mismo resultado. Entonces no hay nada que anotar: alcanza con dejar la opción activa durante toda la guía.

1. **Parámetro `Escenario`.** En el **Toolbox** (panel con el botón **+**), abrí la tabla **Parameters** (grupo *Statistics*) con doble clic. En la fila `Escenario` poné el valor **1** (E0_Pico) y presioná Enter.
2. **Repeat Random Streams.** Menú superior **Statistics > Repeat Random Streams**. Tiene que quedar con tilde (si ya la tenía, no la toques). Mirá el menú de nuevo para confirmar. También hay un botón equivalente en la barra de herramientas.
3. **Corrida.** En la barra de simulación apretá **Reset** y después **Run**. La corrida se detiene sola a las 16:00 (`t = 15600`). Si no se detiene ahí, hacé clic en el reloj **Run Time** y poné el *Stop Time* en 16:00. Para ir más rápido, subí el **Run Speed** o usá **Fast Forward**.
4. **Exportar.** **Toolbox > Excel Import/Export**, pestaña **Export**, y apretá **Export Tables** (con las tres tablas de salida tildadas). Se crea o se actualiza `flexsim/salidas.xlsx`.
5. **Renombrar.** Cerrá `salidas.xlsx` si está abierto en Excel. En el Explorador de Windows, renombrá `flexsim/salidas.xlsx` a `salidas_sin3d_E0_Pico.xlsx`.

Esta es la referencia contra la que se compara al final de la fase 3. Cuando después corras con personas, tiene que estar activo **Repeat Random Streams** también, si no la comparación no vale.

### 0.4 Los números clave de la escena

| Dato | Valor |
|---|---|
| El edificio ocupa | X de 0 a 16,5 · Y de −95,5 a 0 |
| El piso está a | **Z = 0,30** |
| Eje del pasillo central | X = 8,33 |
| Pared de los pasos | Y = −10,1 |

Todos los objetos nuevos van con **Z = 0,30**. Si preferís Z = 0, bajá la Shape a Z = −0,30 y no mezcles las dos.

## 1. Fase 1: poner los objetos en la escena

### 1.1 Cómo se crea y se ubica un objeto

1. **Biblioteca (panel de la izquierda).** Tiene grupos plegables con un **+** o **−** a la izquierda del título. Buscá el grupo **People** (debajo de *Fixed Resources*, *Task Executers*, etc.; hay que bajar con la rueda del mouse) y tocá su **+** para abrirlo. Si no ves la biblioteca: **View > Drag-Drop Library**. En el cuadro de búsqueda de arriba también podés escribir `Location`, `Staff` o `Waiting Line`.
2. **Crear el objeto.** Hacé clic sobre el objeto de la biblioteca, **mantené apretado**, arrastralo a la vista 3D y soltalo en un lugar **vacío** (afuera del edificio, para no mover la Shape sin querer).
3. **Abrir sus propiedades.** Doble clic sobre el objeto nuevo en la vista 3D. Si no aparece el panel, **View > Properties**. También podés elegirlo por nombre en **View > Model Tree**.
4. **Ponerle nombre.** Arriba del panel de propiedades hay un cuadro con el nombre actual (por ejemplo `Location1`). Borralo, escribí el nombre exacto de la tabla y apretá Enter.
5. **Posición.** En el panel, sección **Visuals**, hay tres filas de tres números cada una: la primera es la **posición (X, Y, Z)**, la segunda la **rotación** y la tercera el **tamaño**. Hacé clic en cada casilla de la fila de la posición, escribí el valor y apretá Enter (o Tab para pasar a la siguiente casilla). Los decimales van con **punto**, no con coma.
6. **Verificar.** Mirá en la vista 3D que el objeto cayó donde corresponde. Para alejar o acercar la vista usá la rueda del mouse, y para girarla, el botón derecho apretado†. Para encontrar un objeto perdido: seleccionalo en **View > Model Tree** y mirá su posición en **Visuals**.
7. **Si movés algo sin querer:** **Edit > Undo** (`Ctrl+Z`) deshace el último cambio.

Antes de seguir con todos, probá solo estos dos. Son la prueba de que las coordenadas están bien.

| Objeto | Tipo | X | Y | Z |
|---|---|---|---|---|
| `Caja_Loc1` | Location | 6,72 | −12,41 | 0,30 |
| `Puerta` | Location | 7,98 | −94,50 | 0,30 |

- [ ] `Caja_Loc1` queda en el pasillo, pegado al cubículo izquierdo (donde marcaste con la cruz roja)
- [ ] `Puerta` queda en el extremo sur del salón

Si alguno cae en otro lado, **no sigas**: avisame.

### 1.2 Los Location

Un Location es el lugar donde se para una persona. Creá estos con la secuencia de 1.1:

| Nombre | X | Y | Z |
|---|---|---|---|
| `Puerta` | 7,98 | −94,50 | 0,30 |
| `Salida` | 10,98 | −94,50 | 0,30 |
| `Caja_Loc1` | 6,72 | −12,41 | 0,30 |
| `Caja_Loc2` | 9,80 | −12,50 | 0,30 |
| `Paso_Central` | 8,25 | −10,10 | 0,30 |
| `Mostrador_Loc1` | 2,23 | −8,75 | 0,30 |
| `Mostrador_Loc2` | 5,33 | −8,75 | 0,30 |
| `Mostrador_Loc3` | 8,23 | −8,75 | 0,30 |
| `Mostrador_Loc4` | 11,23 | −8,75 | 0,30 |
| `Veg_Loc` | 15,03 | −8,75 | 0,30 |

`Paso_Central` es un punto de paso: las personas lo cruzan al ir al mostrador y al salir, para no atravesar la pared (ver sección 6).

Configuración sugerida†: a `Caja_Loc1` y `Caja_Loc2`, la forma **Registration**; a los `Mostrador_Loc` y a `Veg_Loc`, **Floor Spot**. Dónde se cambia: abrí el Location con doble clic y, en el panel de propiedades, buscá la lista desplegable de configuraciones prearmadas (arriba de las secciones, junto al ícono del objeto). `Puerta`, `Salida` y `Paso_Central` pueden quedar como Floor Spot. Si no encontrás la lista, dejalos con la forma por defecto: es solo estético.

### 1.3 El personal (Staff)

El personal es decorativo en esta versión: no se adquiere como recurso, solo da vida a la escena.

| Nombre | X | Y | Z | Mira hacia |
|---|---|---|---|---|
| `Cajero1` | 5,33 | −12,41 | 0,30 | +X (el pasillo) |
| `Cajero2` | 11,23 | −12,50 | 0,30 | −X (el pasillo) |
| `Servidor1` | 2,23 | −6,15 | 0,30 | −Y (los clientes) |
| `Servidor2` | 5,33 | −6,15 | 0,30 | −Y |
| `Servidor3` | 8,23 | −6,15 | 0,30 | −Y |
| `Servidor4` | 11,23 | −6,15 | 0,30 | −Y |

1. Creá cada uno con el objeto **Staff** del grupo **People** de la biblioteca (pasos 1 a 5 de la sección 1.1).
2. A los dos cajeros ponerles la configuración **Clerk**†. Se elige en la lista desplegable de configuraciones del panel de propiedades del Staff (doble clic sobre el objeto). A los servidores, la que más se parezca a un cocinero o empleado.
3. Para que miren a donde corresponde, cambiá la **rotación Z**: es la **tercera casilla de la segunda fila de la sección Visuals** del panel de propiedades. Se prueba con 0, 90, 180 y 270 y se mira en la vista 3D hasta que el cajero mire al pasillo.
4. **Cajero2** y **Servidor4** se usan solo en algunos escenarios (sección 5).

### 1.4 Las filas (Waiting Line)

1. De la biblioteca (grupo **People**) arrastrá dos **Waiting Line** a un lugar vacío de la vista 3D y nombralas `Fila_Caja` y `Fila_Servicio` (cuadro de nombre arriba del panel de propiedades).
2. Abrí cada una con doble clic. En el panel de propiedades aparecen los campos **Points** (los puntos de la línea), **Gap Size**, **Single Entry Point**, **Width**, **Draw Floor** y **Draw Stanchions**. Es probable que estén en una pestaña o sección propia de la Waiting Line, aparte de **Visuals**†: recorré las secciones del panel hasta encontrarlos. Los puntos se editan en una tabla con X, Y, Z por fila†: usá el botón de agregar un punto y completá las casillas.
3. Cargá los puntos:

| Fila | Puntos (X, Y) | *Gap Size* | *Single Entry Point* |
|---|---|---|---|
| `Fila_Caja` | 1.º (8,33 ; −13,8), 2.º (8,33 ; −80) | 0,6 | Tildado |
| `Fila_Servicio` | 1.º (8,25 ; −10,6), 2.º (8,25 ; −13,0) | 0,6 | Tildado |

4. Destildá **Draw Floor** en las dos (si no, tapan el damero con un cartel de piso).
5. **Draw Stanchions** podés dejarlo en la `Fila_Caja`: ya hay postas con cuerda en el modelo, así que si se superponen, destildalo.

Si el primer punto resulta ser el fondo y no el frente, se invierten (pregunta L3, fase 2).

### 1.5 Las tablas de estado

1. **Crear la tabla.** En el **Toolbox**, apretá el botón **+** y elegí **Global Table**. Aparece una tabla nueva con un nombre por defecto. Abrila con doble clic: se abre en una pestaña de la vista central. Cambiale el nombre arriba del panel de propiedades a `Ubicaciones`.
2. **Tamaño.** Con la tabla seleccionada, en **Quick Properties** (panel de propiedades de la derecha) están las casillas **Rows** y **Columns**: poné 6 filas y 8 columnas.
3. **Encabezados.** Hacé **doble clic** sobre cada encabezado de columna y escribí `Objeto`, `Rol`, `Numero`, `X`, `Y`, `Z`, `EstX`, `EstY`.
4. **Datos.** Doble clic sobre una celda, escribí el valor y apretá Enter. Cargala con estos valores (los textos como texto y los números con **punto** decimal):

| Objeto | Rol | Numero | X | Y | Z | EstX | EstY |
|---|---|---|---|---|---|---|---|
| Cajero1 | Cajero | 1 | 5,33 | −12,41 | 0,30 | −4 | −12,41 |
| Cajero2 | Cajero | 2 | 11,23 | −12,50 | 0,30 | −4 | −12,50 |
| Servidor1 | Servidor | 1 | 2,23 | −6,15 | 0,30 | −4 | −6,15 |
| Servidor2 | Servidor | 2 | 5,33 | −6,15 | 0,30 | −4 | −6,15 |
| Servidor3 | Servidor | 3 | 8,23 | −6,15 | 0,30 | −4 | −6,15 |
| Servidor4 | Servidor | 4 | 11,23 | −6,15 | 0,30 | −4 | −6,15 |

5. **Tablas de estado.** Repetí los pasos 1 a 4 con el botón **+** del Toolbox para crear `EstadoPuestos` (2 filas, 1 columna `Ocupado`) y `EstadoServidores` (4 filas, 1 columna `Ocupado`). Cargá ceros en todas las celdas.
6. Son **provisorias**: la regla del proyecto es que los valores no se editan a mano. Cuando se confirmen con el referente, hay que pasarlas a `analisis/generar_inputs_flexsim.py` (se edita en un editor de texto, fuera de FlexSim).

### 1.6 Prueba de la fase 1

- [ ] Todos los Location, Staff y Waiting Line están en la escena y con su nombre exacto
- [ ] Los cajeros están dentro de los cubículos y miran al pasillo
- [ ] Los servidores están detrás de las cubetas
- [ ] **Reset** y **Run** (barra de simulación) funcionan igual que antes (el modelo sin personas no cambió)

Guardá el modelo con **File > Save** (`Ctrl+S`).

## 2. Fase 2: laboratorio

Antes de tocar `Comedor`, armá un Process Flow aparte para entender cómo se comporta FlexSim. Las respuestas definen el resto.

### 2.1 Armarlo

1. **Crear el Process Flow.** En el **Toolbox**, botón **+ > Process Flow > General**. Se crea uno nuevo y se abre en una pestaña de la vista central. Nombre `Prueba_People` (cuadro de nombre arriba del panel de propiedades).
2. **Biblioteca de actividades.** Hacé clic en el **fondo vacío** de la ventana del Process Flow: la biblioteca de la izquierda pasa a mostrar las actividades (grupos *Token Creation*, *Basic*, *Shared Assets*, y los de People: *People Basic*, *People Sub Flows*, *People Resources*, *People Activity Sets*).
3. **Schedule Source.** Del grupo *Token Creation* arrastrá **Schedule Source** al fondo de la ventana. Doble clic sobre la actividad: en el panel de propiedades, en su tabla de llegadas (*Arrivals*) poné una fila con *Arrival Time* = 0 y *Quantity* = 20.
4. **Create Person.** Del grupo *People Basic* arrastrá **Create Person** y soltala **pegada debajo** de la anterior (se conectan solas). En sus propiedades: *Person* = Random Person, *Destination* = `Puerta` y *Copy Token Labels* tildado. *Destination* se completa con el **gotero** (ícono de cuentagotas junto al campo): hacés clic en el gotero y después clic en el objeto `Puerta` en la vista 3D.
5. **Set Wait in Line then Process.** Del grupo *People Activity Sets* arrastrá **Wait in Line then Process** debajo de Create Person. Trae los bloques y tres recursos: Waiting Line, Location y Staff. Doble clic en cada recurso y, con el gotero, elegí en la vista 3D: *Waiting Line* = `Fila_Caja`, *Location* = `Caja_Loc1`, *Staff* = `Cajero1`.
6. **Tiempo del proceso.** Doble clic en la actividad *Process* del set y poné un tiempo fijo de 5 segundos en su campo de tiempo (*Delay Time*†).
7. **Cierre.** Del grupo *People Basic* arrastrá **Remove Person** y, del grupo *Basic* o *Token Creation*, un **Sink**, uno debajo del otro.
8. **Conectar lo suelto.** Una actividad sin flecha de entrada no recibe tokens. Para conectar, arrastrá desde el **borde** de la actividad de origen hasta la de destino.

### 2.2 Qué mirar

Apretá **Reset** y **Run** en la barra de simulación. Conviene tener a la vista la pestaña de la vista 3D y, en otra, la del Process Flow `Prueba_People` (las pestañas están en la fila sobre la vista central; podés arrastrar una pestaña para ver las dos lado a lado, o alternar entre ellas). Bajá el **Run Speed** para ver bien. Contestá y anotá en la tabla de la sección 7:

| # | Pregunta | Cómo saberlo |
|---|---|---|
| L1 | ¿En qué *label* del token queda la persona creada? | Frená con **Stop**. En la pestaña del Process Flow, hacé clic sobre un token (el círculo que viaja entre actividades) o sobre una actividad con tokens dentro. En el panel de propiedades, buscá la sección **Labels**† del token y mirá qué nombre tiene el que guarda a la persona |
| L2 | ¿La persona sigue en la fila mientras espera el puesto? | En la vista 3D, con el puesto ocupado 5 s por persona, ¿se ven las 19 personas esperando en la `Fila_Caja`? |
| L3 | ¿El primer punto de la Waiting Line es el frente o el fondo? | En la vista 3D, ¿dónde se para la primera persona: junto a los puestos o en el otro extremo de la línea? |
| L4 | ¿Cuál es la velocidad de caminata y dónde se cambia? | Hacé doble clic sobre una persona en la vista 3D y mirá su panel de propiedades; buscá una sección de viaje o de velocidad† |

Si **L2** da "sale de la fila al llegar al frente", avisame: hay que cambiar el diseño de la sección 3.2.

## 3. Fase 3: personas en el Process Flow del comedor

**Dónde se trabaja.** En el **Toolbox**, grupo de Process Flows, doble clic sobre `Comedor`: se abre su ventana en una pestaña de la vista central. Para ver la biblioteca de actividades, hacé clic en el **fondo vacío** de esa ventana.

**Cómo se inserta una actividad.** Arrastrala desde la biblioteca de actividades (panel izquierdo) y soltala **justo debajo** de la actividad que va antes: queda en el mismo bloque y se conecta sola. Si quedó suelta, arrastrá desde el **borde** de la actividad de origen hasta la de destino.

**Cómo se configura.** Doble clic sobre la actividad: el panel de propiedades muestra sus campos. El nombre se cambia en el cuadro de arriba del panel. Los campos que apuntan a un objeto 3D o a otra actividad tienen un **gotero**: apretás el gotero y hacés clic en el objeto o la actividad.

**Dónde se pega el código.** En una actividad **Custom Code**, el panel tiene un botón con ícono de pergamino (editor de código): al apretarlo se abre una ventana con las cuatro líneas de abajo ya escritas. Pegá el código **debajo** de esas líneas. En los campos de una sola expresión (por ejemplo *Destination*) se escribe directo en el campo, sin las cuatro líneas.

Todos los códigos van **debajo de las cuatro líneas** que trae el editor:

```c
Object current = param(1);
treenode activity = param(2);
Token token = param(3);
treenode processFlow = ownerobject(activity);
```

En esta guía llamo `token.persona` al label donde queda la persona creada. Si la respuesta de L1 es otra, reemplazala.

### 3.1 La persona entra

| Actividad | Nombre | Dónde va | Propiedades |
|---|---|---|---|
| Create Person | `Crear persona` | Justo después de `Asignar tipo y raciones` | *Person:* Random Person · *Destination:* `Puerta` · *Copy Token Labels:* tildado |

### 3.2 La caja

| Orden | Actividad | Nombre | Dónde va | Propiedades |
|---|---|---|---|---|
| 1 | Wait in Line | `Ir a la fila de caja` | Antes de `Esperar en la fila` | *Person:* `token.persona` · *Waiting Line:* `Fila_Caja` |
| 2 | Custom Code | `Elegir puesto de caja` | Después de `Esperar en la fila` | Código de abajo |
| 3 | Walk | `Ir al puesto de caja` | Después de `Elegir puesto de caja` | *Person:* `token.persona` · *Destination:* `Model.find("Caja_Loc" + string.fromNum(token.numPuesto))`† |
| 4 | Custom Code | `Liberar puesto de caja` | Justo antes de `Liberar puesto` | Segundo código de abajo |

`Esperar en la fila` (el Acquire de `PuestosValidacion`) **sigue exactamente como está**.

**Elegir puesto de caja:**

```c
/** Elige el puesto de caja libre de menor número (solo para el 3D) */
Table ep = Table("EstadoPuestos");
int n = 1;
for (int r = 1; r <= ep.numRows; r++) {
	if (ep[r]["Ocupado"] == 0) {
		n = r;
		break;
	}
}
ep[n]["Ocupado"] = 1;
token.numPuesto = n;
```

**Liberar puesto de caja:**

```c
Table("EstadoPuestos")[token.numPuesto]["Ocupado"] = 0;
```

### 3.3 Del cubículo al mostrador

Hay una pared entre el salón y el mostrador, con tres pasos con puerta. Si la persona camina en línea recta del cubículo a un `Mostrador_Loc`, **atraviesa la pared**. Por eso se la hace pasar por `Paso_Central`.

| Orden | Actividad | Nombre | Dónde va | Propiedades |
|---|---|---|---|---|
| 1 | Wait in Line | `Ir a la fila de servicio` | Después de `En la fila de servicio`, antes de `¿Es Vegetariano?` | *Person:* `token.persona` · *Waiting Line:* `Fila_Servicio` |
| 2 | Custom Code | `Elegir lugar del mostrador` | Después de `Esperar Servidor` | Código de abajo |
| 3 | Walk | `Ir al paso` | Después de `Liberar lugar en la fila` | *Person:* `token.persona` · *Destination:* `Paso_Central` |
| 4 | Walk | `Ir al mostrador` | Después de `Ir al paso`, antes de `Empieza el servicio` | *Person:* `token.persona` · *Destination:* ver abajo |
| 5 | Custom Code | `Liberar lugar del mostrador` | Antes de `Liberar servidor` | Código de abajo |

**Elegir lugar del mostrador:**

```c
/** Elige el lugar libre de menor número del mostrador (solo para el 3D) */
Table es = Table("EstadoServidores");
int n = 1;
for (int r = 1; r <= es.numRows; r++) {
	if (es[r]["Ocupado"] == 0) {
		n = r;
		break;
	}
}
es[n]["Ocupado"] = 1;
token.numServidor = n;
```

**Destination de `Ir al mostrador`†.** Los vegetarianos van al puesto vegetariano:

```c
token.esVeg ? Model.find("Veg_Loc") : Model.find("Mostrador_Loc" + string.fromNum(token.numServidor))
```

Si el campo no acepta el operador condicional, resolvelo en `Elegir lugar del mostrador` y guardá el destino en `token.destino`. Si el label del menú vegetariano no se llama `esVeg`, usá el que corresponda.

**Liberar lugar del mostrador:**

```c
Table("EstadoServidores")[token.numServidor]["Ocupado"] = 0;
```

### 3.4 La salida

| Orden | Actividad | Nombre | Dónde va | Propiedades |
|---|---|---|---|---|
| 1 | Walk | `Salir por el paso` | Después de `Registrar y salir` | *Person:* `token.persona` · *Destination:* `Paso_Central` |
| 2 | Walk | `Ir a la salida` | Después de `Salir por el paso` | *Person:* `token.persona` · *Destination:* `Salida` |
| 3 | Remove Person | `Quitar persona` | Después de `Ir a la salida`, antes del Sink | *Person:* `token.persona` |

`Registrar y salir` **no se mueve**: así `tSalida` sigue marcándose al terminar el servicio y la caminata no cambia ningún indicador.

### 3.5 Preparar el día

En la ventana de `Comedor`, buscá la actividad `Preparar el día` (el Custom Code que está debajo de `Inicio del día`, en la primera columna). Doble clic, apretá el botón del pergamino y pegá **al final** del código que ya tiene el bloque de la sección 8.1 de `GUIA_PERSONAS_3D.md` (ubica al personal según el escenario e inicializa las tablas de estado). No borres lo que ya estaba.

### 3.6 Prueba de la fase 3

1. **Escenario.** Toolbox > tabla **Parameters** > `Escenario` = 1. Menú **Statistics > Repeat Random Streams** con tilde.
2. **Correr.** Barra de simulación: **Reset**, **Run** hasta las 16:00.
3. **Exportar.** **Toolbox > Excel Import/Export**, pestaña **Export**, **Export Tables**. Antes de seguir, renombrá `flexsim/salidas.xlsx` a `salidas_con3d_E0_Pico.xlsx` en el Explorador de Windows, para que la próxima exportación no lo pise.
4. **Comparar** con `salidas_sin3d_E0_Pico.xlsx` (abrí los dos en Excel):

| Indicador | Qué tiene que pasar |
|---|---|
| Personas del día | Igual |
| Raciones por franja | Igual |
| Tiempo de validación | Igual |
| Espera en la fila de caja | Casi igual (suma la caminata hasta el puesto) |
| Espera en la fila de servicio | Más alta (suma la caminata y el efecto de la capacidad) |
| Tiempo de servicio | Igual |

5. **Validar.** Este paso es fuera de FlexSim: abrí una terminal en la carpeta del TPI y corré (el script lee `flexsim/salidas.xlsx`, así que para esto tiene que estar el archivo de la corrida con personas con ese nombre):

```bash
python analisis/validar_modelo.py --escenario E0_Pico
```

   Tienen que seguir pasando los 7 chequeos.
6. **Mirar la escena.** En la vista 3D, con **Run Speed** bajo: la fila de caja tiene que mostrar unas 60 personas en la apertura, nadie atraviesa paredes y nadie queda amontonado.

Si cambian el tiempo de validación o las raciones por franja, **algo se rompió**: no sigas.

## 4. Fase 4: el personal según el escenario

Con un solo modelo, el 3D se ajusta al escenario activo al hacer Reset.

1. El bloque 8.1 de `GUIA_PERSONAS_3D.md` ya quedó agregado en 3.5.
2. Para E2 (puesto extra), en la ventana de `Comedor` buscá la **columna 2** del control de puestos (las actividades `Abrir puesto extra` y `Cerrar puesto extra`) y agregá los dos Custom Code de la sección 8.2 de esa guía: `Aparece cajero 2` justo debajo de `Abrir puesto extra` y `Se va cajero 2` justo debajo de `Cerrar puesto extra`. El código se pega con el botón del pergamino, como en la sección 3.
3. Probá cada escenario: **Toolbox > Parameters** (tabla), cambiá el valor de `Escenario` (el número de fila de la tabla `Escenarios`: 1 = E0_Pico, 2 = E1_Pico, 3 = E2_Pico, 4 = E3_Pico, 5 = E4_Pico, 6 = E5_Pico) y apretá **Reset** en la barra de simulación. Mirá en la vista 3D:

| Escenario | Qué tiene que verse |
|---|---|
| 1 (E0_Pico) | 1 cajero y 3 servidores. `Cajero2` y `Servidor4` fuera del edificio, a la izquierda |
| E1 | 2 cajeros desde el principio |
| E2 | 1 cajero. A las 12:00 aparece el 2.º y a las 13:30 se va |
| E3 | Igual que E0 |
| E4 | 1 cajero y 4 servidores |
| E5 | 2 cajeros y 4 servidores |

Después de volver a E0 no tiene que quedar nadie de más.

## 5. Fase 5: la fila de servicio física (S23)

La `Fila_Servicio` mide 2,4 m: entran **unas 4 personas**. La guía original suponía 38.

1. **Antes de fijar el valor**, hablalo con el referente: ¿hay una fila ordenada entre la validación y el mostrador, o la gente espera de pie frente a los tres pasos? Eso define el valor real.
2. Poné el valor en la columna `CapacidadFilaServicio` de la tabla `Escenarios`. Lo correcto es hacerlo en `analisis/generar_inputs_flexsim.py` (en un editor de texto), correrlo (`python analisis/generar_inputs_flexsim.py` en una terminal) y reimportar en FlexSim: **Toolbox > Excel Import/Export**, pestaña **Import**, **Import Tables**. No edites la tabla de entrada a mano en FlexSim.
3. Corré E0_Pico (**Reset**, **Run**) y mirá en la vista 3D y en `Salida_Personas` si quien terminó de validar se queda en el puesto y bloquea la caja.
4. Comparalo con la corrida sin límite y presentalo como la resolución de S23.

Este cambio **sí modifica los resultados**: no lo mezcles con el efecto de las caminatas.

## 6. Problemas esperables

| Síntoma | Qué hacer |
|---|---|
| Las personas atraviesan paredes | Falta pasar por `Paso_Central`. Verificá los Walk de 3.3 y 3.4. Si igual atraviesan algo más, usá **A\* Navigation** (grupo de la biblioteca) con barreras en las paredes† |
| Se amontonan en un punto | Falta el **Wait in Line**, o *Single Entry Point* está mal |
| *Invalid destination* en un Walk | El nombre del Location no coincide con la tabla, o falló la concatenación (probá `string.fromNum`) |
| La fila física se vacía y la cola queda invisible | L2 dio "sale de la fila al llegar al frente": hay que rediseñar 3.2 |
| El mostrador se satura sin motivo | El frente de la fila está lejos de los `Mostrador_Loc`: la caminata retiene al servidor |
| Cambiaron el tiempo de validación o el de servicio | Se movió `Registrar y salir`, o una caminata quedó dentro de un Delay |
| *Undefined variable* | Faltan las cuatro líneas iniciales del editor |
| El modelo va lento | Medí una réplica con personas. Si el Experimenter es demasiado lento, agregá un parámetro `ConPersonas` (0 o 1) y saltá los bloques nuevos con un Decide |

## 7. Respuestas del laboratorio

| # | Pregunta | Respuesta |
|---|---|---|
| L1 | Label donde queda la persona creada | |
| L2 | ¿La persona sigue en la fila mientras espera el recurso? | |
| L3 | ¿El primer punto de la Waiting Line es el frente o el fondo? | |
| L4 | Velocidad de caminata y dónde se cambia | |

## 8. Checklist

- [ ] Fase 0: copia de seguridad y corrida de referencia guardadas
- [ ] Fase 1: los dos objetos de prueba caen bien, todos los objetos puestos
- [ ] Fase 2: laboratorio hecho y sección 7 completa
- [ ] Fase 3: personas en el flujo, prueba contra la referencia
- [ ] Fase 4: personal por escenario, probados los seis
- [ ] Fase 5: S23 hablado con el referente y resuelto
- [ ] `EXPLICACION.md` y `AYUDA_IA.md` actualizados con lo que cambió y por qué
