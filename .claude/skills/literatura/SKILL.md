---
name: literatura
description: Búsqueda, síntesis y organización de literatura académica para la tesis. Activa cuando el usuario pida buscar artículos, antecedentes, referencias, fuentes, o cuando diga "necesito bibliografía", "busca estudios sobre", "dame antecedentes de". También activa cuando el marco teórico está vacío y se necesita construir la base bibliográfica.
argument-hint: "[tema o variable a buscar]"
allowed-tools: Read,Write,Glob,WebSearch,WebFetch
---

# Literatura — Búsqueda y Síntesis Bibliográfica

Organiza la bibliografía del tesista y guía la búsqueda de antecedentes y bases teóricas.

---

## Instrucciones

### Paso 1: Inventario de lo existente

Antes de buscar, revisar:
1. `tesis/referencias.bib` — ¿qué ya tiene?
2. `data/fuentes/` — ¿hay PDFs subidos por el tesista?
3. `master_supporting_docs/` — documentos de referencia del programa

### Paso 2: Identificar qué se necesita

Con el tema y las variables/categorías definidas, determinar:
- ¿Cuántos antecedentes internacionales se necesitan? (mínimo 5 recomendado)
- ¿Cuántos antecedentes nacionales/locales? (mínimo 3 recomendado)
- ¿Qué teorías o modelos sustentan las variables clave?

### Paso 3: Búsqueda guiada

Buscar en:
- Google Scholar (buscar por tema + palabras clave + años recientes)
- Repositorios universitarios (si aplica al contexto del tesista)
- Redalyc, Scielo, Dialnet (para literatura en español)
- PubMed (para ciencias de la salud)

**Regla de búsqueda:** Priorizar últimos 5-10 años, salvo que sean teorías clásicas fundamentales.

**Regla crítica (PE-1):** Solo incluir fuentes que se puedan verificar. No inventar artículos. Si no se encuentra el artículo completo, reportarlo como `[FUENTE NO VERIFICADA — requiere acceso del tesista]`.

### Paso 4: Síntesis de antecedentes

Para cada antecedente encontrado, producir ficha siguiendo INV-12:

```markdown
**Autor(es):** [Apellido, I.]
**Año:** [XXXX]
**Título:** [Título completo]
**Objetivo:** [Qué buscó estudiar]
**Método:** [Diseño, muestra, instrumento]
**Muestra:** [Población, n=]
**Hallazgos principales:** [Resultados clave]
**Relación con esta investigación:** [Por qué es relevante]
**Cita APA 7:** [Formato correcto]
```

### Paso 5: Construir referencias.bib

Para cada fuente verificada, agregar entrada en `tesis/referencias.bib`.
Para fuentes no verificadas: listar en `quality_reports/literatura/pendientes.md`.

### Paso 6: Producir reporte de literatura

Output: `quality_reports/literatura/antecedentes.md`

Estructura:
- Antecedentes internacionales (con ficha completa)
- Antecedentes nacionales/locales
- Bases teóricas identificadas (con fuentes)
- Vacíos o limitaciones de la literatura disponible

---

## Gotchas

- Si el tema es muy reciente (post-2023), advertir que la literatura puede ser escasa
- Si el tesista tiene PDFs subidos, priorizarlos sobre búsqueda en internet
- No incluir Wikipedia, blogs, ni fuentes sin autoría académica como referencias principales
- Señalar cuando una teoría es "clásica" y justifica citas de más de 10 años
