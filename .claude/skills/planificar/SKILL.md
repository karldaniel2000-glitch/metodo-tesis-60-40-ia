---
name: planificar
description: Fase de planificación de la tesis. Guía la construcción de todos los elementos del proyecto de investigación. Activar cuando el usuario pida ayuda con el título, el problema, los objetivos, las variables, la metodología o la matriz de consistencia. Modos disponibles: titulo | problema | objetivos | variables | metodologia | consistencia.
argument-hint: "[modo: titulo | problema | objetivos | variables | metodologia | consistencia]"
allowed-tools: Read,Write,Edit,Glob
---

# Planificar — Fase de Planificación

Construye los elementos fundacionales de la investigación, paso a paso o en el orden que el tesista necesite.

---

## Modos

### `/planificar titulo`

**Agente:** Planificador
**Objetivo:** Formular un título académico preciso, completo y no interrogativo

**Proceso:**
1. Leer tema y enfoque del `quality_reports/diagnostico_inicial.md`
2. Presentar 3 opciones de título con estructura:
   - Fenómeno/variable principal
   - Variable secundaria o resultado esperado (si aplica)
   - Población o unidad de estudio
   - Ámbito geográfico o temporal (si es relevante)
3. Para cada opción: explicar por qué funciona y qué información transmite
4. El tesista elige o pide ajuste
5. Guardar en `tesis/secciones/titulo.md`

**Reglas del título:**
- No es una pregunta
- Sin siglas sin definir
- Sin términos vagos ("análisis de", "estudio sobre") si se puede ser más específico
- Máximo 20 palabras recomendado

**Ejemplo:**
❌ "¿Cómo influyen las redes sociales en los estudiantes?"
✅ "Uso de redes sociales y rendimiento académico en estudiantes universitarios de Lima, 2024"

---

### `/planificar problema`

**Agente:** Planificador
**Objetivo:** Formular realidad problemática, problema general y problemas específicos

**Proceso:**
1. Solicitar al tesista: contexto real del problema (datos, estadísticas, observaciones propias)
2. Con esa información, redactar:
   - **Realidad problemática** (3-5 párrafos): contexto global → nacional → local → el problema específico
   - **Problema general**: pregunta de investigación principal (¿Qué relación hay entre X e Y en Z?)
   - **Problemas específicos** (2-4): subpreguntas derivadas del problema general
3. Verificar: cada problema específico se puede responder con los datos disponibles
4. Critic verifica INV-2, INV-3

**Advertencia:** Si el tesista no tiene datos del contexto, el skill solicita esa información — no inventa estadísticas (PE-2)

---

### `/planificar objetivos`

**Agente:** Planificador
**Objetivo:** Formular objetivo general y objetivos específicos correctamente

**Proceso:**
1. Leer los problemas formulados
2. Convertir cada pregunta en objetivo usando verbos de acción:
   - Cuantitativo: determinar, analizar, identificar, establecer, comparar, evaluar
   - Cualitativo: comprender, explorar, interpretar, describir, construir
3. Verificar estructura: VERBO + OBJETO + CONDICIÓN + ÁMBITO
4. Verificar INV-3: correspondencia 1:1 problema ↔ objetivo
5. Verificar INV-4: objetivos específicos cubren el objetivo general

**Ejemplo:**
- Problema: ¿Qué relación existe entre el uso de redes sociales y el rendimiento académico?
- Objetivo: Determinar la relación entre el uso de redes sociales y el rendimiento académico en estudiantes universitarios de Lima, 2024

---

### `/planificar variables`

**Agente:** Planificador
**Objetivo:** Operacionalizar variables (cuantitativo) o definir categorías (cualitativo)

**Proceso cuantitativo:**
1. Identificar variable independiente(s) y dependiente(s)
2. Para cada variable: dimensiones → indicadores → ítems de instrumento
3. Verificar INV-5: indicadores son observables y medibles
4. Producir tabla de operacionalización

**Proceso cualitativo:**
1. Identificar categorías de análisis
2. Para cada categoría: subcategorías → indicios o unidades de análisis
3. Verificar INV-6: subcategorías derivan del marco teórico o datos
4. Producir tabla de categorización

**Advertencia:** No mezclar lógica cuantitativa y cualitativa sin justificación (mixto requiere diseño explícito)

---

### `/planificar metodologia`

**Agente:** Metodólogo
**Objetivo:** Definir la ruta metodológica completa

**Proceso:**
1. Detectar enfoque desde `pipeline_state.json`
2. Guiar la selección de:
   - **Enfoque:** cuantitativo / cualitativo / mixto
   - **Tipo:** básica / aplicada / descriptiva / explicativa / correlacional
   - **Nivel:** descriptivo / correlacional / explicativo / exploratorio
   - **Diseño:** no experimental (transeccional/longitudinal) / experimental / cuasi-experimental / fenomenológico / estudio de caso / etnográfico / etc.
   - **Población:** descripción completa con criterios de inclusión y exclusión
   - **Muestra:** tamaño y justificación (fórmula estadística para cuant, saturación para cual)
   - **Muestreo:** probabilístico/no probabilístico + tipo específico
   - **Técnicas e instrumentos**
3. Verificar coherencia: diseño es consistente con los objetivos y el enfoque

---

### `/planificar consistencia`

**Agente:** Planificador + Auditor-Coherencia
**Objetivo:** Construir y verificar la matriz de consistencia completa

**Proceso:**
1. Leer todas las secciones de planificación ya producidas
2. Construir la matriz con columnas: Problema → Objetivo → Hipótesis (si aplica) → Variable/Categoría → Indicador/Subcategoría → Instrumento
3. Despachar auditor-coherencia para verificar INV-9
4. Reportar brechas al tesista antes de aprobar

---

## Gotchas

- Si falta algún elemento previo (ej. se pide objetivos pero no hay problema formulado), el skill lo señala y ofrece producirlo primero
- Los verbos de los objetivos deben ser medibles — rechazar verbos vagos: "conocer", "entender", "ver"
- La hipótesis es opcional en estudios descriptivos y cualitativos — no forzarla
