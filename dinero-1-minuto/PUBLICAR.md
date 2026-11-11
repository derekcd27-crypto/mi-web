# 💶 Dinero en 1 Minuto — Episodio 1: Ana vs. Luis (interés compuesto)

## Por qué este nicho
Comparé varias guías de nichos para Shorts sin mostrar la cara (2026). **Finanzas personales** es el nicho que casi todas ponen en primer lugar por pago por cada 1.000 visitas, y el texto/gráficos en pantalla funcionan muy bien en este formato. Ojo: en Shorts el pago es bajo en todos los nichos, así que el canal sirve sobre todo para crecer y llevar luego a vídeos largos (que pagan mucho más en finanzas). Las cifras de las guías son estimaciones de blogs de herramientas, no datos oficiales.

Formato que repetimos: **gancho con una paradoja + ejemplo con números concretos + gráfico animado + un truco aplicable + CTA con pregunta**.

## Archivos
| Archivo | Uso |
|---|---|
| `dinero-ana-vs-luis.mp4` | Short final 1080×1920, 54 s, H.264 + AAC, −14 LUFS |
| `miniatura-vertical.jpg` | Fotograma para la portada del Short |
| `miniatura-1280x720.jpg` | Miniatura horizontal |

## Para YouTube Studio
**Título** (elige uno):
1. `Puso 3 veces MENOS dinero… y acabó con MÁS 🤯 #shorts`
2. `12.000 € que se convierten en 141.000 € (interés compuesto)`
3. `Por qué empezar a ahorrar a los 25 vale más que ahorrar el triple`

**Descripción:**
```
Ana invierte 100 €/mes de los 25 a los 35 (12.000 € en total) y lo deja crecer.
Luis invierte 100 €/mes de los 35 a los 65 (36.000 € en total).
Con un 7 % anual de media, a los 65: Ana ≈ 141.304 € · Luis ≈ 122.709 €.
Eso es el interés compuesto: el tiempo pesa más que la cantidad.

Regla del 72: 72 ÷ rentabilidad anual = años para duplicar tu dinero.

⚠️ Ejemplo educativo con una rentabilidad hipotética constante. No es consejo de inversión: las rentabilidades pasadas no garantizan las futuras y no incluye comisiones, impuestos ni inflación.

👇 ¿A qué edad empezaste tú a ahorrar?
🔔 Suscríbete: un truco de dinero cada día.

#finanzaspersonales #interescompuesto #ahorro #inversion #dinero #educacionfinanciera #shorts
```
**Etiquetas:** `interés compuesto, finanzas personales, ahorrar dinero, invertir, regla del 72, educación financiera, cómo ahorrar, dinero, inversión a largo plazo, shorts`

**Configuración:** No es contenido para niños · Categoría *Educación* · Idioma español · Contenido sintético: **No** (gráficos animados evidentes; la voz es sintética pero no imita a nadie real).
**Comentario fijado:** `¿Cuál quieres mañana: regla 50/30/20, fondo de emergencia o cómo funciona la inflación? 👇`

## Cálculo (comprobable)
Aportación de 100 €/mes, interés del 7 % anual capitalizado mensualmente (0,5833 %/mes):
- Ana: aporta 120 meses (25–35) y mantiene hasta los 65 (480 meses) → **141.304 €**
- Luis: aporta 360 meses (35–65) → **122.709 €**
- Regla del 72: 72 / 7 ≈ 10,3 años para duplicar.

## Próximos episodios
| Día | Gancho |
|---|---|
| 2 | “La regla 50/30/20: así reparto mi sueldo” |
| 3 | “Por qué tus 1.000 € valen menos cada año” (inflación) |
| 4 | “El café de 3 € que te cuesta 30.000 €” |
| 5 | “Fondo de emergencia: cuánto necesitas de verdad” |
| 6 | “Tarjeta de crédito: la trampa del pago mínimo” |
| 7 | “Fondos indexados explicados con una pizza” |
| 8 | “Cuánto necesitas para vivir de las rentas (regla del 4 %)” |

## Reproducir el montaje
Mismo proceso que en `../bicho-ganador/build/README.md`: edita `build/guion.json` → `python3 build/tts.py <modelo>` → `node build/render.js full` → `python3 build/musica.py` → mezcla `ffmpeg`.
