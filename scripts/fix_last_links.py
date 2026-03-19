#!/usr/bin/env python3
"""Fix the last few link issues."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"


def fix_file(locale, doc_path, old, new):
    f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
    text = f.read_text(encoding="utf-8")
    if old in text:
        f.write_text(text.replace(old, new), encoding="utf-8")
        print(f"  {locale}/{doc_path}: fixed")
        return 1
    return 0


def main():
    fixes = 0

    # Arabic: typo in Chrome extension URL (Arabic question mark in URL)
    f = I18N / "ar" / "docusaurus-plugin-content-docs" / "current" / "about" / "security-and-privacy.md"
    text = f.read_text(encoding="utf-8")
    new_text = text.replace("passw\u061ford-alert", "password-alert")
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
        print("  ar/security-and-privacy: fixed Arabic question mark in URL")
        fixes += 1

    # Dutch: missing trailing slash
    fixes += fix_file("nl", "manager/server-setup/cost",
                       "https://www.digitalocean.com)", "https://www.digitalocean.com/)")

    # quay.io: use less-specific English URL
    for locale in ["kk", "mr", "ta", "vi"]:
        fixes += fix_file(locale, "about/how-outline-works",
                          "https://quay.io/repository/outline/shadowbox?tab=tags",
                          "https://quay.io/")

    print(f"\nDone: {fixes} fixes")


if __name__ == "__main__":
    main()
