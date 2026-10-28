# Eje 8. Simulación de sistemas continuos

Bueno, vamos con el eje ocho, que es el más rendidor para mañana, porque entra doble: la teoría en el multiple choice y la práctica a mano. La guía resuelta lo dice explícitamente: los ejercicios de esta guía tienen el mismo formato del parcial práctico, papel y calculadora. Esto dura unos treinta y cuatro minutos; si vas justo de tiempo, priorizá las secciones de nivel y flujo, Euler, bucles, modos de comportamiento y la práctica. Antes, lo que sacó el profe de la teoría: las fórmulas de cálculo, el ejemplo completo de la población, el caso del inventario que no llega, la epidemia y las herramientas. En la teoría te evalúan conceptos, no cuentas. Pero ojo: la práctica entra entera, así que Euler y los seis ejercicios, incluido el del inventario, los tenés que saber hacer a mano. Te adelanto las cuatro ideas que sostienen todo el eje, y si te quedás solo con esto, ya tenés media nota. Primera: la diferencia entre nivel y flujo. Segunda: la ecuación de Euler, con el delta t multiplicando, y qué pasa si el paso es grande. Tercera: el diagrama causal no se simula, el de Forrester sí, y el tipo de bucle sale de contar los signos negativos. Cuarta: la estructura produce el comportamiento. Vamos tema por tema, y te voy marcando dónde te pueden engañar.

## Tres nombres que te pueden mezclar

Este tema aparece con tres nombres, y es una pregunta de multiple choice servida.

Simulación de sistemas continuos es la categoría: simular sistemas cuyo estado cambia de manera continua en el tiempo. Es el nombre del eje. Dinámica de sistemas es una metodología de modelado, creada por Jay Forrester, que representa esos sistemas con niveles, flujos y bucles de realimentación. Es la forma de modelar que usamos. Y simulación dinámica es cualquier simulación que evoluciona en el tiempo, incluida la de eventos discretos.

**Ojo, trampa.** El trabajo integrador en FlexSim es una simulación dinámica, pero no es dinámica de sistemas. Si una opción dice que todo modelo que evoluciona en el tiempo es dinámica de sistemas, es falsa.

**Ojo, trampa.** Toda la dinámica de sistemas es simulación continua, pero no toda la simulación continua es dinámica de sistemas. Simular un circuito, el control de un motor o la trayectoria de un avión es simulación continua, con otras herramientas. Si te dan la frase al revés, que toda simulación continua es dinámica de sistemas, es falsa. La dinámica de sistemas se especializa en sistemas donde importan las acumulaciones y la realimentación: empresas, poblaciones, proyectos, recursos, mercados.

## Qué es un sistema continuo

La definición: un sistema continuo es aquel cuyas variables de estado cambian de manera continua a lo largo del tiempo, y se describe con ecuaciones diferenciales, que dicen a qué velocidad cambia cada variable en cada instante.

Frente a eventos discretos, comparalo así. En discretos, el estado cambia a saltos y el reloj salta al siguiente evento; en continuos, el estado cambia todo el tiempo y el reloj avanza por incrementos fijos delta t. En discretos se representan entidades individuales que recorren un proceso, con distribuciones y colas; en continuos, cantidades agregadas que se acumulan, con ecuaciones diferenciales. La pregunta típica de discretos es cuánto espera un cliente o cuántos servidores hacen falta. La de continuos es cómo evoluciona el sistema y qué política lo estabiliza.

**Ojo, trampa.** Que una cantidad sea entera no impide modelarla como continua. Personas, productos o errores se modelan como continuos cuando son muchos y lo que interesa es el comportamiento agregado. Nadie tiene mil veinte coma cuatro habitantes, pero para una ciudad de un millón la aproximación es razonable. Si una opción dice que solo se pueden modelar como continuas las magnitudes físicas continuas, es falsa.

## Nivel y flujo: lo más importante del eje

Pensá en una bañera. El agua que hay se acumula; la canilla la hace subir y el desagüe la hace bajar. Si entra más de lo que sale, se llena; si sale más, se vacía; si entra lo mismo que sale, el nivel queda quieto aunque el agua circule.

Las definiciones, que tenés que poder decir de memoria. Un nivel es una acumulación: una cantidad que tiene un valor en cada instante y que conserva el efecto de todo lo que entró y salió antes. En inglés se llama stock. Un flujo es la velocidad con la que un nivel cambia, y se mide siempre por unidad de tiempo.

Para distinguirlos está la prueba de la foto. Congelá el tiempo y sacale una foto al sistema. Lo que se puede medir en la foto es un nivel: los litros en la bañera, los productos en el depósito, los errores pendientes. Lo que no tiene sentido en una foto, porque necesita que pase el tiempo, es un flujo: litros por minuto, productos por día, errores corregidos por semana.

La ecuación: la derivada del nivel respecto del tiempo es la suma de las entradas menos la suma de las salidas. Y de ahí sale la regla de unidades: si un nivel se mide en cierta unidad, todos sus flujos se miden en esa unidad por unidad de tiempo. Si las unidades no cierran, el modelo está mal, dé lo que dé la simulación.

**Lo importante.** Nivel es lo que se acumula y se ve en la foto; flujo es velocidad, siempre por unidad de tiempo. Y para saber si un nivel sube o baja, no se mira la entrada ni la salida por separado: se mira la diferencia.

**Ojo, trampa.** Este es el error que el apunte destaca como muy común, incluso entre profesionales: creer que el nivel sigue la forma de la entrada. Si la canilla se va cerrando de a poco, mucha gente dice que el agua empieza a bajar. Falso. Mientras entre más de lo que sale, la bañera sigue llenándose, aunque la entrada esté disminuyendo. El nivel baja recién cuando la entrada se vuelve menor que la salida. El apunte cita un estudio de Booth Sweeney y Sterman, del año dos mil, donde estudiantes de posgrado con buena formación matemática se equivocaban sistemáticamente en esto. En multiple choice te lo van a plantear exactamente así: la entrada disminuye, ¿qué pasa con el nivel? La respuesta depende de si la entrada sigue siendo mayor que la salida.

**Ojo, trampa.** Cuando entrada menos salida es cero, el nivel no necesariamente está en equilibrio: puede estar en su máximo, en su mínimo o en equilibrio. En la bañera del ejercicio uno, el cambio neto cero marca el máximo.

**Si te toca de desarrollo.** Diferenciá nivel y flujo así: primero las dos definiciones; después la prueba de la foto con un ejemplo; después la regla de unidades, que un flujo siempre está en unidades del nivel por tiempo; y cerrá con el error de la bañera, que el nivel depende de la diferencia entre entradas y salidas y no de la forma de la entrada.

## El método de Euler

Una computadora no resuelve la ecuación diferencial de forma continua: avanza de a pasos. El método de Euler supone que, durante cada intervalo delta t, los flujos se mantienen constantes en el valor que tenían al principio del intervalo.

La ecuación, en palabras: el nivel en t más delta t es igual al nivel en t, más delta t multiplicado por la diferencia entre las entradas y las salidas calculadas en t. Revisá las unidades: el flujo neto está en unidades por tiempo, multiplicado por delta t queda en unidades, y eso sí se puede sumar al nivel. El delta t es lo que hace cerrar las unidades.

El ejemplo del apunte es un tanque de cien litros que se vacía, con un caudal de salida igual a la quinta parte del agua, por minuto. Con delta t de un minuto, Euler da menos agua que la solución exacta.

¿Por qué se equivoca? Porque en el primer minuto supone que salen veinte litros por minuto todo el tiempo, cuando en realidad el caudal va bajando con el agua. Sobreestima la salida en cada paso y el error se acumula. Con medio paso, el error baja más o menos a la mitad.

**Lo importante.** El supuesto de Euler es que el flujo es constante durante el paso, con el valor del principio. Y la regla: con Euler, achicar el paso a la mitad reduce el error aproximadamente a la mitad, al precio del doble de cálculos.

**Ojo, trampa.** La ecuación sin delta t, nivel igual a nivel menos flujo, es el error frecuente que marca el apunte. Resta litros por minuto a litros. Si una opción la presenta como correcta, descartala.

**Ojo, trampa.** Achicar el paso a la mitad reduce el error a la mitad, no a la cuarta parte, y tampoco lo elimina. Y el supuesto de Euler es el flujo del principio del intervalo; el que estima un flujo promedio dentro del intervalo es Runge-Kutta. No los cruces.

### Qué pasa si el paso es demasiado grande

Esto es muy preguntable. En el tanque, con un paso de un minuto el agua baja suave, como en la realidad. Con un paso mucho más grande, por ejemplo siete minutos y medio, aparece agua negativa y el resultado oscila. Y con un paso todavía más grande, la oscilación crece sin límite.

**Ojo, trampa.** Esas oscilaciones no existen en el sistema: las fabrica el método. Un tanque no puede tener agua negativa ni oscilar. Si una opción dice que la simulación muestra que el sistema oscila, es falsa. Un resultado raro puede ser un error del modelo o un artefacto numérico por haber elegido mal el paso.

### Cómo elegir delta t

Hay que identificar la constante de tiempo más chica del modelo, que es el tiempo característico en el que un nivel cambia de manera apreciable. En el tanque es cinco minutos.

Tres reglas. Primera: el paso tiene que ser menor que un tercio de la menor constante de tiempo, según la documentación de Vensim; en el tanque, menor que uno coma siete minutos. Segunda: preferir potencias de un medio, como uno, cero coma cinco o cero coma veinticinco, porque se representan exacto en la computadora. Tercera: verificar siempre corriendo con delta t y con delta t sobre dos; si los resultados cambian de manera apreciable, el paso todavía es grande.

**Lo importante.** Si un resultado depende del delta t elegido, no es un resultado del sistema sino del método. Esa verificación es la versión para modelos continuos de la verificación del eje seis.

**Ojo, trampa.** Es la menor constante de tiempo, no la mayor. Y es menor que un tercio, no mayor.

**Ojo, trampa.** Runge-Kutta es más preciso con el mismo paso, pero no siempre conviene. El anexo aclara que no conviene cuando hay cambios bruscos, como un pedido que se hace de golpe un día determinado, porque su promedio suaviza artificialmente el salto. Y Euler, con un paso bien elegido, suele alcanzar para modelos de gestión.

**Si te toca de desarrollo.** Para Euler y la elección del paso: explicá el supuesto del método; escribí la ecuación con delta t y decí por qué hace cerrar las unidades; explicá de dónde viene el error y que baja aproximadamente a la mitad con medio paso; mostrá qué pasa con un paso grande, valores negativos y oscilaciones artificiales; y cerrá con la regla del tercio de la menor constante de tiempo y la verificación con delta t sobre dos.

## Diagramas causales

Un diagrama causal muestra qué variables influyen sobre cuáles y en qué sentido. Una flecha de X a Y significa que X influye directamente sobre Y. Es la herramienta para pensar la estructura antes de escribir ecuaciones.

**Ojo, trampa.** Esta es de las más seguras. El diagrama causal es una hipótesis sobre cómo funciona el sistema, y no se puede simular. No tiene niveles, ni ecuaciones, ni unidades, ni valores iniciales. Y la guía agrega que las constantes no van en el diagrama causal: aparecen recién en el de Forrester. Si una opción dice que el diagrama causal permite simular, o que muestra los niveles, es falsa.

### La polaridad

Un vínculo de X a Y es positivo si, cuando X aumenta y todo lo demás se mantiene igual, Y termina más alto de lo que habría sido. Es negativo si Y termina más bajo de lo que habría sido. El método: imaginá que solo cambia X, congelá todo lo demás y preguntate para dónde se mueve Y.

**Ojo, trampa.** La frase «de lo que habría sido» es la clave. Un inventario donde se vende más de lo que se produce: si aumenta la producción, el inventario puede seguir bajando. ¿El vínculo es negativo? No. Con más producción el inventario queda más alto de lo que habría quedado. El vínculo de producción a inventario es positivo, aunque el inventario esté bajando.

**Ojo, trampa.** El signo no dice si el efecto es bueno o malo. Más muertes es un vínculo negativo sobre la población; más impuestos puede ser un vínculo positivo sobre la recaudación.

### Los bucles

Cuando las flechas forman un circuito cerrado hay un bucle de realimentación, y hay solo dos tipos. El reforzador, R, amplifica cualquier cambio: más población, más nacimientos, más población. Produce crecimiento o caída exponencial. El compensador, B, contrarresta cualquier cambio y empuja al sistema hacia un equilibrio: más población, más muertes, menos población. Produce búsqueda de objetivo o equilibrio.

Para saber el tipo: recorré el circuito suponiendo que una variable aumenta y fijate si vuelve reforzada o contrarrestada. O la regla rápida: contá los vínculos negativos. Cantidad par, incluido el cero, es reforzador. Cantidad impar, compensador.

**Ojo, trampa.** Cero vínculos negativos es par, así que es reforzador. Y dos negativos también es reforzador, aunque suene raro. Un solo negativo, o tres, es compensador.

**Ojo, trampa.** El reforzador no siempre hace crecer: también produce caída exponencial. Amplifica el cambio en la dirección que sea.

Las demoras: cuando el efecto no es inmediato, se marcan con dos barras cruzadas sobre la flecha. Y son importantes porque un bucle compensador con demora puede hacer oscilar al sistema.

Para dibujar bien: variables con sustantivos y no con verbos, personal contratado y no contratar personal; nombres neutros, calidad de atención y no mala atención; cada flecha con un mecanismo que puedas explicar en una oración; no confundir causa con correlación; y no leerlo como un diagrama de flujo, porque las flechas no indican pasos ni orden temporal.

## Diagramas de Forrester

El diagrama de Forrester, también llamado de niveles y flujos, es el que sí se puede simular. Distingue niveles, flujos y variables auxiliares, y muestra cómo viaja la información. En la notación habitual, los niveles son rectángulos; los flujos son válvulas sobre las flechas que entran o salen del nivel; los flujos que vienen de afuera del modelo o van hacia afuera nacen o terminan en una nube; y la información viaja por flechas finas, los canales de información. El apunte aclara que cada programa dibuja los símbolos con pequeñas diferencias, pero el significado es el mismo.

Para pasar del causal al de Forrester hay cinco pasos. Uno: identificar los niveles con la prueba de la foto. Dos: para cada nivel, identificar qué lo hace subir y qué lo hace bajar: esos son los flujos. Tres: agregar auxiliares y constantes, unidas con canales de información a los flujos que ayudan a calcular. Cuatro: escribir las ecuaciones con unidades y el valor inicial de cada nivel, y verificar que cierren. Cinco: simular y revisar.

**Ojo, trampa.** No hay traducción automática del causal al de Forrester, porque el causal no dice qué variables se acumulan. Esa decisión la toma el modelador con la prueba de la foto.

**Si te toca de desarrollo.** Para comparar causal y Forrester: el causal es una hipótesis de estructura, con variables, flechas con polaridad y bucles marcados, y no se simula. El de Forrester distingue niveles, flujos, constantes y canales de información, lleva ecuaciones con unidades y valores iniciales, y sí se simula. Las constantes aparecen recién en Forrester. Y el paso de uno a otro no es automático: hay que decidir qué se acumula.

## Modos de comportamiento

La idea central del eje: la estructura produce el comportamiento. Sistemas muy distintos que comparten la misma estructura de bucles se comportan igual. Hay cuatro patrones, y conviene memorizarlos como pares estructura y comportamiento.

Crecimiento exponencial: un bucle reforzador dominante. Ejemplos, el interés compuesto o usuarios que recomiendan una aplicación.

Búsqueda de objetivo: un bucle compensador. Ejemplos, el café que se enfría hasta la temperatura ambiente, o un equipo que corrige errores hasta un nivel aceptable. El flujo es proporcional a la distancia al objetivo, así que se acerca cada vez más despacio.

Crecimiento en S: un bucle reforzador que choca con un límite. Ejemplos, la venta de un producto nuevo hasta saturar el mercado, o la adopción de una plataforma.

Oscilación: un bucle compensador con una demora. Ejemplos, regular la ducha con un caño largo, o ajustar servidores mirando métricas atrasadas.

**Lo importante.** Los dos fundamentales son el exponencial y la búsqueda de objetivo; los otros se construyen combinándolos.

**Ojo, trampa.** El multiple choice típico te cruza los pares. La oscilación no la produce un reforzador: la produce un compensador con demora. El crecimiento en S no es un compensador solo: es un reforzador que choca con un límite. Y la caída exponencial tiene la misma estructura que el crecimiento exponencial; lo que cambia es el signo de la tasa neta.

### Demoras materiales

Una demora material es algo que tarda en pasar de un estado a otro: pedidos en tránsito, alumnos cursando una carrera. Se modela con un nivel cuya salida depende de cuánto hay acumulado y de cuánto tiempo se queda cada cosa, en promedio. Es la misma estructura que el desagote del tanque, y la misma de la política B del ejercicio seis.

## Verificar el modelo y comparar escenarios

La lista de control del apunte tiene cuatro verificaciones. Unidades: que cada ecuación cierre y que los flujos estén en unidades del nivel por tiempo. Condiciones extremas: que el modelo se comporte razonable con valores límite; con natalidad cero, la población solo puede bajar. Niveles que no pueden ser negativos: una reserva de gas no puede tener volumen negativo. Y sensibilidad al paso: que el resultado no cambie apreciablemente con delta t sobre dos.

**Ojo, trampa.** Cuando aparece un nivel negativo que no debería existir, se corrige el modelo, no el resultado. Es señal de que falta una regla. Poner un cero a mano en la tabla es la respuesta equivocada.

### ¿Hacen falta réplicas?

Los modelos de este eje son en general determinísticos: con los mismos datos dan siempre lo mismo. Por eso no hacen falta réplicas ni intervalos de confianza.

**Ojo, trampa.** Que no haya azar no significa que no haya incertidumbre. Los parámetros casi nunca se conocen con exactitud, y para eso se hace análisis de sensibilidad. Y si se sortean los parámetros inciertos desde una distribución, el modelo pasa a tener azar y vuelven a hacer falta muchas corridas: es un experimento de Monte Carlo. Una opción que diga que nunca hacen falta varias corridas en dinámica de sistemas es falsa por ese «nunca».

### Comparar políticas

La principal utilidad de un modelo de dinámica de sistemas no es pronosticar un número exacto, sino comparar políticas. Una buena comparación no pregunta solo qué política da el mejor número final: pregunta si produce efectos secundarios, si traslada el problema a otra parte del sistema y si el resultado se sostiene cuando los parámetros no son exactamente los supuestos. Como no hay azar, se comparan directamente las trayectorias de una corrida por escenario.

**Ojo, trampa.** Si una opción dice que el objetivo principal es predecir con exactitud el valor futuro, es el distractor. El calamar del ejercicio dos lo dice clarito: el modelo no pronostica cuánto calamar habrá, pero sí responde qué regla de pesca es sostenible.

## Anexos, rápido

Por si cae una pregunta suelta. La simulación continua más allá de la dinámica de sistemas: control con MATLAB y Simulink, electrónica con SPICE, mecánica con Modelica, fluidos y estructuras con elementos finitos; y Cellier y Kofman, autores del libro de referencia, son de la Universidad Nacional de Rosario. Más allá de Euler: Runge-Kutta, paso variable y sistemas rígidos, donde conviven cambios muy rápidos y muy lentos. Funciones tabla: cuando una relación no tiene fórmula simple, se da una lista de puntos y el programa interpola; es la forma habitual de meter límites y saturaciones. Modelos clásicos: difusión de Bass, crecimiento en S; presa y depredador, oscilaciones sostenidas; sobrepaso y colapso; y la ley de Brooks, que agregar gente a un proyecto atrasado lo atrasa más.

Y la validación según Barlas, de mil novecientos noventa y seis. Dos grupos de pruebas: de estructura, que ecuaciones, unidades y bucles correspondan al sistema real y que se comporte bien en condiciones extremas; y de comportamiento, que reproduzca la forma del comportamiento real, si crece, si oscila, cuándo llega a un pico.

**Ojo, trampa.** Validar no exige que el modelo acierte cada dato, sino que reproduzca la forma. Y que un modelo reproduzca bien los datos no prueba que sus reglas sean las correctas: estructuras distintas pueden producir comportamientos parecidos. Un modelo no es verdadero o falso, es más o menos adecuado para una pregunta.

## La práctica: la receta

Ahora la parte que se calcula. Siempre el mismo procedimiento. Uno: identificar niveles con la prueba de la foto, y sus flujos. Dos: diagrama causal con polaridades y tipo de bucle, sin constantes. Tres: diagrama de Forrester con niveles, flujos, constantes y canales de información. Cuatro: ecuaciones con unidades y valor inicial, y verificar que cierren. Cinco: tabla de Euler.

La tabla: una fila por instante; una columna por nivel, una por flujo y una para el cambio neto, entradas menos salidas. En cada fila calculás primero los flujos con los valores de esa fila, después el cambio neto, y el nivel de la fila siguiente con Euler. Todo con dos decimales. En la última fila solo va el nivel.

Y para cualquier pregunta de equilibrio, un solo truco: en el equilibrio el nivel no cambia, entonces entradas iguales a salidas, y despejás.

**Ojo, trampa.** Errores típicos de la práctica, que te pueden costar puntos. Uno: olvidarte del delta t cuando no vale uno; en el café, con delta t de dos, cada fila resta dos veces el enfriamiento. Dos: escribir los flujos dependientes del tiempo con t menos uno; t es el comienzo del paso, así que la fila cero usa t igual a cero. Tres: escribir un número suelto donde va una constante con unidades, como diez menos t en la bañera, que no cierra en unidades; el uno que multiplica a t es el ritmo de cierre. Cuatro: poner constantes en el diagrama causal. Cinco: «corregir» un nivel negativo en la tabla en lugar de agregar la regla al modelo. Seis: las tasas en porcentaje se escriben como cero coma algo, en uno sobre año.

## Los seis ejercicios, con los resultados para comparar

Ejercicio uno, la bañera. Cincuenta litros, salida constante de seis litros por minuto, entrada que empieza en diez y baja uno por minuto. No hay bucles: el agua no cambia ni la entrada ni la salida. La entrada es entrada inicial menos ritmo de cierre por t. El agua va cincuenta, cincuenta y cuatro, cincuenta y siete, cincuenta y nueve, sesenta, sesenta, cincuenta y nueve, cincuenta y siete, del minuto cero al siete. El máximo es sesenta litros, alcanzado por primera vez en el minuto cuatro, donde la entrada vale seis, igual que la salida, y el cambio neto es cero. Es el error de la bañera en forma de ejercicio: la entrada baja desde el principio y el agua sube cuatro minutos.

Ejercicio dos, el calamar. Mil seiscientas toneladas, natalidad veinticinco por ciento, mortalidad dieciocho por ciento, pesca doce por ciento. Tres bucles: nacimientos reforzador, muertes y pesca compensadores. La población va mil seiscientas, mil quinientas veinte, mil cuatrocientas cuarenta y cuatro, mil trescientas setenta y una coma ochenta. En el año cero: nacimientos cuatrocientas, muertes doscientas ochenta y ocho, pesca ciento noventa y dos, cambio neto menos ochenta. La tasa neta es menos cinco por ciento anual: caída exponencial. La pesca sostenible es la que hace cero la tasa neta: siete por ciento anual.

Ejercicio tres, el café. Ochenta grados, ambiente veinte, constante de tiempo diez minutos. Un bucle compensador. Con delta t de dos: ochenta, sesenta y ocho, cincuenta y ocho coma cuarenta, cincuenta coma setenta y dos, con enfriamientos seis, cuatro coma ocho y tres coma ochenta y cuatro. Euler da menos que la exacta, porque supone que el café se enfría a la velocidad del principio de cada paso; la diferencia a los seis minutos es dos coma veintiún grados. Con delta t de quince: ochenta, menos diez, treinta y cinco, doce coma cinco; queda debajo del ambiente y la distancia se achica. Con veinticinco: ochenta, menos setenta, ciento cincuenta y cinco, menos ciento ochenta y dos coma cinco; queda debajo y la distancia crece. La regla pide delta t menor que tres coma treinta y tres minutos: cumplen uno y dos, no cuatro ni cinco.

Ejercicio cuatro, el inventario que no llega. Objetivo dos mil, inventario mil quinientos, ventas veinte por día, tiempo de ajuste cinco días. Bucle compensador entre inventario y producción. Delta t tiene que ser menor que uno coma sesenta y siete días, y uno cumple. El inventario va mil quinientos, mil quinientos ochenta, mil seiscientos cuarenta y cuatro, mil seiscientos noventa y cinco coma veinte, con producción cien, ochenta y cuatro y setenta y uno coma veinte. Se estabiliza en mil novecientos, con producción veinte, y le faltan cien. ¿Por qué no llega? En el equilibrio el inventario no cambia, así que la producción iguala a las ventas, veinte, y la política solo produce veinte cuando faltan cien, porque cien sobre cinco es veinte. No es un error de Euler: es lo que hace esa política, que reacciona solo a la diferencia con el objetivo y no mira las ventas. Con la política corregida, producción igual a ventas más la diferencia sobre el tiempo de ajuste, va mil quinientos, mil seiscientos, mil seiscientos ochenta, mil setecientos cuarenta y cuatro, y se estabiliza en dos mil. La corrección agrega una flecha positiva de ventas a producción.

Ejercicio cinco, la reserva. Mil millones de metros cúbicos, consumo ciento cincuenta por año, sin bucles. La reserva va bajando de a ciento cincuenta y en el año siete queda en menos cincuenta, que no existe. Con la regla consumo igual al mínimo entre el previsto y la reserva sobre delta t: año cinco, doscientos cincuenta con consumo ciento cincuenta; año seis, cien con consumo cien; año siete, cero. Llega a cero en el año siete sin pasar por debajo, y aparece un bucle compensador entre reserva y consumo.

Ejercicio seis, los errores pendientes. Doscientos pendientes, treinta reportados por semana. Política A, corregir veinticinco fijos: sin bucle, los pendientes van doscientos, doscientos cinco, doscientos diez, doscientos quince, doscientos veinte, y crecen cinco por semana para siempre. Política B, corregir la cuarta parte de los pendientes, tiempo de corrección cuatro semanas: bucle compensador; van doscientos, ciento ochenta, ciento sesenta y cinco, ciento cincuenta y tres coma setenta y cinco, ciento cuarenta y cinco coma treinta y uno, con corregidos cincuenta, cuarenta y cinco, cuarenta y uno coma veinticinco y treinta y ocho coma cuarenta y cuatro. Se estabiliza en ciento veinte. Para estabilizar en sesenta hace falta un tiempo de corrección de dos semanas: corregir la mitad cada semana. La lección: una política que no mira el estado del sistema no lo puede controlar.

## Preguntas tipo multiple choice

Pregunta uno. ¿Cuál de estas es un nivel: los litros de agua en la bañera, los litros por minuto que entran, los nacimientos por año o las ventas diarias? La correcta es los litros en la bañera, porque se pueden medir en una foto. Las otras tres son flujos: llevan «por unidad de tiempo».

Pregunta dos. La canilla se va cerrando, pero la entrada sigue siendo mayor que la salida. ¿Qué pasa con el agua? Las opciones típicas: baja, sube, queda constante, depende de la entrada. La correcta es que sube. El distractor es «baja porque la entrada disminuye», que es el error de la bañera.

Pregunta tres. ¿Qué supone Euler sobre los flujos durante un paso? Que son constantes, con el valor del principio del intervalo. El distractor es «usa un flujo promedio dentro del intervalo», que describe a Runge-Kutta.

Pregunta cuatro. Con Euler, si el paso se reduce a la mitad, el error: se reduce aproximadamente a la mitad. Distractores: a la cuarta parte, desaparece, no cambia.

Pregunta cinco. ¿Qué regla práctica se recomienda para delta t? Menor que un tercio de la menor constante de tiempo. El distractor cambia «menor» por «mayor» constante, o el tercio por el doble.

Pregunta seis. Una simulación de un tanque con paso grande da valores negativos que oscilan. ¿Qué indica? Un artefacto numérico por el paso demasiado grande. El distractor es que el sistema real oscila.

Pregunta siete. Sobre el diagrama causal, ¿cuál es verdadera? Que es una hipótesis de estructura y no se puede simular. Distractores: que incluye niveles y ecuaciones, que lleva las constantes, que es equivalente al de Forrester.

Pregunta ocho. Un bucle tiene dos vínculos negativos. ¿De qué tipo es? Reforzador, porque la cantidad de negativos es par. El distractor es compensador, «porque tiene negativos».

Pregunta nueve. Las ventas superan a la producción y el inventario baja. ¿Qué polaridad tiene el vínculo de producción a inventario? Positiva, porque con más producción el inventario queda más alto de lo que habría sido. El distractor es negativa porque el inventario baja.

Pregunta diez. ¿Qué estructura produce oscilación? Un bucle compensador con demora. Distractores: un reforzador dominante, un reforzador que choca con un límite, que es el crecimiento en S.

Pregunta once. En un modelo de reserva, el nivel queda negativo. ¿Qué corresponde? Corregir el modelo agregando una regla que limite el consumo. El distractor es reemplazar el valor negativo por cero en el resultado.

Pregunta doce. ¿Hacen falta réplicas en un modelo de dinámica de sistemas? En general no, porque es determinístico, aunque sí análisis de sensibilidad; y si se sortean parámetros, vuelven a hacer falta muchas corridas. El distractor tiene un absoluto: «nunca hacen falta varias corridas» o «siempre hacen falta réplicas».

Pregunta trece. El trabajo integrador en FlexSim, ¿es dinámica de sistemas? No: es una simulación dinámica de eventos discretos. Dinámica de sistemas es la metodología de Forrester con niveles, flujos y bucles.

## Lo que puede entrar en desarrollo

Primero: nivel y flujo. Definiciones, prueba de la foto con ejemplo, regla de unidades, y el error de la bañera.

Segundo: el método de Euler y la elección de delta t. El supuesto, la ecuación con delta t, el origen del error y cómo baja con medio paso, qué pasa con un paso grande, la regla del tercio y la verificación con delta t sobre dos.

Tercero: diagrama causal contra diagrama de Forrester. Qué muestra cada uno, cuál se simula, dónde van las constantes, polaridad y regla de paridad para el tipo de bucle, y los cinco pasos para pasar de uno a otro.

Cuarto: la estructura produce el comportamiento. Los cuatro modos con su estructura, y que sistemas muy distintos con la misma estructura de bucles se comportan igual.

Quinto: verificación del modelo. Las cuatro verificaciones de la lista de control, por qué un nivel negativo se corrige en el modelo, y por qué no hacen falta réplicas pero sí sensibilidad.

## Lo mínimo que te tenés que llevar

Nivel es lo que se ve en la foto; flujo es velocidad. El nivel sube mientras entrada menos salida sea positiva, aunque la entrada baje.

Euler: nivel más delta t por entradas menos salidas, con el flujo del principio del paso. Medio paso, medio error. Paso grande, valores absurdos que fabrica el método.

Delta t menor que un tercio de la menor constante de tiempo, y verificar con la mitad.

El causal no se simula ni lleva constantes; el de Forrester sí se simula. Par de negativos, reforzador; impar, compensador.

Exponencial, reforzador. Objetivo, compensador. En S, reforzador contra un límite. Oscilación, compensador con demora.

En la práctica: flujos, cambio neto, nivel siguiente, con dos decimales. Para el equilibrio, entradas iguales a salidas. Y un nivel negativo se arregla con una regla en el modelo.

Eso es todo del eje ocho. Si llegaste hasta acá, tenés este eje cubierto. Mucha suerte mañana.
