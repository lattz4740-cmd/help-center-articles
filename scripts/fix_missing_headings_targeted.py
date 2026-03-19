#!/usr/bin/env python3
"""Fix specific missing headings by finding the translated text and converting to ##.

For each known missing heading, finds the plain-text line in the translation
that corresponds to the English heading and converts it to a ## heading.

Strategy: The text content for these missing headings exists as a standalone
short line (the question/title) followed by a longer paragraph (the answer).
We search for lines that are:
- Short (< 100 chars)
- Not already a heading
- Not a list item
- Followed by a longer paragraph
- Not inside a code block
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^#{1,6}\s+', re.MULTILINE)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def extract_heading_count(text):
    return len(HEADING_RE.findall(text))


def find_question_lines(text):
    """Find standalone short lines that look like questions/titles."""
    lines = text.split('\n')
    results = []
    in_frontmatter = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Skip frontmatter
        if stripped == '---':
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue

        # Skip headings, list items, empty lines, code blocks
        if not stripped or stripped.startswith('#') or stripped.startswith('-') or stripped.startswith('*') or stripped.startswith('`') or stripped.startswith('1.'):
            continue

        # Short standalone line (looks like a question/title)
        if len(stripped) < 100 and stripped.endswith('?') or stripped.endswith(':') or stripped.endswith('？') or stripped.endswith('：'):
            # Check that next non-empty line is a longer paragraph
            for j in range(i + 1, min(i + 3, len(lines))):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith('#') and len(next_line) > len(stripped):
                    results.append((i, stripped))
                    break

    return results


def try_match_headings(en_file, tr_file):
    """Try to match missing headings between English and translation."""
    en_text = en_file.read_text(encoding="utf-8")
    tr_text = tr_file.read_text(encoding="utf-8")

    en_count = extract_heading_count(en_text)
    tr_count = extract_heading_count(tr_text)

    if tr_count >= en_count:
        return 0

    needed = en_count - tr_count
    candidates = find_question_lines(tr_text)

    if len(candidates) < needed:
        return 0

    # Convert the first `needed` candidates to headings
    lines = tr_text.split('\n')
    fixes = 0
    for line_idx, line_text in candidates[:needed]:
        if not lines[line_idx].strip().startswith('#'):
            lines[line_idx] = f'## {line_text}'
            fixes += 1

    if fixes > 0:
        tr_file.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def main():
    total = 0

    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS).with_suffix(""))

        for locale in get_locales():
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if not tr_file.exists():
                continue

            fixes = try_match_headings(en_file, tr_file)
            if fixes:
                print(f"  {locale}/{doc_path}: converted {fixes} line(s) to heading(s)")
                total += fixes

    print(f"\nDone: {total} headings added")


if __name__ == "__main__":
    main()
