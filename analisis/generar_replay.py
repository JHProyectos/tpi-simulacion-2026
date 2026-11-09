"""Arma la tabla Replay para el modelo visual 3D a partir de salidas.xlsx.

Lee la hoja Salida_Personas (una fila por persona, exportada por el modelo
completo de FlexSim) y calcula, para cada persona, los instantes en que tiene
que caminar y cuánto dura cada paso, más el puesto de caja y el lugar del
mostrador que le tocan.

Modos:
  - Por defecto: repite la corrida tal cual (todo sale de la corrida, no se inventa nada).
  - --cola-minima N: adelanta las llegadas para que siempre haya N personas esperando en la caja.
  - --ritmo S: reconstruye la animación con llegadas cada S segundos de media después de la
    apertura (las duraciones de cada persona se mantienen, pero los instantes cambian). Ya no
    es una repetición de la corrida: es un escenario más exigido, solo para el video.

Uso (desde la raíz del TPI):
    python analisis/generar_replay.py
    python analisis/generar_replay.py --ritmo 3 --cola-max 100
"""
import argparse
import math
import random
import sys

import openpyxl

ANTICIPO_S = 2.0  # la persona sale de la fila unos segundos antes, para llegar justo al puesto
V_CAMINATA = 1.4  # m/s, supuesto: confirmar en la velocidad de las Person (panel Travel)
SEPARACION_S = 1.0
SEP_ENTRE_PERSONAS_S = 1.6  # entre dos salidas seguidas (de la fila a la caja y de la caja a la fila de servicio), vayan a donde vayan  # tiempo mínimo entre que una persona se va de un puesto y llega la siguiente

# Posiciones (X, Y) en metros de FlexSim, de UBICACIONES_3D.md
PTO_FILA_CAJA = (8.33, -13.8)  # frente de Fila_Caja
CAJA_LOC = {1: (6.72, -12.41), 2: (9.80, -12.50)}
PTO_FILA_SERV = (8.25, -10.6)  # frente de Fila_Servicio
MOSTRADOR_LOC = {0: (15.03, -8.75), 1: (2.23, -8.75), 2: (5.33, -8.75), 3: (8.23, -8.75), 4: (11.23, -8.75)}
PREVIO_Y = -9.6  # los Previo_Loc: un paso antes de cada mostrador, en línea recta hacia el servidor (+Y)


def caminata(a, b, v):
    return math.dist(a, b) / v


def recorrido_mostrador(lugar, v):
    """Del frente de Fila_Servicio al Previo_Loc y de ahí al Mostrador_Loc (dos Walk seguidos)."""
    x, y = MOSTRADOR_LOC[lugar]
    previo = (x, PREVIO_Y)
    return caminata(PTO_FILA_SERV, previo, v) + caminata(previo, (x, y), v)


def asignar(intervalos, cantidad):
    """Reparte intervalos (inicio, fin, idx) en `cantidad` lugares, siempre el libre de menor número.

    Devuelve (lugares, maximo_simultaneo). Si en algún instante hay más intervalos que
    lugares, el sobrante se reparte por resto (solo afecta lo visual).
    """
    libre_desde = [0.0] * cantidad
    lugares = {}
    maximo = 0
    activos = []
    for ini, fin, idx in sorted(intervalos):
        activos = [f for f in activos if f > ini]
        activos.append(fin)
        maximo = max(maximo, len(activos))
        elegido = None
        for n in range(cantidad):
            if libre_desde[n] <= ini:
                elegido = n
                break
        if elegido is None:
            elegido = idx % cantidad
        libre_desde[elegido] = fin
        lugares[idx] = elegido + 1
    return lugares, maximo


def rearmar(filas, ritmo, cola_max, n_cajas, n_serv, semilla, inicio=0.0, cola_pre=0, v=V_CAMINATA, cola_serv=0):
    """Reconstruye los instantes de cada persona con llegadas cada `ritmo` s de media.

    - Quienes ya estaban en la fila al abrir la caja conservan su llegada real.
    - Los demás llegan con separación exponencial de media `ritmo`, pero nadie entra a la fila
      si ya hay `cola_max` esperando (el tope es el largo de la fila `Fila_Caja`).
    - Cada caja atiende de a uno, en orden de llegada. El mostrador tiene `n_serv` lugares y
      el puesto vegetariano atiende aparte. Se mantienen las duraciones reales de cada persona.
    """
    rnd = random.Random(semilla)
    apertura = min(d["tInicioVal"] for d in filas)
    cajas_libre = [apertura] * n_cajas
    srv_libre = [0.0] * n_serv
    veg_libre = 0.0
    ult_ir = -1e9
    ult_fin = -1e9
    r = {k: [] for k in ("llegada", "ir_caja", "puesto", "dur_val", "ir_most", "lugar", "dur_srv", "espera_srv")}
    for i, d in enumerate(filas):
        dv = d["tFinVal"] - d["tInicioVal"]
        ds = d["tSalida"] - d["tInicioServicio"]
        if inicio and not r["llegada"]:
            arr = inicio  # la primera persona llega recién en `inicio`
        elif not inicio and d["tLlegada"] <= apertura:
            arr = d["tLlegada"]  # ya estaba en la fila cuando abrió la caja
        else:
            arr = r["llegada"][-1] + rnd.expovariate(1.0 / ritmo)
            if arr < apertura and cola_pre and i >= cola_pre:
                arr = max(arr, r["ir_caja"][i - cola_pre])  # antes de abrir, tope `cola_pre`
            if arr >= apertura and i >= cola_max:
                arr = max(arr, r["ir_caja"][i - cola_max])  # después, la fila tiene lugar para `cola_max`
        k = min(range(n_cajas), key=lambda j: cajas_libre[j])
        w_caja = caminata(PTO_FILA_CAJA, CAJA_LOC[min(k + 1, 2)], v)
        ini_val = max(arr + w_caja, cajas_libre[k] + SEPARACION_S)
        if cola_serv and i >= cola_serv:
            # la fila de servicio tiene lugar para `cola_serv`: nadie termina de validar
            # hasta que el que está `cola_serv` lugares adelante se va al mostrador
            ini_val = max(ini_val, r["ir_most"][i - cola_serv] - dv + 1.0)
        ini_val = max(ini_val, ult_ir + SEP_ENTRE_PERSONAS_S + w_caja, ult_fin + SEP_ENTRE_PERSONAS_S - dv)
        fin_val = ini_val + dv
        ult_ir = ini_val - w_caja
        ult_fin = fin_val
        cajas_libre[k] = fin_val
        a_fila = caminata(CAJA_LOC[min(k + 1, 2)], PTO_FILA_SERV, v)
        if d["EsVeg"]:
            lugar = 0
            w_m = recorrido_mostrador(0, v)
            libre = veg_libre
        else:
            j = min(range(n_serv), key=lambda x: srv_libre[x])
            lugar = j + 1
            w_m = recorrido_mostrador(lugar, v)
            libre = srv_libre[j]
        ini_srv = max(fin_val + a_fila + w_m, libre + SEPARACION_S)
        if d["EsVeg"]:
            veg_libre = ini_srv + ds
        else:
            srv_libre[j] = ini_srv + ds
        r["llegada"].append(arr)
        r["ir_caja"].append(ini_val - w_caja)
        r["puesto"].append(k + 1)
        r["dur_val"].append(dv)
        r["ir_most"].append(ini_srv - w_m)
        r["lugar"].append(lugar)
        r["dur_srv"].append(ds)
        r["espera_srv"].append(ini_srv - (fin_val + a_fila + w_m))
        r.setdefault("fin_srv", []).append(ini_srv + ds)
    r["salida"] = r["fin_srv"]
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default="flexsim/salidas.xlsx")
    ap.add_argument("--salida", default="flexsim/replay.xlsx")
    ap.add_argument("--puestos", type=int, default=0, help="cajas abiertas (0 = el máximo simultáneo observado)")
    ap.add_argument("--servidores", type=int, default=0, help="servidores (0 = el máximo simultáneo observado)")
    ap.add_argument("--max", type=int, default=0, help="solo las primeras N personas (para pruebas); 0 = todas")
    ap.add_argument("--cola-minima", dest="cola_minima", type=int, default=0,
                    help="personas que siempre esperan en la fila de caja (adelanta las llegadas); 0 = tal cual la corrida")
    ap.add_argument("--ritmo", type=float, default=0.0,
                    help="segundos medios entre llegadas después de la apertura (reconstruye los tiempos); 0 = tal cual la corrida")
    ap.add_argument("--cola-max", dest="cola_max", type=int, default=100,
                    help="con --ritmo: tope de personas esperando en la fila de caja (el largo de Fila_Caja)")
    ap.add_argument("--semilla", type=int, default=1, help="con --ritmo: semilla del azar, para repetir el mismo resultado")
    ap.add_argument("--cola-pre", dest="cola_pre", type=int, default=0,
                    help="con --ritmo: tope de personas esperando ANTES de abrir la caja (0 = el mismo --cola-max)")
    ap.add_argument("--cola-serv", dest="cola_serv", type=int, default=0,
                    help="con --ritmo: tope de personas esperando en Fila_Servicio (0 = sin tope)")
    ap.add_argument("--velocidad", type=float, default=V_CAMINATA,
                    help="con --ritmo: velocidad de caminata supuesta (m/s) para calcular cuánto tarda cada recorrido")
    ap.add_argument("--inicio", type=float, default=0.0,
                    help="con --ritmo: instante (s desde las 11:40) en que empiezan a llegar; 900 = 11:55. 0 = las llegadas reales antes de abrir")
    args = ap.parse_args()

    wb = openpyxl.load_workbook(args.entrada, data_only=True)
    ws = wb["Salida_Personas"]
    cab = [c for c in next(ws.iter_rows(min_row=1, max_row=1, values_only=True))]
    filas = []
    for fila in ws.iter_rows(min_row=2, values_only=True):
        d = dict(zip(cab, fila))
        if d.get("Grupo") in (None, "plantilla"):
            continue
        if not d.get("tSalida"):
            continue  # nunca terminó de servirse: no sale en la animación
        filas.append(d)
    filas.sort(key=lambda d: d["tLlegada"])
    if args.max:
        filas = filas[:args.max]

    val = [(d["tInicioVal"], d["tFinVal"], i) for i, d in enumerate(filas)]
    srv = [(d["tInicioServicio"], d["tSalida"], i) for i, d in enumerate(filas) if not d["EsVeg"]]
    n_p = args.puestos or asignar(val, 99)[1]
    n_s = args.servidores or asignar(srv, 99)[1]

    if args.ritmo:
        r = rearmar(filas, args.ritmo, args.cola_max, n_p, n_s, args.semilla, args.inicio, args.cola_pre, args.velocidad, args.cola_serv)
        llegada, ir_caja, puesto_l = r["llegada"], r["ir_caja"], r["puesto"]
        dur_val, ir_most, lugar_l, dur_srv = r["dur_val"], r["ir_most"], r["lugar"], r["dur_srv"]
        ultima_salida = max(r["salida"])
        espera_max = max(r["espera_srv"])
    else:
        puesto, _ = asignar(val, n_p)
        lugar, _ = asignar(srv, n_s)
        ir_caja = [max(d["tLlegada"], d["tInicioVal"] - ANTICIPO_S) for d in filas]
        llegada = [d["tLlegada"] for d in filas]
        if args.cola_minima:
            # Solo para la animación: se adelanta la llegada de cada persona para que, al irse
            # la persona i de la fila de caja, ya estén esperando al menos `cola_minima` personas.
            # El resto de los tiempos (cuándo valida, cuándo la atienden) no cambia.
            k = args.cola_minima
            for i in range(k, len(filas)):
                llegada[i] = max(llegada[i - 1], min(llegada[i], ir_caja[i - k] - 0.5))
        puesto_l = [puesto[i] for i in range(len(filas))]
        dur_val = [d["tFinVal"] - d["tInicioVal"] for d in filas]
        ir_most = [max(d["tFinVal"], d["tInicioServicio"] - ANTICIPO_S) for d in filas]
        lugar_l = [lugar.get(i, 0) for i in range(len(filas))]
        dur_srv = [d["tSalida"] - d["tInicioServicio"] for d in filas]
        ultima_salida = max(d["tSalida"] for d in filas)
        espera_max = max(d["tInicioServicio"] - d["tFinVal"] for d in filas)

    out = openpyxl.Workbook()
    hoja = out.active
    hoja.title = "Replay"
    # Orden de la tabla interna de la Schedule Source: Time, Name, Quantity y después las 7 labels
    cols = ["Time", "Name", "Quantity", "tIrCaja", "Puesto", "tValidacion", "tIrMostrador", "Lugar", "tServicio", "EsVeg"]
    hoja.append(cols)
    for i, d in enumerate(filas):
        hoja.append([
            round(llegada[i], 2),
            f"P{i + 1}",
            1,
            round(ir_caja[i], 2),
            puesto_l[i],
            round(dur_val[i], 2),
            round(ir_most[i], 2),
            lugar_l[i],
            round(dur_srv[i], 2),
            int(d["EsVeg"]),
        ])
    out.save(args.salida)

    # cola máxima y tramos con la fila vacía después de abrir
    apertura = min(d["tInicioVal"] for d in filas)
    ev = sorted([(llegada[i], 1) for i in range(len(filas))] + [(ir_caja[i], -1) for i in range(len(filas))])
    n = maxn = 0
    for _, dlt in ev:
        n += dlt
        maxn = max(maxn, n)
    vacia = 0.0
    n = 0
    ult = 0.0
    for tiempo, dlt in ev:
        if n == 0 and ult >= apertura and tiempo > ult:
            vacia += tiempo - ult
        n += dlt
        ult = tiempo

    print(f"personas: {len(filas)}")
    print(f"cajas usadas: {n_p}; lugares del mostrador: {n_s}")
    print(f"vegetarianos: {sum(1 for d in filas if d['EsVeg'])}")
    print(f"llegadas de {min(llegada):.0f} s a {max(llegada):.0f} s "
          f"(separación media {(max(llegada) - min(llegada)) / max(1, len(llegada) - 1):.2f} s)")
    post = [t for t in llegada if t > apertura]
    if len(post) > 1:
        print(f"después de la apertura ({apertura:.0f} s): {len(post)} llegadas, "
              f"separación media {(post[-1] - post[0]) / (len(post) - 1):.2f} s")
    en_fila = sum(1 for i in range(len(filas)) if llegada[i] <= apertura and ir_caja[i] > apertura - 3)
    n = pre_max = 0
    for tiempo, dlt in ev:
        if tiempo >= apertura:
            break
        n += dlt
        pre_max = max(pre_max, n)
    print(f"máximo esperando antes de abrir: {pre_max} personas")
    print(f"esperando en la caja cuando abre ({apertura:.0f} s): {en_fila} personas")
    print(f"cola máxima en la caja: {maxn} personas; tiempo con la fila vacía después de abrir: {vacia:.0f} s")
    print(f"espera máxima entre la caja y el mostrador: {espera_max:.0f} s")
    print(f"última salida a {ultima_salida:.0f} s")
    print(f"guardado en {args.salida}")


if __name__ == "__main__":
    sys.exit(main())
