# Pipeline de montaje
Requisitos: Python (`kokoro-onnx soundfile numpy pillow`), Node + Playwright (Chromium), ffmpeg.
Modelo de voz: `kokoro-v1.0.onnx` y `voices-v1.0.bin` de las releases de github.com/thewh1teagle/kokoro-onnx (voz `em_alex`, español).

```bash
cd bicho-ganador
python3 build/tts.py /ruta/al/modelo     # -> build/voz.wav + build/timeline.json
node build/render.js stills 1 10 20      # previsualizar fotogramas (carpeta stills/)
node build/render.js full                # -> build/video_mudo.mp4 (30 fps)
cd build && python3 musica.py            # -> musica.wav (música + efectos originales)
ffmpeg -y -i video_mudo.mp4 -i voz.wav -i musica.wav -filter_complex \
"[1:a]aresample=44100,highpass=f=70,acompressor=threshold=-18dB:ratio=3,volume=1.6,apad,asplit=2[vo][sc];[2:a]volume=0.22[m];[m][sc]sidechaincompress=threshold=0.05:ratio=6:release=300[md];[vo][md]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-14:TP=-1.5[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart ../bicho-ganador-escarabajo.mp4
```
