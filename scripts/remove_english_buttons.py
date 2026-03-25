#!/usr/bin/env python3
"""Remove obviously untranslated English button/description strings from code.json.

These were incorrectly filled in with English during initial generation.
Removing them causes Docusaurus to fall back to the English default (same
visual result) but makes it clear these need translation.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# English UI strings that should NOT appear verbatim in non-English locales
ENGLISH_TO_REMOVE = {
    "Learn more",
    "Get started",
    "Set up a server",
    "Integrate the Outline SDK into your application.",
    "Explore the SDK",
}

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name not in ("partial-translations", "en", "en-GB")
)

total_removed = 0
for locale in locales:
    code_path = I18N / locale / "code.json"
    if not code_path.exists():
        continue

    data = json.loads(code_path.read_text("utf-8"))
    keys_to_remove = []

    for key, entry in data.items():
        if isinstance(entry, dict) and entry.get("message") in ENGLISH_TO_REMOVE:
            keys_to_remove.append(key)

    if keys_to_remove:
        for key in keys_to_remove:
            del data[key]
            total_removed += 1
            print(f"  {locale}: removed {key}")
        code_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", "utf-8")

print(f"\nRemoved {total_removed} untranslated English strings")
