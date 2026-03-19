#!/usr/bin/env python3
"""Clean up heading formatting issues across all docs and translations.

1. Strip bold markers from headings: ## **text** → ## text
2. Strip italic markers from headings: ## *text* → ## text
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

# ## **text** or ## ***text*** or ## *text*
BOLD_HEADING_RE = re.compile(r'^(#{1,6})\s+\*{1,4}(.+?)\*{1,4}\s*$', re.MULTILINE)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def strip_bold_from_headings(filepath):
    """Remove bold/italic markers from inside headings."""
    text = filepath.read_text(encoding="utf-8")
    new_text = BOLD_HEADING_RE.sub(r'\1 \2', text)
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        count = len(BOLD_HEADING_RE.findall(text))
        return count
    return 0


def main():
    total = 0

    # Fix English docs
    for en_file in sorted(DOCS.rglob("*.md")):
        n = strip_bold_from_headings(en_file)
        if n:
            print(f"  en/{en_file.relative_to(DOCS)}: stripped bold from {n} heading(s)")
            total += n

    # Fix all translations
    for locale in get_locales():
        locale_dir = I18N / locale / "docusaurus-plugin-content-docs" / "current"
        for tr_file in sorted(locale_dir.rglob("*.md")):
            n = strip_bold_from_headings(tr_file)
            if n:
                print(f"  {locale}/{tr_file.relative_to(locale_dir)}: stripped bold from {n} heading(s)")
                total += n

    print(f"\nDone: {total} bold markers stripped from headings")


if __name__ == "__main__":
    main()
