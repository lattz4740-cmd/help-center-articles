#!/usr/bin/env python3
"""Restore the two missing description keys in en-GB/code.json with English values."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
code_path = ROOT / "i18n" / "en-GB" / "code.json"

data = json.loads(code_path.read_text("utf-8"))

data["homepage.client.description"] = {
    "message": "Get started with connecting your device and troubleshooting.",
    "description": "Description for the Outline Client card on the homepage",
}
data["homepage.manager.description"] = {
    "message": "Set up and manage your Outline server.",
    "description": "Description for the Outline Manager card on the homepage",
}

# Reorder keys nicely
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
ordered = {}
for k in key_order:
    if k in data:
        ordered[k] = data[k]
for k, v in data.items():
    if k not in ordered:
        ordered[k] = v

code_path.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", "utf-8")
print("Restored homepage.client.description and homepage.manager.description in en-GB")
