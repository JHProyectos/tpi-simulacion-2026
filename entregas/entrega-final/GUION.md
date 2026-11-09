# Guion del video: entrega final del TPI

[TOC]

Duración objetivo: **12 a 13 minutos** (el máximo es 15). Los apartados siguen el orden que pide la consigna.

## Cómo leer este guion

- **🎥 Pantalla:** lo que se ve (captura de OBS, diapositiva o animación).
- **🗣️ Juan / Jonatan:** quién habla y qué dice, palabra por palabra.
- **Las frases en negrita dentro de la locución aparecen escritas en el video en el momento en que se dicen** (Claude Motion). El resto se dice sin texto en pantalla.
- Lo que está entre **[CORCHETES]** se completa cuando estén los resultados de FlexSim.

**Reparto de las voces:** cada orador se queda con bloques enteros, así cada uno graba sus partes de corrido y el cambio de voz marca el cambio de tema.

| Escena | Orador | Duración aprox. |
|---|---|---|
| 0 Apertura | Juan y Jonatan | 0:15 |
| 1 Organización | Juan | 0:45 |
| 2 Problemática | Juan | 0:45 |
| 3 Escenario base | Jonatan | 1:30 |
| 4 Render 3D | Jonatan | 0:30 |
| 5 Ejecución base | Jonatan | 1:30 |
| 6 Resultados base | Juan | 1:45 |
| 7 Alternativos | Juan y Jonatan, alternando | 3:00 |
| 8 Comparación | Jonatan | 1:15 |
| 9 Conclusión | Juan y cierre de Jonatan | 1:15 |

Queda en unos 6 minutos de locución para cada uno. A unas 130 palabras por minuto, el total ronda los **12 minutos**, y queda un minuto para pausas y transiciones.

**Reglas para las frases que aparecen en pantalla:**

- Son **2 o 3 por escena**, no más. Si todo aparece, nada se destaca.
- Aparecen **exactamente cuando se dicen**: en Claude Motion, la palabra arranca con la primera sílaba. Pueden salir palabra por palabra o la frase entera de una vez.
- Se quedan **2 o 3 segundos** después de dichas y se van antes de la siguiente.
- Los números importantes (minutos, porcentajes, personas) siempre van en pantalla: son lo que el profesor tiene que retener.
- La frase en pantalla puede ser **más corta** que la dicha. Si se dice «la espera media en la fila de caja es de 8 minutos», en pantalla alcanza con «Espera en caja: 8 min». En el guion, la negrita marca la parte que aparece.

> **Regla de la consigna:** no se nombra la organización. En la locución se dice siempre «un comedor universitario» o «el comedor». Antes de grabar, revisá que no se vea el nombre en el modelo de FlexSim (títulos, tablas, nombre del archivo en la barra de la ventana) ni en las diapositivas.

## Material grabado y de dónde salen los números

Las tomas están en [`flexsim/LISTA_DE_TOMAS.md`](../../flexsim/LISTA_DE_TOMAS.md), y las grabaciones, en `videos/una-caja.mkv` (escenario base) y `videos/dos-cajas.mkv` (E1).

> **Las grabaciones son una animación ilustrativa**, hecha con un replay de un escenario más exigente que el medido: la cola llega a 100 personas y la caja abre a las 12:01:54. **Ningún número que se diga en voz alta sale de la animación.** Los números de la locución salen del modelo medido ([`validacion_E0_Pico.md`](../../flexsim/validacion_E0_Pico.md)) y, para los escenarios alternativos, del Experimenter.
>
> Mientras se ve la animación, va un pie fijo y chico abajo: «Animación ilustrativa de un escenario más exigente que el medido».

| Escena | Tomas |
|---|---|
| 1 Organización | Toma 1 de `una-caja.mkv` (plano general, acelerada) |
| 2 Problemática | Final de la toma 1: la fila armada antes de abrir |
| 4 Render 3D | Toma 5 (una persona camino a la salida) y planos de la toma 1 |
| 5 Ejecución base | Tomas 2, 3 y 4 de `una-caja.mkv` |
| 7, E1 | Tomas 2 y 3 de `dos-cajas.mkv` y la fila de servicio llena (bloque 5 de la lista) |
| 7, E2 a E5 | **Faltan tomas.** Se cubren con los gráficos de cada escenario o se graban con el mismo encuadre |
| 9 Conclusión | Toma 6 de las dos grabaciones, lado a lado |

> **Pendiente:** la lista de tomas habla de 4 puestos en el mostrador en la toma 4 y de 3 en el bloque 3, y el guion dice 3 personas en el escenario base. Confirmen la cifra y usen la misma en la locución, en los textos y en la lista. Además, en el bloque 1 de la lista, el texto «Comedor Universitario UNC» hay que cambiarlo por «Un comedor universitario».

---

# Escena 0 · Apertura (0:00 – 0:15)

- **🎥 Pantalla:** placa con fondo liso y los apellidos del grupo. Sobre el final, fundido a una foto o al plano 3D del comedor.

**🗣️ Juan:** «Hola. Somos [NOMBRE 1]…»

**🗣️ Jonatan:** «…y [NOMBRE 2]. En este video presentamos nuestro trabajo integrador de Simulación: **la fila de un comedor universitario, modelada en FlexSim**.»

---

# Escena 1 · Presentación de la organización (0:15 – 1:00)

- **🎥 Pantalla:** foto del comedor (sin carteles ni logos) o el plano 3D en vista aérea.

**🗣️ Juan:**

«La organización es un **comedor universitario** que sirve almuerzos subsidiados a estudiantes, becarios y personal. El almuerzo **se reserva antes por internet**.

Al llegar, cada persona hace una fila, **valida su reserva presentando el DNI** y pasa a otra fila para **retirar la bandeja en el mostrador**.

Simulamos ese recorrido: desde que la persona llega a la fila hasta que retira la bandeja. Lo que pasa después, en el salón, queda fuera del estudio.»

---

# Escena 2 · Problemática y objetivo (1:00 – 1:45)

- **🎥 Pantalla:** captura de la cola previa a las 11:59 en FlexSim. Cuando se lee la pregunta, la imagen se oscurece y la pregunta queda sola en el centro.

**🗣️ Juan:**

«En el horario pico se forma una fila larga antes de que abra la atención: **entre 60 y 70 personas**. Hay dos puestos de validación, pero **habitualmente funciona uno solo**.

La pregunta que nos hicimos es esta: **¿qué combinación de puestos de validación y personas en el servicio reduce el tiempo total en el pico, sin trasladar la cola al mostrador?**

La trampa es que si agilizamos la validación, la cola puede simplemente **correrse al mostrador**. Por eso medimos el **tiempo total**, y no solo la espera en la caja.»

> La pregunta es la frase más larga que aparece en todo el video: que se arme palabra por palabra mientras Juan la lee y quede fija unos 4 segundos. Si el grupo reformula la pregunta (D05), cambiá la locución y el texto juntos.

---

# Escena 3 · Escenario base (1:45 – 3:15)

- **🎥 Pantalla:** el Process Flow de FlexSim, con zoom a cada bloque a medida que se nombra. Después, la tabla `Escenarios` con la fila de E0 resaltada.

**🗣️ Jonatan:**

«Este es el **escenario base**, la situación de partida contra la que comparamos todo.

Las personas empiezan a llegar a las 11:40 y forman la fila antes de la **apertura, alrededor de las 12**: la caja casi nunca abre en punto, y esa demora también sale de los registros. Las llegadas salen de los **registros reales de reservas**, por franjas de diez minutos y por tipo de cliente: estudiantes, becarios y personal.

Hay **un solo puesto de validación**. Cada persona presenta un DNI por cada ración que retira, y cada DNI lleva **unos cuatro segundos**, un tiempo que derivamos de los registros reales del puesto.

Después pasa a la fila del servicio, donde **[3] personas arman las bandejas**, a **unos 17 segundos por ración**. La fila del servicio tiene un espacio limitado: si se llena, la caja se frena.

El caso es **mixto**: las llegadas y la validación vienen de datos reales, y lo que no pudimos medir, como el tiempo de servicio o cuántas raciones retira cada persona, lo generamos y lo declaramos como supuesto.»

> Esta escena tiene más negritas que las demás porque presenta los recursos y los tiempos del modelo. Una opción: que vayan apareciendo como una ficha que se arma en un costado y queda completa hasta el final de la escena.

---

# Escena 4 · Renderizado 3D (3:15 – 3:45) · opcional

- **🎥 Pantalla:** recorrido lento de cámara por la escena 3D: entrada, fila de caja, puesto, fila de servicio y mostrador. Se puede armar con planos de la toma 1 y cerrar con la toma 5, siguiendo a una persona que sale con la bandeja.

**🗣️ Jonatan:** «Esta es la representación tridimensional del comedor. Acá se forma la **fila de caja**, este es el **puesto de validación**, y por acá la gente avanza hacia el **mostrador**.»

> Acá las palabras en negrita funcionan mejor como etiquetas que aparecen **sobre cada sector** en el momento en que se nombran. Si el video se pasa de tiempo, esta es la primera escena para recortar: es opcional.

---

# Escena 5 · Ejecución del escenario base (3:45 – 5:15)

- **🎥 Pantalla:** `una-caja.mkv`, con el pie de animación ilustrativa. Tres momentos clave, cada uno con un zoom:
  1. Toma 2: abre la caja y la fila arranca.
  2. Toma 3: plano general alejándose (efecto dron).
  3. Toma 4: el mostrador sirviendo en paralelo, con la fila de servicio llena.

**🗣️ Jonatan:**

«Corremos el escenario base en el día pico. Antes de que abra la caja ya se juntan **más de 60 personas** esperando.

Abre la caja y la fila empieza a bajar rápido: con cuatro segundos por DNI, **la validación no es el problema**. La caja trabaja apenas a un 60 % de su capacidad.

Miren lo que pasa en la fila del servicio: llega a **más de 130 personas**. **El cuello de botella no está en la caja, está en el mostrador.**»

> Los números dichos («más de 60», «más de 130», «un 60 %») son de la corrida medida (cola máxima en caja de 66, cola máxima en servicio de 131, caja al 62,6 %), **no** de lo que se ve en la animación, que es más exigente. Si con las réplicas cambian, ajustalos.
>
> «El cuello de botella no está en la caja, está en el mostrador» es la idea central del video: dale el texto más grande de todos, y en la edición hacé una pausa de un segundo antes de que Jonatan la diga. La locución va aparte de la grabación, así que podés acelerar o pausar la animación sin que la voz se corte.

---

# Escena 6 · Resultados del escenario base (5:15 – 7:00)

- **🎥 Pantalla:** gráficos del Dashboard de FlexSim o del Experimenter: longitud de cola en el tiempo para las dos filas, histograma del tiempo total en el sistema y utilización de la caja y del servicio. Cada gráfico aparece cuando se habla de él.

**🗣️ Juan:**

«Estos son los resultados del escenario base, con **[30] réplicas** del día pico.

Quien llega antes de la apertura espera **unos 13 minutos** en la cola previa. Una vez abierta la caja, la espera ahí es **de menos de un minuto**. Donde se espera es en el mostrador: **casi 8 minutos** de media.

La caja trabaja al **63 %** de su capacidad, mientras que el servicio está al **94 %**: está prácticamente saturado.

El **tiempo total**, desde que la persona llega hasta que tiene la bandeja, es de **[X] minutos**, con un intervalo de confianza del 95 % de [X a X].

Para validar el modelo, comparamos las raciones validadas cada diez minutos contra los registros reales: la curva coincide, con una **correlación de 0,95**, y el total del día difiere en **menos de un 2 %**. La cola máxima de la caja, 66 personas, también cae en el rango que se observa en el comedor.»

> En pantalla, cada número aparece con su etiqueta corta: «Cola previa: 13 min», «Caja: < 1 min», «Mostrador: 8 min», «Caja: 63 %», «Servicio: 94 %», «Correlación: 0,95».
>
> **Atención:** estos valores son de **una sola corrida** de FlexSim ([`validacion_E0_Pico.md`](../../flexsim/validacion_E0_Pico.md)), redondeados. Cuando estén las réplicas, reemplazalos por las medias. No muestren la espera *máxima* en el servicio: la validación la marca para revisar (86 min en FlexSim contra unos 17 en la réplica de Python). El tiempo total todavía no está calculado.
>
> El gráfico de la curva real contra el modelo ya está armado en la validación: se puede mostrar acá tal cual.

---

# Escena 7 · Escenarios alternativos (7:00 – 10:00)

Cada escenario sigue la misma estructura de unos 30 segundos: el nombre del escenario aparece en pantalla, un fragmento corto de la corrida y uno o dos números. Repetir el formato ayuda a que el espectador compare solo. Los oradores **se alternan por escenario**: el cambio de voz marca el cambio de escenario.

- **🎥 Pantalla:** 5 a 10 s de la corrida acelerada de cada escenario → gráfico de colas de ese escenario.
  - **E1:** tomas 2 y 3 de `dos-cajas.mkv`, con el mismo encuadre que en la escena 5 para que se compare, y después la fila de servicio llena (bloque 5 de la lista de tomas).
  - **E2 a E5:** todavía no hay grabación. Dos opciones: grabarlos con el mismo encuadre de la toma 3, o mostrar solo el gráfico de cada escenario. Si solo hay gráficos, conviene darle a cada escenario el mismo tipo de gráfico, para que la repetición del formato se mantenga.

**🗣️ Juan:** «Ahora probamos cinco cambios sobre el escenario base. En cada uno **modificamos una sola cosa**, así sabemos qué causa la diferencia.»

**🗣️ Jonatan (E1):** «**Escenario 1: dos puestos de caja todo el turno.** La espera en caja baja a **[X] minutos**, pero el tiempo total [casi no cambia]: la gente llega antes al mostrador y **espera ahí**.»

**🗣️ Juan (E2):** «**Escenario 2: el segundo puesto, solo en el pico**, de 12:00 a 13:30. [Resultado: **[X] minutos**]. [Comentario sobre si compensa el horario parcial].»

**🗣️ Jonatan (E3):** «**Escenario 3: validación con código QR**, que lleva un 60 % del tiempo del DNI. [Resultado]. Como la caja no era el cuello de botella, [**la mejora es chica**].»

**🗣️ Juan (E4):** «**Escenario 4: un puesto de caja y cuatro personas sirviendo.** Acá el cambio es grande: el tiempo total baja a **[X] minutos** y la cola del servicio a **[X] personas**.»

**🗣️ Jonatan (E5):** «**Escenario 5: dos puestos y cuatro personas sirviendo.** [Resultado]. [¿Mejora sobre E4 o **el segundo puesto no agrega nada**?]»

> El nombre de cada escenario aparece como título arriba a la izquierda y se queda mientras dura su corrida. Si en el análisis de sensibilidad del tiempo de servicio (S15) los resultados cambian mucho, Jonatan lo menciona en una frase al final: «Si el servicio fuera más rápido, de 10 a 12 segundos por ración, [qué cambia].»

---

# Escena 8 · Comparación de resultados (10:00 – 11:15)

- **🎥 Pantalla:** una sola tabla o un gráfico de barras con los seis escenarios. Recomendado: barras del tiempo total medio con sus intervalos de confianza, ordenadas de mejor a peor. El escenario base y el mejor, resaltados con colores distintos; los demás, en gris.

**🗣️ Jonatan:**

«Pongamos todo junto. [Describir el gráfico]: los escenarios que **solo mejoran la caja**, E1, E2 y E3, quedan [prácticamente igual que el base]. Los que **refuerzan el servicio**, E4 y E5, bajan el tiempo total **de [X] a [X] minutos**.

[Si los intervalos de confianza de E4 y E5 se superponen:] Entre E4 y E5 la diferencia no es significativa: **abrir el segundo puesto no suma** cuando el mostrador ya alcanza.»

Tabla para completar (la misma va en el PDF):

| Escenario | Espera en caja (min) | Cola máx. caja | Cola máx. servicio | Tiempo total (min) | Utilización del servicio (%) |
|---|---|---|---|---|---|
| E0 base | [ ] | [ ] | [ ] | [ ] | [ ] |
| E1 | [ ] | [ ] | [ ] | [ ] | [ ] |
| E2 | [ ] | [ ] | [ ] | [ ] | [ ] |
| E3 | [ ] | [ ] | [ ] | [ ] | [ ] |
| E4 | [ ] | [ ] | [ ] | [ ] | [ ] |
| E5 | [ ] | [ ] | [ ] | [ ] | [ ] |

---

# Escena 9 · Conclusión (11:15 – 12:40)

- **🎥 Pantalla:** vuelve la pregunta de la escena 2, achicada arriba; la respuesta se escribe debajo mientras Juan la dice. Para el cierre de Jonatan, la toma 6 de las dos grabaciones lado a lado: la sala vaciándose. Las horas de salida de la animación (14:01 y 13:23) no se dicen ni se escriben: son del escenario exigente, no del medido.

**🗣️ Juan:**

«Volvamos a la pregunta del principio. [Respuesta: por ejemplo, **reforzar el servicio, no la caja**]. Lo que muestra la simulación es que [el cuello de botella está en el mostrador]: **mejorar la validación sola solo traslada la cola**.

Nuestra recomendación es **[configuración recomendada]**, que baja el tiempo total **de [X] a [X] minutos** [con el costo de una persona más en el turno pico].»

**🗣️ Jonatan:**

«Como límite del estudio: el tiempo de servicio por ración no lo pudimos cronometrar; es un supuesto, y el siguiente paso sería medirlo en el comedor. Gracias por mirar.»

- **Cierre (12:40 – 12:50):** placa final con los apellidos y «Simulación · 2026». Sin música fuerte.

---

# Tips para grabar y editar

## Antes de grabar

- **Grabá la voz primero y la pantalla después.** Con la locución ya grabada sabés cuánto tiene que durar cada fragmento de FlexSim, y no te trabás leyendo mientras manejás el mouse.
- **Leé el guion en voz alta una vez cronometrando.** Si pasa de 12 minutos sin pausas, recortá frases antes de grabar, no en la edición.
- **Escribí como hablás.** Frases cortas, una idea por frase. Si una oración necesita una coma en el medio para respirar, partila en dos.
- **Dos voces, dos lugares:** si cada orador graba en su casa, usen el mismo tipo de micrófono y la misma distancia, y procesen las dos voces con los mismos ajustes en Audify para que no suene como dos videos pegados. Cada uno graba solo sus bloques de la tabla de reparto.
- **Dejá todos los resultados listos antes de grabar la pantalla:** el Dashboard armado y los gráficos exportados. No hay que buscar nada en vivo.

## Configuración de OBS

- **Resolución y cuadros:** 1920 × 1080 a 30 fps alcanzan. FlexSim no necesita 60 fps.
- **Formato:** grabá en **MKV** (si se corta, no perdés el archivo) y convertilo a MP4 desde *Archivo → Remux*.
- **Calidad:** en *Salida*, modo simple, calidad «Alta» o «Indistinguible». Encoder por hardware (NVENC o QuickSync) si tenés, para que FlexSim no se trabe mientras graba.
- **Una escena de OBS por tipo de toma:** pantalla completa de FlexSim, solo el Process Flow, solo la vista 3D. Así cambiás sin mover ventanas.
- **Escala de pantalla:** si trabajás con la escala de Windows al 125 % o 150 %, bajala al 100 % para grabar o agrandá las fuentes de FlexSim. El texto chico de los Process Flow no se lee en un video.
- **Grabá la pantalla sin audio** (o con el micrófono silenciado) si la voz va aparte. Evita ecos y clics de teclado.

## Al grabar FlexSim

- **Limpiá la pantalla:** cerrá las notificaciones (modo «No molestar» de Windows), el chat y las pestañas del navegador. Que no aparezcan el nombre de la organización, tu mail del trabajo ni rutas de OneDrive con el nombre de la empresa.
- **Mové el mouse despacio** y dejalo quieto cuando no señalás nada. Un cursor que da vueltas distrae.
- **Usá la velocidad de simulación a tu favor:** corré rápido las partes aburridas y bajá la velocidad en los momentos clave (apertura de las 12:00, pico de la cola). En la edición podés acelerar más.
- **Grabá tomas largas y de sobra.** Es más fácil recortar que volver a abrir FlexSim, configurar el escenario y repetir.
- **Fijá la semilla** del generador para la corrida que grabes, así la corrida del video coincide con los números que mostrás.
- **Hacé zoom en la edición, no en FlexSim:** grabá la vista amplia y acercá en Claude Motion a la zona que importa. Queda más prolijo que acercar en vivo.

## Locución

- **Micrófono:** cualquier auricular con micrófono anda mejor que el de la notebook. A un puño de distancia de la boca, un poco al costado para que no pegue el aire de la «p».
- **Ambiente:** una habitación con ropa, cortinas o un placard abierto absorbe el eco. Evitá cocinas y paredes desnudas.
- **Grabá 10 segundos de silencio** al principio de cada sesión. Es la muestra que usa la reducción de ruido.
- **Si te equivocás, no cortes:** hacé una pausa de dos segundos y repetí la frase entera desde el principio. En la edición se ve clarito dónde cortar.
- **Grabá por escena,** un archivo por bloque de cada orador (por ejemplo `Juan-escena2.wav`). Si una escena sale mal, rehacés solo esa. En la escena 7, cada orador graba sus escenarios por separado.
- **Sonreí al hablar.** Se escucha. Y hablá un poco más lento de lo que te parece natural.
- **Mismo lugar y mismo micrófono para todo,** así las escenas suenan iguales.

## Corrección de voz con Audify

Orden recomendado (cada paso funciona mejor sobre el anterior):

1. **Reducción de ruido**, con la muestra de silencio. Suave: si te pasás, la voz suena metálica o «bajo el agua».
2. **Recorte de muletillas y silencios largos.** Revisá a mano lo que corta automáticamente: a veces se lleva el principio de una palabra.
3. **De-esser** para las eses. También suave: con demasiado, suena a ceceo.
4. **Normalización** a un volumen parejo para todas las escenas (si da la opción, alrededor de -16 LUFS, el estándar de video en internet).

Hacé todo esto **antes** de llevar la voz a la edición, así sincronizás las letras sobre el audio final.

## Edición en Claude Motion

- **La voz manda:** armá primero la pista de la locución completa y después acomodá el video de FlexSim debajo.
- **Frases que aparecen al decirlas:** sincronizalas sobre la forma de onda de la voz ya procesada, con la primera sílaba. Máximo 6 a 8 palabras en pantalla a la vez; si la frase dicha es larga, mostrá solo la parte en negrita del guion.
- **Que cada frase dure** lo suficiente para leerla dos veces (unos 2 a 3 segundos después de dicha) y que salga antes de que aparezca la siguiente.
- **Una sola tipografía y dos colores:** uno neutro para todo y uno de acento para lo que hay que mirar (el escenario mejor, el número clave). Usá el mismo color de acento en todo el video.
- **Transiciones:** cortes directos o fundidos cortos. Nada de efectos de giro o barrido.
- **Música:** opcional, instrumental y muy baja debajo de la voz (unos 20 a 25 dB menos). Si hay duda, sin música. Usá música libre de derechos.
- **Subtítulos:** suman si el profesor ve el video sin audio o acelerado. Si Claude Motion los genera desde la locución, revisalos.

## Antes de entregar

- **Mirá el video completo de una vez,** sin pausas, como lo vería el profesor. Anotá dónde te aburrís: eso se recorta.
- **Chequeá el tiempo:** 12 a 13 minutos. Nunca más de 15.
- **Buscá el nombre de la organización** en todo el video, cuadro por cuadro en las capturas de FlexSim.
- **Escuchá con auriculares y con parlantes:** detecta ruidos y volúmenes que con uno solo no se notan.
- **Exportá en MP4 (H.264), 1080p.** Probá que el archivo se abra en otra computadora antes de subirlo al campus, y fijate el límite de tamaño del campus: si lo pasa, subilo a Drive y entregá el enlace.

---

# Checklist de grabación

- [ ] Pregunta de estudio cerrada (D05) y placa de la escena 2 actualizada
- [ ] Resultados de E0 a E5 con réplicas y la tabla de la escena 8 completa
- [ ] Gráficos exportados: colas en el tiempo, tiempo total, utilización y comparación
- [ ] Nombre de la organización fuera del modelo y de las capturas
- [ ] Locución grabada por escena y procesada en Audify
- [ ] Tomas de FlexSim grabadas en OBS (escenas 3, 4, 5, 6 y 7)
- [ ] Edición, textos y subtítulos en Claude Motion
- [ ] Revisión completa, duración entre 12 y 13 minutos
- [ ] MP4 exportado y probado en otra computadora
