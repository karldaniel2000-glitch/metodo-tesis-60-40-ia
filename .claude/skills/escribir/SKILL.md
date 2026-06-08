---
name: escribir
description: Redacción de secciones de la tesis. Produce borradores académicos listos para revisión del tesista. Activar cuando el usuario pida redactar o desarrollar: introducción, marco teórico, metodología, resultados, discusión, conclusiones, recomendaciones, o resumen/abstract. También activar con "escríbeme", "redacta", "desarrolla la sección de", "ayúdame con".
argument-hint: "[sección: intro | marco | metodologia | resultados | discusion | conclusiones | abstract | completo]"
allowed-tools: Read,Write,Edit,Glob
---

# Escribir — Redacción de Secciones

Produce borradores académicos de cada sección. Cada borrador pasa por el escritor-critic antes de entregarse al tesista.

---

## Preparación (todas las secciones)

Antes de redactar cualquier sección, leer:
1. `quality_reports/diagnostico_inicial.md` — contexto general
2. `quality_reports/pipeline_state.json` — estado actual
3. `tesis/secciones/` — lo ya redactado (para coherencia)
4. `tesis/referencias.bib` — bibliografía disponible
5. `quality_reports/literatura/` — antecedentes y síntesis

---

## Secciones

### `/escribir intro`
Estructura: contexto → problema → justificación → objetivos (breve) → estructura del trabajo.
Input requerido: problema formulado, objetivos aprobados.
Extensión típica: 1-2 páginas.

### `/escribir marco`
Estructura: antecedentes internacionales → antecedentes nacionales/locales → bases teóricas por variable/categoría → definición de términos.
Input requerido: variables/categorías definidas + bibliografía disponible.
Advertencia: NUNCA inventar antecedentes. Trabajar solo con literatura proporcionada o buscada con `/literatura`.

### `/escribir metodologia`
Estructura completa: diseño → tipo → nivel → enfoque → población → muestra → muestreo → técnicas → instrumentos → procedimiento → análisis → ética.
Input requerido: metodología de planificación aprobada.

### `/escribir resultados`
REGLA CRÍTICA: Solo narra datos reales. El tesista debe proporcionar los datos, tablas o estadísticas.
Estructura: presentar tabla/figura → describir → interpretar → responder al objetivo correspondiente.
Input requerido: datos reales del tesista (tablas, gráficos, outputs de software).

### `/escribir discusion`
Estructura: hallazgo principal → contraste con antecedente 1 → contraste con teoría → interpretación propia → coincidencias y divergencias.
Input requerido: resultados redactados + antecedentes del marco teórico.

### `/escribir conclusiones`
Estructura: una conclusión por objetivo específico → conclusión general → recomendaciones por actor → limitaciones.
Input requerido: discusión redactada.

### `/escribir abstract`
Estructura: objetivo → método → resultados clave → conclusión principal.
Extensión: 150-250 palabras. En español e inglés si se requiere.
Input requerido: tesis prácticamente completa.

### `/escribir completo`
Redacta todas las secciones en secuencia. Pausa entre secciones mayores para revisión del tesista.

---

## Checklist escritor (antes de pasar al critic)

- [ ] Sección corresponde al objetivo declarado
- [ ] Sin primera persona singular
- [ ] Sin lenguaje valorativo sin respaldo
- [ ] Toda cita tiene clave en referencias.bib
- [ ] Sin datos generados por IA (especialmente en resultados)
- [ ] Tablas y figuras con título y nota
- [ ] Texto marcado como BORRADOR

---

## Gotchas

- En resultados: si el tesista no ha proporcionado datos, solicitar antes de redactar — no inventar
- En marco teórico: si la bibliografía es insuficiente, ejecutar `/literatura` primero
- Los borradores son puntos de partida — recordar al tesista que debe revisarlos y adaptarlos con su voz
