#!/usr/bin/env python3
"""Fix remaining self-referencing links in feedback and how-outline-works.

These have count mismatches (translations have different number of links),
so we can't do positional matching. Instead, replace all self-referencing
links with the English external URLs based on the link text context.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def fix_self_links_in_doc(doc_path, self_url, replacement_url):
    """Replace self-referencing links with a specific replacement URL."""
    fixes = 0
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        # Replace [text](/doc_path) with [text](replacement_url)
        # but only exact self-links, not anchored ones
        pattern = re.compile(
            r'\[([^\]]+)\]\(' + re.escape(self_url) + r'\)'
        )
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        new_text = pattern.sub(lambda m: f'[{m.group(1)}]({replacement_url})', text)
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            fixes += 1
    return fixes


def main():
    total = 0

    # how-outline-works: self-links should just be removed (keep text, drop link)
    # since the original external URLs can't be recovered from position
    print("1. Removing self-links in how-outline-works...")
    fixes = 0
    pattern = re.compile(r'\[([^\]]+)\]\(/about/how-outline-works\)')
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "about" / "how-outline-works.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        # Replace self-links with just the link text
        new_text = pattern.sub(lambda m: m.group(1), text)
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            fixes += 1
    print(f"   Fixed {fixes} files")
    total += fixes

    # feedback: self-links should just be removed too
    print("2. Removing self-links in feedback...")
    fixes = 0
    pattern = re.compile(r'\[([^\]]+)\]\(/about/feedback\)')
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "about" / "feedback.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        new_text = pattern.sub(lambda m: m.group(1), text)
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            fixes += 1
    print(f"   Fixed {fixes} files")
    total += fixes

    print(f"\nDone: {total} total fixes")


if __name__ == "__main__":
    main()
