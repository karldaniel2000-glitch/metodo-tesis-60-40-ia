---
name: diagnostico
description: Diagnóstico inicial de la tesis. Evalúa el estado actual del tesista — si tiene idea, borrador, o tesis avanzada — y produce una hoja de ruta personalizada. Activar cuando el usuario diga "quiero empezar mi tesis", "tengo esta idea", "revisa mi avance", "no sé por dónde empezar", o cualquier consulta sobre el estado o punto de partida de una investigación.
argument-hint: "[descripción libre del estado actual o idea]"
allowed-tools: Read,Write,Glob
---

# Diagnóstico Inicial de Tesis

Punto de entrada al sistema. Evalúa el estado del tesista y produce una hoja de ruta personalizada.

---

## Instrucciones

### Paso 1: Conversación diagnóstica

Inicia una conversación diagnóstica. Haz las preguntas de forma conversacional — máximo 2 a la vez. Espera las respuestas antes de continuar.

**Bloque A — Estado actual (1-2 preguntas):**
- ¿Tienes un tema definido, una idea aproximada, o todavía no sabes de qué va a tratar tu investigación?
- ¿Tienes algún borrador, esquema o avance, aunque sea mínimo?

**Bloque B — Contexto institucional (1-2 preguntas):**
- ¿Qué tipo de trabajo estás haciendo? (tesis de pregrado, maestría, doctorado, trabajo de suficiencia, proyecto de investigación)
- ¿Tu universidad o programa tiene una estructura específica que debas seguir? (si la tiene, ¿puedes describírmela o compartir el reglamento?)

**Bloque C — Enfoque metodológico (1-2 preguntas):**
- ¿Ya tienes una idea del enfoque? (cuantitativo, cualitativo, mixto, documental, revisión sistemática)
- ¿Tienes acceso a datos o campo para recolectarlos, o trabajarás con fuentes secundarias?

**Bloque D — Recursos y tiempo (1 pregunta):**
- ¿Cuánto tiempo tienes para desarrollar la tesis? ¿Hay una fecha de entrega o sustentación?

### Paso 2: Producir el diagnóstico

Con las respuestas, producir `quality_reports/diagnostico_inicial.md` con esta estructura:

```markdown
# Diagnóstico Inicial — [Nombre o ID del tesista] — [Fecha]

## Estado actual
[Descripción del punto de partida basada en las respuestas]

## Fortalezas identificadas
- [Lo que el tesista ya tiene o sabe]

## Brechas críticas
- [Lo que falta y es indispensable para avanzar]

## Ruta sugerida
**Fase 1 — Planificación** (estimado: X sesiones)
- [ ] Definir/refinar el tema
- [ ] Formular el título
- [ ] Plantear el problema
- [ ] Formular objetivos
- [ ] Definir variables o categorías
- [ ] Diseñar la ruta metodológica
- [ ] Construir la matriz de consistencia

**Fase 2 — Desarrollo** (estimado: X sesiones)
- [ ] Búsqueda de literatura
- [ ] Marco teórico
- [ ] Metodología detallada
- [ ] [Si aplica: instrumentos y recolección]
- [ ] Resultados
- [ ] Discusión
- [ ] Conclusiones y recomendaciones

**Fase 3 — Refinamiento** (estimado: X sesiones)
- [ ] Auditoría de coherencia
- [ ] Corrección APA 7
- [ ] Revisión académica
- [ ] Preparación de sustentación

## Enfoque metodológico detectado
[Cuantitativo / Cualitativo / Mixto / Documental / otro]

## Skills recomendados para iniciar
1. /[skill] — [por qué empezar aquí]
2. /[skill] — [segundo paso]

## Advertencias
[Riesgos detectados: tema muy amplio, datos no disponibles, tiempo insuficiente, etc.]
```

### Paso 3: Inicializar pipeline_state.json

Crear o actualizar `quality_reports/pipeline_state.json`:

```json
{
  "proyecto": "[nombre o descripción breve]",
  "fecha_inicio": "YYYY-MM-DD",
  "enfoque": "cuantitativo|cualitativo|mixto|documental",
  "fase_actual": "planificacion",
  "fases": {
    "planificacion": { "estado": "en_progreso", "puntaje": null },
    "desarrollo": { "estado": "no_iniciada", "puntaje": null },
    "refinamiento": { "estado": "no_iniciada", "puntaje": null },
    "presentacion": { "estado": "no_iniciada", "puntaje": null }
  },
  "secciones": {
    "titulo": "pendiente",
    "problema": "pendiente",
    "objetivos": "pendiente",
    "variables": "pendiente",
    "metodologia": "pendiente",
    "consistencia": "pendiente",
    "literatura": "pendiente",
    "marco_teorico": "pendiente",
    "resultados": "pendiente",
    "discusion": "pendiente",
    "conclusiones": "pendiente"
  },
  "ultimo_puntaje_global": null
}
```

### Paso 4: Presentar al tesista

Mostrar el diagnóstico de forma amigable. Explicar la ruta sugerida y preguntar: "¿Con cuál paso quieres comenzar?"

---

## Ejemplo

**Usuario dice:** "Quiero hacer mi tesis sobre el uso de redes sociales en estudiantes universitarios pero no sé cómo empezar"

**El skill hace:**
1. Hace 2 preguntas diagnósticas sobre el estado actual y contexto
2. Con las respuestas: produce diagnóstico con tema detectado (cuantitativo probable), brechas (falta definir problema específico, variables, metodología), ruta de 3 fases con estimado de tiempo
3. Recomienda iniciar con `/planificar titulo`

---

## Gotchas

- Si el tesista ya tiene un borrador avanzado, NO reiniciar desde cero — entrar a la fase correspondiente
- Si el tema es muy amplio ("educación", "salud"), señalarlo como brecha crítica antes de continuar
- Si hay reglamento institucional específico, leerlo y ajustar la ruta
