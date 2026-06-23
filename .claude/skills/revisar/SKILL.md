---
name: revisar
description: Sistema de revisión y auditoría de la tesis. Verifica coherencia interna, formato APA 7 y calidad académica. Activar cuando el usuario diga "revisa mi tesis", "verifica la coherencia", "chequea las citas", "audita todo", o cuando se quiera saber si la tesis está lista para entregar. Modos: coherencia | apa | academico | todo.
argument-hint: "[modo: coherencia | apa | academico | todo] [sección opcional]"
allowed-tools: Read,Write,Glob
---

# Revisar — Sistema de Auditoría

Auditoría completa o parcial de la tesis. Despacha los agentes revisores según el modo solicitado.

---

## Modos

### `/revisar coherencia`

**Agente:** Auditor-Coherencia
**Output:** `quality_reports/coherence_checks/reporte_YYYY-MM-DD.md`

Verifica las 8 cadenas de coherencia definidas en `auditor-coherencia.md`:
1. Título → Problema → Objetivos
2. Objetivos → Variables/Categorías → Metodología
3. Marco Teórico → Variables
4. Metodología → Instrumentos → Resultados
5. Objetivos → Resultados → Conclusiones
6. Antecedentes → Discusión
7. Hipótesis → Resultados (si aplica)
8. Integridad de datos (INV-25)

Produce reporte con estado por cadena, brechas críticas y puntaje de coherencia.

---

### `/revisar apa`

**Agente:** Corrector-APA + Corrector-APA-Critic
**Output:** `quality_reports/coherence_checks/reporte_apa_YYYY-MM-DD.md`

Revisa:
- Todas las citas en texto del borrador completo
- Toda la lista de referencias
- Produce lista de errores con correcciones (o marcas `[DATO FALTANTE]`)
- Verifica INV-14 al INV-19

---

### `/revisar academico`

**Agente:** Escritor-Critic (modo auditoría global)
**Output:** `quality_reports/coherence_checks/reporte_academico_YYYY-MM-DD.md`

Revisa:
- Calidad de redacción en todas las secciones
- Cumplimiento de INV-20 al INV-24
- Lenguaje valorativo sin respaldo
- Afirmaciones sin cita
- Formato de tablas y figuras

---

### `/revisar todo`

Despacha en paralelo:
1. Auditor-Coherencia → reporte coherencia
2. Corrector-APA → reporte APA
3. Escritor-Critic → reporte académico

Luego produce un **Reporte Integrado Final** con:
- Puntaje global ponderado
- Tabla de estado por componente
- Lista priorizada de correcciones (bloqueantes primero, observaciones después)
- Veredicto: LISTA PARA ENTREGAR / REQUIERE CORRECCIONES MENORES / REQUIERE REVISIÓN IMPORTANTE / NO LISTA

---

## Reglas de Estilo y Antidetección (Stop Words de IA)
En todas las revisiones (especialmente la auditoría académica), el asistente DEBE PENALIZAR y marcar para corrección el uso de las siguientes palabras hiperutilizadas por modelos de lenguaje, para garantizar que la redacción de la tesis supere detectores de IA:
- **Español:** adentrarse, profundizar, sumergirse, crucial, fundamental, vital, tapiz, entramado, ámbito, esfera, terreno, intrincado, complejo, destacar, subrayar, enfatizar, resaltar, testamento (como prueba), en resumen, en conclusión, en definitiva, desentrañar, descifrar, multifacético, multidimensional, panorama, paisaje, aprovechar, apalancar, metódico, riguroso, en última instancia, transformador, dinámico.
- **Inglés:** delve, crucial, vital, pivotal, tapestry, realm, intricate, nuanced, underscore, emphasize, highlight, testament, in summary, in conclusion, ultimately, unravel, unveil, multifaceted, comprehensive, landscape, leverage, harness, meticulous, rigorous, navigating, transformative, dynamic.

---

## Formato del Reporte Integrado

```markdown
# Reporte de Revisión Final — [Fecha]

## Puntaje Global: [XX]/100

| Componente | Puntaje | Estado |
|---|---|---|
| Coherencia interna | XX/100 | ✅/⚠️/❌ |
| Formato APA 7 | XX/100 | ✅/⚠️/❌ |
| Calidad académica | XX/100 | ✅/⚠️/❌ |
| **GLOBAL PONDERADO** | **XX/100** | |

## Veredicto
[LISTA PARA ENTREGAR / REQUIERE CORRECCIONES MENORES / REQUIERE REVISIÓN IMPORTANTE / NO LISTA]

## Correcciones bloqueantes (deben resolverse antes de entregar)
1. [Descripción con evidencia específica]

## Observaciones menores (mejoran la calidad pero no bloquean)
- [Lista]

## Próximo paso sugerido
[/corregir [sección] / /planificar [elemento] / listo para /sustentar]
```

---

## Gotchas

- Si el borrador está incompleto (< 50% de secciones), advertirlo y ofrecer revisar lo disponible con nota de que el reporte es parcial
- Nunca reportar "todo perfecto" — siempre hay algo que mejorar; si el puntaje es 90+, reportar observaciones menores igual
- Las brechas críticas de coherencia siempre se escalan al tesista — el sistema no las "arregla" sin decisión del tesista
