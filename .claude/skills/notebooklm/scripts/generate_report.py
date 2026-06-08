#!/usr/bin/env python3
"""
Generate a Studio report (study guide, briefing doc, FAQ, timeline, etc.)
from a NotebookLM notebook.

Modes:
  diagnose  - Dump candidate buttons from the page (for selector discovery)
  generate  - Click a report-type button, wait for generation, extract text

Examples:
  python scripts/run.py generate_report.py diagnose --notebook-url URL
  python scripts/run.py generate_report.py generate --type study-guide --notebook-url URL
  python scripts/run.py generate_report.py generate --type briefing --output guide.md
"""

import argparse
import sys
import time
import re
from pathlib import Path

from patchright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from notebook_manager import NotebookLibrary
from browser_utils import BrowserFactory, StealthUtils


# Map our CLI type → (aria_label_regex of option button inside "Informes" submenu)
REPORT_TYPE_LABELS = {
    "study-guide": re.compile(r"^Guía de estudio$", re.IGNORECASE),
    "briefing": re.compile(r"^Documento informativo$", re.IGNORECASE),
    "blog": re.compile(r"^Entrada de blog$", re.IGNORECASE),
    "custom": re.compile(r"^Crea tu propio informe$", re.IGNORECASE),
}


def open_notebook(playwright, notebook_url, headless):
    """Launch context and navigate to the notebook. Returns (context, page)."""
    context = BrowserFactory.launch_persistent_context(playwright, headless=headless)
    page = context.new_page()
    print(f"  🌐 Opening notebook...")
    page.goto(notebook_url, wait_until="domcontentloaded")
    page.wait_for_url(
        re.compile(r"^https://notebooklm\.google\.com/"), timeout=15000
    )
    # Give Studio panel time to render
    time.sleep(4)
    return context, page


def activate_studio_tab(page):
    """Click the 'Studio' tab so its panel renders. Returns True on success."""
    studio_label = re.compile(r"^\s*Studio\s*$", re.IGNORECASE)
    for sel in ["[role='tab']", ".mat-mdc-tab", "mat-tab"]:
        try:
            els = page.query_selector_all(sel)
        except Exception:
            continue
        for el in els:
            try:
                txt = (el.inner_text() or "").strip()
            except Exception:
                continue
            if studio_label.match(txt):
                try:
                    el.scroll_into_view_if_needed()
                except Exception:
                    pass
                StealthUtils.random_delay(150, 400)
                try:
                    el.click()
                except Exception:
                    continue
                print("  📑 Clicked Studio tab")
                time.sleep(3)  # let the panel populate
                return True
    print("  ⚠️ Could not find Studio tab")
    return False


def collect_button_candidates(page):
    """Return a list of {tag, text, aria, classes} for buttons and role=button elements."""
    candidates = []
    selectors = ["button", "[role='button']", "mat-chip", ".mdc-button", "a"]
    seen = set()
    for sel in selectors:
        try:
            els = page.query_selector_all(sel)
        except Exception:
            continue
        for el in els:
            try:
                txt = (el.inner_text() or "").strip()
                aria = el.get_attribute("aria-label") or ""
                cls = el.get_attribute("class") or ""
                tag = el.evaluate("e => e.tagName.toLowerCase()")
            except Exception:
                continue
            key = (tag, txt[:120], aria[:120])
            if key in seen:
                continue
            seen.add(key)
            if txt or aria:
                candidates.append(
                    {"tag": tag, "text": txt, "aria": aria, "class": cls[:80]}
                )
    return candidates


def click_by_aria(page, aria_label_pattern):
    """Click the first element whose aria-label matches the given regex."""
    rx = re.compile(aria_label_pattern, re.IGNORECASE)
    for sel in ["button", "[role='button']", "div[aria-label]", "[aria-label]"]:
        try:
            els = page.query_selector_all(sel)
        except Exception:
            continue
        for el in els:
            try:
                aria = el.get_attribute("aria-label") or ""
            except Exception:
                continue
            if aria and rx.search(aria):
                try:
                    el.scroll_into_view_if_needed()
                except Exception:
                    pass
                StealthUtils.random_delay(150, 350)
                try:
                    el.click()
                    print(f"  🖱️  Clicked aria='{aria}'")
                    return True
                except Exception:
                    continue
    print(f"  ⚠️ No clickable element with aria matching: {aria_label_pattern}")
    return False


def diagnose(notebook_url, headless, screenshot_path=None, click_aria=None, click_arias=None):
    """Print all visible button candidates on the notebook page."""
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python scripts/run.py auth_manager.py setup")
        return 1

    playwright = sync_playwright().start()
    context = None
    try:
        context, page = open_notebook(playwright, notebook_url, headless)
        # Switch to the Studio tab before collecting elements
        activate_studio_tab(page)
        # Optionally click multiple aria-labels in sequence, then dump
        sequence = []
        if click_arias:
            sequence = [a.strip() for a in click_arias.split("|") if a.strip()]
        elif click_aria:
            sequence = [click_aria]
        for pat in sequence:
            time.sleep(2)
            click_by_aria(page, pat)
            time.sleep(3)
        # Extra wait so Studio cards have time to render
        time.sleep(6)

        print(f"\n📍 URL: {page.url}")
        print(f"📍 Title: {page.title()}")

        print("\n🔍 DIAGNOSE: collecting interactive elements...")
        cands = collect_button_candidates(page)
        print(f"\nFound {len(cands)} button/role-button/chip candidates:\n")
        for i, c in enumerate(cands):
            text = c["text"].replace("\n", " ⏎ ")[:140]
            aria = c["aria"][:120]
            print(f"  [{i:3d}] <{c['tag']}> text={text!r}  aria={aria!r}")

        # Dump mat-card elements (where Studio artifact cards likely live)
        print("\n--- mat-card / artifact card candidates ---")
        mat_cards = []
        for sel in [
            "mat-card",
            ".mat-mdc-card",
            "[data-test-id*='artifact']",
            "[class*='artifact']",
            "[class*='studio']",
            "[class*='Studio']",
            "[id*='studio']",
        ]:
            try:
                els = page.query_selector_all(sel)
            except Exception:
                continue
            for el in els:
                try:
                    text = (el.inner_text() or "").strip()
                    aria = el.get_attribute("aria-label") or ""
                    cls = (el.get_attribute("class") or "")[:120]
                    if text or aria:
                        mat_cards.append((sel, text[:200], aria[:120], cls))
                except Exception:
                    continue
        if mat_cards:
            for i, (sel, txt, aria, cls) in enumerate(mat_cards):
                t = txt.replace("\n", " ⏎ ")
                print(f"  [{i:3d}] sel={sel} text={t!r} aria={aria!r} class={cls!r}")
        else:
            print("  (none found)")

        # Dump tab elements
        print("\n--- tabs / tablists ---")
        for sel in ["[role='tab']", "[role='tablist']", "mat-tab", ".mat-mdc-tab"]:
            try:
                els = page.query_selector_all(sel)
            except Exception:
                continue
            for el in els:
                try:
                    text = (el.inner_text() or "").strip()
                    aria = el.get_attribute("aria-label") or ""
                    if text or aria:
                        print(f"  sel={sel} text={text[:100]!r} aria={aria[:100]!r}")
                except Exception:
                    continue

        # Look for keywords anywhere in the visible body
        print("\n--- text search in body for key terms ---")
        try:
            body_text = page.inner_text("body")
        except Exception:
            body_text = ""
        for keyword in [
            "Guía de estudio",
            "Study guide",
            "Briefing",
            "FAQ",
            "Cronología",
            "Timeline",
            "Mapa mental",
            "Mind map",
            "Studio",
            "Estudio",
            "Resumen de audio",
            "Audio Overview",
            "Informe",
        ]:
            if keyword.lower() in body_text.lower():
                print(f"  ✓ FOUND keyword: {keyword!r}")
            else:
                print(f"  ✗ not present: {keyword!r}")

        # Save screenshot for inspection
        if screenshot_path:
            try:
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"\n📸 Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"  ⚠️ Could not save screenshot: {e}")

        return 0
    finally:
        if context:
            try:
                context.close()
            except Exception:
                pass
        try:
            playwright.stop()
        except Exception:
            pass


def click_aria_exact(page, aria_regex):
    """Click first visible element whose aria-label matches the given regex."""
    for sel in ["button", "[role='button']", "div[aria-label]", "[aria-label]"]:
        try:
            els = page.query_selector_all(sel)
        except Exception:
            continue
        for el in els:
            try:
                aria = el.get_attribute("aria-label") or ""
                if not aria_regex.search(aria):
                    continue
                if not el.is_visible():
                    continue
                el.scroll_into_view_if_needed()
                StealthUtils.random_delay(120, 320)
                el.click()
                return True
            except Exception:
                continue
    return False


def click_text_exact(page, text_regex):
    """Click first visible button whose visible text matches the regex."""
    for sel in ["button", "[role='button']"]:
        try:
            els = page.query_selector_all(sel)
        except Exception:
            continue
        for el in els:
            try:
                txt = (el.inner_text() or "").strip()
                if not text_regex.search(txt):
                    continue
                if not el.is_visible():
                    continue
                el.scroll_into_view_if_needed()
                StealthUtils.random_delay(120, 320)
                el.click()
                return True
            except Exception:
                continue
    return False


def wait_for_completed_artifact(page, timeout_seconds=600):
    """
    Wait until an artifact card is no longer in the "Generando informe…" / shimmer state.
    Returns the finished card element (the most recent completed one).
    """
    print(f"  ⏳ Waiting for artifact generation to finish (up to {timeout_seconds}s)...")
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            cards = page.query_selector_all(".artifact-item-button")
        except Exception:
            cards = []

        if cards:
            # A card is "generating" if its class contains 'shimmer' or it shows
            # 'Generando informe…' text.
            still_generating = False
            finished_cards = []
            for c in cards:
                try:
                    if not c.is_visible():
                        continue
                    cls = c.get_attribute("class") or ""
                    txt = (c.inner_text() or "").strip()
                except Exception:
                    continue
                if "shimmer" in cls or "Generando informe" in txt:
                    still_generating = True
                else:
                    finished_cards.append(c)

            # If there's at least one finished card AND no shimmering one,
            # return the first (most recently created sits at the top).
            if finished_cards and not still_generating:
                return finished_cards[0]
        time.sleep(3)
    return None


def extract_artifact_text(page, timeout_seconds=180):
    """After the artifact panel opens, wait for stable substantial text and return it."""
    print(f"  ⏳ Extracting artifact content (up to {timeout_seconds}s)...")
    deadline = time.time() + timeout_seconds
    last_text = None
    stable_count = 0

    content_selectors = [
        ".artifact-display",
        ".artifact-content",
        ".artifact-body",
        ".mat-mdc-dialog-content",
        "[class*='artifact-display']",
        "[class*='artifact-content']",
        "article",
    ]

    while time.time() < deadline:
        spinner_visible = False
        for s in [
            "mat-spinner",
            ".mat-mdc-progress-spinner",
            ".loading-indicator",
        ]:
            try:
                el = page.query_selector(s)
                if el and el.is_visible():
                    spinner_visible = True
                    break
            except Exception:
                pass
        if spinner_visible:
            time.sleep(2)
            continue

        for sel in content_selectors:
            try:
                els = page.query_selector_all(sel)
            except Exception:
                continue
            for el in els:
                try:
                    if not el.is_visible():
                        continue
                    text = el.inner_text().strip()
                except Exception:
                    continue
                if text and len(text) > 400:
                    if text == last_text:
                        stable_count += 1
                        if stable_count >= 3:
                            return text
                    else:
                        stable_count = 0
                        last_text = text
        time.sleep(2)
    return last_text


def generate(notebook_url, report_type, headless, output_path):
    """Studio → Informes → <type> → Generar → wait → open → extract."""
    if report_type not in REPORT_TYPE_LABELS:
        print(f"❌ Unknown type '{report_type}'. Valid: {', '.join(REPORT_TYPE_LABELS)}")
        return 1
    type_regex = REPORT_TYPE_LABELS[report_type]

    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python scripts/run.py auth_manager.py setup")
        return 1

    print(f"📝 Generating report type: {report_type}")
    print(f"📚 Notebook: {notebook_url}")

    playwright = sync_playwright().start()
    context = None
    try:
        context, page = open_notebook(playwright, notebook_url, headless)

        if not activate_studio_tab(page):
            print("  ❌ Could not open Studio tab")
            return 2
        time.sleep(2)

        # Click "Informes" tile to open the report submenu
        print("  🖱️  Opening 'Informes' submenu...")
        if not click_aria_exact(page, re.compile(r"^Informes$", re.IGNORECASE)):
            print("  ❌ Could not find 'Informes' tile")
            return 3
        time.sleep(2)

        # Click the report format option — this auto-submits generation
        # (the visible "Generar" button only applies to 'Crea tu propio informe').
        print(f"  🖱️  Selecting report format: {type_regex.pattern}")
        if not click_aria_exact(page, type_regex):
            print(f"  ❌ Could not find report format option matching {type_regex.pattern}")
            return 4

        # Wait for the artifact card to finish generating
        card = wait_for_completed_artifact(page)
        if not card:
            print("  ❌ Artifact did not finish within timeout")
            return 6
        print("  ✅ Artifact finished. Opening...")
        try:
            card.scroll_into_view_if_needed()
        except Exception:
            pass
        StealthUtils.random_delay(300, 700)
        try:
            card.click()
        except Exception:
            pass
        time.sleep(4)

        text = extract_artifact_text(page)
        if not text:
            print("  ❌ Could not extract artifact text")
            return 7

        print("  ✅ Captured report content.")
        if output_path:
            Path(output_path).write_text(text, encoding="utf-8")
            print(f"  💾 Saved to {output_path}")
        else:
            print("\n" + "=" * 60)
            print(text)
            print("=" * 60)
        return 0

    finally:
        if context:
            try:
                context.close()
            except Exception:
                pass
        try:
            playwright.stop()
        except Exception:
            pass


def resolve_notebook_url(args):
    if args.notebook_url:
        return args.notebook_url
    if args.notebook_id:
        lib = NotebookLibrary()
        nb = lib.get_notebook(args.notebook_id)
        if nb:
            return nb["url"]
        print(f"❌ Notebook '{args.notebook_id}' not found in library")
        return None
    lib = NotebookLibrary()
    active = lib.get_active_notebook()
    if active:
        print(f"📚 Using active notebook: {active['name']}")
        return active["url"]
    print("❌ No notebook URL provided and no active notebook.")
    return None


def main():
    parser = argparse.ArgumentParser(description="Generate a Studio report from NotebookLM")
    sub = parser.add_subparsers(dest="command", required=True)

    d = sub.add_parser("diagnose", help="Dump candidate buttons for selector discovery")
    d.add_argument("--notebook-url")
    d.add_argument("--notebook-id")
    d.add_argument("--show-browser", action="store_true")
    d.add_argument("--screenshot", help="Save a full-page screenshot to this path")
    d.add_argument(
        "--click-aria",
        help="After opening Studio, click first element whose aria-label matches this regex",
    )
    d.add_argument(
        "--click-arias",
        help="Sequence of aria-label regexes to click (separated by '|')",
    )

    g = sub.add_parser("generate", help="Generate a report")
    g.add_argument(
        "--type",
        required=True,
        choices=sorted(REPORT_TYPE_LABELS.keys()),
        help="Report type to generate",
    )
    g.add_argument("--notebook-url")
    g.add_argument("--notebook-id")
    g.add_argument("--output", help="Save report text to this file")
    g.add_argument("--show-browser", action="store_true")

    args = parser.parse_args()

    url = resolve_notebook_url(args)
    if not url:
        return 1

    headless = not args.show_browser

    if args.command == "diagnose":
        return diagnose(
            url,
            headless,
            getattr(args, "screenshot", None),
            getattr(args, "click_aria", None),
            getattr(args, "click_arias", None),
        )
    elif args.command == "generate":
        return generate(url, args.type, headless, args.output)


if __name__ == "__main__":
    sys.exit(main())
