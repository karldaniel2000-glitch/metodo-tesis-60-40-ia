# Logging — Registro de Sesiones y Diario de Tesis

---

## 1. SESSION_REPORT.md

Agregar entrada al final de cada sesión o antes de comprimir contexto.
**Regla:** Solo agregar. Nunca sobreescribir.

**Formato:**
```markdown
## YYYY-MM-DD HH:MM — [Título breve de la sesión]

**Operaciones:**
- [Secciones redactadas, archivos creados/modificados]

**Decisiones:**
- [Decisión tomada] — [justificación]

**Resultados:**
- [Borradores producidos, puntajes obtenidos]

**Estado:**
- Completado: [qué está listo]
- Pendiente: [qué sigue]
```

---

## 2. Diario de Tesis (research_journal.md)

Agregar entrada cada vez que un agente completa trabajo — redacción, revisión, análisis, o transición de fase.

**Formato:**
```markdown
### YYYY-MM-DD HH:MM — [Nombre del Agente]
**Fase:** [Planificación / Desarrollo / Refinamiento / Presentación]
**Objetivo:** [sección o tarea]
**Puntaje:** [XX/100 o APROBADO/RECHAZADO o N/A]
**Veredicto:** [una línea — hallazgo clave o decisión]
**Reporte:** [ruta al reporte completo]
```

**Por qué existe:** Los agentes leen este diario para entender el estado del pipeline. El auditor-coherencia verifica qué puntajes obtuvo el escritor, el orquestador sabe qué fases pasaron. Es el contexto compartido entre agentes.

---

## 3. Pipeline State (pipeline_state.json)

Estado estructurado del pipeline en `quality_reports/pipeline_state.json`.

**Actualizar después de:**
- Cada skill completado con su puntaje
- Cada transición de fase
- Cada decisión metodológica del tesista

**Leer como primera acción al recuperar una sesión.**

---

## 4. Dashboard de Tesis

El dashboard (`tesis_dashboard.html`) se regenera después de cada interacción que cambie el estado del pipeline:

| Trigger | Qué actualiza |
|---|---|
| `/planificar` completa | Sección de planificación, barras de progreso |
| `/literatura` completa | Sección de literatura, contador de fuentes |
| `/escribir` completa | Sección de desarrollo, estado de cada capítulo |
| `/revisar` completa | Sección de calidad, scores |
| Datos agregados | Sección de análisis |
