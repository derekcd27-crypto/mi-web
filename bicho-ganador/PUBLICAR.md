# 🏆 El Bicho Ganador del Día — Episodio 1: el escarabajo pelotero

## Archivos listos
| Archivo | Uso |
|---|---|
| `bicho-ganador-escarabajo.mp4` | Vídeo final: 1080×1920, 47 s, H.264 + AAC, volumen normalizado a −14 LUFS → **YouTube Short** |
| `miniatura-vertical.jpg` | Fotograma para elegir como portada del Short |
| `miniatura-1280x720.jpg` | Miniatura para usar en el canal / si lo subes también en horizontal |

## Datos para pegar en YouTube Studio

**Título** (elige uno):
1. `El animal MÁS FUERTE del planeta mide 1 cm 🪲 #shorts`
2. `No es la hormiga: este bicho aguanta 1.141 veces su peso 😳`
3. `¿Hormiga, elefante o escarabajo? El más fuerte te va a sorprender`

**Descripción:**
```
Cada día coronamos a un bicho ganador 🏆
Hoy: el escarabajo pelotero de cuernos (Onthophagus taurus). En un estudio de 2010 (Knell & Simmons, Queen Mary University of London) los machos soportaron fuerzas de hasta 1.141 veces su propio peso. Es como si una persona sujetara seis autobuses de dos pisos llenos de gente.

👇 Comenta qué bicho quieres que compita mañana.
🔔 Suscríbete para ver al ganador de cada día.

#animales #insectos #curiosidades #escarabajo #naturaleza #shorts #sabiasque
```

**Etiquetas:** `animal más fuerte, escarabajo pelotero, insectos, curiosidades de animales, sabías que, hormiga, elefante, récords animales, bicho ganador, naturaleza, shorts`

**Configuración:**
- Público: *No, no es contenido creado para niños* (si lo marcas como infantil se desactivan comentarios, y el CTA pide comentar).
- Contenido alterado o sintético: **No** — son ilustraciones animadas evidentes. La voz es sintética (Kokoro TTS) pero no imita a ninguna persona real.
- Categoría: Educación. Idioma: Español.
- Comentario fijado sugerido: `¿Quién gana mañana: mantis religiosa 🦗, camarón mantis 🦐 o tardígrado 🐻? Vota aquí 👇`

## Por qué este formato (investigación)
- La tendencia de “peleas de bichos” en Shorts (vídeos de 10–30 s con insectos en terrarios) es real, pero son **peleas montadas con animales vivos o vídeos generados con IA**: hay denuncias por maltrato animal y desmentidos de verificadores ([Lead Stories, jul. 2026](https://leadstories.com/hoax-alert/2026/07/prebunk-ai-insect-animal-fight-videos-have-bugs-in-them-stop-fakes-from-crawling-through.html)). Copiarlo es arriesgado: posible desmonetización o strikes.
- Lo que sí funciona y es seguro: el formato **“¿quién ganaría?” / récord animal** con datos reales, y los Shorts de curiosidades de animales sin cara, uno de los nichos faceless más recomendados para 2026.
- Por eso el canal enfrenta a candidatos **con datos** y corona a un ganador cada día: mantiene el gancho competitivo sin peleas reales.

### Estructura que repite cada episodio (≈45 s)
1. **Gancho 0–3 s:** afirmación sorprendente + descartar al favorito (“y no, no es la hormiga”).
2. **Cortinilla** “El Bicho Ganador del Día” (1–2 s, para que reconozcan la marca).
3. **Candidatos #1 y #2** con un número cada uno y un “NO GANA”.
4. **Revelación** con redoble, confeti y el nombre del ganador.
5. **El dato** con contador animado y fuente en pantalla.
6. **Comparación humana** (“como sujetar 6 autobuses”).
7. **Ficha del campeón** (3 stats, la última graciosa).
8. **CTA:** “comenta qué bicho compite mañana” → genera comentarios = ideas para el siguiente.

## Próximos 7 episodios (ya pensados)
| Día | Categoría | Candidatos | Ganador |
|---|---|---|---|
| 2 | Golpe más rápido | boxeador, mantis religiosa | **Camarón mantis** |
| 3 | Más resistente | cucaracha, escorpión | **Tardígrado** |
| 4 | Salto más alto (proporción) | canguro, saltamontes | **Pulga / cercópido** |
| 5 | Más venenoso | cobra real, araña viuda negra | **Rana dardo dorada** |
| 6 | Más rápido en picado | guepardo, pez vela | **Halcón peregrino** |
| 7 | Mordida más fuerte | león, tiburón blanco | **Cocodrilo marino** |
| 8 | Mejor cazador (% éxito) | león, tiburón | **Libélula** |

## Cómo hacer el siguiente episodio
Todo el montaje es reproducible en `build/`:
1. Edita `build/guion.json` (texto de cada escena).
2. `python3 build/tts.py <carpeta-modelo-kokoro>` → voz y tiempos.
3. Ajusta ilustraciones/escenas en `build/escena.html`.
4. `node build/render.js full` → vídeo; luego `python3 build/musica.py` y la mezcla `ffmpeg` (ver `build/README.md`).
