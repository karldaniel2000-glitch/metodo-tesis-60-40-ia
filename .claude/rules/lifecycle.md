# Lifecycle: Validación Pre y Post Despacho

El orquestador ejecuta estas validaciones antes y después de cada skill. Sin excepción.

---

## Validación PRE-despacho

Antes de despachar cualquier skill, el orquestador lee su entrada en `permissions.md` y verifica:

1. **Los artefactos REQUIERE existen:**
   - Para rutas de archivo: confirmar que el archivo existe y no está vacío
   - Para datos del tesista (en `analizar`): confirmar que el tesista ha subido datos reales
   - Para puntajes previos: leer el research journal para el puntaje más reciente

2. **Si la validación PRE falla:**
   - NO despachar el skill
   - Reportar: "No puedo ejecutar [skill]: falta [artefacto específico]"
   - Sugerir: "Ejecuta [skill previo] primero para generar [artefacto]"

---

## Validación POST-despacho

Después de que un skill completa, antes de avanzar:

1. **Los artefactos PRODUCE existen:**
   - Verificar que el archivo fue creado o actualizado
   - Verificar que las secciones requeridas están presentes

2. **El puntaje del critic está registrado:**
   - El critic pareado produjo su reporte
   - El puntaje está en el research journal

3. **Si la validación POST falla:**
   - NO avanzar a la siguiente fase
   - Reportar: "El skill [nombre] completó pero el output está incompleto: [detalles]"
   - Re-despachar con las brechas indicadas

---

## Principio Fail-Fast

- Reportar el problema inmediatamente con un mensaje claro y accionable
- Nunca despachar un skill con inputs faltantes esperando que "funcione igual"
- Nunca avanzar con outputs incompletos
- El orquestador incluye el fallo de validación en su reporte al tesista
