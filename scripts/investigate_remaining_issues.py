#!/usr/bin/env python3
"""Investigate remaining verification issues to determine which have unambiguous fixes."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

CODE_BLOCK_RE = re.compile(r'```[^`]*```', re.DOTALL)


def compare_code_blocks(doc_path):
    """Compare code blocks between English and a sample translation."""
    en_file = DOCS / f"{doc_path}.md"
    en_text = en_file.read_text(encoding="utf-8")
    en_blocks = CODE_BLOCK_RE.findall(en_text)

    # Check a sample translation
    for locale in ["af", "fr", "ar"]:
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
        if not tr_file.exists():
            continue
        tr_text = tr_file.read_text(encoding="utf-8")
        tr_blocks = CODE_BLOCK_RE.findall(tr_text)

        print(f"\n  {locale}: {len(en_blocks)} EN blocks vs {len(tr_blocks)} TR blocks")
        for i, b in enumerate(en_blocks):
            print(f"    EN block {i}: {b[:100]}")
        for i, b in enumerate(tr_blocks):
            print(f"    TR block {i}: {b[:100]}")

        if len(en_blocks) == len(tr_blocks):
            for i, (eb, tb) in enumerate(zip(en_blocks, tr_blocks)):
                if eb != tb:
                    print(f"    DIFF block {i}:")
                    print(f"      EN: {eb[:150]}")
                    print(f"      TR: {tb[:150]}")
        break


def compare_link_counts(doc_path):
    """Show link count differences for a doc."""
    LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')
    en_file = DOCS / f"{doc_path}.md"
    en_text = en_file.read_text(encoding="utf-8")
    en_links = LINK_RE.findall(en_text)

    for locale in ["af", "fr"]:
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
        if not tr_file.exists():
            continue
        tr_text = tr_file.read_text(encoding="utf-8")
        tr_links = LINK_RE.findall(tr_text)
        print(f"\n  {locale}: EN {len(en_links)} links vs TR {len(tr_links)} links")
        if len(en_links) != len(tr_links):
            print(f"    EN links: {[url for _, url in en_links]}")
            print(f"    TR links: {[url for _, url in tr_links]}")
        break


def main():
    print("=== CODE_BLOCKS: access-key-issues ===")
    compare_code_blocks("client/troubleshooting/access-key-issues")

    print("\n\n=== CODE_BLOCKS: install-linux ===")
    compare_code_blocks("client/getting-started/install-linux")

    print("\n\n=== LINKS count mismatch: connection-issues ===")
    compare_link_counts("client/troubleshooting/connection-issues")

    print("\n\n=== LINKS count mismatch: internet-access ===")
    compare_link_counts("client/troubleshooting/internet-access")

    print("\n\n=== LINKS count mismatch: connecting-device ===")
    compare_link_counts("client/getting-started/connecting-device")

    print("\n\n=== LINKS count mismatch: feedback ===")
    compare_link_counts("about/feedback")

    print("\n\n=== LINKS count mismatch: how-outline-works ===")
    compare_link_counts("about/how-outline-works")


if __name__ == "__main__":
    main()
