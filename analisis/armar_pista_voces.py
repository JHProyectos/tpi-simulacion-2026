"""Arma la pista de voces de un film de Motion, lista para montar sobre el video.

Cada locucion se empareja a un mismo volumen y se ubica en el segundo en que
arranca su escena, asi que la pista dura exactamente lo mismo que el film y se
monta sin mover nada.

    python analisis/armar_pista_voces.py parte-a

Deja videos/audios/<parte>-voces.wav en 48 kHz, mono, PCM de 16 bits.

El mapeo de escena a audio sale de videos/motion/TIEMPOS-PARTE-A.md y de los
STORYBOARD de las otras partes. Si cambia la duracion de una escena hay que
tocar PARTES, que es la unica fuente de verdad de este script.
"""

import json
import os
import re
import subprocess
import tempfile
import sys

FFMPEG = os.path.join(
    r"C:\Users\harbejon\AppData\Local\Microsoft\WinGet\Packages",
    r"Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe",
    r"ffmpeg-9.0.2-full_build\bin\ffmpeg.exe",
)

# Objetivo de volumen. -16 LUFS es el nivel parejo de una voz en video; el pico
# real queda en -1,5 dB para dejar aire a la musica que se monta despues.
OBJETIVO, PICO, RANGO = -16.0, -1.5, 11.0

# Por cada parte: cuanto dura el film y, por escena, en que segundo arranca y
# que locucion suena. Los segundos son desde el arranque del film.
PARTES = {
    "parte-a": {
        "largo": 184.0,
        "tramos": [
            ("abrir", 0.0, "videos/audios/jonatan/jonatan-e00.wav"),
            ("recorrido", 16.0, "videos/audios/editados/juan_escena01.wav"),
            ("pregunta", 45.0, "videos/audios/editados/juan_escena02.wav"),
            ("ficha", 79.0, "videos/audios/jonatan/jonatan-e03.wav"),
            ("ajuste", 151.0, "videos/audios/jonatan/jonatan-e10-ajuste.wav"),
        ],
    },
    # La Parte C es la unica de las tres donde una locucion abarca dos escenas:
    # jonatan-e08.wav dura 45,3 s y cubre "comparar" y "pendiente", que juntas
    # duran 46 s. "cierre" no lleva voz.
    "parte-c": {
        "largo": 191.0,
        "tramos": [
            ("cambios", 0.0, "videos/audios/juan-e07-a.ogg"),
            ("e1", 20.0, "videos/audios/jonatan/jonatan-e07-e1.wav"),
            ("e2", 38.0, "videos/audios/juan-e07-b.ogg"),
            ("e3", 51.0, "videos/audios/jonatan/jonatan-e07-e3.wav"),
            ("e4", 67.0, "videos/audios/juan-e07-c.ogg"),
            ("e5", 78.0, "videos/audios/jonatan/jonatan-e07-e5.wav"),
            ("comparar", 94.0, "videos/audios/jonatan/jonatan-e08.wav"),
            ("respuesta", 140.0, "videos/audios/juan-e09.ogg"),
            ("limites", 166.0, "videos/audios/jonatan/jonatan-e09.wav"),
        ],
    },
}


def correr(args):
    return subprocess.run(args, capture_output=True, text=True, errors="replace").stderr


def emparejar(fuente, destino):
    """Lleva un audio al volumen objetivo, midiendolo primero y corrigiendo despues.

    Las dos pasadas son necesarias: en una sola, loudnorm corrige a ciegas sobre
    lo que va escuchando y el resultado no da el valor pedido.
    """
    err = correr([FFMPEG, "-v", "info", "-i", fuente, "-af",
                  f"loudnorm=I={OBJETIVO}:TP={PICO}:LRA={RANGO}:print_format=json",
                  "-f", "null", "-"])
    medido = json.loads(re.search(r"\{[^{}]*\"input_i\".*?\}", err, re.S).group(0))
    filtro = (f"loudnorm=I={OBJETIVO}:TP={PICO}:LRA={RANGO}"
              f":measured_I={medido['input_i']}:measured_TP={medido['input_tp']}"
              f":measured_LRA={medido['input_lra']}:measured_thresh={medido['input_thresh']}"
              f":offset={medido['target_offset']}:linear=true")
    correr([FFMPEG, "-y", "-v", "error", "-i", fuente, "-af", filtro,
            "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", destino])
    return float(medido["input_i"]), float(medido["input_tp"])


def armar(parte, tmp):
    receta = PARTES[parte]
    emparejados = []
    for escena, inicio, fuente in receta["tramos"]:
        destino = os.path.join(tmp, f"{parte}-{escena}.wav")
        antes, pico = emparejar(fuente, destino)
        print(f"  {escena:<12} {os.path.basename(fuente):<24} "
              f"{antes:>6.1f} -> {OBJETIVO:.1f} LUFS   pico {pico:>5.1f} -> {PICO}")
        emparejados.append((inicio, destino))

    # Cada tramo se retrasa hasta su segundo y se suman. Como no se superponen,
    # sumar es lo mismo que pegarlos, pero sin acumular error de redondeo.
    args = [FFMPEG, "-y", "-v", "error"]
    for _, destino in emparejados:
        args += ["-i", destino]
    retrasos = ";".join(f"[{i}:a]adelay={int(round(inicio * 1000))}:all=1[t{i}]"
                        for i, (inicio, _) in enumerate(emparejados))
    entradas = "".join(f"[t{i}]" for i in range(len(emparejados)))
    salida = f"videos/audios/{parte}-voces.wav"
    filtro = (f"{retrasos};{entradas}amix=inputs={len(emparejados)}"
              f":normalize=0:dropout_transition=0[s];"
              f"[s]apad,atrim=0:{receta['largo']},asetpts=PTS-STARTPTS[out]")
    args += ["-filter_complex", filtro, "-map", "[out]",
             "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", salida]
    err = correr(args)
    if err.strip():
        print("ffmpeg dijo:", err.strip()[:600])
    print(f"\n{salida} · {receta['largo']:.0f} s")
    return salida


if __name__ == "__main__":
    parte = sys.argv[1] if len(sys.argv) > 1 else "parte-a"
    if parte not in PARTES:
        sys.exit(f"No tengo receta para {parte}. Hay para: {', '.join(PARTES)}")
    tmp = os.path.join(tempfile.gettempdir(), "pista-voces")
    os.makedirs(tmp, exist_ok=True)
    armar(parte, tmp)
