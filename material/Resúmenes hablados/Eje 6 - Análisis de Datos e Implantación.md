# Eje 6. Análisis de datos e implantación

Vamos con el eje seis, análisis de datos e implantación. Este repaso dura unos veinticinco minutos. Entra solo la teoría, casi toda en multiple choice, con alguna posible pregunta de desarrollo. El profe sacó de este eje todas las fórmulas de cálculo, las distribuciones una por una, las pruebas de Kolmogorov-Smirnov y chi cuadrado con sus dos ejemplos, y todo lo de FlexSim. Eso no lo estudies: se evalúan los conceptos. Las ideas centrales son cuatro. Una: el promedio solo no alcanza, y la distribución de entrada se elige combinando histograma, medidas descriptivas y prueba de bondad de ajuste. Dos: no rechazar una hipótesis no demuestra nada. Tres: una corrida es un futuro posible, no la respuesta; por eso hay réplicas, intervalos de confianza y, en sistemas no terminantes, warm-up. Cuatro: verificar, validar e implantar son cosas distintas, y la implantación va por etapas, con piloto.

## Datos de entrada

### Qué medir y cómo preparar los datos

Un modelo bien armado da resultados poco confiables si los datos de entrada están mal medidos. El ejemplo del apunte: la atención media es de cinco minutos, y alguien carga todas las atenciones como cinco minutos fijos. Eso esconde la variabilidad, que es lo que genera las colas. Dos sistemas con el mismo promedio se comportan muy distinto si uno varía poco y el otro mucho.

Se miden las variables aleatorias que cambian la congestión: tiempos entre llegadas, de servicio, cantidades, y tiempos de falla y reparación. Y la muestra tiene que ser representativa: distintos momentos, días y condiciones, no diez casos cómodos.

Preparar es unificar unidades, sacar duplicados, revisar valores imposibles como tiempos negativos, ordenar y separar por tipo cuando corresponda: en una mesa de ayuda, pedidos rápidos y lentos mezclados dan una distribución sin sentido.

Un outlier es un dato muy alejado del resto, y no siempre se elimina: puede ser un error de carga o un caso real, como el cliente que tardó muchísimo por un problema con el pago. Con los faltantes, igual: si son pocos, se descartan; si son muchos, se vuelve a medir.

Los atípicos se ven con el boxplot. La caja tiene el cincuenta por ciento central, entre el primer y el tercer cuartil, y la línea de adentro es la mediana. Lo que queda afuera de los bigotes son posibles outliers.

**Lo importante.** La dispersión y la forma importan tanto como el promedio. Y limpiar no es borrar lo que molesta.

**Ojo, trampa.** "Con el tiempo medio alcanza" es falso, y el apunte lo lista como error frecuente. Otros que marca: confundir instantes con duraciones, cargar tiempos absolutos cuando se necesitan tiempos entre eventos y elegir una distribución por costumbre. "Los outliers siempre se eliminan" también es falso.

## Estadística descriptiva

Las medidas descriptivas orientan el ajuste. La media es el promedio y la afectan los extremos. La mediana es el dato central y es más robusta frente a outliers; si media y mediana se parecen, la distribución suele ser simétrica. La moda es el valor más repetido, y puede no existir o haber más de una.

La varianza y el desvío miden cuánto se alejan los datos de la media, y el desvío está en la unidad del dato. Y el coeficiente de variación compara dispersión entre procesos.

Ejemplo del apunte: con cuatro, cinco, cinco, seis y ocho, la media queda un poco por encima de la mediana porque el ocho la empuja.

El histograma da la primera hipótesis de forma, pero la frase del apunte es: el gráfico dice parece, la prueba dice qué tan bien ajusta.

**Lo importante.** Media contra mediana te da una pista de la simetría.

**Ojo, trampa.** La moda puede no ser única. Y si te dicen que la media es más robusta que la mediana frente a outliers, es al revés.

## Bondad de ajuste

### Qué es y cómo se lee

Bondad de ajuste es medir qué tan cerca están los datos reales de una distribución propuesta. En el eje dos se probaba si el generador daba números uniformes; acá, si los datos reales se pueden representar con una distribución candidata.

Dos frases del apunte. La prueba no elige por sí sola: primero se mira el histograma y se entiende el proceso, y después la prueba respalda o cuestiona. Y un valor p mayor que cero coma cero cinco significa que no hay evidencia suficiente para rechazar la distribución, no que quedó demostrada como la única verdadera. Además, la mejor distribución no es la más compleja, sino la que ajusta y tiene sentido para el fenómeno.

**Lo importante.** No rechazar no es demostrar.

**Ojo, trampa.** Cualquier opción que diga que la prueba "demuestra" o "confirma" la distribución es falsa. Lo correcto es "no se rechaza" o "los datos son compatibles".

### La limitación de las pruebas

Las tablas estándar de las pruebas de bondad de ajuste suponen que la distribución está completamente especificada de antemano. En simulación los parámetros se estiman con los mismos datos que después se prueban, y entonces la prueba tiende a aceptar de más. Por eso no conviene apoyarse solo en ella: se combinan tres miradas, histograma, medidas descriptivas y bondad de ajuste.

**Lo importante.** La prueba sola no decide: cuando histograma, medidas descriptivas y bondad de ajuste coinciden, la decisión suele ser sólida.

**Ojo, trampa.** La opción tramposa dice que estimar los parámetros con la muestra vuelve la prueba más exigente. Es al revés: acepta de más.

**Si te toca de desarrollo.** Definí bondad de ajuste y para qué sirve. Aclará que la prueba no elige por sí sola: primero se mira el histograma y se entiende el proceso. Sumá la limitación de los parámetros estimados y las tres miradas. Y cerrá con que no rechazar no demuestra.

## Planeación táctica

Define cuánto simular, desde cuándo medir y cuántas réplicas correr. La frase del apunte: una corrida es un futuro posible, no la respuesta.

### Variabilidad y réplicas

Dos corridas del mismo modelo dan resultados distintos porque las entradas son aleatorias. No es un error del software; el error es mirar una sola corrida y creerla definitiva.

Con n réplicas calculás la media de las réplicas, que es el resultado estimado; el desvío entre réplicas, que dice cuánto cambia una corrida de otra; y el error estándar, que mide la incertidumbre de la media.

Una réplica es una ejecución completa e independiente: reinicia el estado y las estadísticas, y usa aleatorios independientes. Cortar una corrida larga en trozos no es lo mismo, porque los trozos pueden estar correlacionados.

**Lo importante.** Un resultado se informa con varias réplicas independientes, no con una corrida.

**Ojo, trampa.** Con más réplicas baja el error estándar, no la variabilidad del sistema. "Si dos corridas dan distinto, el modelo tiene un error" es falso. Y una corrida larga en trozos no equivale a réplicas.

### Sistemas terminantes, no terminantes y warm-up

El terminante, como un supermercado de ocho a veintiuna, se vacía o se reinicia cada jornada, y la pregunta es cómo fue ese día. El no terminante, como un hospital de veinticuatro horas o un servidor web, no tiene final natural, y la pregunta es cómo funciona a largo plazo.

Si un sistema que normalmente tiene cola arranca vacío, los primeros minutos parecen tranquilos y se subestima la espera: es el sesgo de inicialización. El warm-up es el período inicial en que el modelo corre normalmente pero no se mide. Ejemplo: un hospital simulado treinta días, con dos de warm-up, se mide del día tres al treinta. Para elegirlo, se grafican corridas piloto, promediadas o con media móvil, y se toma el punto donde termina la tendencia de arranque.

**Lo importante.** El warm-up es para sistemas no terminantes, y elimina el sesgo de arrancar vacío.

**Ojo, trampa.** Durante el warm-up el modelo funciona; solo se descartan las estadísticas. En el supermercado simulado desde su apertura real, el apunte dice que no hace falta warm-up. Y warm-up y réplicas resuelven cosas distintas: el sesgo de arranque y la variabilidad entre corridas.

### Cuántas réplicas

No hay un número mágico: depende de la variabilidad y de la precisión que necesitás. Con las réplicas se arma un intervalo de confianza para la media, por ejemplo del noventa y cinco por ciento, y en la práctica el software calcula el intervalo y su semiancho. El apunte recomienda un error relativo de hasta un quince por ciento, aproximadamente.

El procedimiento: fijás la precisión, corrés un piloto de al menos diez réplicas y mirás el semiancho. Si supera lo aceptable, recalculás la cantidad de réplicas necesarias y volvés a correr; si ya cumple, documentás el resultado.

**Lo importante.** La cantidad de réplicas sale de la precisión que necesitás: piloto, semiancho y ajuste.

**Ojo, trampa.** "Siempre alcanza con diez réplicas" es falso: diez es el mínimo del piloto, y después la cantidad se ajusta según la precisión.

**Si te toca de desarrollo.** Arrancá con que una corrida es un futuro posible. Definí réplica y por qué no sirve partir una corrida larga. Contá para qué sirve el intervalo de confianza. Explicá el piloto y cómo se ajusta la cantidad de réplicas hasta la precisión buscada. Y sumá el warm-up.

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

Pregunta uno. Dos cajas tienen la misma atención media, pero en una los tiempos varían mucho más que en la otra. ¿Qué esperás al simularlas? Opciones: que se comporten igual, porque el promedio es el mismo; que se comporten distinto, porque la dispersión y la forma también afectan las colas y las esperas; que la más variable tenga menos cola; que la diferencia sea un error del modelo. La correcta es la segunda, porque la variabilidad es lo que genera las colas. El distractor tramposo es la primera: creer que el promedio alcanza es un error frecuente que marca el apunte.

Pregunta dos. Medís las atenciones de una caja y aparece un cliente que tardó muchísimo por un problema con el pago. ¿Qué hacés con ese dato? Opciones: lo eliminás siempre, porque es un outlier; lo revisás, porque puede ser un error de carga o un caso real que conviene conservar; lo reemplazás por la media; descartás toda la muestra. La correcta es la segunda, porque un outlier no siempre se elimina, y este caso forma parte del proceso. El distractor tramposo es la primera: limpiar no es borrar lo que molesta.

Pregunta tres. Una prueba de bondad de ajuste da un valor p de cero coma treinta. Opciones: los datos siguen esa distribución; no hay evidencia suficiente para rechazarla; se rechaza; quedó demostrada. La correcta es la segunda. El distractor tramposo es la primera, que convierte no rechazar en demostrar.

Pregunta cuatro. ¿Qué pasa si los parámetros se estiman con la misma muestra que se prueba? Opciones: la prueba se vuelve más exigente; tiende a aceptar de más; no cambia nada; no se puede usar. La correcta es la segunda. El distractor tramposo es la primera, que dice lo contrario.

Pregunta cinco. ¿Qué es una réplica? Opciones: cada trozo de una corrida larga; una ejecución completa e independiente, que reinicia el estado y las estadísticas y usa aleatorios independientes; volver a correr el modelo con la misma secuencia de aleatorios; el período inicial que no se mide. La correcta es la segunda, porque cada réplica tiene que representar un futuro posible, independiente de los demás. El distractor tramposo es la primera: los trozos de una corrida larga pueden estar correlacionados, así que no equivalen a réplicas.

Pregunta seis. ¿En qué caso hace falta warm-up? Opciones: un supermercado simulado desde su apertura real; un hospital de veinticuatro horas; todos los modelos; ninguno, porque las réplicas lo corrigen. La correcta es el hospital, no terminante. El distractor es "todos los modelos": el supermercado que de verdad arranca vacío no lo necesita.

Pregunta siete. ¿De qué depende la cantidad de réplicas que hay que correr? Opciones: siempre alcanza con diez; de cuánto varían los resultados y de cuánta precisión necesitás para decidir; solo de la duración de cada corrida; del warm-up elegido. La correcta es la segunda, porque no hay un número mágico universal. El distractor tramposo es la primera: diez es el mínimo del piloto, y después la cantidad se ajusta según el semiancho obtenido.

Pregunta ocho. ¿Qué es la técnica de números aleatorios comunes? Opciones: la misma secuencia en todas las réplicas de un escenario; la misma demanda aleatoria en cada réplica de las alternativas, comparando par por par; secuencias opuestas; una forma de mejorar el sistema real. La correcta es la segunda. La tercera son las antitéticas, y la primera es la más tramposa.

Pregunta nueve. Revisás que la regla FIFO esté bien programada. ¿Qué estás haciendo? Opciones: validación, verificación, credibilidad o calibración. La correcta es verificación. El distractor es validación, que compara con el sistema real.

Pregunta diez. Comparás dos y tres cajas y no se rechaza la hipótesis nula. Opciones: los escenarios son iguales; no hubo evidencia suficiente para detectar una diferencia; conviene dejar dos cajas; el modelo no es válido. La correcta es la segunda. La primera es el error frecuente que marca el apunte.

Pregunta once. En un diagrama tornado, ¿qué indica la barra más larga? Opciones: el factor menos influyente; el supuesto que más cambia el resultado; la variabilidad entre réplicas; el mejor escenario. La correcta es la segunda. El distractor es "el mejor escenario": el tornado ordena supuestos.

Pregunta doce. El modelo se parece a la realidad en la espera media, pero da bastante menos en el percentil noventa y cinco. Opciones: es válido porque la media coincide; probablemente no representa bien los picos; hay que mover parámetros hasta que coincida; no importa. La correcta es la segunda. El distractor tramposo es la tercera: calibrar no es forzar.

Pregunta trece. ¿Qué afirmación sobre el piloto es correcta? Opciones: reemplaza a la simulación; el criterio de éxito se define al terminar; es una prueba limitada, con línea de base y criterio previo; alcanza con comparar promedios. La correcta es la tercera. El distractor más tramposo es la última: con menos demanda, la mejora parece mayor.

## Lo que puede entrar en desarrollo

Tema uno: cómo se elige la distribución de un dato de entrada. Por qué el promedio no alcanza. Cómo se prepara la muestra, con outliers que no siempre se eliminan. Medidas descriptivas e histograma. Prueba de bondad de ajuste, con sus límites. Y la decisión: la que ajusta y tiene sentido para el fenómeno.

Tema dos: planeación táctica. Una corrida es un futuro posible. Terminantes y no terminantes, sesgo de inicialización y warm-up. Réplicas independientes, intervalo de confianza y cómo se decide cuántas réplicas correr. Y números aleatorios comunes para comparar alternativas.

Tema tres: validación. Verificación, validación y credibilidad, con la validez ligada al propósito. Validar durante la construcción. Métodos subjetivos y objetivos. Pruebas de campo y análisis de sensibilidad.

Tema cuatro: implantación. Recomendación con significancia práctica. Plan con sus seis componentes. Piloto con línea de base y criterio previo. Seguimiento y comunicación honesta de la incertidumbre.

## Lo mínimo que te tenés que llevar

El promedio solo no alcanza: la dispersión y la forma generan las colas.

La prueba de bondad de ajuste no elige sola: se combinan histograma, medidas descriptivas y prueba. Y con parámetros estimados con la misma muestra, la prueba acepta de más.

No rechazar no es demostrar, ni en el ajuste ni al comparar escenarios. Y significativo no es lo mismo que importante.

Una corrida es un futuro posible: réplicas independientes, tantas como pida la precisión que necesitás. Warm-up, solo en no terminantes.

Verificar es construir el modelo como se describió; validar, que represente al sistema para ese objetivo; credibilidad, que los usuarios confíen. Y la implantación va por etapas, con piloto.
