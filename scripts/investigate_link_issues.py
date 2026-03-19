#!/usr/bin/env python3
"""Investigate remaining link issues to determine which are fixable."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')


def show_links(doc_path, locales):
    """Show link comparison for a doc across sample locales."""
    en_file = DOCS / f"{doc_path}.md"
    en_text = en_file.read_text(encoding="utf-8")
    en_links = [(m.group(1)[:30], m.group(2)) for m in LINK_RE.finditer(en_text)]

    print(f"\n=== {doc_path} ===")
    print(f"  EN ({len(en_links)} links): {[url for _, url in en_links]}")

    for locale in locales:
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
        if not tr_file.exists():
            continue
        tr_text = tr_file.read_text(encoding="utf-8")
        tr_links = [(m.group(1)[:30], m.group(2)) for m in LINK_RE.finditer(tr_text)]
        print(f"  {locale} ({len(tr_links)} links): {[url for _, url in tr_links]}")
        break


def main():
    # Step anchor diffs
    print("=== STEP ANCHOR DIFFS ===")
    show_links("about/terminology", ["ar", "de"])
    show_links("manager/troubleshooting/windows-install", ["ar", "de"])

    # Count mismatches
    print("\n\n=== COUNT MISMATCHES ===")
    show_links("client/troubleshooting/connection-issues", ["af", "bg"])
    show_links("client/getting-started/connecting-device", ["ar", "fr"])
    show_links("about/how-outline-works", ["ar", "de"])
    show_links("about/feedback", ["ar", "fr", "en-GB"])
    show_links("client/troubleshooting/windows-install", ["de", "es"])
    show_links("manager/server-management/delete-server", ["af", "de"])


if __name__ == "__main__":
    main()
