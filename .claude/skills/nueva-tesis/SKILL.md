---
name: nueva-tesis
description: Pipeline completo desde cero. Orquesta todas las fases desde idea hasta tesis lista para sustentar. Activar cuando el usuario diga "quiero hacer mi tesis desde cero", "empieza mi tesis", "nuevo proyecto de tesis", o cuando se quiera lanzar el pipeline completo. Este es el único skill siempre orquestado — nunca corre en modo standalone.
argument-hint: "[tema o idea inicial]"
allowed-tools: Read,Write,Edit,Glob
---

# Nueva Tesis — Pipeline Completo

Orquesta el pipeline de investigación completo desde la idea inicial hasta la tesis lista para defender.

---

## Instrucciones

### Paso 1: Diagnóstico (siempre primero)

Despachar `/diagnostico` con la descripción inicial del tesista.
- Esperar resultados del diagnóstico
- Presentar hoja de ruta al tesista
- Obtener aprobación antes de continuar

### Paso 2: Planificación (secuencial)

Con el diagnóstico aprobado, recorrer en orden:
1. `/planificar titulo` → aprobación del tesista
2. `/planificar problema` → aprobación
3. `/planificar objetivos` → aprobación
4. `/planificar variables` → aprobación
5. `/planificar metodologia` → aprobación
6. `/planificar consistencia` → verificación del auditor → aprobación

**Regla:** Cada elemento requiere aprobación explícita del tesista antes de continuar. No asumir aprobación silenciosa.

**Paralelo permitido:** `/literatura` puede correr mientras se trabaja en objetivos o metodología, ya que no depende de esos outputs.

### Paso 3: Desarrollo (paralelo posible)

Con planificación aprobada, despachar según disponibilidad:

**Secuencia obligatoria:**
- Marco teórico requiere: literatura aprobada
- Metodología detallada requiere: metodología de planificación aprobada
- Resultados requieren: datos reales del tesista
- Discusión requiere: resultados redactados
- Conclusiones requieren: discusión redactada

**Paralelo posible:** Marco teórico + Metodología detallada pueden correr simultáneamente

### Paso 4: Refinamiento

Con al menos 80% de secciones redactadas:
1. `/revisar todo` → reporte integrado
2. Si puntaje < 80 en algún componente: `/corregir [sección]`
3. Loop hasta que todos los componentes >= 80
4. `/revisar todo` final → debe dar >= 85 global

### Paso 5: Presentación

Con tesis aprobada en refinamiento:
- `/sustentar` → estructura de defensa oral

---

## Puntos de pausa obligatoria (esperar decisión del tesista)

1. Después del diagnóstico → antes de iniciar planificación
2. Después de formular el problema → antes de objetivos
3. Después de variables → antes de metodología (puede cambiar el diseño)
4. Antes de recolectar/procesar datos → confirmar instrumentos
5. Después del reporte de coherencia → si hay brechas críticas
6. Antes de `/sustentar` → confirmar que la tesis está lista

---

## Comunicación al tesista

Al inicio de cada fase:
- Anunciar qué se va a hacer y por qué
- Indicar qué input necesita del tesista si lo hay
- Estimar duración o número de intercambios

Al final de cada fase:
- Presentar lo producido
- Indicar el puntaje de calidad
- Sugerir el siguiente paso
- Esperar confirmación
