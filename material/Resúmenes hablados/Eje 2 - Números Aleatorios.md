# Eje 2. Números aleatorios

Hola. Este es el resumen hablado del eje dos: números aleatorios. Dura unos treinta minutos. Para el parcial de mañana no entra: se toma práctica de los ejes cinco y ocho y teoría del cuatro al ocho. Pero el eje dos es la base de todo lo que simula con azar, y en el parcial práctico uno ya apareció con un generador congruencial y una prueba de corridas. Lo escuchás como repaso de fondo, y si te queda tiempo, es el más fácil de recuperar.

## Por qué hacen falta

Toda simulación que representa un sistema real tiene una característica inevitable: el mundo real no es determinístico. Los clientes no llegan exactamente cada tres minutos, las máquinas no fallan exactamente cada cien horas, los pacientes no tardan exactamente lo mismo en ser atendidos. Hay variabilidad, y esa variabilidad es justamente lo que hace que valga la pena simular en lugar de calcular con una fórmula cerrada.

Para reproducir esa variabilidad dentro de una computadora necesitamos una fuente de aleatoriedad. Y acá aparece la primera tensión: una computadora es, por definición, una máquina determinística. Dada una entrada, siempre produce la misma salida. ¿Cómo le pedimos a algo determinístico que produzca algo aleatorio?

La respuesta histórica son los números pseudoaleatorios: secuencias generadas por algoritmos determinísticos, pero que para fines prácticos se comportan como si fueran aleatorios. Tienen que cumplir dos propiedades fundamentales. Una: uniformidad, o sea que estén distribuidos uniformemente en el intervalo de cero a uno, sin incluir el uno, todos los valores igualmente probables. Dos: independencia, o sea que cada número no se pueda predecir a partir de los anteriores. Todo lo que viene después, generar variables con cualquier distribución, tiempos entre llegadas, tiempos de servicio, decisiones probabilísticas, réplicas, se apoya en estas dos propiedades.

### Por qué no usar números verdaderamente aleatorios

Existen fuentes de aleatoriedad física real: ruido térmico, decaimiento radioactivo, fluctuaciones cuánticas. Pero no sirven para simulación por tres razones. Son lentas: generar millones de números desde un fenómeno físico es órdenes de magnitud más lento que un algoritmo. No son reproducibles, y la reproducibilidad es esencial: si querés comparar tres cajas contra cuatro cajas en el supermercado, necesitás que las dos configuraciones vean exactamente las mismas llegadas de clientes para que la comparación sea justa. Y no se pueden depurar: si encontrás un comportamiento raro, necesitás repetir exactamente la misma corrida para encontrar el error.

## Un poco de historia

El problema nace en el Proyecto Manhattan, durante la Segunda Guerra Mundial. John von Neumann y Stanislaw Ulam, trabajando en Los Álamos en simulaciones de difusión de neutrones, necesitaban grandes cantidades de números aleatorios, y las tablas impresas y las urnas con bolillas no escalaban.

En mil novecientos cuarenta y seis, von Neumann propuso el método de los cuadrados medios: tomar un número, elevarlo al cuadrado, extraer los dígitos centrales y repetir. Es históricamente importante pero pésimo en la práctica: las secuencias colapsan rápido a ciclos cortos o al cero. Hoy se enseña como ejemplo de lo que no hay que hacer.

El salto de calidad llegó en mil novecientos cuarenta y nueve con Derrick Henry Lehmer, que presentó el generador multiplicativo congruencial. La fórmula: el siguiente valor es a por el valor actual, módulo m. Se convirtió en la base de toda la familia de generadores congruenciales lineales. En mil novecientos cincuenta y ocho, Thomson y Rotenberg le agregaron una constante aditiva c, y nació el congruencial mixto: el siguiente valor es a por el actual, más c, todo módulo m. Tiene solo cuatro parámetros, a, c, m y la semilla, pero esos parámetros deciden si el generador es bueno o un desastre.

### Y hoy, ¿qué se usa?

Los congruenciales lineales ya no son lo más usado, aunque siguen siendo valiosos para aprender. Hoy se usan tres familias. Mersenne Twister, de Matsumoto y Nishimura, de mil novecientos noventa y siete, con un período enorme de dos a la diecinueve mil novecientos treinta y siete menos uno; fue durante dos décadas el generador por defecto en Python, R, MATLAB y Excel. PCG64, de O'Neill, de dos mil catorce, que desde dos mil diecinueve es el generador por defecto de NumPy. Y los generadores combinados de L'Ecuyer, que combinan varios congruenciales simples para obtener períodos larguísimos; son los preferidos en bibliotecas profesionales de simulación.

Todos siguen siendo, en el fondo, algoritmos determinísticos con una semilla. Entender el congruencial es entender el ADN de toda la generación de aleatoriedad.

## Qué hace bueno a un generador

Cinco propiedades, que el apunte llama no negociables. Uno: uniformidad estadística, sin acumularse en zonas ni tener huecos. Dos: independencia estadística, sin correlación entre números sucesivos; si graficás los pares, un número contra el siguiente, no debe aparecer ningún patrón. Tres: período largo; la secuencia eventualmente se repite, porque hay finitos estados posibles en una computadora, pero el período tiene que ser tan largo que en ninguna simulación práctica se llegue a repetir. Cuatro: reproducibilidad; la misma semilla produce exactamente la misma secuencia, lo que es esencial para depurar y para comparar alternativas con números aleatorios comunes. Cinco: eficiencia computacional; rápido y con poca memoria, porque una simulación industrial puede pedir miles de millones de números.

## Cuadrados medios

El procedimiento. Uno: se toma una semilla de N cifras, típicamente cuatro. Dos: se eleva al cuadrado, que da un número de hasta dos N cifras; si tiene menos, se completa con ceros a la izquierda. Tres: se extraen las N cifras centrales; ese es el siguiente número de la sucesión. Cuatro: se divide ese número por diez a la N para obtener el uniforme entre cero y uno. Cinco: se repite usando el nuevo número como semilla.

El ejemplo del apunte: semilla siete mil ciento ochenta y dos. Al cuadrado da cincuenta y un millones quinientos ochenta y un mil ciento veinticuatro; las cuatro cifras centrales son cinco mil ochocientos once; el uniforme es cero coma cinco ocho uno uno. Después, cinco mil ochocientos once al cuadrado da treinta y tres millones setecientos sesenta y siete mil setecientos veintiuno; centrales, siete mil seiscientos setenta y siete; uniforme cero coma siete seis siete siete. Y así sigue.

Un detalle: cuando el cuadrado tiene menos de ocho cifras, se completa con un cero a la izquierda. En el apunte, tres mil ciento cincuenta y seis al cuadrado da nueve millones novecientos sesenta mil trescientos treinta y seis, que se trata como cero nueve nueve seis cero tres tres seis, y las centrales son nueve mil seiscientos tres.

### Limitaciones

Con ciertas semillas la sucesión colapsa rápido al cero: cero al cuadrado es cero y se queda ahí para siempre. Otras semillas generan ciclos cortos. El período total es difícil de predecir a partir de la semilla. Y no supera las pruebas estadísticas de independencia. Por eso en los años cincuenta fue desplazado por los congruenciales lineales.

Variantes históricas con las mismas limitaciones: el producto medio, que usa dos semillas que se multiplican, y el multiplicador constante, que multiplica la semilla por una constante fija.

## Congruenciales lineales

Propuestos por Lehmer en mil novecientos cuarenta y nueve, siguen siendo la familia más estudiada. La forma general: el siguiente valor es a por el actual más c, módulo m. Tres variantes según los parámetros. Mixto cuando c es mayor que cero. Multiplicativo cuando c es cero. Y aditivo, una variante histórica donde a es uno, que hoy casi no se usa.

### El congruencial mixto

Los parámetros: la semilla es mayor o igual a cero; el multiplicador a es mayor que cero; la constante c es mayor que cero; el módulo m es mayor que a, que c y que la semilla.

El módulo m define el universo de valores posibles: los valores generados son enteros entre cero y m menos uno, por lo tanto m es la cantidad máxima de valores distintos antes de que la secuencia empiece a repetirse.

¿Por qué se divide por m? Porque la recurrencia produce enteros, pero la simulación necesita uniformes entre cero y uno, que es la entrada de todos los métodos posteriores: transformada inversa, rechazo, composición. Entonces el uniforme es el entero dividido m. Los valores posibles son cero, uno sobre m, dos sobre m, y así hasta m menos uno sobre m. Para m grande aproxima perfectamente al continuo. Con m igual a ocho, como en el ejemplo, solo hay ocho valores posibles, lo que es muy pobre. Con m igual a dos a la treinta y uno menos uno, hay más de dos mil millones.

### Cómo elegir los parámetros

Tres criterios prácticos. Primero: m grande, porque es el límite superior del período; en la práctica real se usa una potencia de dos o un primo grande; en clase se usa chico para poder calcular a mano. Segundo: a, c y m elegidos para asegurar período completo, que es recorrer los m valores antes de repetirse; hay condiciones conocidas, el teorema de Hull y Dobell, de mil novecientos sesenta y dos. Tercero: la semilla no afecta el período si se cumplen las condiciones; solo determina desde dónde se arranca.

### El ejercicio resuelto

Parámetros: semilla cuatro, a igual a cinco, c igual a siete, m igual a ocho. Recurrencia: el siguiente es cinco por el actual más siete, módulo ocho.

Desde el cuatro: cinco por cuatro más siete es veintisiete, módulo ocho da tres. Uniforme tres octavos, cero coma trescientos setenta y cinco. Desde el tres: cinco por tres más siete es veintidós, módulo ocho da seis; uniforme cero coma setecientos cincuenta. Desde el seis: treinta y siete, módulo ocho da cinco; uniforme cero coma seiscientos veinticinco. Desde el cinco: treinta y dos, módulo ocho da cero; uniforme cero. Desde el cero: siete, que da siete; uniforme cero coma ochocientos setenta y cinco. Desde el siete: cuarenta y dos, módulo ocho da dos; uniforme cero coma doscientos cincuenta. Desde el dos: diecisiete, da uno; uniforme cero coma ciento veinticinco. Desde el uno: doce, da cuatro; uniforme cero coma cinco. Y ahí volvió la semilla: cuatro.

Entonces la secuencia es cuatro, tres, seis, cinco, cero, siete, dos, uno, y vuelve al cuatro. El período es ocho, igual a m. Eso se llama período completo, y es lo deseable.

Pero atención: no todos los generadores tienen período completo. Podría pensarse que el período siempre es m, y es falso. Depende de los valores de los parámetros.

### El congruencial multiplicativo

Es el caso con c igual a cero: el siguiente es a por el actual, módulo m. Es el más antiguo de la familia, el que propuso Lehmer. Su ventaja es la eficiencia: no tiene suma, una operación menos por iteración, algo crítico en las computadoras de los cincuenta y todavía relevante hoy.

Su limitación: si en algún momento el valor es cero, la secuencia colapsa, porque cualquier cosa por cero es cero. Por eso la semilla debe ser distinta de cero, y el período máximo posible es m menos uno, no m como en el mixto. Ese máximo se alcanza cuando m es primo y a es una raíz primitiva módulo m.

El ejemplo histórico es el generador de Park y Miller, de mil novecientos ochenta y ocho, también llamado MINSTD: a igual a dieciséis mil ochocientos siete y m igual a dos a la treinta y uno menos uno, que es dos mil ciento cuarenta y siete millones cuatrocientos ochenta y tres mil seiscientos cuarenta y siete. Período de unos dos mil millones y fue durante décadas la referencia en C y Pascal.

Recomendaciones para el multiplicativo: semilla distinta de cero; m primo y grande, por ejemplo un primo de Mersenne como dos a la treinta y uno menos uno; a raíz primitiva módulo m; y período máximo m menos uno porque el cero nunca puede aparecer.

### Cómo calcular el módulo en la calculadora

Muchas calculadoras no tienen tecla de módulo. Tres formas. Una: cálculo mental para números chicos; a módulo b es el resto de dividir a por b; veintisiete módulo ocho es tres, porque veintisiete es ocho por tres más tres. Dos: la fórmula a módulo b es igual a a menos b por la parte entera de a dividido b. Funciona en cualquier calculadora. Dividís, descartás los decimales sin redondear, multiplicás por b y restás del valor original. Ejemplo: veintisiete sobre ocho es tres coma trescientos setenta y cinco; descartás decimales, tres; tres por ocho, veinticuatro; veintisiete menos veinticuatro, tres. Tres: la tecla específica. La Casio fx novecientos noventa y uno tiene en el menú OPTN la opción división con resto. La Casio fx ochenta y dos, la más común en Argentina, no tiene función directa, así que hay que usar la forma dos. En Excel es la función RESIDUO, o MOD en inglés. Recomendación del apunte: la forma dos es la más segura.

## Pruebas estadísticas

Antes de usar un generador hay que verificar que cumple uniformidad e independencia. Para eso se aplican pruebas estadísticas, que no demuestran que el generador sea bueno, sino que permiten descartarlo si no cumple una propiedad. Esto es importante: una prueba que no rechaza no prueba nada, solo dice que no hay evidencia en contra.

Todas siguen el mismo esquema. Uno: se plantean dos hipótesis, la nula, que es la afirmación a poner a prueba, típicamente el generador es uniforme o los números son independientes, y la alternativa, que es la negación. Dos: se calcula un estadístico de prueba a partir de la muestra. Tres: se compara con un valor crítico de tabla, que depende del nivel de significancia alfa, típicamente cero coma cero cinco, o sea noventa y cinco por ciento de confianza. Cuatro: se decide. Si el estadístico cae en la región de aceptación, no se puede rechazar la hipótesis nula y el generador pasa. Si cae en la región de rechazo, se rechaza y se descarta el generador.

El mapa de las cuatro pruebas. Promedios: evalúa que la media esté cerca de cero coma cinco; es teórica, introductoria. Chi cuadrado: uniformidad de la distribución; práctica. Kolmogorov y Smirnov: uniformidad de la distribución acumulada; práctica. Corridas arriba y abajo de la media: independencia entre números sucesivos; práctica. Las tres prácticas son las que se aplican en los trabajos prácticos.

## Prueba de promedios

La más intuitiva y la primera históricamente. Si el generador produce uniformes, el promedio de una muestra grande debería estar cerca de la media teórica, cero coma cinco. La hipótesis nula: la media es cero coma cinco. La alternativa: no lo es.

El estadístico, en palabras: Z cero es igual al promedio de la muestra menos cero coma cinco, multiplicado por la raíz de N, y todo dividido por la raíz de un doceavo. Un doceavo es la varianza de una uniforme. La guía lo simplifica como el promedio menos cero coma cinco, por la raíz de doce por N.

Se compara con la normal estándar. Con alfa cero coma cero cinco, dos colas, el valor crítico es uno coma noventa y seis. Si el valor absoluto de Z cero es menor que uno coma noventa y seis, no se rechaza. Si es mayor o igual, se rechaza.

Su limitación: solo evalúa la media, no la forma de la distribución. Una secuencia perfectamente alternada, cero coma uno, cero coma nueve, cero coma uno, cero coma nueve, pasa la prueba porque su media es cero coma cinco, pero claramente no es aleatoria. Sirve como filtro grueso, pero nunca alcanza sola.

## Prueba de chi cuadrado

La prueba clásica de uniformidad, propuesta por Karl Pearson en mil novecientos y adaptada a simulación. Compara las frecuencias observadas, cuántos números cayeron en cada subintervalo, con las esperadas, cuántos deberían caer si fuera uniforme.

El procedimiento. Uno: dividir el intervalo de cero a uno en n subintervalos de igual ancho. Dos: contar cuántos números cayeron en cada uno: frecuencias observadas. Tres: calcular la frecuencia esperada, que si el ancho es igual es N sobre n para todos. Cuatro: calcular el estadístico, que es la suma, sobre todos los subintervalos, de la diferencia entre observada y esperada, al cuadrado, dividida la esperada. Cinco: comparar con el valor crítico de la tabla con n menos uno grados de libertad.

Se rechaza si el estadístico es mayor o igual al crítico.

Tres criterios prácticos importantes. Primero: la cantidad de subintervalos suele ser la raíz de N redondeada; para treinta números, cinco o seis. Segundo: la frecuencia esperada tiene que ser al menos cinco en cada subintervalo; si alguno no lo cumple, hay que agrupar subintervalos, o sea reducir n. Tercero: los grados de libertad son siempre n menos uno, donde n es el número de subintervalos, no el tamaño de la muestra. Con cinco subintervalos, cuatro grados de libertad.

El ejemplo del apunte: treinta números en cinco subintervalos de ancho cero coma dos; frecuencia esperada seis en cada uno. Observadas: siete, ocho, cuatro, cinco, seis. El estadístico da aproximadamente uno coma sesenta y siete. El crítico, con alfa cero coma cero cinco y cuatro grados de libertad, es nueve coma cuarenta y nueve. Como uno coma sesenta y siete es menor que nueve coma cuarenta y nueve, no se rechaza: es consistente con una uniforme.

La guía aclara que chi cuadrado tiene dos usos. El primero, uniformidad de un generador, con frecuencias esperadas todas iguales. El segundo, bondad de ajuste: comparar una muestra con una distribución teórica cualquiera, no necesariamente uniforme, en cuyo caso las frecuencias esperadas salen de multiplicar las probabilidades de la distribución por el tamaño de la muestra.

## Prueba de Kolmogorov y Smirnov

Desarrollada por Kolmogorov en mil novecientos treinta y tres y Smirnov en mil novecientos cuarenta y ocho. Resuelve limitaciones de chi cuadrado: no requiere agrupar los datos, porque cada número se trata individualmente; es más potente para muestras chicas, menores a cincuenta; y no depende de decisiones arbitrarias sobre cuántos intervalos usar. La idea: comparar la acumulada empírica de la muestra con la acumulada teórica de la uniforme.

El procedimiento. Uno: generar N números. Dos: ordenarlos de menor a mayor. Tres: calcular la acumulada empírica de cada uno: i sobre N, donde i es la posición en el vector ordenado. Cuatro: calcular el estadístico D, que es el máximo, sobre todos los i, de la diferencia absoluta entre i sobre N y el valor del número. Cinco: comparar con el valor crítico de la tabla.

Se rechaza si D es mayor o igual al crítico.

Los valores críticos más usados, con alfa cero coma cero cinco: para diez números, cero coma cuatrocientos nueve; para quince, cero coma trescientos treinta y ocho; para veinte, cero coma doscientos noventa y cuatro; para veinticinco, cero coma doscientos sesenta y cuatro; para treinta, cero coma doscientos cuarenta y dos; para treinta y cinco, cero coma doscientos veinticuatro; para cuarenta, cero coma doscientos diez. Y para más de treinta y cinco, con cinco por ciento, uno coma treinta y seis sobre la raíz de N. Con diez por ciento es uno coma veintidós sobre la raíz de N, y con uno por ciento, uno coma sesenta y tres sobre la raíz de N.

El ejemplo del apunte: treinta números, el máximo de la diferencia dio cero coma cero cincuenta y dos, contra un crítico de cero coma doscientos cuarenta y dos: no se rechaza.

Un detalle técnico: algunos autores calculan dos diferencias por fila, hacia arriba, i sobre N menos el número, y hacia abajo, i menos uno sobre N menos el número, y toman el máximo de ambas. Es el estadístico bilateral. El apunte del eje dos usa la versión simplificada, la de una sola diferencia, que es la que figura en Coss Bu. Fijate qué versión pide la consigna en el parcial.

## Prueba de corridas arriba y abajo de la media

Las tres anteriores evalúan uniformidad, pero ninguna evalúa independencia. Una secuencia uniforme pero predecible, como cero coma uno, cero coma dos, hasta cero coma nueve, y vuelve a empezar, pasaría las tres anteriores aunque claramente no sea aleatoria. Las pruebas de corridas, o de rachas, detectan dependencias entre números sucesivos. La idea: contar las rachas y comparar el número observado con el esperado bajo aleatoriedad.

La hipótesis nula: los números son independientes. La alternativa: presentan dependencia.

El procedimiento. Uno: a cada número se le asigna un más si está por encima de cero coma cinco y un menos si está por debajo; los iguales a cero coma cinco se descartan o se asignan al grupo mayoritario. Dos: identificar las corridas; cada secuencia consecutiva de símbolos iguales es una corrida. Por ejemplo, más más, menos menos menos, más, menos, más más, menos, tiene seis corridas. Tres: contar n uno, cantidad de números arriba, n dos, cantidad abajo, y C, cantidad total de corridas. Cuatro: calcular la cantidad esperada de corridas, que es dos por n uno por n dos, dividido n uno más n dos, más un medio; y su varianza, que es dos por n uno por n dos, por dos por n uno por n dos menos n uno menos n dos, todo dividido n uno más n dos al cuadrado, por n uno más n dos menos uno. Cinco: calcular Z cero, que es C menos la esperada, dividido el desvío. Seis: comparar el valor absoluto con uno coma noventa y seis.

Si el valor absoluto de Z cero es menor que uno coma noventa y seis, no se rechaza: los números son consistentes con una secuencia independiente. Si es mayor o igual, hay evidencia de dependencia.

La interpretación intuitiva. Muy pocas corridas significa que los números tienden a agruparse, varios seguidos arriba, varios seguidos abajo: tendencia o correlación positiva. Demasiadas corridas significa que alternan en exceso: anticorrelación. Los dos casos son indicio de no independencia.

El ejemplo del apunte: veinte números, con once arriba y nueve abajo y once corridas. La esperada es dos por once por nueve, dividido veinte, más cero coma cinco: ciento noventa y ocho sobre veinte es nueve coma nueve, más cero coma cinco, diez coma cuatro. La varianza da aproximadamente cuatro coma seiscientos treinta y siete, y el desvío dos coma ciento cincuenta y tres. Z cero es once menos diez coma cuatro, sobre dos coma ciento cincuenta y tres: cero coma doscientos setenta y nueve. Menor que uno coma noventa y seis, no se rechaza.

## La práctica del eje dos, resuelta

Hice las cuentas de los ejercicios de la guía. Revisalas con tu hoja, porque son mías.

Generadores. El primero: cinco por X más uno, módulo nueve, semilla uno. La secuencia es uno, seis, cuatro, tres, siete, cero, y vuelve al uno. Período seis, y como m es nueve, no es de período completo. Los uniformes son el entero dividido nueve. Se explica con Hull y Dobell: para período completo, a menos uno tiene que ser múltiplo de todos los primos que dividen a m, y acá a menos uno es cuatro, que no es múltiplo de tres.

El segundo: cinco por X más tres, módulo dieciséis, semilla siete. La secuencia es siete, seis, uno, ocho, once, diez, cinco, doce, quince, catorce, nueve, cero, tres, dos, trece, cuatro, y vuelve al siete. Período dieciséis, igual a m: período completo.

El tercero, multiplicativo: tres por X, módulo cien, semilla cincuenta y uno. La secuencia es cincuenta y uno, cincuenta y tres, cincuenta y nueve, setenta y siete, treinta y uno, noventa y tres, setenta y nueve, treinta y siete, once, treinta y tres, noventa y nueve, noventa y siete, noventa y uno, setenta y tres, diecinueve, cincuenta y siete, setenta y uno, trece, treinta y nueve, diecisiete, y vuelve al cincuenta y uno. Período veinte, no es de período completo: ni siquiera llega a cien, y el máximo de un multiplicativo es m menos uno.

Repaso de generadores: el mixto de cinco, siete, ocho, semilla cuatro, es el ejercicio resuelto: período ocho, completo. El multiplicativo cinco por X módulo treinta y dos, semilla cinco: secuencia cinco, veinticinco, veintinueve, diecisiete, veintiuno, nueve, trece, uno, y vuelve al cinco. Período ocho, no es completo; para un multiplicativo con m igual a treinta y dos el máximo posible es ocho.

Pruebas. Promedios, ejercicio uno: veinte valores con media cero coma cincuenta y uno. Z cero es cero coma cero uno por la raíz de doscientos cuarenta, que da cero coma quince. Menor que uno coma noventa y seis: se acepta. En el repaso, doce valores con media cero coma quinientos quince: Z cero es cero coma dieciocho, se acepta.

Chi cuadrado, ejercicio uno: cien números, cinco subintervalos, esperada veinte, observadas veintiuno, veintidós, diecinueve, veintitrés, quince. Las diferencias al cuadrado son uno, cuatro, uno, nueve y veinticinco, que suman cuarenta; dividido veinte da dos. Contra nueve coma cuarenta y nueve: se acepta. Ejercicio dos, grupos sanguíneos: las frecuencias esperadas con ciento cincuenta donantes son tres, cuarenta y cinco coma setenta y cinco, trece coma noventa y cinco y ochenta y siete coma tres. El estadístico da aproximadamente cero coma setenta y tres, con tres grados de libertad, contra siete coma ochocientos quince: se acepta. Ojo, que la frecuencia esperada del grupo AB es tres, menor que cinco, y la regla del apunte pediría agrupar. En el repaso, la concesionaria: esperada doce por modelo, observadas quince, once, diez y doce; el estadístico da uno coma diecisiete, contra siete coma ochocientos quince: se acepta.

Kolmogorov y Smirnov, ejercicio uno: veinte valores ordenados; con la versión simplificada, la diferencia máxima da cero coma cero siete, contra cero coma doscientos noventa y cuatro: se acepta. En el repaso, ocho valores todos entre cero coma noventa y cinco y uno, con alfa uno por ciento: la diferencia máxima da cero coma ochenta y tres, muchísimo mayor que cualquier crítico razonable: se rechaza, que tiene sentido porque están todos amontonados cerca del uno. La tabla del apunte arranca en diez números, así que para ocho hace falta una tabla completa.

## Para cerrar: lo que más puede caer

Primero: por qué se usan pseudoaleatorios y no aleatorios verdaderos. Tres razones: lentos, no reproducibles, no depurables. Las dos propiedades de los números: uniformidad e independencia. Las cinco propiedades de un buen generador.

Segundo: cuadrados medios, el procedimiento y por qué es malo; y los congruenciales, con las tres variantes por el valor de c. Para el mixto, la recurrencia, y que el período completo no es automático. Para el multiplicativo, la semilla distinta de cero y el período máximo m menos uno.

Tercero: las cuatro pruebas y qué evalúa cada una. Promedios mira la media; chi cuadrado y Kolmogorov y Smirnov miran uniformidad; corridas mira independencia. Los valores críticos de memoria: uno coma noventa y seis para promedios y corridas; nueve coma cuarenta y nueve para chi cuadrado con cuatro grados de libertad.

Cuarto: una prueba que no rechaza no demuestra que el generador sea bueno, solo que no hay evidencia en contra. Y la limitación de promedios: puede pasar una secuencia alternada.

Eso es todo del eje dos.
