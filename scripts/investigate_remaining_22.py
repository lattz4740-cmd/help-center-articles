#!/usr/bin/env python3
"""Investigate remaining 22 heading issues in detail, showing full heading +
plain-text-line structure for each affected locale."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$', re.MULTILINE)


def show_structure(filepath, label, max_lines=None):
    """Show all headings and short standalone lines (potential headings)."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.split('\n')
    in_fm = False
    print(f"  {label}:")
    shown = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '---':
            in_fm = not in_fm
            continue
        if in_fm:
            continue
        hm = HEADING_RE.match(line)
        if hm:
            print(f"    {i:3d} H{len(hm.group(1))} {hm.group(2)[:70]}")
            shown += 1
        elif stripped and len(stripped) < 80 and not stripped.startswith('-') and not stripped.startswith('*') and not stripped.startswith('1.') and not stripped.startswith('`'):
            # Check if next non-empty line is longer (answer paragraph)
            for j in range(i + 1, min(i + 3, len(lines))):
                if lines[j].strip():
                    if len(lines[j].strip()) > len(stripped):
                        print(f"    {i:3d} ?? {stripped[:70]}")
                        shown += 1
                    break
        if max_lines and shown >= max_lines:
            break


def main():
    issues = {
        "manager/server-setup/google-cloud": ["ar", "fr", "it", "ja", "nl", "pt-BR", "es", "tr", "zh-Hans", "zh-Hant"],
        "client/troubleshooting/connection-issues": ["en-GB", "es", "fa", "pl", "pt-BR", "th", "zh-Hans"],
        "manager/server-setup/setup-server": ["am", "he", "ja"],
        "about/terminology": ["ur"],
        "manager/server-management/manage-access-keys": ["ur"],
    }

    for doc_path, locales in issues.items():
        en_file = DOCS / f"{doc_path}.md"
        print(f"\n{'='*70}")
        print(f"=== {doc_path} ===")
        show_structure(en_file, "EN", max_lines=20)

        for locale in locales:
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if tr_file.exists():
                show_structure(tr_file, locale, max_lines=20)


if __name__ == "__main__":
    main()
