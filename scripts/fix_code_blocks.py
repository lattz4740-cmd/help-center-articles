#!/usr/bin/env python3
"""Fix remaining code block issues.

1. he/access-key-issues: Remove invisible RTL mark from code block
2. hr/install-linux: Fix broken wget command (missing spaces)
3. ms/install-linux: Replace translated commands with English code blocks
4. si/install-linux: Replace translated commands with English code blocks
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

CODE_BLOCK_RE = re.compile(r'```[^`]*```', re.DOTALL)


def replace_code_blocks(locale, doc_path, block_indices=None):
    """Replace specific code blocks in a translation with English versions.

    If block_indices is None, replace all differing blocks.
    """
    en_file = DOCS / f"{doc_path}.md"
    tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"

    en_text = en_file.read_text(encoding="utf-8")
    tr_text = tr_file.read_text(encoding="utf-8")

    en_blocks = list(CODE_BLOCK_RE.finditer(en_text))
    tr_blocks = list(CODE_BLOCK_RE.finditer(tr_text))

    if len(en_blocks) != len(tr_blocks):
        print(f"  SKIP {locale}/{doc_path}: block count mismatch ({len(en_blocks)} vs {len(tr_blocks)})")
        return 0

    fixes = 0
    new_text = tr_text

    for i in range(len(en_blocks) - 1, -1, -1):
        if block_indices is not None and i not in block_indices:
            continue

        en_block = en_blocks[i].group(0)
        tr_block = tr_blocks[i].group(0)

        # Normalize for comparison
        en_norm = "\n".join(l.strip() for l in en_block.strip().split("\n"))
        tr_norm = "\n".join(l.strip() for l in tr_block.strip().split("\n"))

        if en_norm != tr_norm:
            # Replace translation block with English block (without indentation
            # since translations have code blocks outside list items)
            en_lines = en_block.split("\n")
            stripped_block = "\n".join(l.lstrip() for l in en_lines)
            new_text = new_text[:tr_blocks[i].start()] + stripped_block + new_text[tr_blocks[i].end():]
            fixes += 1

    if fixes > 0:
        tr_file.write_text(new_text, encoding="utf-8")
    return fixes


def fix_hebrew_rtl():
    """Remove invisible RTL mark from Hebrew access-key-issues code block."""
    f = I18N / "he" / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "access-key-issues.md"
    text = f.read_text(encoding="utf-8")
    # Remove LRM (U+200E) and RLM (U+200F) and other invisible marks from code blocks
    new_text = text.replace('\u200e', '').replace('\u200f', '').replace('\u200b', '')
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
        return 1
    return 0


def main():
    total = 0

    # Hebrew: RTL mark in code block
    n = fix_hebrew_rtl()
    if n:
        print(f"  he/access-key-issues: removed invisible RTL mark")
    total += n

    # Croatian: broken wget command — replace block 4 (index 3)
    n = replace_code_blocks("hr", "client/getting-started/install-linux", {3})
    if n:
        print(f"  hr/install-linux: fixed {n} broken command(s)")
    total += n

    # Malay: translated commands — replace blocks 2, 4, 5 (indices 1, 3, 4)
    n = replace_code_blocks("ms", "client/getting-started/install-linux", {1, 3, 4})
    if n:
        print(f"  ms/install-linux: replaced {n} translated command(s)")
    total += n

    # Sinhala: translated commands — replace blocks 2, 5 (indices 1, 4)
    n = replace_code_blocks("si", "client/getting-started/install-linux", {1, 4})
    if n:
        print(f"  si/install-linux: replaced {n} translated command(s)")
    total += n

    print(f"\nDone: {total} fixes")


if __name__ == "__main__":
    main()
