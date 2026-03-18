#!/usr/bin/env python3
"""Remove extra artifact links from translations.

1. connection-issues: remove full-path self-referencing links
2. internet-access: remove Salesforce sandbox URLs
3. access-key-issues: add missing code block
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

CODE_BLOCK_RE = re.compile(r'```[^`]*```', re.DOTALL)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def fix_connection_issues():
    fixes = 0
    pattern = re.compile(r'\[([^\]]*)\]\(/client/troubleshooting/connection-issues#\w+\)')
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        new_text = text
        for m in reversed(matches):
            new_text = new_text[:m.start()] + m.group(1).strip() + new_text[m.end():]
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            fixes += 1
    return fixes


def fix_internet_access():
    fixes = 0
    sandbox_re = re.compile(r'\[([^\]]*)\]\(https://google-jigsaw--jigsawuat\.sandbox\.my\.site\.com/[^)]+\)')
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "internet-access.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        matches = list(sandbox_re.finditer(text))
        if not matches:
            continue
        new_text = text
        for m in reversed(matches):
            new_text = new_text[:m.start()] + m.group(1) + new_text[m.end():]
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            fixes += 1
    return fixes


def fix_access_key_issues():
    en_file = DOCS / "client" / "troubleshooting" / "access-key-issues.md"
    en_blocks = CODE_BLOCK_RE.findall(en_file.read_text(encoding="utf-8"))
    if not en_blocks:
        return 0
    example_block = en_blocks[0]
    fixes = 0
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "access-key-issues.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        if CODE_BLOCK_RE.search(text):
            continue
        lines = text.split('\n')
        insert_idx = len(lines) - 1
        for i, line in enumerate(lines):
            if 'ss://' in line.lower() or 'outline=1' in line.lower():
                insert_idx = i + 1
                break
        lines.insert(insert_idx, '')
        lines.insert(insert_idx + 1, example_block)
        lines.insert(insert_idx + 2, '')
        f.write_text('\n'.join(lines), encoding='utf-8')
        fixes += 1
    return fixes


def main():
    print(f"connection-issues extra links: fixed {fix_connection_issues()} files")
    print(f"internet-access sandbox URLs: fixed {fix_internet_access()} files")
    print(f"access-key-issues missing code block: fixed {fix_access_key_issues()} files")


if __name__ == "__main__":
    main()
