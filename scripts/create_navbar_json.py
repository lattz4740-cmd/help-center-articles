#!/usr/bin/env python3
"""Create navbar.json translation files for all locales.

The navbar items "About Outline", "Outline Client", "Outline Manager" need
translations. We can pull these from the old current.json sidebar category
translations (which we just removed) — they're in the code.json homepage
title keys.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Navbar translation key format for docSidebar items
# See: https://docusaurus.io/docs/i18n/tutorial#translate-plugin-data
NAVBAR_KEYS = {
    "item.label.About Outline": {
        "code_json_key": "homepage.about.title",
        "default": "About Outline",
        "description": "Navbar item with label 'About Outline'",
    },
    "item.label.Outline Client": {
        "code_json_key": "homepage.client.title",
        "default": "Outline Client",
        "description": "Navbar item with label 'Outline Client'",
    },
    "item.label.Outline Manager": {
        "code_json_key": "homepage.manager.title",
        "default": "Outline Manager",
        "description": "Navbar item with label 'Outline Manager'",
    },
}

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name != "partial-translations"
)

created = 0
for locale in locales:
    theme_dir = I18N / locale / "docusaurus-theme-classic"
    theme_dir.mkdir(parents=True, exist_ok=True)

    navbar_path = theme_dir / "navbar.json"

    # Read code.json for translations
    code_path = I18N / locale / "code.json"
    code = {}
    if code_path.exists():
        code = json.loads(code_path.read_text("utf-8"))

    navbar = {}
    for key, info in NAVBAR_KEYS.items():
        code_entry = code.get(info["code_json_key"], {})
        message = code_entry.get("message", info["default"])
        navbar[key] = {
            "message": message,
            "description": info["description"],
        }

    navbar_path.write_text(json.dumps(navbar, ensure_ascii=False, indent=2) + "\n", "utf-8")
    created += 1
    print(f"  CREATED {locale}")

print(f"\nCreated {created} navbar.json files")
