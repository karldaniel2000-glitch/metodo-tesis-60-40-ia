---
name: checkpoint
description: Guarda el estado de la sesión de trabajo en la tesis. Activar al cerrar una sesión, antes de comprimir el contexto, o cuando el tesista diga "guarda el progreso", "cierra la sesión", "checkpoint", "hasta aquí por hoy".
argument-hint: ""
allowed-tools: Read,Write,Edit,Glob
---

# Checkpoint — Guardado de Sesión

Persiste el estado de trabajo para que la próxima sesión pueda retomar exactamente donde se quedó.

---

## Instrucciones

### Paso 1: Recopilar estado actual

1. Leer `quality_reports/pipeline_state.json` — estado antes de esta sesión
2. Identificar qué se completó en esta sesión
3. Identificar qué quedó pendiente
4. Registrar decisiones importantes tomadas

### Paso 2: Actualizar pipeline_state.json

Actualizar el estado de cada sección y fase completada en esta sesión.

### Paso 3: Agregar entrada a SESSION_REPORT.md

Formato definido en `logging.md`. Incluir:
- Operaciones realizadas
- Decisiones del tesista
- Puntajes obtenidos
- Estado final: completado / pendiente

### Paso 4: Agregar entrada al diario de tesis

`quality_reports/research_journal.md` — entrada por cada agente que trabajó en la sesión.

### Paso 5: Actualizar MEMORY.md

Si en la sesión el tesista corrigió algo, cambió de enfoque, o dio una preferencia nueva — agregarla a `MEMORY.md` como `[APREND:categoría]`.

### Paso 6: Confirmar al tesista

Reportar:
- "Guardé el progreso de esta sesión."
- Qué se completó
- Qué sigue en la próxima sesión
- Cómo retomar: "La próxima vez, di `/nueva-tesis` o el skill específico que necesites"
