# Registro de Permisos — Skills y Dependencias

El orquestador lee este archivo para determinar qué skills puede despachar, en qué orden y con qué dependencias. Agregar un skill nuevo: crear el archivo en `.claude/skills/`, agregar entrada aquí.

---

## diagnostico
- **FASE:** Planificación
- **GRUPO_PARALELO:** —
- **REQUIERE:** Idea o descripción del tema de tesis (puede ser oral/conversacional)
- **PRODUCE:** `quality_reports/diagnostico_inicial.md`
  - Secciones requeridas: Estado actual, Fortalezas, Brechas críticas, Ruta sugerida
- **CRÍTICO:** diagnostico-critic
- **ESCALACIÓN:** Tesista — si la idea es demasiado amplia o no tiene viabilidad metodológica
- **PESO_CALIDAD:** 5%

## planificar
- **FASE:** Planificación
- **GRUPO_PARALELO:** planificacion
- **REQUIERE:** `quality_reports/diagnostico_inicial.md`
- **PRODUCE:** `tesis/secciones/` (sección correspondiente al argumento)
  - Modos: titulo | problema | objetivos | variables | metodologia | consistencia
- **CRÍTICO:** planificador-critic
- **ESCALACIÓN:** Tesista — decisiones metodológicas fundamentales
- **PESO_CALIDAD:** 15%

## literatura
- **FASE:** Planificación / Desarrollo (puede correr en paralelo)
- **GRUPO_PARALELO:** planificacion
- **REQUIERE:** Tema de tesis (al menos título tentativo)
- **PRODUCE:** `quality_reports/literatura/antecedentes.md`, `tesis/referencias.bib`
  - Secciones requeridas: Antecedentes internacionales, Antecedentes nacionales, Base teórica
- **CRÍTICO:** bibliografista-critic
- **ESCALACIÓN:** Tesista — si la literatura es muy escasa o muy abundante para filtrar
- **PESO_CALIDAD:** 10%

## escribir
- **FASE:** Desarrollo
- **GRUPO_PARALELO:** desarrollo
- **REQUIERE:** Plan de sección aprobado + literatura básica disponible
  - Para `resultados`: datos reales del tesista obligatorios
  - Para `discusion`: resultados ya redactados
  - Para `conclusiones`: discusión ya redactada
- **PRODUCE:** `tesis/secciones/[seccion].md` o `.docx`
- **CRÍTICO:** escritor-critic
- **ESCALACIÓN:** Orquestador — si requiere reescritura estructural, no solo pulido
- **PESO_CALIDAD:** 20%

## metodologia
- **FASE:** Desarrollo
- **GRUPO_PARALELO:** desarrollo
- **REQUIERE:** Objetivos aprobados + enfoque metodológico declarado
- **PRODUCE:** `tesis/secciones/metodologia.md`
  - Secciones: Diseño, Tipo, Nivel, Enfoque, Población, Muestra, Muestreo, Técnicas, Instrumentos, Procedimiento, Análisis de datos
- **CRÍTICO:** metodólogo-critic
- **ESCALACIÓN:** Tesista — si hay incompatibilidad entre objetivos y diseño propuesto
- **PESO_CALIDAD:** 15%

## analizar
- **FASE:** Desarrollo
- **GRUPO_PARALELO:** desarrollo
- **REQUIERE:** Datos reales aportados por el tesista + metodología aprobada
- **PRODUCE:** `tesis/tablas/`, `tesis/figuras/`, `quality_reports/resultados_summary.md`
- **CRÍTICO:** analista-critic
- **ESCALACIÓN:** Tesista — si los datos no son suficientes o tienen problemas de calidad
- **PESO_CALIDAD:** 15%

## revisar
- **FASE:** Refinamiento
- **GRUPO_PARALELO:** refinamiento
- **REQUIERE:** Borrador de al menos 3 secciones en `tesis/secciones/`
- **PRODUCE:** `quality_reports/coherence_checks/reporte_YYYY-MM-DD.md`
  - Modos: coherencia | apa | todo
- **CRÍTICO:** auditor-coherencia (es solo critic, no crea)
- **ESCALACIÓN:** Tesista — si hay contradicción fundamental entre objetivos y resultados
- **PESO_CALIDAD:** 10%

## corregir
- **FASE:** Refinamiento
- **GRUPO_PARALELO:** refinamiento
- **REQUIERE:** Sección redactada en `tesis/secciones/`
- **PRODUCE:** Versión corregida de la sección
- **CRÍTICO:** corrector-apa-critic
- **ESCALACIÓN:** Escritor — si la corrección requiere reescritura estructural
- **PESO_CALIDAD:** 5%

## sustentar
- **FASE:** Refinamiento / Presentación
- **GRUPO_PARALELO:** presentacion
- **REQUIERE:** Tesis en estado avanzado (>= 80% de secciones completas)
- **PRODUCE:** `tesis/presentacion/defensa.md` — estructura de la defensa oral
- **CRÍTICO:** expositor-critic
- **ESCALACIÓN:** Tesista — decisiones sobre qué énfasis dar en la defensa
- **PESO_CALIDAD:** Orientativo (no bloquea)

## checkpoint
- **FASE:** Cualquiera
- **GRUPO_PARALELO:** utilidades
- **REQUIERE:** —
- **PRODUCE:** Actualiza `SESSION_REPORT.md`, `MEMORY.md`, `quality_reports/research_journal.md`, `quality_reports/pipeline_state.json`
- **CRÍTICO:** —
- **ESCALACIÓN:** —
- **PESO_CALIDAD:** —

## dashboard
- **FASE:** Cualquiera
- **GRUPO_PARALELO:** utilidades
- **REQUIERE:** Al menos `CLAUDE.md` y `quality_reports/pipeline_state.json`
- **PRODUCE:** `tesis_dashboard.html`
- **CRÍTICO:** —
- **ESCALACIÓN:** —
- **PESO_CALIDAD:** —

## nueva-tesis
- **FASE:** Inicio (siempre orquestado)
- **GRUPO_PARALELO:** —
- **REQUIERE:** Idea o tema inicial del tesista
- **PRODUCE:** Activa pipeline completo desde Fase 1
- **CRÍTICO:** —
- **ESCALACIÓN:** Tesista en cada punto de decisión
- **PESO_CALIDAD:** —

---

## Grupos paralelos

| Grupo | Skills | Cuándo |
|---|---|---|
| planificacion | planificar, literatura | Desde diagnóstico aprobado |
| desarrollo | escribir, metodologia, analizar | Desde plan de sección aprobado |
| refinamiento | revisar, corregir | Desde borrador disponible |
| presentacion | sustentar | Tesis avanzada |
| utilidades | checkpoint, dashboard | En cualquier momento |

## Orden de fases

```
Diagnóstico → Planificación → Desarrollo → Refinamiento → Presentación
                   ↕
             Literatura (corre en paralelo con Planificación y Desarrollo)
```

Reentrada permitida en todas las fases excepto Presentación (no terminal — el tesista puede volver a revisar).
