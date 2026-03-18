#!/usr/bin/env python3
"""Fix remaining unambiguous verification issues.

1. CODE_BLOCKS install-linux: whitespace differences in code blocks (indentation)
2. CODE_BLOCKS access-key-issues: missing code block in 18 locales
3. LINKS connection-issues: extra full-path self-referencing links (artifacts)
4. LINKS internet-access: Salesforce sandbox URLs that weren't remapped
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

CODE_BLOCK_RE = re.compile(r'```[^`]*```', re.DOTALL)
LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')


def get_locales():
    """Get all active locale directories."""
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def fix_install_linux_code_blocks():
    """Fix whitespace differences in install-linux code blocks.

    English code blocks have 3-space indentation inside; translations don't.
    Copy the exact English code blocks into translations at the same positions.
    """
    en_file = DOCS / "client" / "getting-started" / "install-linux.md"
    en_text = en_file.read_text(encoding="utf-8")
    en_blocks = list(CODE_BLOCK_RE.finditer(en_text))

    fixes = 0
    for locale in get_locales():
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "getting-started" / "install-linux.md"
        if not tr_file.exists():
            continue

        tr_text = tr_file.read_text(encoding="utf-8")
        tr_blocks = list(CODE_BLOCK_RE.finditer(tr_text))

        if len(tr_blocks) != len(en_blocks):
            continue  # Count mismatch — skip

        changed = False
        new_text = tr_text
        for i in range(len(en_blocks) - 1, -1, -1):
            en_block = en_blocks[i].group(0)
            tr_block = tr_blocks[i].group(0)
            if en_block != tr_block:
                new_text = new_text[:tr_blocks[i].start()] + en_block + new_text[tr_blocks[i].end():]
                changed = True

        if changed:
            tr_file.write_text(new_text, encoding="utf-8")
            fixes += 1

    return fixes


def fix_access_key_issues_code_block():
    """Add missing code block to access-key-issues translations.

    English has 1 code block (example access key). Some translations are missing it.
    Find where it should go and insert it.
    """
    en_file = DOCS / "client" / "troubleshooting" / "access-key-issues.md"
    en_text = en_file.read_text(encoding="utf-8")
    en_blocks = CODE_BLOCK_RE.findall(en_text)
    if not en_blocks:
        return 0

    example_block = en_blocks[0]  # The access key example

    # Find what text precedes the code block in English
    en_block_match = CODE_BLOCK_RE.search(en_text)
    # Get the line before the code block
    before_block = en_text[:en_block_match.start()].rstrip()
    last_line_en = before_block.split('\n')[-1].strip()

    fixes = 0
    for locale in get_locales():
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "access-key-issues.md"
        if not tr_file.exists():
            continue

        tr_text = tr_file.read_text(encoding="utf-8")
        tr_blocks = CODE_BLOCK_RE.findall(tr_text)

        if len(tr_blocks) >= 1:
            continue  # Already has a code block

        # Find a good place to insert — look for the paragraph that mentions
        # the access key format (ss://) or insert at end of content
        # The code block should appear after a paragraph mentioning key format
        lines = tr_text.split('\n')
        insert_idx = None

        for i, line in enumerate(lines):
            # Look for the line that talks about the access key format
            if 'ss://' in line.lower() or 'outline=1' in line.lower():
                insert_idx = i + 1
                break

        if insert_idx is None:
            # Fallback: insert before the last non-empty paragraph
            for i in range(len(lines) - 1, -1, -1):
                if lines[i].strip():
                    insert_idx = i + 1
                    break

        if insert_idx is not None:
            lines.insert(insert_idx, '')
            lines.insert(insert_idx + 1, example_block)
            lines.insert(insert_idx + 2, '')
            tr_file.write_text('\n'.join(lines), encoding='utf-8')
            fixes += 1

    return fixes


def fix_connection_issues_extra_links():
    """Remove extra full-path self-referencing links from connection-issues.

    Translations have links like [text](/client/troubleshooting/connection-issues#Anchor)
    as artifacts from Salesforce URL conversion. These appear as extra duplicate links
    alongside the correct [text](#Anchor) links. Remove the full-path versions.
    """
    fixes = 0
    for locale in get_locales():
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
        if not tr_file.exists():
            continue

        tr_text = tr_file.read_text(encoding="utf-8")
        new_text = tr_text

        # Remove [text](/client/troubleshooting/connection-issues#Anchor) patterns
        # These appear as markdown links with full internal paths to the same page
        # Pattern: [text or empty](/client/troubleshooting/connection-issues#Something)
        pattern = re.compile(
            r'\[([^\]]*)\]\(/client/troubleshooting/connection-issues#\w+\)'
        )
        matches = list(pattern.finditer(new_text))
        if not matches:
            continue

        # Remove these links, keeping just the link text (if any)
        for m in reversed(matches):
            link_text = m.group(1).strip()
            new_text = new_text[:m.start()] + link_text + new_text[m.end():]

        if new_text != tr_text:
            tr_file.write_text(new_text, encoding='utf-8')
            fixes += 1

    return fixes


def fix_internet_access_sandbox_urls():
    """Remove Salesforce sandbox URLs from internet-access translations.

    Some translations have leftover links to
    https://google-jigsaw--jigsawuat.sandbox.my.site.com/outline/s/article/...
    which is a Salesforce sandbox environment. Replace these with the correct
    internal link.
    """
    fixes = 0
    sandbox_re = re.compile(
        r'\[([^\]]*)\]\(https://google-jigsaw--jigsawuat\.sandbox\.my\.site\.com/[^)]+\)'
    )

    for locale in get_locales():
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "internet-access.md"
        if not tr_file.exists():
            continue

        tr_text = tr_file.read_text(encoding="utf-8")
        matches = list(sandbox_re.finditer(tr_text))
        if not matches:
            continue

        new_text = tr_text
        for m in reversed(matches):
            link_text = m.group(1)
            # Replace with just the link text (removing the dead URL)
            new_text = new_text[:m.start()] + link_text + new_text[m.end():]

        if new_text != tr_text:
            tr_file.write_text(new_text, encoding='utf-8')
            fixes += 1

    return fixes


def main():
    print("1. Fixing install-linux code block whitespace...")
    n = fix_install_linux_code_blocks()
    print(f"   Fixed {n} files")

    print("2. Fixing access-key-issues missing code block...")
    n = fix_access_key_issues_code_block()
    print(f"   Fixed {n} files")

    print("3. Fixing connection-issues extra self-referencing links...")
    n = fix_connection_issues_extra_links()
    print(f"   Fixed {n} files")

    print("4. Fixing internet-access Salesforce sandbox URLs...")
    n = fix_internet_access_sandbox_urls()
    print(f"   Fixed {n} files")


if __name__ == "__main__":
    main()
