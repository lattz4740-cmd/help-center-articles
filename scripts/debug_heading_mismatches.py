#!/usr/bin/env python3
"""Debug remaining heading structure mismatches.

For each doc with heading count mismatches, show the English heading structure
alongside a sample translation to understand what's different.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$', re.MULTILINE)
BOLD_LINE_RE = re.compile(r'^(\*{2,4})(.+?)\1\s*$', re.MULTILINE)

# Docs with remaining heading structure issues
PROBLEM_DOCS = {
    "client/troubleshooting/firewall-errors": 22,
    "client/troubleshooting/connection-issues": 17,
    "client/getting-started/connecting-device": 16,
    "manager/server-setup/google-cloud": 9,
    "manager/server-management/data-limits": 5,
    "manager/server-setup/setup-server": 4,
    "about/terminology": 3,
    "manager/server-setup/setup-faqs": 2,
    "manager/server-management/manage-access-keys": 1,
}


def show_structure(filepath, label):
    """Show headings and bold lines in a file."""
    text = filepath.read_text(encoding="utf-8")
    headings = [(len(m.group(1)), m.group(2)[:50]) for m in HEADING_RE.finditer(text)]
    bolds = [m.group(2)[:50] for m in BOLD_LINE_RE.finditer(text)]
    print(f"  {label}: {len(headings)} headings, {len(bolds)} bold lines")
    for level, text in headings:
        print(f"    H{level} {text}")
    for text in bolds:
        print(f"    ** {text}")


def main():
    for doc_path, count in sorted(PROBLEM_DOCS.items(), key=lambda x: -x[1]):
        en_file = DOCS / f"{doc_path}.md"
        if not en_file.exists():
            continue

        print(f"\n{'='*60}")
        print(f"=== {doc_path} ({count} locales affected) ===")
        show_structure(en_file, "EN")

        # Find a sample locale that has the issue
        for locale in ["ar", "de", "fr", "bg", "ko", "zh-Hans", "en-GB"]:
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if not tr_file.exists():
                continue
            en_levels = [len(m.group(1)) for m in HEADING_RE.finditer(en_file.read_text(encoding="utf-8"))]
            tr_levels = [len(m.group(1)) for m in HEADING_RE.finditer(tr_file.read_text(encoding="utf-8"))]
            if en_levels != tr_levels:
                show_structure(tr_file, locale)
                break


if __name__ == "__main__":
    main()
