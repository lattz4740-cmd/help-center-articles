#!/usr/bin/env python3
"""Investigate specific link issues in problem locales."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')


def show(doc_path, locales):
    en_file = DOCS / f"{doc_path}.md"
    en_links = [m.group(2) for m in LINK_RE.finditer(en_file.read_text(encoding="utf-8"))]
    print(f"\n=== {doc_path} ===")
    print(f"  EN ({len(en_links)}): {en_links}")
    for locale in locales:
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
        if not tr_file.exists():
            continue
        tr_links = [m.group(2) for m in LINK_RE.finditer(tr_file.read_text(encoding="utf-8"))]
        print(f"  {locale} ({len(tr_links)}): {tr_links}")


def main():
    # Feedback: EN 3 vs TR 4 (most locales) or 2 (en-GB)
    show("about/feedback", ["de", "fr", "en-GB"])

    # Connecting-device: EN 1 vs TR 0
    show("client/getting-started/connecting-device", ["de", "fr", "ko"])

    # Connection-issues: EN 12 vs TR 8
    show("client/troubleshooting/connection-issues", ["de", "es"])

    # How-outline-works: EN 10 vs TR 4
    show("about/how-outline-works", ["de", "ko"])

    # Windows-install: EN 3 vs TR 2
    show("client/troubleshooting/windows-install", ["de", "es"])

    # Delete-server: EN 1 vs TR 2
    show("manager/server-management/delete-server", ["de", "fr"])


if __name__ == "__main__":
    main()
