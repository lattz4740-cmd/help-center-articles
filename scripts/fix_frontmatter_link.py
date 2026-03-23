#!/usr/bin/env python3
"""Fix frontmatter broken by fix_orphaned_link_text.py.

The orphaned-link script sometimes joined link text directly onto the
closing `---` frontmatter delimiter, like:
    --- [text](url)

This script finds those and moves the link text to a new line after ---.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Pattern: line is exactly "---" followed by space then markdown content
PATTERN = re.compile(r'^(---)\s+(\S.*)$', re.MULTILINE)

files_to_check = [
    "ja/docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md",
    "ko/docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md",
    "ko/docusaurus-plugin-content-docs/current/manager/server-management/delete-server.md",
    "th/docusaurus-plugin-content-docs/current/manager/server-management/delete-server.md",
    "zh-Hans/docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md",
    "zh-Hant/docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md",
    "zh-Hant/docusaurus-plugin-content-docs/current/manager/server-management/delete-server.md",
]

total = 0
for rel in files_to_check:
    f = I18N / rel
    if not f.exists():
        print(f"  SKIP {rel} (not found)")
        continue

    text = f.read_text('utf-8')

    # Find the closing --- of frontmatter (second occurrence of ---)
    # and check if content is appended to it
    lines = text.split('\n')
    fixed = False
    dash_count = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('---'):
            dash_count += 1
            if dash_count == 2 and len(stripped) > 3:
                # Content appended to closing ---
                rest = stripped[3:].strip()
                lines[i] = '---'
                # Insert blank line + content after ---
                lines.insert(i + 1, '')
                lines.insert(i + 2, rest)
                fixed = True
                break

    if fixed:
        f.write_text('\n'.join(lines), 'utf-8')
        print(f"  FIXED {rel}")
        total += 1
    else:
        print(f"  OK    {rel}")

print(f"\nDone: {total} files fixed")
