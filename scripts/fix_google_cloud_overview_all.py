#!/usr/bin/env python3
"""Remove the first ## heading from all google-cloud translations that have
one more heading than English (9 vs 8). The extra heading is always the
"Overview" equivalent at the top."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$', re.MULTILINE)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def main():
    en_file = DOCS / "manager" / "server-setup" / "google-cloud.md"
    en_count = len(HEADING_RE.findall(en_file.read_text(encoding="utf-8")))
    print(f"English heading count: {en_count}")

    total = 0
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "manager" / "server-setup" / "google-cloud.md"
        if not f.exists():
            continue

        text = f.read_text(encoding="utf-8")
        headings = list(HEADING_RE.finditer(text))

        if len(headings) != en_count + 1:
            continue  # Not the "one extra Overview" pattern

        # Remove the first heading
        first = headings[0]
        heading_text = first.group(2).strip()
        lines = text.split('\n')

        # Find the heading line
        for i, line in enumerate(lines):
            if line.strip() == first.group(0).strip():
                # Remove heading and trailing blank line
                end = i + 1
                while end < len(lines) and not lines[end].strip():
                    end += 1
                lines = lines[:i] + lines[end:]
                f.write_text('\n'.join(lines), encoding='utf-8')
                print(f"  {locale}: removed '## {heading_text[:40]}'")
                total += 1
                break

    print(f"\nDone: {total} headings removed")


if __name__ == "__main__":
    main()
