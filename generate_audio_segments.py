from gtts import gTTS
from mutagen.mp3 import MP3
import json

segments = {
    "title": "En este video explicamos el área bajo la curva y su relación con la integral.",
    "intro_func": "Primero mostramos la función f de x igual a media por x al cuadrado.",
    "riemann_4": "Luego aproximamos el área entre cero y cuatro con sumas de Riemann, usando cuatro rectángulos.",
    "riemann_8": "Aumentamos el número de rectángulos para mejorar la aproximación.",
    "limit": "Al aumentar el número de rectángulos la aproximación converge a la integral definida.",
    "integral": "La integral de cero a cuatro de un medio por x al cuadrado es treinta y dos tercios, aproximadamente diez coma sesenta y siete.",
    "explanation": "La integral mide el área bajo la curva entre a y b. Las sumas de Riemann usan rectángulos para aproximar esa área.",
    "bye": "Fin. Prueba este ejemplo con otras funciones y límites."
}

durations = {}

for key, text in segments.items():
    filename = f"audio_{key}.mp3"
    tts = gTTS(text, lang="es")
    tts.save(filename)
    audio = MP3(filename)
    durations[key] = {
        "file": filename,
        "duration": float(audio.info.length)
    }
    print(f"Generated {filename} ({durations[key]['duration']:.2f}s)")

with open("audio_segments.json", "w", encoding="utf-8") as f:
    json.dump(durations, f, indent=2, ensure_ascii=False)

print("Wrote audio_segments.json with durations.")
