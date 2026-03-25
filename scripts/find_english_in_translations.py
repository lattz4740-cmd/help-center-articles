#!/usr/bin/env python3
"""Find code.json entries where the translated message is identical to the English default.

Compares against English defaults extracted from source files.
Skips en-GB since it legitimately uses English.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
SRC = ROOT / "src"

# Extract English defaults from source
english_defaults: dict[str, str] = {}

for f in SRC.rglob("*.tsx"):
    text = f.read_text("utf-8")
    # Static: <Translate id="some.id">Default text</Translate>
    for m in re.finditer(
        r'<Translate\s+id=["\']([^"\']+)["\']>\s*\n?\s*(.+?)\s*\n?\s*</Translate>',
        text, re.DOTALL,
    ):
        english_defaults[m.group(1)] = m.group(2).strip()
    # Dynamic: card definitions
    for m in re.finditer(
        r"(\w+)Id:\s*'(homepage\.[^']+)'.*?\1:\s*'([^']+)'",
        text, re.DOTALL,
    ):
        english_defaults[m.group(2)] = m.group(3)

# Also check navbar.json keys
config_text = (ROOT / "docusaurus.config.ts").read_text("utf-8")
navbar_match = re.search(r'navbar:\s*\{.*?items:\s*\[(.*?)\]', config_text, re.DOTALL)
navbar_defaults: dict[str, str] = {}
if navbar_match:
    for m in re.finditer(r"label:\s*'([^']+)'", navbar_match.group(1)):
        navbar_defaults[f"item.label.{m.group(1)}"] = m.group(1)

print("English defaults found:")
for k, v in sorted(english_defaults.items()):
    print(f"  {k} = {v!r}")
print()

# Scan all locales
matches_by_key: dict[str, list[str]] = {}

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name not in ("partial-translations", "en", "en-GB")
)

for locale in locales:
    # Check code.json
    code_path = I18N / locale / "code.json"
    if code_path.exists():
        data = json.loads(code_path.read_text("utf-8"))
        for key, english in english_defaults.items():
            entry = data.get(key, {})
            msg = entry.get("message", "") if isinstance(entry, dict) else ""
            if msg == english:
                matches_by_key.setdefault(key, []).append(locale)

    # Check navbar.json
    navbar_path = I18N / locale / "docusaurus-theme-classic" / "navbar.json"
    if navbar_path.exists():
        data = json.loads(navbar_path.read_text("utf-8"))
        for key, english in navbar_defaults.items():
            entry = data.get(key, {})
            msg = entry.get("message", "") if isinstance(entry, dict) else ""
            if msg == english:
                matches_by_key.setdefault(key, []).append(locale)

print("Untranslated strings (message == English default):")
for key in sorted(matches_by_key):
    locales_list = matches_by_key[key]
    english = english_defaults.get(key) or navbar_defaults.get(key)
    print(f"\n  {key} = {english!r}")
    print(f"    {len(locales_list)} locales: {', '.join(locales_list)}")
