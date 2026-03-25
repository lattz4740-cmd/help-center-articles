#!/usr/bin/env python3
"""Remove obviously untranslated English description strings from code.json files.

These were incorrectly filled in with English during initial code.json generation.
Removing them will cause Docusaurus to fall back to the English default, which is
the same result visually but makes it clear these need translation.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# English strings that were copied verbatim into translations
ENGLISH_STRINGS_TO_REMOVE = {
    "Get started with connecting your device and troubleshooting.",
    "Set up and manage your Outline server.",
}

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name != "partial-translations" and p.name != "en"
)

total_removed = 0
for locale in locales:
    code_path = I18N / locale / "code.json"
    if not code_path.exists():
        continue

    data = json.loads(code_path.read_text("utf-8"))
    changed = False

    keys_to_remove = []
    for key, entry in data.items():
        if isinstance(entry, dict) and entry.get("message") in ENGLISH_STRINGS_TO_REMOVE:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        del data[key]
        changed = True
        total_removed += 1
        print(f"  {locale}: removed {key}")

    if changed:
        code_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", "utf-8")

print(f"\nRemoved {total_removed} untranslated English strings")
