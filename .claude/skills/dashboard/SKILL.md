---
name: dashboard
description: Genera o actualiza el panel HTML de progreso de la tesis. Muestra el estado de cada sección, puntajes de calidad, bibliografía disponible, y próximos pasos. Activar cuando el usuario diga "muéstrame el progreso", "cómo va mi tesis", "panel de estado", "dashboard", o al final de cada sesión de trabajo.
argument-hint: ""
allowed-tools: Read,Write,Glob
---

# Dashboard — Panel de Progreso de la Tesis

Genera `tesis_dashboard.html` — una página HTML única que muestra el estado completo del proyecto de tesis.

---

## Instrucciones

### Paso 1: Recopilar estado actual

Leer en paralelo:
1. `quality_reports/pipeline_state.json` — estado de cada sección
2. `tesis/secciones/` — archivos existentes y su tamaño
3. `quality_reports/coherence_checks/` — último reporte de coherencia
4. `quality_reports/research_journal.md` — últimas entradas
5. `tesis/referencias.bib` — contar fuentes
6. `CLAUDE.md` — nombre del proyecto y enfoque

### Paso 2: Generar el HTML

Producir `tesis_dashboard.html` con esta estructura:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Dashboard — [Nombre del proyecto]</title>
  <style>
    /* Sistema de diseño clo-author adaptado */
    :root {
      --ivory: #FAFAF7;
      --clay: #C4622D;
      --slate: #2C3E50;
      --sage: #5D8A6A;
      --g200: #E8E8E2;
      --g300: #D4D4CB;
      --g500: #6B6B64;
    }
    body { font-family: Georgia, serif; background: var(--ivory); color: var(--slate); max-width: 960px; margin: 0 auto; padding: 24px; }
    h1 { font-size: 1.6rem; color: var(--slate); }
    h2 { font-size: 1.1rem; color: var(--clay); border-bottom: 2px solid var(--clay); padding-bottom: 6px; margin-top: 32px; }
    .stat-row { display: flex; gap: 16px; flex-wrap: wrap; margin: 16px 0; }
    .stat-card { background: white; border: 1.5px solid var(--g300); border-radius: 8px; padding: 16px 20px; min-width: 140px; }
    .stat-card .number { font-size: 2rem; font-weight: bold; color: var(--clay); }
    .stat-card .label { font-size: 0.8rem; color: var(--g500); }
    table { width: 100%; border-collapse: collapse; margin: 16px 0; }
    th { background: var(--g200); text-align: left; padding: 8px 12px; font-size: 0.85rem; }
    td { padding: 8px 12px; border-bottom: 1px solid var(--g200); font-size: 0.9rem; }
    .pill { display: inline-block; padding: 2px 10px; border-radius: 999px; font-size: 0.75rem; font-weight: 500; }
    .pill-ok { background: #D4EDDA; color: #155724; }
    .pill-warn { background: #FFF3CD; color: #856404; }
    .pill-danger { background: #F8D7DA; color: #721C24; }
    .pill-pending { background: var(--g200); color: var(--g500); }
    .progress-bar { height: 8px; background: var(--g200); border-radius: 4px; margin: 4px 0; }
    .progress-fill { height: 100%; background: var(--clay); border-radius: 4px; }
    .alert { background: #FFF3CD; border-left: 4px solid #FFC107; padding: 12px 16px; margin: 12px 0; border-radius: 4px; font-size: 0.9rem; }
  </style>
</head>
<body>
  <h1>📋 [Nombre del proyecto o tema de tesis]</h1>
  <p style="color: var(--g500); font-size:0.9rem">Actualizado: [fecha] · Enfoque: [cuantitativo/cualitativo/mixto]</p>

  <!-- FILA DE STATS -->
  <div class="stat-row">
    <div class="stat-card">
      <div class="number">[N]%</div>
      <div class="label">Progreso global</div>
    </div>
    <div class="stat-card">
      <div class="number">[N]</div>
      <div class="label">Secciones completas</div>
    </div>
    <div class="stat-card">
      <div class="number">[N]</div>
      <div class="label">Fuentes en bibliografía</div>
    </div>
    <div class="stat-card">
      <div class="number">[XX]</div>
      <div class="label">Último puntaje global</div>
    </div>
  </div>

  <!-- PROGRESO GENERAL -->
  <h2>Estado del Pipeline</h2>
  <table>
    <tr><th>Fase</th><th>Estado</th><th>Progreso</th><th>Puntaje</th></tr>
    <tr>
      <td>Fase 1: Planificación</td>
      <td><span class="pill [clase según estado]">[estado]</span></td>
      <td>[barra de progreso]</td>
      <td>[puntaje o —]</td>
    </tr>
    <!-- repetir para Desarrollo, Refinamiento, Presentación -->
  </table>

  <!-- ESTADO POR SECCIÓN -->
  <h2>Estado por Sección</h2>
  <table>
    <tr><th>Sección</th><th>Estado</th><th>Puntaje</th><th>Observación</th></tr>
    <!-- Una fila por sección del pipeline_state -->
  </table>

  <!-- COHERENCIA -->
  <h2>Coherencia Interna</h2>
  <!-- Si hay reporte de coherencia: mostrar tabla de cadenas -->
  <!-- Si no hay: mostrar empty state -->

  <!-- BIBLIOGRAFÍA -->
  <h2>Bibliografía</h2>
  <p>[N] fuentes en tesis/referencias.bib · [N] marcadas como pendientes de verificación</p>

  <!-- PRÓXIMOS PASOS -->
  <h2>Próximos Pasos</h2>
  <ol>
    <!-- Derivar de las secciones pendientes y brechas detectadas -->
  </ol>

  <!-- ALERTAS -->
  <!-- Si hay brechas críticas o invariantes violadas: mostrar alert -->

</body>
</html>
```

### Paso 3: Calcular progreso

**Progreso global:** secciones completadas (puntaje >= 80) / total de secciones requeridas × 100

**Estado de cada sección:**
- ✅ Completa (puntaje >= 80)
- ⚠️ En revisión (puntaje 70-79)
- ❌ Requiere trabajo (puntaje < 70 o borrador sin puntaje)
- ⬜ No iniciada

### Paso 4: Abrir el dashboard

Indicar al tesista que puede abrir `tesis_dashboard.html` en su navegador.

---

## Cuándo se regenera

El dashboard se actualiza automáticamente al finalizar cualquier skill que cambie el estado del pipeline:
- Después de `/planificar [cualquier modo]`
- Después de `/escribir [sección]`
- Después de `/revisar [modo]`
- Después de `/checkpoint`

---

## Gotchas

- Si el pipeline_state.json no existe: crearlo con valores null antes de generar el dashboard
- El progreso es orientativo — no reemplaza el criterio del asesor ni del jurado
- Si todas las secciones están en null: mostrar empty state con sugerencia de `/nueva-tesis` o `/diagnostico`
