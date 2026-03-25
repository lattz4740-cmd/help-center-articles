#!/usr/bin/env python3
"""Check which locales have the description and button keys translated."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

DESCRIPTION_KEYS = [
    "homepage.client.description",
    "homepage.manager.description",
    "homepage.developers.description",
]
BUTTON_KEYS = [
    "homepage.about.button",
    "homepage.client.button",
    "homepage.manager.button",
    "homepage.developers.button",
]

LOCALES = [
    "af", "am", "ar", "az", "bg", "bn", "bs",
    "ca", "cs", "da", "de", "el", "en-GB",
    "es", "es-419", "et", "fa", "fi", "fil", "fr",
    "he", "hi", "hr", "hu", "hy", "id",
    "is", "it", "ja", "ka", "kk", "km", "ko", "lo", "lv",
    "mk", "mn", "mr", "ms", "my", "nb", "ne", "nl", "pl",
    "pt", "pt-BR", "ro", "ru", "si", "sk", "sl", "sq", "sr", "sv", "sw",
    "ta", "th", "tr", "uk", "ur", "vi", "zh-Hans",
    "zh-Hant", "zh-HK",
]

has_descriptions = []
missing_descriptions = []
has_buttons = []
missing_buttons = []

for locale in LOCALES:
    code_path = I18N / locale / "code.json"
    if not code_path.exists():
        continue
    data = json.loads(code_path.read_text("utf-8"))

    has_all_desc = all(k in data for k in DESCRIPTION_KEYS)
    has_all_btn = all(k in data for k in BUTTON_KEYS)

    if has_all_desc:
        has_descriptions.append(locale)
    else:
        missing_descriptions.append(locale)

    if has_all_btn:
        has_buttons.append(locale)
    else:
        missing_buttons.append(locale)

print(f"Have all 3 descriptions ({len(has_descriptions)}):")
print(f"  {', '.join(has_descriptions)}")
print()
print(f"Missing descriptions ({len(missing_descriptions)}):")
print(f"  {', '.join(missing_descriptions)}")
print()
print(f"Have all 4 buttons ({len(has_buttons)}):")
print(f"  {', '.join(has_buttons)}")
print()
print(f"Missing buttons ({len(missing_buttons)}):")
print(f"  {', '.join(missing_buttons)}")
