#!/usr/bin/env python3
"""Debug heading structure for connection-issues.md in problematic locales.

Prints all headings and bold-only lines with their line numbers to understand
why the fix_connection_issues_structure.py script didn't catch them.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)(?:\s*\{#[^}]+\})?\s*$')
BOLD_RE = re.compile(r'^\*\*(.+?)\*\*\s*:?\s*$')
ANCHOR_RE = re.compile(r'\{#([^}]+)\}')

# Locales that still had broken anchors in the last full build
PROBLEM_LOCALES = ['bg', 'ca', 'de', 'en-GB', 'es', 'it', 'ja', 'ko', 'nl', 'pl', 'pt-BR', 'ru', 'sr', 'th', 'tr', 'zh-Hans']


def main():
    for locale in PROBLEM_LOCALES:
        f = I18N / locale / 'docusaurus-plugin-content-docs' / 'current' / 'client' / 'troubleshooting' / 'connection-issues.md'
        if not f.exists():
            print(f'{locale}: FILE MISSING')
            continue

        text = f.read_text(encoding='utf-8')
        existing_anchors = set(ANCHOR_RE.findall(text))
        missing = set(['Internetissues', 'FirewallIssues', 'SoftwareIssues', 'DeviceSettings', 'ServerIssues']) - existing_anchors

        if not missing:
            print(f'{locale}: ALL ANCHORS PRESENT')
            continue

        print(f'\n=== {locale} (missing: {sorted(missing)}) ===')
        for i, line in enumerate(text.split('\n')):
            hm = HEADING_RE.match(line)
            bm = BOLD_RE.match(line)
            if hm:
                print(f'  {i:3d} H{len(hm.group(1))} {line.strip()[:80]}')
            elif bm:
                print(f'  {i:3d} B  {line.strip()[:80]}')


if __name__ == '__main__':
    main()
