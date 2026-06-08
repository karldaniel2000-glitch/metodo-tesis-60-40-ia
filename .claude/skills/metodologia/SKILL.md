---
name: metodologia
description: Diseña y redacta la metodología de investigación. Guía la selección del diseño, tipo, nivel, población, muestra, muestreo, técnicas e instrumentos. Activar cuando el usuario diga "ayúdame con la metodología", "qué diseño usar", "cómo calculo la muestra", "qué instrumento necesito", "redacta el capítulo de metodología". Adapta automáticamente al enfoque: cuantitativo, cualitativo, mixto, documental o revisión sistemática.
argument-hint: "[modo: disenar | redactar | instrumentos | muestra] [enfoque opcional]"
allowed-tools: Read,Write,Edit,Glob
---

# Metodología — Diseño y Redacción

Construye la metodología de investigación paso a paso según el enfoque declarado.

---

## Modos

### `/metodologia disenar`

**Agente:** Metodólogo
**Objetivo:** Seleccionar y justificar cada componente del diseño metodológico

**Proceso conversacional** — pregunta de a una decisión a la vez:

#### Decisión 1: Enfoque
Presentar opciones con criterio de selección:
- **Cuantitativo:** cuando se busca medir, cuantificar, establecer relaciones o diferencias entre variables
- **Cualitativo:** cuando se busca comprender, explorar significados, experiencias o procesos
- **Mixto:** cuando se necesitan ambas perspectivas para responder la pregunta
- **Documental:** cuando se trabaja solo con fuentes secundarias
- **Revisión sistemática:** cuando se busca sintetizar evidencia de múltiples estudios

#### Decisión 2: Tipo de investigación
- Básica / Aplicada
- Descriptiva / Correlacional / Explicativa / Exploratoria (pueden combinarse)

#### Decisión 3: Nivel
- Exploratorio (fenómeno poco estudiado)
- Descriptivo (caracterizar sin establecer relaciones)
- Correlacional (establecer asociaciones)
- Explicativo/Causal (determinar causas)

#### Decisión 4: Diseño específico

**Cuantitativo:**
- No experimental transeccional (descriptivo / correlacional / causal)
- No experimental longitudinal (tendencia / cohorte / panel)
- Experimental (verdadero / cuasi-experimental / pre-experimental)

**Cualitativo:**
- Fenomenológico
- Teoría fundamentada
- Etnográfico
- Estudio de caso
- Investigación-acción
- Narrativo

**Mixto:**
- Explicativo secuencial (CUAN → CUAL)
- Exploratorio secuencial (CUAL → CUAN)
- Convergente paralelo (CUAN + CUAL simultáneos)

Para cada opción: explicar implicancias y requerir que el tesista justifique su elección.

---

### `/metodologia muestra`

**Agente:** Metodólogo
**Objetivo:** Determinar población, criterios y tamaño de muestra

**Proceso cuantitativo:**
1. Definir población objetivo: ¿quiénes? ¿dónde? ¿cuándo?
2. Criterios de inclusión y exclusión (el tesista los provee)
3. Calcular tamaño muestral según fórmula correspondiente:

**Para poblaciones finitas (< 100,000):**
```
n = (N × Z² × p × q) / (e² × (N-1) + Z² × p × q)
N = población total
Z = nivel de confianza (95% → 1.96)
p = proporción esperada (0.5 si no se sabe)
q = 1 - p
e = margen de error (típico: 0.05)
```

**Para poblaciones infinitas o muy grandes:**
```
n = (Z² × p × q) / e²
```

4. Tipo de muestreo: probabilístico (aleatorio simple, estratificado, por conglomerados) o no probabilístico (por conveniencia, intencional, bola de nieve)
5. Justificar el tipo de muestreo en función del diseño

**Proceso cualitativo:**
1. No se calcula "n" — se trabaja con saturación teórica
2. Muestro intencional / por conveniencia / teórico
3. Técnicas: informantes clave, casos típicos, casos extremos, variación máxima
4. Mencionar criterio de saturación: "hasta que nuevos datos no aporten información nueva"

---

### `/metodologia instrumentos`

**Agente:** Metodólogo
**Objetivo:** Diseñar o seleccionar los instrumentos de recolección de datos

**Por técnica:**

| Técnica | Instrumento | Cuándo usar |
|---|---|---|
| Encuesta | Cuestionario | Variables medibles, muestras grandes |
| Entrevista | Guía de entrevista | Exploración profunda, experiencias |
| Observación | Ficha de observación / Lista de cotejo | Comportamientos, procesos |
| Grupo focal | Guía de sesión | Construcción social de significados |
| Análisis documental | Ficha de análisis | Fuentes secundarias |
| Test psicométrico | Escala validada | Medir constructos psicológicos |

**Para cuestionarios:**
1. Un ítem por indicador (de la tabla de operacionalización)
2. Escala Likert (1-5 o 1-7) para variables de actitud/percepción
3. Preguntas dicotómicas (Sí/No) para variables categóricas simples
4. Validez: juicio de expertos (presentar formato de validación)
5. Confiabilidad: Alfa de Cronbach (mencionar que el tesista debe aplicarlo)

**Para guías de entrevista:**
1. Una pregunta abierta por subcategoría
2. Preguntas de profundización ("¿Puede ampliar eso?", "¿Qué quiso decir con...?")
3. No más de 10-12 preguntas principales

---

### `/metodologia redactar`

**Agente:** Metodólogo → escritor-critic
**Objetivo:** Redactar el capítulo/sección de metodología completo

**Requiere:** Decisiones de diseño ya tomadas (ejecutar `/metodologia disenar` primero)

**Estructura del capítulo:**

```
3. METODOLOGÍA DE LA INVESTIGACIÓN

3.1 Tipo y diseño de investigación
    [Explicar tipo + diseño + justificación vinculada a objetivos]

3.2 Población y muestra
    3.2.1 Población
    3.2.2 Criterios de inclusión y exclusión
    3.2.3 Muestra y muestreo

3.3 Técnicas e instrumentos de recolección de datos
    [Por variable/categoría: técnica → instrumento → qué mide]

3.4 Procedimiento de recolección de datos
    [Pasos concretos: cómo, cuándo, dónde, con quién]

3.5 Método de análisis de datos
    [Cuantitativo: software (SPSS, R), estadísticos usados]
    [Cualitativo: método (análisis temático, teoría fundamentada)]

3.6 Aspectos éticos
    [Consentimiento informado, confidencialidad, anonimato]
```

---

## Adaptación por enfoque

### Revisión sistemática
Reemplaza el diseño estándar por protocolo PRISMA:
- Criterios de inclusión/exclusión de estudios
- Bases de datos consultadas
- Ecuación de búsqueda
- Proceso de selección (diagrama PRISMA)
- Extracción de datos
- Evaluación de calidad de estudios

### Documental
Sin muestra de personas — muestra de documentos:
- Criterios de selección de fuentes
- Tipo de análisis: hermenéutico, de contenido, crítico del discurso

---

## Gotchas

- Si el tesista tiene reglamento institucional con estructura diferente, seguirlo exactamente
- Nunca calcular el Alfa de Cronbach por el tesista — indicar que debe hacerlo con su software
- Si el tesista no tiene acceso a la población real, señalar como limitación metodológica, no ignorarla
- Verificar INV-9: el diseño es coherente con las variables/categorías ya definidas
