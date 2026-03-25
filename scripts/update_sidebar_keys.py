#!/usr/bin/env python3
"""Update current.json sidebar translation keys after splitting into 3 sidebars.

Old: single helpSidebar with top-level categories for About/Client/Manager/Developers
New: aboutSidebar (flat), clientSidebar, managerSidebar (no developers)

Key changes:
- Remove: sidebar.helpSidebar.category.About Outline (now a sidebar, not category)
- Remove: sidebar.helpSidebar.category.Outline Client (now a sidebar, not category)
- Remove: sidebar.helpSidebar.category.Outline Manager (now a sidebar, not category)
- Remove: sidebar.helpSidebar.category.For Developers (section removed)
- Rename: sidebar.helpSidebar.category.Getting Started -> sidebar.clientSidebar.category.Getting Started
- Rename: sidebar.helpSidebar.category.client-troubleshooting -> sidebar.clientSidebar.category.client-troubleshooting
- Rename: sidebar.helpSidebar.category.Server Setup -> sidebar.managerSidebar.category.Server Setup
- Rename: sidebar.helpSidebar.category.Server Management -> sidebar.managerSidebar.category.Server Management
- Rename: sidebar.helpSidebar.category.manager-troubleshooting -> sidebar.managerSidebar.category.manager-troubleshooting
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Keys to remove (top-level categories that became sidebars, or removed sections)
REMOVE_KEYS = {
    "sidebar.helpSidebar.category.About Outline",
    "sidebar.helpSidebar.category.Outline Client",
    "sidebar.helpSidebar.category.Outline Manager",
    "sidebar.helpSidebar.category.For Developers",
}

# Keys to rename (old -> new)
RENAME_KEYS = {
    "sidebar.helpSidebar.category.Getting Started": "sidebar.clientSidebar.category.Getting Started",
    "sidebar.helpSidebar.category.client-troubleshooting": "sidebar.clientSidebar.category.client-troubleshooting",
    "sidebar.helpSidebar.category.Server Setup": "sidebar.managerSidebar.category.Server Setup",
    "sidebar.helpSidebar.category.Server Management": "sidebar.managerSidebar.category.Server Management",
    "sidebar.helpSidebar.category.manager-troubleshooting": "sidebar.managerSidebar.category.manager-troubleshooting",
}

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name != "partial-translations"
)

updated = 0
for locale in locales:
    current_path = I18N / locale / "docusaurus-plugin-content-docs" / "current.json"
    if not current_path.exists():
        continue

    data = json.loads(current_path.read_text("utf-8"))
    new_data = {}
    changed = False

    for key, value in data.items():
        if key in REMOVE_KEYS:
            changed = True
            continue
        if key in RENAME_KEYS:
            new_key = RENAME_KEYS[key]
            # Update description too
            if isinstance(value, dict) and "description" in value:
                old_desc = value["description"]
                new_desc = old_desc.replace("'helpSidebar'", f"'{new_key.split('.')[1]}'")
                value = {**value, "description": new_desc}
            new_data[new_key] = value
            changed = True
        else:
            new_data[key] = value

    if changed:
        current_path.write_text(json.dumps(new_data, ensure_ascii=False, indent=2) + "\n", "utf-8")
        updated += 1
        print(f"  UPDATED {locale}")

print(f"\nUpdated {updated} current.json files")
