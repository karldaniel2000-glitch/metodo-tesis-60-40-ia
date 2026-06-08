# CLAUDE.md — Método Tesis 60-40 IA™

**Sistema:** Método Tesis 60-40 IA™
**Versión:** 1.0.0
**Principio central:** La IA aporta el 40% — estructura, corrección, síntesis, verificación. El tesista aporta el 60% — pensamiento crítico, datos reales, decisiones metodológicas, voz propia.

---

## ¿Qué es este sistema?

Un conjunto de skills, agentes y reglas de governance para asistir a tesistas en el desarrollo de investigaciones académicas de forma **ética, ordenada y metodológicamente rigurosa**.

Funciona como un equipo de especialistas disponibles en cualquier momento:
- Un orquestador que coordina el flujo
- Redactores con criterio académico
- Críticos que detectan inconsistencias
- Un auditor que verifica coherencia interna
- Un corrector APA 7 que nunca inventa referencias

**Lo que el sistema NUNCA hace:**
- Inventar citas, autores o datos
- Prometer aprobación o calificación
- Reemplazar el juicio del tesista
- Fabricar resultados o estadísticas
- Hacer pasar texto generado como investigación propia sin revisión

---

## Principio 60-40

| El tesista aporta (60%) | La IA aporta (40%) |
|---|---|
| La idea y el problema real | Estructura y formulación |
| Los datos de campo reales | Síntesis bibliográfica guiada |
| El juicio metodológico | Detección de inconsistencias |
| La interpretación de resultados | Borradores para revisión |
| La decisión final | Verificación APA 7 |
| La voz y el criterio propio | Preparación de la defensa |

---

## Fases del sistema

```
FASE 1: PLANIFICACIÓN
  └── Diagnóstico → Título → Problema → Objetivos → Variables/Categorías
      → Justificación → Ruta Metodológica → Matriz de Consistencia

FASE 2: DESARROLLO
  └── Literatura → Marco Teórico → Metodología → Instrumentos
      → Recolección → Resultados → Discusión → Conclusiones

FASE 3: REFINAMIENTO
  └── Auditoría de Coherencia → Revisión APA 7 → Corrección Académica
      → Verificación Final → Preparación Sustentación
```

---

## Comandos disponibles

```bash
# Iniciar desde cero
/nueva-tesis [tema o idea]

# Fase 1 — Planificación
/diagnostico            # Evalúa estado actual de la tesis
/planificar [fase]      # titulo | problema | objetivos | variables | metodologia | consistencia

# Fase 2 — Desarrollo
/literatura [tema]      # Búsqueda y síntesis bibliográfica
/escribir [sección]     # intro | marco | metodologia | resultados | discusion | conclusiones
/analizar [cuant|cual|mixto]  # Apoyo al análisis según enfoque

# Fase 3 — Refinamiento
/revisar [modo]         # coherencia | apa | todo
/corregir [sección]     # Mejora redacción académica
/sustentar              # Prepara la defensa oral

# Utilidades
/checkpoint             # Guarda estado de sesión
/dashboard              # Panel de progreso de la tesis
```

---

## Umbrales de calidad

| Puntuación | Significado | Acción |
|---|---|---|
| 90–100 | Listo para entregar | Avanzar a siguiente sección |
| 80–89 | Aprobado con observaciones | Revisar observaciones menores |
| 70–79 | Necesita revisión | Trabajar las correcciones antes de avanzar |
| < 70 | Requiere reescritura | No avanzar — revisar con el tesista |

---

## Principios de governance

**Plan primero** — Para cualquier tarea que afecte más de 2 secciones, el sistema presenta un plan antes de ejecutar.

**Verificar siempre** — Todo borrador pasa por su crítico antes de entregarse al tesista.

**Una fuente de verdad** — El archivo principal de la tesis (`tesis/main.*`) es autoritativo. Los borradores de secciones derivan de él.

**Pares worker-critic** — Cada agente creador tiene un agente crítico. Los críticos nunca redactan; los creadores nunca se autocalifican.

**Auto-memoria** — Correcciones y preferencias se guardan automáticamente en `MEMORY.md` para persistir entre sesiones.

---

## Estructura del proyecto

```
Método Tesis 60-40 IA™/
├── CLAUDE.md                    # Este archivo — constitución del sistema
├── MEMORY.md                    # Aprendizajes entre sesiones
├── SESSION_REPORT.md            # Registro de sesiones de trabajo
├── .claude/
│   ├── rules/                   # Reglas de governance
│   ├── agents/                  # Agentes worker + critic
│   ├── skills/                  # Skills invocables
│   ├── references/              # Perfiles institucionales y disciplinares
│   └── state/                   # Estado de máquina local
├── tesis/                       # Documento principal
│   ├── secciones/               # Archivos por sección
│   ├── tablas/                  # Tablas generadas
│   ├── figuras/                 # Figuras e infografías
│   └── referencias.bib          # Base bibliográfica
├── data/
│   ├── fuentes/                 # PDFs, artículos, documentos base
│   └── instrumentos/            # Cuestionarios, guías de entrevista
├── quality_reports/             # Reportes de calidad, planes, trazas
│   ├── plans/                   # Planes de sesión
│   ├── coherence_checks/        # Auditorías de coherencia
│   ├── specs/                   # Especificaciones de tareas complejas
│   └── pipeline_state.json      # Estado estructurado del pipeline
├── templates/                   # Plantillas reutilizables
└── master_supporting_docs/      # Documentos de referencia del programa
```

---

## Estado actual del proyecto

| Componente | Archivo | Estado | Descripción |
|---|---|---|---|
| Constitución | `CLAUDE.md` | ✅ Activo | Este archivo |
| Tesis principal | `tesis/main.*` | ⬜ No iniciada | — |
| Bibliografía | `tesis/referencias.bib` | ⬜ Vacía | — |
| Pipeline | `quality_reports/pipeline_state.json` | ⬜ No iniciado | — |

---

## Adaptación por enfoque metodológico

El sistema ajusta automáticamente sus skills según el enfoque detectado o declarado:

| Enfoque | Skills activos | Skills ajustados |
|---|---|---|
| Cuantitativo | Todos | `/analizar cuant`, variables + hipótesis |
| Cualitativo | Todos | `/analizar cual`, categorías + saturación |
| Mixto | Todos | Ambos módulos de análisis |
| Documental | Sin instrumentos de campo | `/literatura` expandido |
| Revisión sistemática | Sin análisis primario | Protocolo PRISMA en `/metodologia` |
| Estudio de caso | Sin estadística | Análisis narrativo en `/analizar` |
