#!/usr/bin/env python3
"""Show code block diffs for remaining CODE_BLOCKS issues."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

CODE_BLOCK_RE = re.compile(r'```[^`]*```', re.DOTALL)

CASES = [
    ("he", "client/troubleshooting/access-key-issues"),
    ("hr", "client/getting-started/install-linux"),
    ("lv", "client/getting-started/install-linux"),
    ("ms", "client/getting-started/install-linux"),
    ("si", "client/getting-started/install-linux"),
]


def main():
    for locale, doc_path in CASES:
        en_file = DOCS / f"{doc_path}.md"
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"

        en_blocks = CODE_BLOCK_RE.findall(en_file.read_text(encoding="utf-8"))
        tr_blocks = CODE_BLOCK_RE.findall(tr_file.read_text(encoding="utf-8"))

        print(f"\n=== {locale}/{doc_path} ({len(en_blocks)} EN vs {len(tr_blocks)} TR) ===")

        max_blocks = max(len(en_blocks), len(tr_blocks))
        for i in range(max_blocks):
            en_b = en_blocks[i].strip() if i < len(en_blocks) else "(missing)"
            tr_b = tr_blocks[i].strip() if i < len(tr_blocks) else "(missing)"
            # Normalize whitespace for comparison
            en_norm = "\n".join(l.strip() for l in en_b.split("\n"))
            tr_norm = "\n".join(l.strip() for l in tr_b.split("\n"))
            if en_norm != tr_norm:
                print(f"  Block {i+1} DIFFERS:")
                print(f"    EN: {en_b[:200]}")
                print(f"    TR: {tr_b[:200]}")


if __name__ == "__main__":
    main()
