#!/usr/bin/env python3
"""Add 'For Developers' translation to all navbar.json files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name != "partial-translations"
)

updated = 0
for locale in locales:
    navbar_path = I18N / locale / "docusaurus-theme-classic" / "navbar.json"
    if not navbar_path.exists():
        continue

    navbar = json.loads(navbar_path.read_text("utf-8"))

    # Get the "For Developers" translation from code.json
    code_path = I18N / locale / "code.json"
    code = {}
    if code_path.exists():
        code = json.loads(code_path.read_text("utf-8"))

    dev_entry = code.get("homepage.developers.title", {})
    message = dev_entry.get("message", "For Developers")

    navbar["item.label.For Developers"] = {
        "message": message,
        "description": "Navbar item with label 'For Developers'",
    }

    navbar_path.write_text(json.dumps(navbar, ensure_ascii=False, indent=2) + "\n", "utf-8")
    updated += 1

print(f"Updated {updated} navbar.json files with 'For Developers' translation")
