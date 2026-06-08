---
name: analizar
description: Apoya el análisis e interpretación de datos. Para cuantitativo: orienta qué pruebas estadísticas usar y cómo interpretar los outputs. Para cualitativo: guía la codificación, categorización y construcción de hallazgos. NUNCA genera estadísticas — trabaja solo con datos reales proporcionados por el tesista. Activar cuando el usuario diga "tengo mis datos y no sé cómo analizarlos", "qué prueba estadística uso", "ayúdame a interpretar estos resultados", "cómo codifico las entrevistas", "analiza esto".
argument-hint: "[enfoque: cuant | cual | mixto] [descripción del dato o pregunta]"
allowed-tools: Read,Write,Edit,Glob
---

# Analizar — Apoyo al Análisis de Datos

Guía al tesista en el análisis e interpretación de sus propios datos. No genera datos, no ejecuta software, no inventa estadísticas.

---

## REGLA CRÍTICA (INV-25, PE-2)

Este skill NUNCA:
- Genera estadísticas, coeficientes, p-valores, medias, frecuencias, porcentajes
- Crea tablas con datos inventados
- Interpreta resultados que el tesista no ha proporcionado

Este skill SÍ:
- Explica qué prueba estadística usar y por qué
- Ayuda a interpretar outputs reales que el tesista comparte
- Guía la codificación y categorización de datos cualitativos
- Orienta la construcción de tablas y figuras a partir de datos reales
- Detecta errores metodológicos en el análisis

---

## Modo cuantitativo: `/analizar cuant`

### Paso 1: Identificar el objetivo del análisis

Preguntar:
- ¿Qué objetivo específico estás respondiendo con este análisis?
- ¿Qué tipo de variable tienes? (nominal, ordinal, de intervalo, de razón)
- ¿Cuántos grupos o variables estás comparando?
- ¿Tienes los supuestos de normalidad verificados? (o guiar para verificarlos)

### Paso 2: Orientar la selección de prueba estadística

**Árbol de decisión:**

```
¿Cuántas variables?
  ├── Una variable → Estadística descriptiva
  │     (media, mediana, moda, desviación estándar, frecuencias)
  │
  ├── Dos variables
  │     ├── Relación/correlación
  │     │     ├── Ambas cuantitativas + normalidad → Pearson
  │     │     ├── Ordinal o sin normalidad → Spearman
  │     │     └── Una nominal + una cuantitativa → ver comparación
  │     │
  │     └── Comparación de grupos
  │           ├── 2 grupos independientes + normalidad → t de Student
  │           ├── 2 grupos independientes + sin normalidad → U Mann-Whitney
  │           ├── 2 grupos relacionados → t pareada / Wilcoxon
  │           ├── 3+ grupos independientes + normalidad → ANOVA
  │           └── 3+ grupos sin normalidad → Kruskal-Wallis
  │
  └── Predicción → Regresión
        ├── Una variable predictora → Regresión simple
        └── Varias predictoras → Regresión múltiple
```

**Para Chi-cuadrado:** dos variables nominales/categóricas

### Paso 3: Ayudar a interpretar el output real

Cuando el tesista comparte un output de SPSS, R, Excel u otro software:

1. Identificar el estadístico relevante en el output
2. Leer el p-valor o el nivel de significancia
3. Comparar con α = 0.05 (o el que el tesista haya establecido)
4. Redactar la interpretación en lenguaje académico:
   - "Se encontró una correlación positiva moderada (r = [valor del tesista], p = [valor del tesista]) entre..."
   - "No se encontraron diferencias estadísticamente significativas (p > 0.05) entre..."

5. Construir la tabla de resultados a partir de los datos del tesista
6. Redactar el párrafo de resultados para esa prueba

### Paso 4: Verificar coherencia

- ¿La prueba usada es coherente con el tipo de variable y diseño? (INV-9)
- ¿Los resultados responden al objetivo específico correspondiente?

---

## Modo cualitativo: `/analizar cual`

### Paso 1: Organizar el material

Preguntar:
- ¿Qué tipo de material tienes? (transcripciones de entrevistas, notas de campo, documentos)
- ¿Cuántas entrevistas/casos tienes?
- ¿Has comenzado a codificar o partes desde cero?

### Paso 2: Guiar el proceso de codificación

**Fase 1 — Codificación abierta:**
1. El tesista comparte fragmentos del material (transcripciones, notas)
2. El sistema propone códigos preliminares basados en el contenido literal
3. El tesista revisa, ajusta y aprueba los códigos
4. IMPORTANTE: los códigos emergen del material — no se imponen desde la teoría (en teoría fundamentada) O se verifican contra las categorías del marco teórico (en análisis temático deductivo)

**Fase 2 — Codificación axial:**
1. Agrupar códigos en subcategorías
2. Subcategorías forman categorías
3. Verificar que las categorías coincidan con las declaradas en la metodología

**Fase 3 — Codificación selectiva:**
1. Identificar la categoría central que integra las demás
2. Construir la narrativa analítica

### Paso 3: Construcción de hallazgos

Para cada categoría:
```
Nombre de la categoría: [...]
Subcategorías: [...]
Citas representativas (del material del tesista):
  - "[cita textual del participante]" (Participante X, línea Y)
Interpretación: [análisis del investigador]
Relación con el marco teórico: [...]
```

**Regla crítica:** Las citas son textuales del material real — nunca inventadas.

### Paso 4: Criterios de rigor cualitativo

Guiar al tesista para declarar:
- **Credibilidad:** triangulación de fuentes o métodos
- **Transferibilidad:** descripción densa del contexto
- **Dependencia:** auditoría del proceso de análisis
- **Confirmabilidad:** reflexividad del investigador

---

## Modo mixto: `/analizar mixto`

1. Identificar el diseño mixto (secuencial explicativo, exploratorio, o convergente)
2. Analizar la fase cuantitativa primero (si es secuencial CUAN → CUAL)
3. Analizar la fase cualitativa
4. Guiar la integración de resultados:
   - ¿Los hallazgos se confirman mutuamente?
   - ¿Se complementan?
   - ¿Hay divergencias? (declarar y analizar)

---

## Gotchas

- Si el tesista pide "analiza mis datos" pero no los comparte: pedir que los comparta antes de continuar
- Si comparte una tabla con muchos valores: pedir que identifique qué objetivo específico responde ese análisis
- Si detecta que la prueba estadística usada es incorrecta para el tipo de variable: señalarlo antes de interpretar
- No recomendar software específico como único camino: SPSS, R, Excel, Atlas.ti, NVivo, MaxQDA son igualmente válidos
