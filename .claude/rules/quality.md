# Calidad: Puntuación, Umbrales y Severidad

---

## 1. Protocolo de puntuación

### Pesos por componente

| Componente | Peso | Agente que puntúa |
|---|---|---|
| Planificación (título, problema, objetivos, variables) | 15% | planificador-critic |
| Literatura y antecedentes | 10% | bibliografista-critic |
| Marco teórico | 10% | escritor-critic (modo marco) |
| Metodología | 15% | metodólogo-critic |
| Análisis y resultados | 15% | analista-critic |
| Redacción y escritura | 20% | escritor-critic |
| Coherencia interna | 10% | auditor-coherencia |
| APA 7 y referencias | 5% | corrector-apa-critic |

Total: 100%

### Mínimo por componente

Para avanzar a la fase de refinamiento, ningún componente puede estar por debajo de 70.
Para la versión final, ningún componente puede estar por debajo de 80.

### Fuentes de puntaje

- Cada critic produce un puntaje de 0 a 100, comenzando en 100 y deduciendo por problemas
- Las invariantes violadas tienen deducción declarada (ver `content-invariants.md`)
- El auditor-coherencia es puntaje compuesto: suma de checks de coherencia superados / total

---

## 2. Umbrales y puertas de calidad

| Puntuación | Puerta | Acción |
|---|---|---|
| 90–100 | Listo para entrega | Avanzar sin cambios |
| 80–89 | Aprobado con observaciones | El tesista revisa observaciones menores |
| 70–79 | Necesita revisión | Corregir antes de avanzar |
| < 70 | Requiere reescritura | No avanzar — reunión con el tesista |

---

## 3. Gradiente de severidad por fase

| Fase | Postura del crítico | Rationale |
|---|---|---|
| Planificación | Constructiva (severidad media) | Las ideas necesitan espacio para madurar |
| Desarrollo | Estricta (severidad alta) | Los borradores están casi listos — los errores son costosos |
| Refinamiento | Máxima severidad | Simula al jurado — sin concesiones |
| Presentación | Profesional (orientativa) | La defensa tiene componentes subjetivos; puntuación como guía |

### Escalado de deducciones por fase

| Problema | Planificación | Desarrollo | Refinamiento |
|---|---|---|---|
| Objetivo mal formulado | -3 | -8 | -15 |
| Cita sin referencia | -5 | -10 | -15 |
| Incoherencia objetivo-resultado | — | -10 | -20 |
| APA mal aplicada | -2 | -5 | -10 |
| Dato sin fuente | -5 | -15 | -25 |

---

## 4. Puntaje cuando faltan componentes

Si el tesista entra al sistema con la tesis ya parcialmente hecha y algunos componentes no se evaluaron:
- Excluirlos del promedio ponderado
- Renormalizar los pesos restantes
- Indicar explícitamente qué componentes fueron excluidos y por qué
