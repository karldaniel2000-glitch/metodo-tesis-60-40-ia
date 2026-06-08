# Workflow: Planificación, Orquestación y Dependencias

---

## 1. Protocolo Plan-Primero

Para cualquier tarea que afecte más de 2 secciones o tome más de 30 minutos:

1. Entrar en modo plan antes de ejecutar
2. Leer `MEMORY.md` — entradas relevantes a la tarea
3. Si la tarea es ambigua: especificación de requerimientos (ver abajo)
4. Redactar el plan: qué secciones, en qué orden, qué produce
5. Guardar en `quality_reports/plans/YYYY-MM-DD_descripcion.md`
6. Presentar al tesista — esperar aprobación
7. Solo después: ejecutar vía orquestador

### Especificación de requerimientos (tareas complejas)

Usar cuando:
- La instrucción es vaga ("desarrolla el marco teórico")
- Hay múltiples interpretaciones válidas
- El trabajo afecta 3+ secciones o toma más de 1 hora

Protocolo:
1. Hacer 3-5 preguntas de clarificación al tesista
2. Crear `quality_reports/specs/YYYY-MM-DD_descripcion.md`
3. Clasificar cada requerimiento: DEBE / DEBERÍA / PUEDE
4. Declarar estado: CLARO / ASUMIDO / BLOQUEADO
5. Obtener aprobación del tesista
6. Luego: redactar el plan

---

## 2. El Loop del Orquestador

Una vez aprobado el plan:

```
Plan aprobado → orquestador activa
  │
  Paso 1: IDENTIFICAR — revisar dependencias, determinar qué skills activar
  │
  Paso 2: DESPACHAR — lanzar agentes worker (paralelos cuando son independientes)
  │         Cada worker va emparejado con su critic
  │
  Paso 3: REVISAR — critic evalúa, produce puntuación
  │         Si puntuación < 80 → worker corrige → critic revisa (máx. 3 rondas)
  │         Si 3 rondas fallan → ESCALAR al tesista
  │
  Paso 4: VERIFICAR — revisar coherencia con otras secciones ya redactadas
  │         Si verificación falla → corregir → re-verificar (máx. 2 intentos)
  │
  Paso 5: PUNTUAR — agregar puntajes por componente
  │
  └── Puntuación >= umbral?
        SÍ → Presentar al tesista con resumen
        NO → Identificar componentes bloqueantes, volver al Paso 2
              Tras 5 rondas totales → presentar con issues pendientes
```

### Límites del loop

- **Pares worker-critic:** máx. 3 rondas (luego escalar)
- **Loop general:** máx. 5 rondas
- **Reintentos de verificación:** máx. 2
- Nunca loop infinito

---

## 3. Dependencias entre fases

Las fases se activan por dependencia, no por secuencia rígida.

```
FASE 1: PLANIFICACIÓN
  diagnostico → planificar (título → problema → objetivos → variables → metodología → consistencia)

FASE 2: DESARROLLO
  literatura (paralelo con planificar)
  escribir secciones (requiere: plan aprobado + literatura básica)
  analizar (requiere: datos recolectados)

FASE 3: REFINAMIENTO
  revisar coherencia (requiere: borrador completo o parcial)
  corregir APA (requiere: referencias en el texto)
  sustentar (requiere: tesis lista o casi lista)
```

El tesista puede entrar en cualquier fase si ya tiene los inputs necesarios — no es obligatorio empezar desde el principio.

---

## 4. Gestión de contexto entre sesiones

### Antes de cerrar una sesión

Ejecutar `/checkpoint`. Guarda:
1. Estado del pipeline → `quality_reports/pipeline_state.json`
2. Entrada en `SESSION_REPORT.md`
3. Entrada en `quality_reports/research_journal.md`
4. Actualización de `MEMORY.md` si hubo correcciones o aprendizajes

### Al iniciar una sesión nueva

Primero:
1. Leer `quality_reports/pipeline_state.json`
2. Leer última entrada de `SESSION_REPORT.md`
3. Leer `CLAUDE.md` + plan activo en `quality_reports/plans/`
4. Anunciar: "Retomando sesión. Última tarea: [...]. Estado actual: [...]"

### Compactación

Preferir `/checkpoint` + `/compact` manual en puntos naturales de cierre, antes de que el contexto se comprima automáticamente.
