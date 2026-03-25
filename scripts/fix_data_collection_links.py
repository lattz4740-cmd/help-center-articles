#!/usr/bin/env python3
"""Replace /about/data-collection links with the privacy policy URL."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVACY_URL = "https://getoutline.org/policies/data-collection"

total = 0
for f in ROOT.joinpath("i18n").rglob("*.md"):
    text = f.read_text("utf-8")
    if "/about/data-collection" in text:
        new_text = text.replace("/about/data-collection", PRIVACY_URL)
        f.write_text(new_text, "utf-8")
        total += 1

print(f"Updated {total} files")
