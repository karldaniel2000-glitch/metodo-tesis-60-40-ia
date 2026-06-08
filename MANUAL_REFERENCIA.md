# Manual de Referencia Rápida
# Método Tesis 60-40 IA™

> Versión 1.0 | Junio 2026
> Sistema de asistencia ética para el desarrollo de tesis académicas

---

## ¿Qué es el Método Tesis 60-40 IA™?

Un sistema de asistencia académica basado en IA que guía al tesista desde la idea inicial hasta la sustentación. El número "60-40" define la división de responsabilidades:

| Actor | Porcentaje | Responsabilidad |
|---|---|---|
| **Tesista (tú)** | **60%** | Pensamiento crítico, datos reales, decisiones metodológicas, voz propia, juicio académico |
| **IA (el sistema)** | **40%** | Estructura, corrección, síntesis, verificación de formato, organización lógica |

> **Regla de oro:** La IA asiste — el tesista decide. Ningún resultado del sistema reemplaza el criterio del investigador.

---

## Los 10 Principios Éticos (inmutables)

| # | Principio |
|---|---|
| PE-1 | Nunca inventa citas — las fuentes no verificadas se marcan `[PENDIENTE DE VERIFICACIÓN]` |
| PE-2 | Nunca genera estadísticas — los datos los aporta el tesista |
| PE-3 | Nunca reemplaza el juicio metodológico del tesista |
| PE-4 | Nunca promete aprobación académica |
| PE-5 | Nunca fabrica autores ni teorías |
| PE-6 | Nunca oculta limitaciones del estudio |
| PE-7 | Siempre marca afirmaciones no verificadas |
| PE-8 | Siempre recuerda que los borradores son puntos de partida |
| PE-9 | Siempre es transparente sobre sus propias limitaciones |
| PE-10 | El tesista puede auditar todo el proceso en SESSION_REPORT y research_journal |

---

## Las 3 Fases del Proceso

```
FASE 1: PLANIFICACIÓN          FASE 2: DESARROLLO             FASE 3: REFINAMIENTO
─────────────────────          ──────────────────             ────────────────────
/diagnostico                   /literatura                    /revisar todo
/planificar titulo             /escribir marco                /corregir completo
/planificar problema           /escribir metodologia          /revisar coherencia
/planificar objetivos          /escribir resultados*          /revisar apa
/planificar variables          /escribir discusion
/planificar metodologia        /escribir conclusiones              + PRESENTACIÓN
/planificar consistencia       /escribir abstract             /sustentar estructura
                                                              /sustentar diapositivas
                                                              /sustentar simulacro
* Solo con datos reales del tesista
```

---

## Los 12 Comandos (Skills)

### `/diagnostico`
**Qué hace:** Evalúa el estado actual del tesista mediante 4 bloques de preguntas conversacionales.
**Cuándo usarlo:** Al inicio de cualquier proyecto nuevo.
**Produce:** `diagnostico_inicial.md` con fortalezas, brechas y ruta sugerida.

```
Ejemplo:
/diagnostico
→ El sistema pregunta: ¿En qué etapa estás? ¿Qué tienes hasta ahora?
→ Genera un mapa de tu situación actual
```

---

### `/planificar [modo]`
**Qué hace:** Construye los elementos del Capítulo I paso a paso.
**Modos disponibles:** `titulo` | `problema` | `objetivos` | `variables` | `metodologia` | `consistencia`
**Cuándo usarlo:** Después del diagnóstico, uno por uno, con aprobación entre cada elemento.

```
Ejemplo:
/planificar titulo
→ Genera 3 opciones de título con análisis de 4 componentes
→ El tesista elige y puede modificar

/planificar consistencia
→ Genera la matriz de consistencia completa + auditoría de las 8 cadenas de coherencia
```

---

### `/literatura`
**Qué hace:** Ayuda a identificar, organizar y registrar fuentes bibliográficas.
**Produce:** `antecedentes.md` (fichas verificadas) + `referencias.bib` (formato BibTeX) + `pendientes.md` (fuentes no verificadas)
**Regla crítica:** Fuentes no verificadas NUNCA van a `antecedentes.md`.

```
Ejemplo:
/literatura
→ Identifica fuentes existentes del tesista
→ Sugiere búsqueda adicional (Google Scholar, Redalyc, Scielo, etc.)
→ Genera fichas de 8 campos por cada antecedente
```

---

### `/escribir [sección]`
**Qué hace:** Redacta borradores de cada sección de la tesis.
**Secciones:** `intro` | `marco` | `metodologia` | `resultados` | `discusion` | `conclusiones` | `abstract` | `completo`
**Regla crítica para resultados:** No avanza sin datos reales. El tesista debe aportar sus datos.

```
Ejemplo:
/escribir marco
→ Lee las fuentes verificadas y redacta el marco teórico estructurado
→ Produce un borrador con citas en formato APA 7
→ El tesista revisa, adapta y valida con su asesor
```

---

### `/metodologia [modo]`
**Qué hace:** Guía el diseño metodológico completo.
**Modos:** `disenar` | `muestra` | `instrumentos` | `redactar`

```
Ejemplo:
/metodologia disenar
→ Árbol de decisiones: ¿Cuantitativo, cualitativo o mixto?
→ Ayuda a seleccionar tipo, nivel y diseño específico

/metodologia muestra
→ Proporciona la fórmula para calcular muestra
→ El tesista realiza el cálculo con sus datos reales
```

---

### `/analizar [modo]`
**Qué hace:** Guía el análisis de datos.
**Modos:** `cuantitativo` | `cualitativo` | `mixto`
**Regla crítica (INV-25):** NUNCA genera estadísticas. El tesista usa su software (SPSS, R, Atlas.ti).

```
Ejemplo:
/analizar cuantitativo
→ Árbol de decisión estadístico: ¿Pearson o Spearman? ¿t-Student o Mann-Whitney?
→ Guía sobre qué prueba aplicar según los datos y supuestos

/analizar cualitativo
→ Guía las 3 fases de codificación: abierta → axial → selectiva
→ Proporciona matrices de análisis temático
```

---

### `/revisar [modo]`
**Qué hace:** Revisión sistemática con agentes críticos.
**Modos:** `coherencia` | `apa` | `academico` | `todo`
**El modo `todo` es el más completo** — ejecuta todos los críticos y genera el Informe Final.

```
Ejemplo:
/revisar todo
→ Dispara: auditor-coherencia + corrector-apa-critic + escritor-critic en paralelo
→ Produce: Informe Final con puntaje global, tabla de estado y lista de correcciones
→ Veredicto: LISTA / APROBADA CON OBSERVACIONES / REVISIÓN IMPORTANTE / NO LISTA
```

---

### `/corregir [modo]`
**Qué hace:** Aplica correcciones sobre el texto.
**Modos:** `estilo` | `apa` | `completo`
**Formato de salida:** `~~texto anterior~~` → `**texto corregido**` (permite ver todos los cambios)

```
Ejemplo:
/corregir apa
→ Revisa TODAS las citas en texto y referencias
→ Corrige formato según APA 7
→ Datos faltantes: [DATO FALTANTE — verificar con el tesista] — NUNCA inventa

/corregir estilo
→ Mejora registro académico, precisión léxica, coherencia local
→ NUNCA reescribe desde cero
```

---

### `/sustentar [modo]`
**Qué hace:** Prepara la defensa oral de la tesis.
**Modos:** `estructura` | `diapositivas` | `preguntas` | `simulacro`
**Fórmula R-E-C:** Reconocer + Explicar + Conectar (para responder al jurado)

```
Ejemplo:
/sustentar simulacro
→ Simula preguntas del jurado por categoría
→ El tesista practica con la fórmula R-E-C
→ El sistema retroalimenta la respuesta (modo orientativo, no bloqueante)
```

---

### `/dashboard`
**Qué hace:** Genera un panel visual HTML del estado de la tesis.
**Cuándo usarlo:** En cualquier momento para ver el avance general.
**Produce:** `tesis_dashboard.html` — abre en cualquier navegador.

---

### `/checkpoint`
**Qué hace:** Guarda el estado completo de la sesión en disco.
**Cuándo usarlo:** Al final de cada sesión de trabajo.
**Produce:** Actualiza `pipeline_state.json` + `SESSION_REPORT.md` + `research_journal.md`.

---

### `/nueva-tesis [tema]`
**Qué hace:** Inicia un proyecto completo de tesis desde cero con el flujo orquestado completo.
**Cuándo usarlo:** Solo cuando se comienza un proyecto nuevo, no para continuar uno en curso.

```
Ejemplo:
/nueva-tesis "relación entre liderazgo directivo y clima organizacional en colegios públicos"
→ Ejecuta diagnóstico → planificación (con aprobaciones) → desarrollo → refinamiento → presentación
→ 6 pausas obligatorias donde el tesista debe tomar decisiones
```

---

## Umbrales de Calidad

| Puntaje | Estado | Acción |
|---|---|---|
| 90 - 100 | ✅ LISTA | Lista para entregar |
| 80 - 89 | ⚠️ APROBADA | Resolver observaciones menores |
| 70 - 79 | 🔶 REVISAR | Correcciones importantes requeridas |
| < 70 | ❌ REESCRIBIR | Sección necesita reescritura |

---

## Arquitectura del Sistema (resumen técnico)

```
CONSTITUCIÓN (CLAUDE.md)
│
├── GOVERNANCE RULES (.claude/rules/)
│   ├── workflow.md          — Protocolo de trabajo y orquestación
│   ├── ethical-principles.md — PE-1 a PE-10 (inmutables)
│   ├── content-invariants.md — INV-1 a INV-26 (inmutables)
│   ├── permissions.md       — Skills registradas y dependencias
│   ├── quality.md           — Pesos y umbrales de calidad
│   ├── lifecycle.md         — Validación pre/post dispatch
│   └── logging.md           — SESSION_REPORT, journal, pipeline
│
├── AGENTES (.claude/agents/)
│   ├── orchestrator.md      — Coordina todo el flujo
│   ├── escritor.md          — Redacta secciones
│   ├── escritor-critic.md   — Revisa redacción global
│   ├── planificador.md      — Construye Capítulo I
│   ├── planificador-critic  — Verifica planificación
│   ├── metodólogo.md        — Diseño metodológico
│   ├── metodólogo-critic    — Verifica metodología
│   ├── bibliografista.md    — Gestión de fuentes
│   ├── bibliografista-critic— Verifica bibliografía
│   ├── analista-critic.md   — Verifica resultados (INV-25)
│   ├── auditor-coherencia   — 8 cadenas de coherencia
│   ├── corrector-apa.md     — Corrección APA 7
│   ├── corrector-apa-critic — Verifica corrección APA
│   ├── expositor.md         — Prepara sustentación
│   └── expositor-critic     — Retroalimenta práctica oral
│
├── SKILLS (.claude/skills/)
│   └── 12 comandos con SKILL.md completo
│
├── TEMPLATES (templates/)
│   └── 16 plantillas reutilizables por sección
│
└── ESTADO DEL PROYECTO
    ├── quality_reports/pipeline_state.json
    ├── quality_reports/research_journal.md
    ├── SESSION_REPORT.md
    └── MEMORY.md
```

---

## Estructura de Archivos de un Proyecto de Tesis

```
/tesis/
├── tesis_principal.md         ← Documento principal (o por capítulos)
├── referencias.bib            ← Todas las referencias en BibTeX
├── antecedentes.md            ← Fichas de antecedentes verificadas
├── pendientes.md              ← Fuentes NO verificadas (no usar en tesis)
├── diagnostico_inicial.md     ← Diagnóstico del tesista
├── pipeline_state.json        ← Estado del proyecto
├── secciones/
│   ├── cap1_planificacion.md
│   ├── cap2_marco_teorico.md
│   ├── cap3_metodologia.md
│   ├── cap4_resultados.md
│   ├── cap5_discusion.md
│   └── cap6_conclusiones.md
└── quality_reports/
    ├── coherencia_report.md
    ├── apa_report.md
    └── informe_final.md
```

---

## Preguntas frecuentes

**¿Puedo usar el sistema para escribir toda mi tesis?**
No exactamente. El sistema genera borradores estructurados, pero el tesista debe revisarlos, adaptarlos con su voz y validarlos con su asesor. Los borradores son puntos de partida, no el producto final.

**¿El sistema puede buscar fuentes por mí?**
Puede guiar la búsqueda y generar fichas, pero no puede acceder a bases de datos de pago. El tesista debe proporcionar los PDFs o confirmar el acceso a las fuentes identificadas.

**¿Qué pasa si no tengo datos para la sección de resultados?**
El sistema se detiene y solicita los datos. Nunca genera estadísticas inventadas. Esta es una regla inmutable (INV-25 / PE-2).

**¿Las correcciones APA son definitivas?**
Son muy precisas, pero el tesista debe verificar las referencias contra los documentos originales. Si hay datos faltantes, el sistema los marca como `[DATO FALTANTE]` — el tesista debe completarlos.

**¿El sistema reemplaza al asesor de tesis?**
No. El asesor tiene autoridad académica e institucional que el sistema no puede replicar. El sistema complementa al asesor, no lo reemplaza.

---

*Método Tesis 60-40 IA™ | Manual de Referencia Rápida v1.0 | Junio 2026*
