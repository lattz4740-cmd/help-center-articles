#!/usr/bin/env python3
"""Add homepage title translations to code.json, pulling from current.json.

Also report which descriptions/buttons are still untranslated (same as English).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Mapping from homepage title IDs to current.json sidebar keys
TITLE_MAP = {
    "homepage.about.title": "sidebar.helpSidebar.category.About Outline",
    "homepage.client.title": "sidebar.helpSidebar.category.Outline Client",
    "homepage.manager.title": "sidebar.helpSidebar.category.Outline Manager",
    "homepage.developers.title": "sidebar.helpSidebar.category.For Developers",
}

TITLE_DESCRIPTIONS = {
    "homepage.about.title": "Title for the About Outline card on the homepage",
    "homepage.client.title": "Title for the Outline Client card on the homepage",
    "homepage.manager.title": "Title for the Outline Manager card on the homepage",
    "homepage.developers.title": "Title for the For Developers card on the homepage",
}

# English defaults
ENGLISH_DEFAULTS = {
    "homepage.about.title": "About Outline",
    "homepage.client.title": "Outline Client",
    "homepage.manager.title": "Outline Manager",
    "homepage.developers.title": "For Developers",
    "homepage.about.description": "Learn how Outline works, its security model, and more.",
    "homepage.client.description": "Get started with connecting your device and troubleshooting.",
    "homepage.manager.description": "Set up and manage your Outline server.",
    "homepage.developers.description": "Integrate the Outline SDK into your application.",
    "homepage.about.button": "Learn more",
    "homepage.client.button": "Get started",
    "homepage.manager.button": "Set up a server",
    "homepage.developers.button": "Explore the SDK",
}

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name != "partial-translations" and (p / "code.json").exists()
)

untranslated = []
updated = 0

for locale in locales:
    code_path = I18N / locale / "code.json"
    current_path = I18N / locale / "docusaurus-plugin-content-docs" / "current.json"

    code = json.loads(code_path.read_text("utf-8"))

    # Load current.json for sidebar translations
    current = {}
    if current_path.exists():
        current = json.loads(current_path.read_text("utf-8"))

    changed = False

    # Add title keys from current.json
    for homepage_key, sidebar_key in TITLE_MAP.items():
        if homepage_key not in code:
            # Get translation from current.json
            sidebar_entry = current.get(sidebar_key, {})
            message = sidebar_entry.get("message", ENGLISH_DEFAULTS[homepage_key])
            code[homepage_key] = {
                "message": message,
                "description": TITLE_DESCRIPTIONS[homepage_key],
            }
            changed = True

    # Check for untranslated strings (same as English)
    for key, english in ENGLISH_DEFAULTS.items():
        entry = code.get(key, {})
        msg = entry.get("message", "")
        if msg == english:
            untranslated.append((locale, key))

    if changed:
        # Reorder: put keys in a nice order
        ordered = {}
        key_order = [
            "homepage.hero.title",
            "homepage.hero.searchPlaceholder",
            "homepage.browseTopics",
            "homepage.about.title",
            "homepage.about.description",
            "homepage.about.button",
            "homepage.client.title",
            "homepage.client.description",
            "homepage.client.button",
            "homepage.manager.title",
            "homepage.manager.description",
            "homepage.manager.button",
            "homepage.developers.title",
            "homepage.developers.description",
            "homepage.developers.button",
        ]
        for k in key_order:
            if k in code:
                ordered[k] = code[k]
        # Add any extra keys not in the order list
        for k, v in code.items():
            if k not in ordered:
                ordered[k] = v

        code_path.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", "utf-8")
        updated += 1
        print(f"  UPDATED {locale}")

print(f"\nUpdated {updated} code.json files with title translations")
print(f"\nUntranslated strings (same as English):")
for locale, key in untranslated:
    print(f"  {locale}: {key}")
