#!/usr/bin/env python3
"""Fix inline bold text that should be headings in translations.

The GKMS source has some headings as bold text at the START of a paragraph
(not standalone bold paragraphs). The converter missed these. This script
finds them in the markdown output and splits them into headings.

Pattern in markdown: **bold text**rest of paragraph on same line
Should become: ## bold text\n\nrest of paragraph
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$', re.MULTILINE)

# Pattern: line starts with **bold** or ***bold*** followed by more text
# The bold part is the heading, the rest is the paragraph
INLINE_BOLD_START_RE = re.compile(
    r'^(\*{2,4})([^*\n]+?)\1([.。:：]?)\s*(.+)$',
    re.MULTILINE
)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def extract_heading_levels(text):
    return [len(m.group(1)) for m in HEADING_RE.finditer(text)]


def fix_file(en_file, tr_file):
    """Fix inline bold headings in a translation to match English heading count."""
    en_text = en_file.read_text(encoding="utf-8")
    tr_text = tr_file.read_text(encoding="utf-8")

    en_levels = extract_heading_levels(en_text)
    tr_levels = extract_heading_levels(tr_text)

    if en_levels == tr_levels:
        return 0  # Already matches

    if len(tr_levels) >= len(en_levels):
        return 0  # Translation has same or more headings

    # Find inline bold starts that could be headings
    matches = list(INLINE_BOLD_START_RE.finditer(tr_text))
    if not matches:
        return 0

    # Filter: only convert if the bold text looks like a heading
    # (not just inline emphasis in a normal paragraph)
    # Heuristic: the bold part should be short-ish (< 100 chars)
    # and the remaining text should be substantial
    candidates = []
    for m in matches:
        bold_text = m.group(2).strip()
        punct = m.group(3)
        rest = m.group(4).strip()
        if len(bold_text) < 100 and len(rest) > 20:
            candidates.append(m)

    if not candidates:
        return 0

    # Only convert enough to match English heading count
    needed = len(en_levels) - len(tr_levels)
    to_convert = candidates[:needed]

    new_text = tr_text
    fixes = 0
    for m in reversed(to_convert):
        bold_text = m.group(2).strip()
        punct = m.group(3)
        rest = m.group(4).strip()
        replacement = f"## {bold_text}{punct}\n\n{rest}"
        new_text = new_text[:m.start()] + replacement + new_text[m.end():]
        fixes += 1

    if fixes > 0:
        tr_file.write_text(new_text, encoding="utf-8")
    return fixes


def main():
    total = 0

    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS).with_suffix(""))

        for locale in get_locales():
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if not tr_file.exists():
                continue

            fixes = fix_file(en_file, tr_file)
            if fixes:
                print(f"  {locale}/{doc_path}: split {fixes} inline bold heading(s)")
                total += fixes

    # Also fix English docs
    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS).with_suffix(""))
        text = en_file.read_text(encoding="utf-8")
        matches = list(INLINE_BOLD_START_RE.finditer(text))
        if matches:
            new_text = text
            for m in reversed(matches):
                bold_text = m.group(2).strip()
                punct = m.group(3)
                rest = m.group(4).strip()
                if len(bold_text) < 100 and len(rest) > 20:
                    replacement = f"## {bold_text}{punct}\n\n{rest}"
                    new_text = new_text[:m.start()] + replacement + new_text[m.end():]
            if new_text != text:
                en_file.write_text(new_text, encoding="utf-8")

    print(f"\nDone: {total} inline bold headings fixed")


if __name__ == "__main__":
    main()
