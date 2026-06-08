---
name: sustentar
description: Prepara al tesista para la defensa oral de su tesis. Estructura la presentación, anticipa preguntas del jurado, ensaya respuestas y genera la guía de diapositivas. Activar cuando el usuario diga "me voy a sustentar", "prepárame para la defensa", "qué me pueden preguntar", "cómo presento mi tesis", "ayúdame con la exposición", "tengo mi sustentación en X días".
argument-hint: "[fecha de sustentación o tiempo disponible]"
allowed-tools: Read,Write,Edit,Glob
---

# Sustentar — Preparación para la Defensa Oral

Prepara al tesista para defender su investigación con claridad, seguridad y solidez argumentativa.

---

## Instrucciones

### Paso 1: Evaluación del estado

Leer `quality_reports/pipeline_state.json` y las secciones de `tesis/secciones/`. Verificar:
- ¿La tesis está completa o casi completa?
- ¿Hay brechas críticas de coherencia pendientes? (leer último reporte de coherencia)
- ¿Cuánto tiempo tiene el tesista para prepararse?

Si hay brechas críticas no resueltas: señalarlas antes de continuar — la defensa mal preparada expone esas debilidades.

### Paso 2: Estructura de la defensa (20-30 minutos típicos)

Producir `tesis/presentacion/estructura_defensa.md`:

```
BLOQUE 1 — APERTURA (2-3 minutos)
  - Saludo y presentación del tesista
  - Título de la investigación
  - Una oración: "Esta investigación busca [objetivo general en lenguaje simple]"
  - Por qué importa este tema (gancho de relevancia)

BLOQUE 2 — PROBLEMA Y OBJETIVOS (3-4 minutos)
  - Problema central (sin tecnicismos — el jurado ya leyó la tesis)
  - Objetivos (general + específicos en una diapositiva)
  - Hipótesis si aplica

BLOQUE 3 — METODOLOGÍA (3-4 minutos)
  - Diseño, tipo, nivel, enfoque (solo lo más relevante)
  - Población y muestra (con justificación breve)
  - Instrumento principal y cómo se aplicó

BLOQUE 4 — RESULTADOS (5-7 minutos)
  - Un resultado por objetivo específico
  - Apoyarse en tablas/figuras del documento
  - Enunciar con claridad si se confirma/rechaza la hipótesis (si aplica)

BLOQUE 5 — DISCUSIÓN (3-4 minutos)
  - Los 2-3 hallazgos más importantes confrontados con antecedentes
  - Qué confirma y qué difiere de la literatura existente

BLOQUE 6 — CONCLUSIONES Y RECOMENDACIONES (3-4 minutos)
  - Una conclusión por objetivo (breve)
  - Conclusión general
  - 2-3 recomendaciones concretas
  - Limitaciones del estudio (no saltarlas — el jurado las preguntará de todos modos)

BLOQUE 7 — CIERRE (1 minuto)
  - Agradecimiento al asesor, jurado, institución
  - "Quedo a disposición para las preguntas"
```

### Paso 3: Guía de diapositivas

Producir `tesis/presentacion/guia_diapositivas.md`:

| Diapositiva | Título | Contenido | Nota del expositor |
|---|---|---|---|
| 1 | Portada | Título, tesista, asesor, institución, fecha | Presentarse brevemente |
| 2 | Índice | Bloques de la presentación | Solo mencionar, no leer |
| 3 | Problema | Realidad problemática visual | Máx. 3 viñetas + 1 dato clave |
| 4 | Objetivos | Lista de objetivos | Leer el general, mencionar los específicos |
| 5 | Metodología | Tabla resumen del diseño | Hablar del instrumento |
| 6-8 | Resultados | Una tabla/figura por objetivo | Explicar, no leer |
| 9 | Discusión | Tabla: Hallazgo vs. Antecedente | 2-3 comparaciones |
| 10 | Conclusiones | Una por objetivo + general | Conciso |
| 11 | Recomendaciones + Limitaciones | Lista breve | Declarar limitaciones con confianza |
| 12 | Cierre | Agradecimientos | Invitar preguntas |

**Reglas de las diapositivas:**
- Máx. 5 líneas por diapositiva
- Sin bloques de texto — usar viñetas cortas
- Las tablas y figuras deben ser las mismas que en la tesis (coherencia)
- Usar un tamaño de fuente legible desde el fondo del salón (≥ 24pt para cuerpo)

### Paso 4: Banco de preguntas del jurado

Producir `tesis/presentacion/preguntas_jurado.md` con las preguntas más probables organizadas por categoría:

**Sobre el problema y la relevancia:**
- ¿Por qué es importante estudiar este tema ahora?
- ¿Qué vacío en la literatura llena su investigación?
- ¿Cuál es el aporte práctico de su estudio?

**Sobre la metodología:**
- ¿Por qué eligió ese diseño y no uno experimental?
- ¿Cómo garantizó la validez y confiabilidad de su instrumento?
- ¿Cómo seleccionó la muestra? ¿Es representativa?
- ¿Qué hubiera hecho diferente en la metodología?

**Sobre los resultados:**
- ¿Cómo explicaría [resultado específico] que parece contradictorio?
- ¿Por qué cree que encontró esos resultados y no otros?
- ¿Los resultados se pueden generalizar? ¿A qué población?

**Sobre el marco teórico:**
- ¿Por qué usó la teoría de [X] y no la de [Y]?
- ¿Cómo define [concepto clave] en el contexto de su investigación?

**Sobre las limitaciones:**
- ¿Cuáles son las principales limitaciones de su estudio?
- ¿Qué futuras investigaciones sugiere?

Para cada pregunta, producir una respuesta guía (sin inventar datos):
```
Pregunta: [...]
Respuesta sugerida: "[Cómo enmarcar la respuesta sin entrar en pánico]"
Qué NO decir: [errores comunes al responder esto]
```

### Paso 5: Ensayo de respuestas

Si el tesista quiere practicar: simular una sesión de preguntas del jurado.
- Hacer una pregunta difícil a la vez
- El tesista responde
- El sistema retroalimenta: ¿fue clara? ¿completa? ¿concisa?

---

## Gotchas

- Si quedan menos de 3 días para la sustentación: priorizar preguntas del jurado y estructura de defensa — no revisar la tesis completa a último momento
- Si el tesista tiene nervios extremos: recordar que el jurado ya leyó la tesis y no busca eliminar — busca confirmar que el tesista comprende su propia investigación
- Las limitaciones son parte de toda investigación rigurosa — no son debilidades, son honestidad científica
- Nunca prometer que las preguntas del jurado serán exactamente las del banco — es preparación, no adivinanza
