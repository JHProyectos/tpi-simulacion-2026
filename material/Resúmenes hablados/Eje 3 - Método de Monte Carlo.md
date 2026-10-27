# Eje 3. Método de Monte Carlo

Hola. Este es el resumen hablado del eje tres: método de Monte Carlo. Dura unos quince minutos. Para el parcial de mañana no entra, pero es corto, es el puente entre los números aleatorios del eje dos y todo el resto, y en el parcial práctico uno ya cayó un problema de Monte Carlo, el de la florería. Una aclaración honesta: en tu carpeta de este eje solo hay la guía práctica, no hay un apunte teórico. Así que la explicación del método sale de lo que muestran los tres problemas de la guía y de ideas que aparecen en los otros ejes. Lo que sigue es la receta y los tres problemas resueltos.

## La idea del método

Monte Carlo es usar números aleatorios para estimar algo que no podés calcular con una fórmula cerrada, o que simplemente es más fácil simular que calcular. Se toma una variable que tiene azar, se la representa con su distribución de probabilidad, se sortea muchas veces y se calcula el resultado que interesa con lo que salió: un promedio, una probabilidad, una ganancia.

Es el uso más directo de lo que vimos en el eje dos: los números pseudoaleatorios uniformes entre cero y uno son la materia prima, y el método consiste en convertir cada número uniforme en un valor de la variable que se está modelando. En el eje dos se mencionó el origen: von Neumann y Ulam, en Los Álamos, durante el Proyecto Manhattan, necesitando muchísimos números aleatorios para simular difusión de neutrones.

Y una relación con el resto: en el eje ocho se dice que si se sortean los parámetros inciertos de un modelo a partir de una distribución, el modelo pasa a tener azar y vuelven a hacer falta muchas corridas, y que eso es un experimento de Monte Carlo como los del eje tres.

## La receta, paso a paso

Siempre es la misma, en los tres problemas.

Primero: identificar la variable aleatoria y su distribución, que normalmente viene como una tabla de frecuencias observadas durante cierta cantidad de días.

Segundo: convertir frecuencias en probabilidades, dividiendo cada frecuencia por el total. Si hubo cincuenta días y un valor apareció seis veces, su probabilidad es seis sobre cincuenta, cero coma doce.

Tercero: calcular la probabilidad acumulada, sumando de arriba hacia abajo. La última tiene que dar uno.

Cuarto: construir los intervalos de números aleatorios. Si las probabilidades tienen dos decimales se usan números de dos dígitos, de cero cero a noventa y nueve. Cada valor de la variable recibe un tramo de ese rango, de tamaño proporcional a su probabilidad. El truco para no equivocarte: el límite superior de cada intervalo es la acumulada por cien menos uno. Por ejemplo, si la acumulada es cero coma treinta, el límite superior es veintinueve. El límite inferior es el superior del anterior más uno. Y el último siempre termina en noventa y nueve. Los intervalos no se pueden superponer ni dejar huecos.

Quinto: para cada número aleatorio que te dan, buscar en qué intervalo cae y anotar el valor de la variable que le corresponde. Esa es la simulación en sí: es mecánica.

Sexto: con todos los valores simulados, calcular lo que pide el problema: el promedio, la probabilidad de un evento como la proporción de veces que ocurrió, o la ganancia.

Séptimo, y esto es lo que se pregunta siempre al final: interpretar y decidir. Y acordarse de que con pocas repeticiones el resultado es solo una estimación, y que mientras más repeticiones, más confiable.

## Problema uno: la mesa de ayuda

Una mesa de ayuda registró durante cincuenta días la cantidad de tickets por jornada. Doce tickets en seis días, catorce en nueve, dieciséis en trece, dieciocho en once, veinte en siete y veintidós en cuatro. El equipo puede resolver hasta dieciocho por día sin horas extra. Se pide simular quince días con números dados, estimar el promedio de tickets por día y estimar la probabilidad de superar la capacidad, o sea más de dieciocho.

Probabilidades: cero coma doce, cero coma dieciocho, cero coma veintiséis, cero coma veintidós, cero coma catorce y cero coma ocho. Acumuladas: cero coma doce, cero coma treinta, cero coma cincuenta y seis, cero coma setenta y ocho, cero coma noventa y dos y uno.

Intervalos. Doce tickets: de cero cero a once. Catorce tickets: de doce a veintinueve. Dieciséis: de treinta a cincuenta y cinco. Dieciocho: de cincuenta y seis a setenta y siete. Veinte: de setenta y ocho a noventa y uno. Veintidós: de noventa y dos a noventa y nueve.

Los números aleatorios son cincuenta y ocho, cero tres, noventa y uno, veintisiete, setenta y seis, catorce, cuarenta y nueve, ochenta y ocho, treinta y cinco, sesenta y dos, cero nueve, setenta y uno, cuarenta y cuatro, noventa y seis y veinte.

Los tickets simulados, día por día: dieciocho, doce, veinte, catorce, dieciocho, catorce, dieciséis, veinte, dieciséis, dieciocho, doce, dieciocho, dieciséis, veintidós y catorce.

La suma da doscientos cuarenta y ocho. El promedio es doscientos cuarenta y ocho sobre quince: dieciséis coma cincuenta y tres tickets por día.

Para la probabilidad de superar la capacidad: más de dieciocho es veinte o veintidós. Hay tres días: los dos de veinte y el de veintidós. Tres sobre quince es cero coma veinte: veinte por ciento. Cuidado con la trampa del enunciado: más de dieciocho es estrictamente mayor, así que los días con exactamente dieciocho no cuentan.

Como control: con la distribución original, el promedio teórico es dieciséis coma sesenta y cuatro y la probabilidad teórica de superar la capacidad es veintidós por ciento. La simulación con solo quince días dio algo muy parecido. Ese control lo calculé yo, no figura en la guía.

## Problema dos: cuántas docenas hornear

Una panadería hornea medialunas para la venta del día. Cada docena vendida deja mil pesos de ganancia, y las docenas horneadas que no se venden se descartan, con una pérdida de mil pesos por docena. La demanda diaria de docenas en cincuenta días: treinta docenas en cinco días, treinta y cinco en doce, cuarenta en dieciocho, cuarenta y cinco en diez y cincuenta en cinco. El panadero duda entre hornear cuarenta o cuarenta y cinco docenas.

Probabilidades: diez por ciento, veinticuatro por ciento, treinta y seis por ciento, veinte por ciento y diez por ciento. Acumuladas: diez por ciento, treinta y cuatro por ciento, setenta por ciento, noventa por ciento y cien por ciento.

Intervalos. Treinta docenas: de cero cero a cero nueve. Treinta y cinco: de diez a treinta y tres. Cuarenta: de treinta y cuatro a sesenta y nueve. Cuarenta y cinco: de setenta a ochenta y nueve. Cincuenta: de noventa a noventa y nueve.

Los números aleatorios de demanda, doce días: cuarenta y siete, ochenta y dos, quince, sesenta y tres, treinta y ocho, noventa y uno, veintiséis, setenta, cincuenta y cuatro, cero ocho, setenta y siete y treinta y tres.

La demanda simulada: cuarenta, cuarenta y cinco, treinta y cinco, cuarenta, cuarenta, cincuenta, treinta y cinco, cuarenta y cinco, cuarenta, treinta, cuarenta y cinco y treinta y cinco.

Ahora la ganancia de cada política. La regla: vendés lo que sea menor entre la demanda y lo que horneaste. Ganás mil por cada docena vendida y perdés mil por cada docena sobrante. Si la demanda supera lo horneado, no ganás de más: las ventas perdidas no suman.

Política de cuarenta docenas. Si la demanda es cuarenta o más, vendés cuarenta y ganás cuarenta mil. Si la demanda es treinta y cinco, vendés treinta y cinco, sobran cinco: treinta y cinco mil menos cinco mil, treinta mil. Si es treinta, vendés treinta, sobran diez: veinte mil. Día por día: cuarenta mil, cuarenta mil, treinta mil, cuarenta mil, cuarenta mil, cuarenta mil, treinta mil, cuarenta mil, cuarenta mil, veinte mil, cuarenta mil, treinta mil. Total cuatrocientos treinta mil, promedio treinta y cinco mil ochocientos treinta y tres pesos por día.

Política de cuarenta y cinco docenas. Demanda de cuarenta y cinco o más: vendés cuarenta y cinco, cuarenta y cinco mil. Demanda cuarenta: vendés cuarenta, sobran cinco, treinta y cinco mil. Demanda treinta y cinco: sobran diez, veinticinco mil. Demanda treinta: sobran quince, quince mil. Día por día: treinta y cinco mil, cuarenta y cinco mil, veinticinco mil, treinta y cinco mil, treinta y cinco mil, cuarenta y cinco mil, veinticinco mil, cuarenta y cinco mil, treinta y cinco mil, quince mil, cuarenta y cinco mil, veinticinco mil. Total cuatrocientos diez mil, promedio treinta y cuatro mil ciento sesenta y siete pesos por día.

La recomendación: conviene hornear cuarenta docenas, que da treinta y cinco mil ochocientos treinta y tres contra treinta y cuatro mil ciento sesenta y siete. La diferencia es de unos mil seiscientos sesenta y siete pesos por día.

Como control, con la distribución completa, la ganancia esperada es treinta y cinco mil seiscientos con cuarenta docenas y treinta y tres mil seiscientos con cuarenta y cinco. Da la misma conclusión. La razón: como lo que ganás por docena vendida es igual a lo que perdés por docena sobrante, una docena extra solo conviene si tiene más de cincuenta por ciento de probabilidad de venderse. La probabilidad de que la demanda llegue a cuarenta y cinco o más es de treinta por ciento, así que pasar de cuarenta a cuarenta y cinco docenas no se paga. Este control y este razonamiento también son míos.

Detalle que sirve para el parcial: las dos políticas se evalúan con la misma demanda simulada. Es la misma idea de reproducibilidad del eje dos y de números aleatorios comunes del eje cuatro y seis: para comparar alternativas con justicia, las dos tienen que ver exactamente las mismas condiciones.

## Problema tres: duración de un proyecto de software

Un equipo debe estimar la duración de un proyecto con dos fases secuenciales: análisis y desarrollo. El cliente pide comprometer una fecha de entrega a treinta días.

Análisis: ocho días con probabilidad cero coma treinta, diez días con cero coma cincuenta y doce días con cero coma veinte. Desarrollo: quince días con cero coma veinte, dieciocho con cero coma cuarenta, veinte con cero coma veinticinco y veintidós con cero coma quince.

Intervalos de análisis: ocho días, de cero cero a veintinueve; diez días, de treinta a setenta y nueve; doce días, de ochenta a noventa y nueve.

Intervalos de desarrollo: quince días, de cero cero a diecinueve; dieciocho días, de veinte a cincuenta y nueve; veinte días, de sesenta a ochenta y cuatro; veintidós días, de ochenta y cinco a noventa y nueve.

Como hay dos variables, se usa un número aleatorio por fase en cada proyecto. Es importante: no se reutiliza el mismo número para las dos fases, porque cada variable necesita su propio sorteo independiente. Los pares, análisis y desarrollo, son: cincuenta y ocho y doce; cero siete y setenta y tres; noventa y uno y cuarenta; treinta y cuatro y ochenta y ocho; setenta y seis y diecinueve; veintidós y cincuenta y cinco; cuarenta y nueve y sesenta y siete; ochenta y ocho y treinta y uno; quince y noventa y dos; sesenta y tres y cuarenta y ocho.

Proyecto por proyecto, análisis más desarrollo. Uno: diez más quince, veinticinco. Dos: ocho más veinte, veintiocho. Tres: doce más dieciocho, treinta. Cuatro: diez más veintidós, treinta y dos. Cinco: diez más quince, veinticinco. Seis: ocho más dieciocho, veintiséis. Siete: diez más veinte, treinta. Ocho: doce más dieciocho, treinta. Nueve: ocho más veintidós, treinta. Diez: diez más dieciocho, veintiocho.

Las duraciones totales son entonces veinticinco, veintiocho, treinta, treinta y dos, veinticinco, veintiséis, treinta, treinta, treinta y veintiocho. La duración promedio es veintiocho coma cuatro días.

Probabilidad de terminar en treinta días o menos: de los diez proyectos, solo uno duró treinta y dos, así que nueve terminaron en treinta o menos. Nueve sobre diez es cero coma noventa: noventa por ciento. Atención: treinta días o menos incluye los treinta.

¿Es razonable comprometer la fecha de treinta días? Con esta simulación, noventa por ciento parece alto. Pero hay que mirar dos cosas. Una: son solo diez proyectos; es una muestra muy chica, y el noventa por ciento podría ser bastante distinto con más repeticiones. Dos: queda un diez por ciento de riesgo de entregar tarde, y varios proyectos cayeron justo en treinta, sin margen. Una respuesta razonable es que se puede comprometer treinta días con riesgo aceptable, pero que conviene simular muchas más veces antes de prometerlo, o negociar un margen.

Como control, calculé la probabilidad exacta con las dos distribuciones, y da ochenta y cuatro coma cinco por ciento. O sea que la simulación de diez corridas dio un poco más optimista que la realidad del modelo, y eso confirma que hay que desconfiar de muestras tan chicas. Este valor también lo calculé yo.

## Errores típicos para evitar

Armar mal los intervalos, con superposiciones o huecos, o que no terminen en noventa y nueve. Olvidar que más de dieciocho es estrictamente mayor. Calcular el promedio de los intervalos en lugar del promedio de los valores simulados. En el problema de las medialunas, sumar ganancia por demanda no satisfecha, que no existe. Reusar el mismo número aleatorio para dos variables distintas. Y concluir con demasiada seguridad a partir de pocas repeticiones.

## Para cerrar: lo que más puede caer

Primero, la receta: tabla de frecuencias, probabilidades, acumuladas, intervalos de números aleatorios, sorteo, estadístico, decisión. El límite superior de cada intervalo es la acumulada por cien menos uno.

Segundo, los tres tipos de pregunta de la guía: un promedio, una probabilidad de un evento, y una comparación de políticas por ganancia. Los tres resultados de la guía: dieciséis coma cincuenta y tres tickets por día con veinte por ciento de superar la capacidad; cuarenta docenas dan treinta y cinco mil ochocientos treinta y tres contra treinta y cuatro mil ciento sesenta y siete de las cuarenta y cinco; y proyectos de veintiocho coma cuatro días con noventa por ciento de terminar en treinta o menos.

Tercero, las ideas de fondo: con pocas repeticiones, el resultado es una estimación y no un valor exacto; para comparar políticas se usan los mismos números aleatorios en todas; y cada variable aleatoria necesita su propio sorteo.

Eso es todo del eje tres. Con esto cerramos los ocho ejes.
