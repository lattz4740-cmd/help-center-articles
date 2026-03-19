#!/usr/bin/env python3
"""Remove ## headings that duplicate the page title from all docs.

When a doc's first ## heading matches (or is very close to) the frontmatter
title, it's redundant since Docusaurus already renders the title as h1.
Remove it from both English and translations.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

TITLE_RE = re.compile(r'^title:\s*"?(.+?)"?\s*$', re.MULTILINE)
FIRST_HEADING_RE = re.compile(r'^(##\s+.+)$', re.MULTILINE)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def remove_title_heading(filepath):
    """Remove first ## heading if it matches the frontmatter title."""
    text = filepath.read_text(encoding="utf-8")

    title_match = TITLE_RE.search(text)
    if not title_match:
        return 0

    title = title_match.group(1).strip().strip('"').strip("'")

    heading_match = FIRST_HEADING_RE.search(text)
    if not heading_match:
        return 0

    heading_text = heading_match.group(1).lstrip('#').strip()

    # Check if heading matches title (case-insensitive, ignoring punctuation)
    title_norm = re.sub(r'[^\w\s]', '', title.lower()).strip()
    heading_norm = re.sub(r'[^\w\s]', '', heading_text.lower()).strip()

    if title_norm == heading_norm:
        # Remove the heading line and any blank line after it
        start = heading_match.start()
        end = heading_match.end()
        # Also remove trailing newline(s)
        while end < len(text) and text[end] == '\n':
            end += 1
        new_text = text[:start] + text[end:]
        filepath.write_text(new_text, encoding="utf-8")
        return 1

    return 0


def main():
    total = 0

    # Check all English docs
    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS).with_suffix(""))
        n = remove_title_heading(en_file)
        if n:
            print(f"  en/{doc_path}: removed redundant title heading")
            total += n

        # Check all translations for this doc
        for locale in get_locales():
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if not tr_file.exists():
                continue
            n = remove_title_heading(tr_file)
            if n:
                print(f"  {locale}/{doc_path}: removed redundant title heading")
                total += n

    print(f"\nDone: {total} redundant title headings removed")


if __name__ == "__main__":
    main()
