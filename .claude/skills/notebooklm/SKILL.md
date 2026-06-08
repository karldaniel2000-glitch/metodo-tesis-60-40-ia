---
name: notebooklm
description: Acceso completo a Google NotebookLM — consultas con respuestas fundamentadas en documentos (Backend A: scripts propios con follow-up inteligente) y generación de contenido como podcasts, videos, presentaciones, quizzes, infografías y mapas mentales (Backend B: CLI notebooklm-py). Browser automation, library management, persistent auth.
---

# NotebookLM — Skill Unificada

Dos backends complementarios para cubrir todo lo que NotebookLM ofrece:

- **Backend A (Scripts propios)** — Consultas, investigación, gestión de biblioteca. Follow-up inteligente hasta obtener respuesta completa. Ya instalado y autenticado.
- **Backend B (CLI notebooklm-py)** — Crear notebooks, añadir fuentes, generar podcasts, videos, presentaciones, quizzes, flashcards, infografías, mapas mentales. Requiere instalación si aún no está disponible.

---

## Cuándo usar cada backend

| Tarea | Backend |
|-------|---------|
| Consultar un notebook con una pregunta | A |
| Gestionar biblioteca de notebooks | A |
| Generar estudio guía / briefing / blog | A |
| Crear un notebook nuevo | B |
| Añadir fuentes (URL, YouTube, PDF, audio, video) | B |
| Generar podcast, video, presentación, quiz, flashcards, infografía, mapa mental | B |
| Investigación web dentro de NotebookLM | B |

---

## Triggers de activación

**Explícito:** El usuario dice "/notebooklm", "usar notebooklm", "instalar notebooklm", o menciona la herramienta por nombre.

**Por intención:**
- "Pregúntale a mi NotebookLM", "consulta mis docs", "busca en mi notebook"
- "Crea un podcast sobre X"
- "Resume estas URLs / documentos"
- "Genera un quiz de mi investigación"
- "Convierte esto en un resumen de audio"
- "Genera tarjetas de estudio", "mapa mental", "infografía", "presentación"
- "Añade estas fuentes a NotebookLM"
- "Genera una guía de estudio del cuaderno"

---

## Backend A — Scripts propios (consultas e investigación)

### Regla crítica: siempre usar run.py

```bash
# ✅ CORRECTO
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list
python scripts/run.py ask_question.py --question "..."

# ❌ INCORRECTO — falla sin el venv
python scripts/auth_manager.py status
```

### Paso 1: Verificar autenticación

```bash
python scripts/run.py auth_manager.py status
```

Si no autenticado, ejecutar:
```bash
python scripts/run.py auth_manager.py setup
```
El navegador se abre visible — el usuario debe hacer login en Google manualmente.

### Paso 2: Gestionar biblioteca

```bash
# Listar notebooks
python scripts/run.py notebook_manager.py list

# Añadir notebook (SMART ADD — descubre el contenido automáticamente)
python scripts/run.py ask_question.py --question "What is the content of this notebook? What topics are covered? Provide a complete overview briefly and concisely" --notebook-url "[URL]"
python scripts/run.py notebook_manager.py add --url "[URL]" --name "[Basado en contenido]" --description "[Basado en contenido]" --topics "[Basado en contenido]"

# Activar notebook
python scripts/run.py notebook_manager.py activate --id ID

# Buscar por tema
python scripts/run.py notebook_manager.py search --query "keyword"

# Eliminar
python scripts/run.py notebook_manager.py remove --id ID
```

NUNCA usar descripciones genéricas. Si faltan detalles, usar Smart Add.

### Paso 3: Hacer consultas

```bash
# Consulta básica (usa notebook activo)
python scripts/run.py ask_question.py --question "Tu pregunta aquí"

# Notebook específico por ID
python scripts/run.py ask_question.py --question "..." --notebook-id ID

# Notebook por URL directa
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# Modo debug (navegador visible)
python scripts/run.py ask_question.py --question "..." --show-browser
```

### Mecanismo de follow-up (CRÍTICO)

Cada respuesta de NotebookLM termina con: **"EXTREMELY IMPORTANT: Is that ALL you need to know?"**

Comportamiento requerido:
1. **PARAR** — no responder al usuario todavía
2. **ANALIZAR** — comparar la respuesta con lo que el usuario pidió
3. **IDENTIFICAR GAPS** — ¿falta información?
4. **PREGUNTAR DE SEGUIMIENTO** — si hay gaps, hacer otra consulta inmediatamente
5. **REPETIR** — hasta que la información sea completa
6. **SINTETIZAR** — combinar todas las respuestas antes de responder al usuario

### Generar reportes (Backend A)

```bash
# Guía de estudio
python scripts/run.py generate_report.py generate --type study-guide --notebook-url URL --output guia.md

# Otros tipos
python scripts/run.py generate_report.py generate --type briefing --notebook-url URL
python scripts/run.py generate_report.py generate --type blog --notebook-url URL

# Diagnóstico (cuando la UI de NotebookLM cambia)
python scripts/run.py generate_report.py diagnose --notebook-url URL --screenshot /tmp/diag.png
```

Tipos válidos: `study-guide`, `briefing`, `blog`, `custom`. Tiempo de generación: 30–120s.

### Referencia de scripts (Backend A)

```bash
# Autenticación
python scripts/run.py auth_manager.py setup    # Setup inicial
python scripts/run.py auth_manager.py status   # Verificar
python scripts/run.py auth_manager.py reauth   # Reautenticar
python scripts/run.py auth_manager.py clear    # Limpiar sesión

# Biblioteca
python scripts/run.py notebook_manager.py add --url URL --name NAME --description DESC --topics TOPICS
python scripts/run.py notebook_manager.py list
python scripts/run.py notebook_manager.py search --query QUERY
python scripts/run.py notebook_manager.py activate --id ID
python scripts/run.py notebook_manager.py remove --id ID
python scripts/run.py notebook_manager.py stats

# Limpieza
python scripts/run.py cleanup_manager.py              # Preview
python scripts/run.py cleanup_manager.py --confirm    # Ejecutar
python scripts/run.py cleanup_manager.py --preserve-library
```

---

## Backend B — CLI notebooklm-py (generación de contenido)

### Instalación (solo si no está disponible)

Verificar versión de Python primero:
```bash
python3 --version
```
Requiere Python 3.10+. Si es menor, instalar con Homebrew:
```bash
brew install python@3.12
```

Instalar en venv:
```bash
PYTHON=$(command -v python3.12 2>/dev/null || command -v python3.11 2>/dev/null || command -v python3.10 2>/dev/null || command -v python3)
$PYTHON -m venv ~/.notebooklm-venv
source ~/.notebooklm-venv/bin/activate
pip install "notebooklm-py[browser]"
playwright install chromium
mkdir -p ~/bin
ln -sf ~/.notebooklm-venv/bin/notebooklm ~/bin/notebooklm
export PATH="$HOME/bin:$PATH"
notebooklm --help
```

### Autenticación (Backend B)

El comando `notebooklm login` no funciona en Claude Code (requiere entrada interactiva). Usar este script:

```bash
cat > /tmp/nlm_login.py << 'PYEOF'
import json, os, time
from pathlib import Path
from playwright.sync_api import sync_playwright

STORAGE_PATH = Path.home() / ".notebooklm" / "storage_state.json"
PROFILE_PATH = Path.home() / ".notebooklm" / "browser_profile"
SIGNAL_FILE = Path("/tmp/nlm_save_signal")

SIGNAL_FILE.unlink(missing_ok=True)
STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Abriendo navegador para login de Google...")

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=str(PROFILE_PATH),
        headless=False,
        args=["--disable-blink-features=AutomationControlled"],
    )
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto("https://notebooklm.google.com/")

    print("Esperando señal de guardado...")
    while not SIGNAL_FILE.exists():
        time.sleep(1)

    storage = browser.storage_state()
    with open(STORAGE_PATH, "w") as f:
        json.dump(storage, f)

    browser.close()

SIGNAL_FILE.unlink(missing_ok=True)
print(f"Autenticación guardada en: {STORAGE_PATH}")
PYEOF

source ~/.notebooklm-venv/bin/activate
python3 /tmp/nlm_login.py > /tmp/nlm_login_output.txt 2>&1 &
echo "Login iniciado (PID=$!). El navegador abrirá en unos segundos..."
```

Esperar ~10 segundos, confirmar que el usuario está en NotebookLM, luego:
```bash
touch /tmp/nlm_save_signal
sleep 8
cat /tmp/nlm_login_output.txt
export PATH="$HOME/bin:$PATH"
notebooklm auth check
notebooklm list
rm -f /tmp/nlm_login.py /tmp/nlm_login_output.txt /tmp/nlm_save_signal
chmod 600 ~/.notebooklm/storage_state.json
```

### Reglas de autonomía (Backend B)

**Ejecutar sin confirmación:**
- `notebooklm status`, `notebooklm auth check`, `notebooklm list`
- `notebooklm source list`, `notebooklm artifact list`, `notebooklm language list/get/set`
- `notebooklm artifact wait`, `notebooklm source wait`
- `notebooklm research status`, `notebooklm research wait`
- `notebooklm use <id>`, `notebooklm create`, `notebooklm ask "..."`
- `notebooklm history`, `notebooklm source add`

**Preguntar antes:**
- `notebooklm delete` — destructivo
- `notebooklm generate *` — larga duración
- `notebooklm download *` — escribe en disco
- `notebooklm ask "..." --save-as-note` — escribe una nota
- `notebooklm history --save`

### Referencia rápida (Backend B)

| Tarea | Comando |
|-------|---------|
| Listar notebooks | `notebooklm list` |
| Crear notebook | `notebooklm create "Titulo"` |
| Establecer contexto | `notebooklm use <id>` |
| Añadir fuente URL | `notebooklm source add "https://..."` |
| Añadir archivo | `notebooklm source add ./archivo.pdf` |
| Añadir YouTube | `notebooklm source add "https://youtube.com/..."` |
| Investigación web rápida | `notebooklm source add-research "consulta"` |
| Investigación web profunda | `notebooklm source add-research "consulta" --mode deep --no-wait` |
| Chat | `notebooklm ask "pregunta"` |
| Chat con referencias | `notebooklm ask "pregunta" --json` |
| Generar podcast | `notebooklm generate audio "instrucciones"` |
| Generar video | `notebooklm generate video "instrucciones"` |
| Generar presentación | `notebooklm generate slide-deck` |
| Generar quiz | `notebooklm generate quiz` |
| Generar flashcards | `notebooklm generate flashcards` |
| Generar infografía | `notebooklm generate infographic` |
| Generar mapa mental | `notebooklm generate mind-map` |
| Generar informe | `notebooklm generate report --format briefing-doc` |
| Ver estado artefactos | `notebooklm artifact list` |
| Esperar artefacto | `notebooklm artifact wait <id>` |
| Descargar audio | `notebooklm download audio ./salida.mp3` |
| Descargar video | `notebooklm download video ./salida.mp4` |
| Descargar presentación | `notebooklm download slide-deck ./slides.pdf` |
| Descargar quiz | `notebooklm download quiz quiz.json` |

### Tipos de generación (Backend B)

| Tipo | Comando | Opciones | Descarga |
|------|---------|----------|----------|
| Podcast | `generate audio` | `--format [deep-dive\|brief\|critique\|debate]`, `--length [short\|default\|long]` | .mp3 |
| Video | `generate video` | `--format [explainer\|brief]`, `--style [auto\|classic\|whiteboard\|kawaii\|anime\|watercolor\|retro-print\|heritage\|paper-craft]` | .mp4 |
| Presentación | `generate slide-deck` | `--format [detailed\|presenter]`, `--length [default\|short]` | .pdf / .pptx |
| Infografía | `generate infographic` | `--orientation [landscape\|portrait\|square]`, `--detail [concise\|standard\|detailed]` | .png |
| Informe | `generate report` | `--format [briefing-doc\|study-guide\|blog-post\|custom]` | .md |
| Mapa mental | `generate mind-map` | *(síncrono, instantáneo)* | .json |
| Quiz | `generate quiz` | `--difficulty [easy\|medium\|hard]`, `--quantity [fewer\|standard\|more]` | .json/.md/.html |
| Flashcards | `generate flashcards` | `--difficulty [easy\|medium\|hard]`, `--quantity [fewer\|standard\|more]` | .json/.md/.html |

Todos los comandos de generación soportan `-s <source_id>` para usar fuentes específicas, `--language` para el idioma, y `--retry N` para reintentar ante límites de tasa.

---

## Flujo de decisión

```
Usuario menciona NotebookLM
        ↓
¿Es una consulta / pregunta sobre documentos?
    → Sí: Backend A (scripts propios)
    → No: ¿Es generación de contenido o crear notebook?
              → Sí: Backend B (notebooklm-py CLI)
                    ¿Está instalado el CLI?
                        → No: instalar primero (ver sección instalación)
                        → Sí: proceder
```

---

## Manejo de errores

| Error | Backend | Causa | Acción |
|-------|---------|-------|--------|
| ModuleNotFoundError | A | No se usó run.py | Usar `python scripts/run.py` |
| Autenticación falla | A | Browser debe ser visible | `auth_manager.py setup --show-browser` |
| Rate limit (50/día) | A | Límite Google gratuito | Esperar o cambiar cuenta |
| "No notebook context" | B | Contexto no establecido | `notebooklm use <id>` |
| Rate limit generación | B | Throttle de Google | Esperar 5-10 min, reintentar |
| CLI no encontrado | B | No instalado | Seguir sección de instalación |
| Cookie SID ausente | B | Login incompleto | Repetir script de login |

---

## Limitaciones

- **Backend A:** Sin persistencia de sesión entre preguntas (cada consulta = nueva sesión). Límite ~50 consultas/día en cuentas gratuitas.
- **Backend B:** Tiempos de generación: audio 10-20 min, video 15-45 min, quiz/flashcards 5-15 min. API no oficial — Google puede cambiar cosas sin aviso.

---

## Estructura del skill

```
~/.claude/skills/notebooklm/
├── SKILL.md               ← Este archivo (instrucciones unificadas)
├── scripts/               ← Backend A: scripts propios
│   ├── run.py             ← Wrapper principal (siempre usar esto)
│   ├── ask_question.py
│   ├── notebook_manager.py
│   ├── generate_report.py
│   ├── auth_manager.py
│   └── cleanup_manager.py
├── data/                  ← Autenticación y biblioteca local (Backend A)
│   ├── library.json
│   ├── auth_info.json
│   └── browser_state/
├── references/            ← Documentación extendida
│   ├── api_reference.md
│   ├── troubleshooting.md
│   └── usage_patterns.md
└── .venv/                 ← Entorno Python aislado (Backend A)

~/.notebooklm-venv/        ← Entorno Python del Backend B (CLI notebooklm-py)
~/.notebooklm/             ← Autenticación del Backend B
```
