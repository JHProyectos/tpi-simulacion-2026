# Eje 6. Análisis de datos e implantación

Vamos con el eje seis, análisis de datos e implantación. Este repaso dura unos treinta y un minutos. Entra solo la teoría, casi toda en multiple choice, con alguna posible pregunta de desarrollo. Las ideas centrales son cuatro. Una: el promedio solo no alcanza, y la distribución de entrada se elige combinando histograma, medidas descriptivas y prueba de bondad de ajuste. Dos: no rechazar una hipótesis no demuestra nada. Tres: una corrida es un futuro posible, no la respuesta; por eso hay réplicas, intervalos de confianza y, en sistemas no terminantes, warm-up. Cuatro: verificar, validar e implantar son cosas distintas, y la implantación va por etapas, con piloto.

## Datos de entrada

### Qué medir y cómo preparar los datos

Un modelo bien armado da resultados poco confiables si los datos de entrada están mal medidos. El ejemplo del apunte: la atención media es de cinco minutos, y alguien carga todas las atenciones como cinco minutos fijos. Eso esconde la variabilidad, que es lo que genera las colas. Dos sistemas con el mismo promedio se comportan muy distinto si uno varía poco y el otro mucho.

Se miden las variables aleatorias que cambian la congestión: tiempos entre llegadas, de servicio, cantidades, y tiempos de falla y reparación. Y la muestra tiene que ser representativa: distintos momentos, días y condiciones, no diez casos cómodos.

Preparar es unificar unidades, sacar duplicados, revisar valores imposibles como tiempos negativos, ordenar y separar por tipo cuando corresponda: en una mesa de ayuda, pedidos rápidos y lentos mezclados dan una distribución sin sentido.

Un outlier es un dato muy alejado del resto, y no siempre se elimina: puede ser un error de carga o un caso real, como el cliente que tardó muchísimo por un problema con el pago. Con los faltantes, igual: si son pocos, se descartan; si son muchos, se vuelve a medir.

Los atípicos se ven con el boxplot. La caja tiene el cincuenta por ciento central, entre el primer y el tercer cuartil, y la línea de adentro es la mediana. El rango intercuartílico es el tercer cuartil menos el primero. El límite inferior es el primer cuartil menos uno coma cinco veces ese rango, y el superior, el tercer cuartil más lo mismo. Lo que queda afuera son posibles outliers.

**Lo importante.** La dispersión y la forma importan tanto como el promedio. Y limpiar no es borrar lo que molesta.

**Ojo, trampa.** "Con el tiempo medio alcanza" es falso, y el apunte lo lista como error frecuente. Otros que marca: confundir instantes con duraciones, cargar tiempos absolutos cuando se necesitan tiempos entre eventos y elegir una distribución por costumbre. "Los outliers siempre se eliminan" también es falso. Y en el boxplot, el factor multiplica al rango intercuartílico, no al desvío.

## Estadística descriptiva

Las medidas descriptivas orientan el ajuste. La media es el promedio y la afectan los extremos. La mediana es el dato central y es más robusta frente a outliers; si media y mediana se parecen, la distribución suele ser simétrica. La moda es el valor más repetido, y puede no existir o haber más de una.

La varianza muestral suma los cuadrados de las diferencias con la media y divide por n menos uno. El desvío es su raíz, en la unidad del dato. Y el coeficiente de variación, el desvío dividido la media, por cien, compara dispersión entre procesos.

Ejemplo del apunte: con cuatro, cinco, cinco, seis y ocho, la media da cinco coma seis y la mediana cinco; la media queda arriba porque el ocho la empuja.

El histograma da la primera hipótesis de forma, pero la frase del apunte es: el gráfico dice parece, la prueba dice qué tan bien ajusta.

**Lo importante.** Media contra mediana te da una pista de la simetría.

**Ojo, trampa.** La varianza muestral divide por n menos uno, no por n. La moda puede no ser única. Y si te dicen que la media es más robusta que la mediana frente a outliers, es al revés.

## Distribuciones: cuál usar y cuándo

Clásico de multiple choice: te describen una situación y elegís la distribución.

### Exponencial y Poisson

La exponencial es continua, con muchos valores chicos y una cola larga a la derecha. Es la candidata natural para tiempos entre llegadas. Su parámetro lambda es una tasa, y se estima como uno dividido la media muestral. Ejemplo del apunte: con una media de tres coma treinta y un minutos, lambda es cero coma trescientos dos por minuto.

La Poisson es discreta: cuenta cuántos eventos ocurren en un intervalo fijo, por ejemplo cuántos clientes llegan en diez minutos. Pueden ser dos o tres, nunca dos y medio. Su media y su varianza son iguales, lambda por t.

Son dos caras del mismo proceso: si el tiempo entre llegadas es exponencial con tasa lambda, la cantidad de llegadas en un tiempo t es Poisson con media lambda por t.

**Lo importante.** Tiempo entre eventos, exponencial. Cantidad de eventos en un intervalo, Poisson.

**Ojo, trampa.** Es el par que más se confunde: si la pregunta habla de tiempo entre llegadas, Poisson es el distractor. Y lambda no es la media: la media de la exponencial es uno sobre lambda.

### Las demás distribuciones

La uniforme se usa cuando solo conocés un mínimo y un máximo, sin ningún valor más frecuente. Ejemplo: reponer una góndola tarda entre dos y cuatro minutos. Su media es a más b, dividido dos.

La triangular se usa cuando conocés mínimo, valor más probable y máximo, que puede dar un experto. Ejemplo: un cambio de turno dura como mínimo cuatro minutos, normalmente seis y como máximo diez. Su media es a más m más b, dividido tres. Las dos sirven en estudios preliminares, con pocos datos.

La normal es la campana simétrica, como el peso de paquetes de un mismo producto. Si la usás para tiempos, revisá que la probabilidad de valores negativos sea despreciable.

La lognormal es asimétrica a la derecha: muchos valores moderados y algunos altos, como los tiempos de pago. Se prueba cuando hay cola a la derecha pero no parece una exponencial pura. Sus parámetros son la media y el desvío de los logaritmos de los datos.

La gamma es flexible, y aparece en tiempos de servicio como la suma de varias etapas al preparar un pedido. La Weibull es la de confiabilidad: fallas, desgaste y vida útil, como el tiempo de una impresora hasta que falla.

Y si ninguna curva ajusta, o hay dos picos, se usa la empírica, que copia la forma de la muestra; en FlexSim es Continuous Empirical. No es mágica: necesita una muestra grande, limpia y representativa, y si mezcla horario pico y valle, primero hay que separarlos.

**Lo importante.** Mínimo y máximo, uniforme. Con valor más probable, triangular. Simétrica, normal. Cola a la derecha, lognormal o gamma. Fallas, Weibull. Nada ajusta, empírica.

**Ojo, trampa.** Si el enunciado da un valor "normal" o "más común", es triangular, no uniforme, y su m es la moda, no la media. Los parámetros de la lognormal salen de los logaritmos, no de los datos. Y algo que el apunte marca como importante: no se necesita una distribución de salida. La salida de clientes es un resultado del modelo; lo que se ajusta son las entradas, los arribos en el Source y el servicio en el Processor.

## Bondad de ajuste

### Qué es y cómo se lee

Bondad de ajuste es medir qué tan cerca están los datos reales de una distribución propuesta. En el eje dos se probaba si el generador daba números uniformes; acá, si los datos reales se pueden representar con una distribución candidata.

Dos frases del apunte. La prueba no elige por sí sola: primero se mira el histograma y se entiende el proceso, y después la prueba respalda o cuestiona. Y un valor p mayor que cero coma cero cinco significa que no hay evidencia suficiente para rechazar la distribución, no que quedó demostrada como la única verdadera. Además, la mejor distribución no es la más compleja, sino la que ajusta y tiene sentido para el fenómeno.

**Lo importante.** No rechazar no es demostrar.

**Ojo, trampa.** Cualquier opción que diga que la prueba "demuestra" o "confirma" la distribución es falsa. Lo correcto es "no se rechaza" o "los datos son compatibles".

### Kolmogorov-Smirnov

Trabaja con acumuladas. La acumulada empírica, que el apunte llama ECDF, da para cada valor la proporción de datos menores o iguales, y se ve como una escalera. La prueba la compara con la acumulada teórica, y el estadístico D es la mayor distancia vertical entre las dos. No necesita agrupar los datos, por eso es cómoda para variables continuas.

La versión de este apunte es bilateral: en cada escalón medís los dos lados. Después del salto, i sobre n menos F de x i. Antes del salto, F de x i menos i menos uno sobre n. Y te quedás con la máxima. En el eje dos se usaba una versión simplificada, que miraba un solo lado.

El ejemplo: veinte tiempos entre llegadas contra una exponencial. El D máximo da cero coma ciento cuarenta y uno, menor que el crítico de cero coma doscientos noventa y cuatro para veinte datos y alfa cero coma cero cinco. No se rechaza la exponencial.

**Lo importante.** Compara acumuladas, sin agrupar, midiendo los dos lados de cada escalón.

**Ojo, trampa.** Si una opción dice que D se calcula solo como i sobre n menos F de x i, describe la versión del eje dos. Y no cruces los criterios: con D, rechaza un valor grande; con el valor p, uno chico.

### Chi cuadrado y la limitación común

Trabaja con frecuencias. Agrupás los datos en intervalos, contás las observadas, calculás las esperadas según la distribución, y sumás observado menos esperado al cuadrado, dividido esperado. Los grados de libertad son k menos uno menos p, con k intervalos y p parámetros estimados. Las esperadas no pueden ser menores que cinco; si lo son, se agrupa más. Y el resultado depende de cómo agrupes.

El ejemplo: sesenta tiempos de atención contra una normal, con cinco intervalos. El estadístico da dos coma doscientos treinta y nueve, con dos grados de libertad, contra un crítico de cinco coma novecientos noventa y uno. No se rechaza la normal, y el apunte aclara que eso no demuestra normalidad.

La limitación que comparten las dos pruebas: sus tablas suponen que la distribución está completamente especificada de antemano. En simulación los parámetros se estiman con los mismos datos que después se prueban, y entonces la prueba tiende a aceptar de más. Por eso se combinan tres miradas: histograma, medidas descriptivas y bondad de ajuste.

**Lo importante.** Kolmogorov-Smirnov compara acumuladas y no agrupa. Chi cuadrado compara frecuencias, agrupa, pide esperadas de al menos cinco y depende de los intervalos.

**Ojo, trampa.** Olvidarse de restar los parámetros: con cinco intervalos y una normal son dos grados de libertad, no cuatro. Y la opción tramposa dice que estimar los parámetros con la muestra vuelve la prueba más exigente. Es al revés: acepta de más.

**Si te toca de desarrollo.** Definí bondad de ajuste y para qué sirve. Explicá Kolmogorov-Smirnov: acumuladas, D a los dos lados de cada escalón, sin agrupar. Explicá chi cuadrado: intervalos, esperadas de al menos cinco, k menos uno menos p. Sumá la limitación de los parámetros estimados. Y cerrá con que no rechazar no demuestra.

## Planeación táctica

Define cuánto simular, desde cuándo medir y cuántas réplicas correr. La frase del apunte: una corrida es un futuro posible, no la respuesta.

### Variabilidad y réplicas

Dos corridas del mismo modelo dan resultados distintos porque las entradas son aleatorias. No es un error del software; el error es mirar una sola corrida y creerla definitiva.

Con n réplicas calculás la media de las réplicas, que es el resultado estimado; el desvío entre réplicas, que dice cuánto cambia una corrida de otra; y el error estándar, el desvío dividido raíz de n, que mide la incertidumbre de la media.

Una réplica es una ejecución completa e independiente: reinicia el estado y las estadísticas, y usa aleatorios independientes. Cortar una corrida larga en trozos no es lo mismo, porque los trozos pueden estar correlacionados.

**Lo importante.** Un resultado se informa con varias réplicas independientes, no con una corrida.

**Ojo, trampa.** Con más réplicas baja el error estándar, no la variabilidad del sistema. "Si dos corridas dan distinto, el modelo tiene un error" es falso. Y una corrida larga en trozos no equivale a réplicas.

### Sistemas terminantes, no terminantes y warm-up

El terminante, como un supermercado de ocho a veintiuna, se vacía o se reinicia cada jornada, y la pregunta es cómo fue ese día. El no terminante, como un hospital de veinticuatro horas o un servidor web, no tiene final natural, y la pregunta es cómo funciona a largo plazo.

Si un sistema que normalmente tiene cola arranca vacío, los primeros minutos parecen tranquilos y se subestima la espera: es el sesgo de inicialización. El warm-up es el período inicial en que el modelo corre normalmente pero no se mide. Ejemplo: un hospital simulado treinta días, con dos de warm-up, se mide del día tres al treinta. Para elegirlo, se grafican corridas piloto, promediadas o con media móvil, y se toma el punto donde termina la tendencia de arranque.

En FlexSim, el Warmup Time indica cuándo se reinician las estadísticas, y el Stop Time cuándo termina la réplica.

**Lo importante.** El warm-up es para sistemas no terminantes, y elimina el sesgo de arrancar vacío.

**Ojo, trampa.** Durante el warm-up el modelo funciona; solo se descartan las estadísticas. En el supermercado simulado desde su apertura real, el apunte dice que no hace falta warm-up. Y warm-up y réplicas resuelven cosas distintas: el sesgo de arranque y la variabilidad entre corridas.

### Cuántas réplicas

No hay un número mágico: depende de la variabilidad y de la precisión que necesitás. El intervalo de confianza del noventa y cinco por ciento es la media de las réplicas, más o menos el t de Student con n menos uno grados de libertad, por el desvío dividido raíz de n. El apunte recomienda un error relativo de hasta un quince por ciento, aproximadamente.

El procedimiento: fijás la precisión, corrés un piloto de al menos diez réplicas, mirás el semiancho y recalculás. El n nuevo es el n inicial por el cociente entre el semiancho obtenido y el deseado, al cuadrado. Ejemplo: diez réplicas con semiancho de un minuto, y querés medio. Uno dividido cero coma cinco es dos; al cuadrado, cuatro; por diez, cuarenta. Y el apunte aclara: cuarenta en total, no cuarenta adicionales.

**Lo importante.** Por el cuadrado, reducir el semiancho a la mitad pide cuatro veces más réplicas, no el doble.

**Ojo, trampa.** La fórmula da el total, no lo que hay que agregar. Y el t va con n menos uno grados de libertad, no con n.

**Si te toca de desarrollo.** Arrancá con que una corrida es un futuro posible. Definí réplica y por qué no sirve partir una corrida larga. Contá el intervalo de confianza. Explicá el piloto y la fórmula, con el ejemplo de diez a cuarenta en total. Y sumá el warm-up.

### Números aleatorios comunes

Reducir varianza es comparar con más claridad sin multiplicar réplicas. No mejora el sistema real ni los resultados: mejora la forma de experimentar.

Con números aleatorios comunes, la réplica uno de las dos alternativas corre con la misma demanda aleatoria, la réplica dos con otra demanda común, y así. Comparás par por par, y la demanda del día no tapa el efecto de agregar una caja. El apunte menciona también las variables antitéticas, que usan secuencias opuestas, y las de control, que aprovechan una medida conocida y correlacionada.

**Lo importante.** Sirve para comparar alternativas bajo las mismas condiciones aleatorias.

**Ojo, trampa.** No es usar la misma secuencia en todas las réplicas: cada réplica tiene su demanda, y lo que se comparte es entre alternativas. Y no la confundas con las antitéticas, que usan secuencias opuestas.

## Validación y análisis

### Verificación, validación y credibilidad

Un modelo es válido, para un objetivo concreto, cuando hay evidencia suficiente de que representa al sistema con una precisión útil para decidir.

Verificación pregunta si construimos el modelo como lo describimos: si la regla FIFO y los horarios de las cajas están bien programados. Se vio en el eje cuatro. Validación pregunta si el modelo representa razonablemente al sistema real para este objetivo: si la espera y la utilización simuladas se parecen a las observadas. Credibilidad pregunta si los usuarios confían en el estudio y lo entienden: si el encargado reconoce las reglas y acepta las conclusiones.

Se valida a medida que se construye, no al final: definir el objetivo, documentar supuestos, revisar el modelo conceptual con quienes conocen el proceso, probar componentes por separado, comparar con datos reales y registrar limitaciones. Un modelo puede ser válido para estimar la espera y no para diseñar la distribución física del local: la validez está ligada al propósito.

Los métodos se combinan. Los subjetivos usan conocimiento experto: recorrido con expertos, revisión de la animación y juicio de coherencia, como preguntarse si al duplicar la demanda la cola debería crecer. Los objetivos usan datos: comparar media, percentiles y throughput con la realidad, intervalos, pruebas de hipótesis, balances y trazas.

**Lo importante.** Verificar mira hacia adentro, contra lo que describiste; validar mira hacia afuera, contra el sistema real; credibilidad mira a los usuarios. Primero se verifica, después se valida.

**Ojo, trampa.** Es el trío que más cae: lógica bien programada es verificación; parecido con la realidad, validación; confianza del usuario, credibilidad. Son falsas "un modelo válido sirve para cualquier decisión" y "se valida al final". Y el apunte lo dice textual: los métodos subjetivos no son menos serios.

**Si te toca de desarrollo.** Definí los tres conceptos con su pregunta y un ejemplo. Aclará que la validez depende del objetivo. Listá los pasos, remarcando que se valida durante la construcción. Y cerrá con los métodos subjetivos y objetivos.

### Pruebas de hipótesis sobre los resultados

Sirven para decidir si una diferencia entre escenarios es azar de las réplicas o es consistente. Ejemplo: hipótesis nula, dos y tres cajas tienen la misma espera media; alternativa, con tres es menor. Si el intervalo de la diferencia queda por encima de cero, hay evidencia a favor de tres cajas.

Un valor p chico indica que los datos son poco compatibles con la hipótesis nula, pero no dice que sea falsa con un porcentaje exacto ni mide la importancia práctica: ahorrar cero coma cero tres minutos puede ser detectable e irrelevante.

**Lo importante.** No rechazar no es demostrar igualdad, y significativo no es lo mismo que importante.

**Ojo, trampa.** El error que el apunte marca como frecuente: leer "no se rechaza la hipótesis nula" como "los escenarios son iguales". Solo significa que no hubo evidencia suficiente; tal vez faltan réplicas.

### Estructura interna y pruebas de campo

La estructura interna se revisa por dentro. La traza sigue a un cliente desde que llega hasta que sale. El balance controla que las entradas sean iguales a las salidas más las que siguen adentro, y detecta entidades duplicadas o perdidas. El caso extremo prueba cero llegadas o capacidad infinita. Y la sensibilidad lógica aumenta la demanda o reduce recursos para ver que el resultado vaya en la dirección esperada.

Las pruebas de campo comparan indicadores reales y simulados en condiciones equivalentes: no sirve comparar una semana de promociones con un día simulado sin promociones. No hace falta que cada cifra coincida, sino que la diferencia sea aceptable para decidir. En el ejemplo del apunte, el percentil noventa y cinco de la espera da doce minutos en el campo y ocho coma siete en el modelo: el modelo probablemente no representa bien los picos.

Calibrar es ajustar parámetros inciertos dentro de rangos defendibles, documentando cada cambio. No es mover valores hasta que el gráfico quede lindo.

**Lo importante.** Un promedio razonable puede esconder errores, dentro del modelo o en los picos.

**Ojo, trampa.** El apunte llama a la estructura interna validación en el índice y verificación en el título: aprendete qué detecta cada prueba. No confundas la sensibilidad lógica, que mira la dirección del resultado, con el análisis de sensibilidad, que mira si cambia la conclusión. Y calibrar no es ocultar un problema.

### Análisis de sensibilidad

Pregunta: si este supuesto cambia dentro de un rango razonable, ¿cambia mi conclusión? Sirve para saber dónde invertir esfuerzo de medición y qué recomendaciones son robustas. Se prueban factores inciertos con valores bajo, base y alto, con réplicas por escenario.

El gráfico típico es el diagrama tornado: cada factor es una barra que muestra cuánto cambia la espera respecto del caso base. Las barras más largas son los supuestos más influyentes; en el ejemplo, el tiempo de atención y la tasa de arribos, que conviene medir mejor.

**Lo importante.** El tornado te dice qué supuestos pesan más y dónde conviene medir mejor.

**Ojo, trampa.** Barra más larga, factor más influyente, no al revés. Y no se hace con una corrida por escenario.

**Si te toca de desarrollo.** Planteá la pregunta central, explicá para qué sirve, contá los pasos con valores bajo, base y alto y réplicas, y describí el tornado con el ejemplo de atención y arribos.

## Implantación

### De resultado a decisión

"El escenario B es mejor" no alcanza. Una recomendación útil dice qué cambiar, cuánto se espera mejorar, qué cuesta y con qué incertidumbre. Ejemplo: tres cajas bajan la espera media de cinco coma cuatro a tres coma nueve minutos, entonces se abre una tercera caja de dieciocho a veintiuna. Y si la utilización baja, no significa personal ocioso: la capacidad extra evita picos.

La significancia práctica: bajar cero coma un minuto puede ser real y no justificar contratar a alguien; evitar esperas de más de quince minutos en hora pico puede valer mucho aunque el promedio cambie poco.

**Lo importante.** La mejora tiene que importar para el objetivo real, no solo ser detectable.

**Ojo, trampa.** Significancia estadística no es significancia práctica.

### Plan, piloto y seguimiento

La implantación va por etapas, sobre todo si afecta personas, turnos o costos. El plan tiene objetivo, alcance, responsable, recursos, riesgos y criterio de éxito; en el ejemplo, que el percentil noventa y cinco de la espera no pase de diez minutos.

El piloto es una prueba limitada antes de extender la mejora. No reemplaza la simulación, la complementa: la simulación explora alternativas sin riesgo y el piloto verifica la elegida en el contexto real. Lleva alcance acotado, una línea de base medida antes del cambio, las condiciones especiales registradas y la decisión de detener, corregir o escalar definida de antemano. Y no se comparan solo promedios: si en el piloto hubo menos demanda, la mejora parece mayor de lo que es.

Después viene el seguimiento, hasta uno a tres meses más tarde, y ante cambios relevantes hay que revalidar el modelo. Al comunicar, no se oculta la incertidumbre, no se presenta la animación como prueba suficiente y no se prometen resultados exactos. Y se documenta todo.

**Lo importante.** Piloto acotado, con línea de base y criterio fijado antes, y seguimiento después.

**Ojo, trampa.** "El piloto reemplaza a la simulación" es falso. El criterio de éxito se define antes, no después de ver los resultados. Y un modelo validado una vez no queda validado para siempre.

**Si te toca de desarrollo.** Explicá cómo se traduce un resultado en recomendación, con significancia práctica. Nombrá los componentes del plan. Desarrollá el piloto con línea de base y criterio previo. Y cerrá con seguimiento, comunicación y documentación.

## Preguntas tipo multiple choice

Pregunta uno. ¿Qué distribución usás para el tiempo entre llegadas de clientes? Opciones: Poisson, exponencial, uniforme o triangular. La correcta es la exponencial, porque modela el tiempo entre eventos. El distractor tramposo es Poisson, que cuenta llegadas en un intervalo.

Pregunta dos. Una prueba de bondad de ajuste da un valor p de cero coma treinta. Opciones: los datos siguen esa distribución; no hay evidencia suficiente para rechazarla; se rechaza; quedó demostrada. La correcta es la segunda. El distractor tramposo es la primera, que convierte no rechazar en demostrar.

Pregunta tres. Chi cuadrado con cinco intervalos para una normal, con media y desvío estimados. ¿Grados de libertad? Opciones: cuatro, tres, dos o cinco. La correcta es dos: cinco menos uno menos dos. El distractor es cuatro, por olvidarse de los parámetros.

Pregunta cuatro. ¿Qué pasa si los parámetros se estiman con la misma muestra que se prueba? Opciones: la prueba se vuelve más exigente; tiende a aceptar de más; no cambia nada; no se puede usar. La correcta es la segunda. El distractor tramposo es la primera, que dice lo contrario.

Pregunta cinco. En la Kolmogorov-Smirnov de este eje, ¿cómo se obtiene D? Opciones: solo con i sobre n menos la acumulada teórica; con la máxima distancia a los dos lados de cada escalón; con la suma de las diferencias; con observado menos esperado al cuadrado, agrupando. La correcta es la segunda. La primera es la versión del eje dos, y la última es chi cuadrado.

Pregunta seis. ¿En qué caso hace falta warm-up? Opciones: un supermercado simulado desde su apertura real; un hospital de veinticuatro horas; todos los modelos; ninguno, porque las réplicas lo corrigen. La correcta es el hospital, no terminante. El distractor es "todos los modelos": el supermercado que de verdad arranca vacío no lo necesita.

Pregunta siete. Diez réplicas dieron un semiancho de un minuto y querés medio minuto. Opciones: veinte, cuarenta en total, cuarenta adicionales o cien. La correcta es cuarenta en total. Veinte sale de pensar que es lineal, y cuarenta adicionales lo desmiente el apunte.

Pregunta ocho. ¿Qué es la técnica de números aleatorios comunes? Opciones: la misma secuencia en todas las réplicas de un escenario; la misma demanda aleatoria en cada réplica de las alternativas, comparando par por par; secuencias opuestas; una forma de mejorar el sistema real. La correcta es la segunda. La tercera son las antitéticas, y la primera es la más tramposa.

Pregunta nueve. Revisás que la regla FIFO esté bien programada. ¿Qué estás haciendo? Opciones: validación, verificación, credibilidad o calibración. La correcta es verificación. El distractor es validación, que compara con el sistema real.

Pregunta diez. Comparás dos y tres cajas y no se rechaza la hipótesis nula. Opciones: los escenarios son iguales; no hubo evidencia suficiente para detectar una diferencia; conviene dejar dos cajas; el modelo no es válido. La correcta es la segunda. La primera es el error frecuente que marca el apunte.

Pregunta once. En un diagrama tornado, ¿qué indica la barra más larga? Opciones: el factor menos influyente; el supuesto que más cambia el resultado; la variabilidad entre réplicas; el mejor escenario. La correcta es la segunda. El distractor es "el mejor escenario": el tornado ordena supuestos.

Pregunta doce. El modelo se parece a la realidad en la espera media, pero da bastante menos en el percentil noventa y cinco. Opciones: es válido porque la media coincide; probablemente no representa bien los picos; hay que mover parámetros hasta que coincida; no importa. La correcta es la segunda. El distractor tramposo es la tercera: calibrar no es forzar.

Pregunta trece. ¿Qué afirmación sobre el piloto es correcta? Opciones: reemplaza a la simulación; el criterio de éxito se define al terminar; es una prueba limitada, con línea de base y criterio previo; alcanza con comparar promedios. La correcta es la tercera. El distractor más tramposo es la última: con menos demanda, la mejora parece mayor.

## Lo que puede entrar en desarrollo

Tema uno: cómo se elige la distribución de un dato de entrada. Por qué el promedio no alcanza. Cómo se prepara la muestra, con outliers que no siempre se eliminan. Medidas descriptivas e histograma. Prueba de bondad de ajuste, con sus límites. Y la decisión: la que ajusta y tiene sentido, o la empírica.

Tema dos: Kolmogorov-Smirnov contra chi cuadrado. Qué compara cada una, cómo se calcula el estadístico, qué exige cada una, la limitación común y la lectura correcta del resultado.

Tema tres: planeación táctica. Una corrida es un futuro posible. Terminantes y no terminantes, sesgo de inicialización y warm-up. Réplicas independientes, intervalo de confianza y cálculo de réplicas. Y números aleatorios comunes para comparar alternativas.

Tema cuatro: validación. Verificación, validación y credibilidad, con la validez ligada al propósito. Validar durante la construcción. Métodos subjetivos y objetivos. Pruebas de campo y análisis de sensibilidad.

Tema cinco: implantación. Recomendación con significancia práctica. Plan con sus seis componentes. Piloto con línea de base y criterio previo. Seguimiento y comunicación honesta de la incertidumbre.

## Lo mínimo que te tenés que llevar

El promedio solo no alcanza: la dispersión y la forma generan las colas.

Tiempo entre llegadas, exponencial; cantidad de llegadas, Poisson. Con valor más probable, triangular; sin él, uniforme. Fallas, Weibull.

Kolmogorov-Smirnov compara acumuladas a los dos lados del escalón y no agrupa. Chi cuadrado agrupa y pide esperadas de al menos cinco. Con parámetros estimados, las dos aceptan de más.

No rechazar no es demostrar, ni en el ajuste ni al comparar escenarios. Y significativo no es lo mismo que importante.

Una corrida es un futuro posible: réplicas independientes, la fórmula da el total, y la mitad del semiancho pide cuatro veces más réplicas. Warm-up, solo en no terminantes.

Verificar es construir el modelo como se describió; validar, que represente al sistema para ese objetivo; credibilidad, que los usuarios confíen. Y la implantación va por etapas, con piloto.
