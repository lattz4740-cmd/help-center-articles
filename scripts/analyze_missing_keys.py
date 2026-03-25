#!/usr/bin/env python3
"""Analyze which locales are missing which known-missing keys."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

KNOWN_MISSING_KEYS = {
    "homepage.about.button",
    "homepage.client.button",
    "homepage.client.description",
    "homepage.developers.button",
    "homepage.developers.description",
    "homepage.manager.button",
    "homepage.manager.description",
}

locales = sorted(
    p.name for p in I18N.iterdir()
    if p.is_dir() and p.name not in ("partial-translations", "en")
)

# For each locale, find which keys are missing
locale_missing: dict[str, set[str]] = {}
for locale in locales:
    code_path = I18N / locale / "code.json"
    if not code_path.exists():
        continue
    data = json.loads(code_path.read_text("utf-8"))
    missing = set()
    for key in KNOWN_MISSING_KEYS:
        if key not in data:
            missing.add(key)
    if missing:
        locale_missing[locale] = missing

# Group locales by their missing key set
from collections import defaultdict
groups: dict[tuple, list[str]] = defaultdict(list)
for locale, missing in locale_missing.items():
    groups[tuple(sorted(missing))].append(locale)

print("Missing key groups:\n")
for keys, group_locales in sorted(groups.items(), key=lambda x: -len(x[1])):
    print(f"  {len(group_locales)} locales missing {len(keys)} keys:")
    print(f"    Locales: {', '.join(group_locales)}")
    print(f"    Keys: {', '.join(keys)}")
    print()
