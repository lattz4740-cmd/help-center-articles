#!/usr/bin/env python3
"""Fix connection-issues anchor placement and heading hierarchy across all translations.

Problem: the fix_heading_anchors.py script placed {#anchor} IDs on sub-headings
(How to test:, Things to fix:) instead of section titles. This script:
1. Strips ALL {#anchor} IDs from headings
2. Finds the 5 section title headings and re-adds the correct anchors
3. Demotes all non-section headings from ## to ###

Section titles are identified by NOT matching common sub-heading patterns
like "test", "fix", "check", "correct", "verify" etc.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{2,6})\s+(.*)$', re.MULTILINE)
ANCHOR_RE = re.compile(r'\s*\{#[^}]+\}')

SECTION_ANCHORS = ['Internetissues', 'FirewallIssues', 'SoftwareIssues', 'DeviceSettings', 'ServerIssues']

# Sub-heading patterns in various languages — these should be ### not ##
# Matches "How to test:", "Things to fix:", "Things to check:", etc.
SUB_HEADING_KEYWORDS = [
    # English
    'test', 'fix', 'check', 'verify',
    # Romance languages
    'prueba', 'probar', 'corregir', 'comprobar', 'verificar',  # es
    'tester', 'corriger', 'vérifier',  # fr
    'testare', 'correggere', 'verificare', 'controllare',  # it
    'testar', 'corrigir', 'verificar',  # pt
    # Germanic
    'testen', 'beheben', 'prüfen', 'überprüfen',  # de
    'toets', 'regstel', 'nagaan',  # af
    # Slavic
    'тест', 'исправ', 'провер', 'поправ',  # ru/bg/sr
    'napraw', 'sprawdz', 'test',  # pl
    # Asian
    'テスト', '修正', '確認', '테스ト', '수정', '확인',  # ja/ko
    '测试', '修复', '检查', '設定',  # zh
    # Other
    'آزمایش', 'اصلاح', 'بررسی',  # fa
    'ทดสอบ', 'แก้ไข', 'ตรวจสอบ',  # th
]


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def fix_file(filepath):
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    # Step 1: Find all headings, strip anchors
    headings = []  # (line_idx, level, clean_text)
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            full_text = m.group(2)
            clean_text = ANCHOR_RE.sub('', full_text).strip()
            headings.append((i, level, clean_text))

    if not headings:
        return 0

    # Step 2: Identify section titles vs sub-headings by uniqueness.
    # Sub-headings repeat (e.g. "How to test:" appears multiple times).
    # Section titles are unique.
    text_counts = {}
    for _, _, clean_text in headings:
        norm = clean_text.rstrip(':').rstrip('：').strip().lower()
        text_counts[norm] = text_counts.get(norm, 0) + 1

    section_indices = set()
    for idx, (_, _, clean_text) in enumerate(headings):
        norm = clean_text.rstrip(':').rstrip('：').strip().lower()
        if text_counts[norm] == 1:
            section_indices.add(idx)

    # If we have more than 5 unique headings, some "unique" ones are still
    # sub-headings with slightly different wording. Take only the first 5 unique.
    if len(section_indices) > 5:
        sorted_sections = sorted(section_indices)
        section_indices = set(sorted_sections[:5])

    # If we have fewer than 5, some section titles appear with the same text
    # as sub-headings. Try: take the first heading that starts each "group"
    # (a group = section title followed by repeated sub-headings).
    if len(section_indices) < 5:
        section_indices = set()
        seen_repeated = set()
        for idx, (_, _, clean_text) in enumerate(headings):
            norm = clean_text.rstrip(':').rstrip('：').strip().lower()
            if norm not in seen_repeated:
                if text_counts[norm] > 1:
                    seen_repeated.add(norm)
                else:
                    section_indices.add(idx)

    # Step 3: Apply changes
    fixes = 0
    anchor_idx = 0

    for idx, (line_idx, level, clean_text) in enumerate(headings):
        if idx in section_indices:
            new_anchor = ""
            if anchor_idx < len(SECTION_ANCHORS):
                new_anchor = f" {{#{SECTION_ANCHORS[anchor_idx]}}}"
                anchor_idx += 1
            new_line = f"## {clean_text}{new_anchor}"
        else:
            new_line = f"### {clean_text}"

        if lines[line_idx] != new_line:
            lines[line_idx] = new_line
            fixes += 1

    if fixes > 0:
        filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def main():
    total = 0
    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
        if not f.exists():
            continue
        n = fix_file(f)
        if n:
            print(f"  {locale}: fixed {n} heading(s)")
            total += n
    print(f"\nDone: {total} fixes")


if __name__ == "__main__":
    main()
