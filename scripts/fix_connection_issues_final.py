#!/usr/bin/env python3
"""Final fix for connection-issues.md heading structure.

For locales where section titles are **bold** lines (bg, ca, sr, etc.):
1. Convert bold section titles to ## headings with correct anchors
2. Remove misplaced anchors from sub-section headings
3. Also handles de/it/ja/nl which have different structural issues

Strategy: find the 5 bold section title lines (Internet, Firewall, Software,
Device, Server) and convert them to ## headings. Remove any anchor IDs that
were incorrectly placed on sub-section headings.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

ANCHOR_RE = re.compile(r'\s*\{#([^}]+)\}')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')
BOLD_LINE_RE = re.compile(r'^\*\*(.+?)\*\*\s*:?\s*$')

SECTION_ANCHORS = ['Internetissues', 'FirewallIssues', 'SoftwareIssues', 'DeviceSettings', 'ServerIssues']

# Locales still missing anchors after previous fixes
PROBLEM_LOCALES = ['bg', 'ca', 'de', 'it', 'ja', 'nl', 'sr']


def fix_bold_section_locales(filepath):
    """Fix locales where section titles are bold text (bg, ca, sr).

    These have a pattern of 5 bold section titles interleaved with ## sub-sections.
    The anchors were incorrectly placed on the ## sub-sections instead.
    """
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    # Find all bold lines and ## headings
    bold_lines = []  # (line_idx, text)
    heading_lines = []  # (line_idx, text, anchor_or_none)

    for i, line in enumerate(lines):
        bm = BOLD_LINE_RE.match(line)
        hm = HEADING_RE.match(line)
        if bm:
            bold_lines.append((i, bm.group(1).strip()))
        elif hm:
            anchor = ANCHOR_RE.search(line)
            heading_lines.append((i, hm.group(2).strip(), anchor.group(1) if anchor else None))

    # Skip intro bold lines (in the bullet list, before first ## heading)
    first_heading_line = heading_lines[0][0] if heading_lines else len(lines)
    section_bolds = [(i, t) for i, t in bold_lines if i > 6]  # Skip frontmatter area

    if len(section_bolds) < 5:
        return 0  # Not enough bold lines to be section titles

    # The 5 section titles should be the bold lines that appear BEFORE ## headings
    # (not the ones in the bullet list intro)
    # Filter: keep bold lines that are followed (within 3 lines) by a ## heading
    section_titles = []
    for idx, (line_idx, bold_text) in enumerate(section_bolds):
        # Check if next non-empty line is a ## heading
        for j in range(line_idx + 1, min(line_idx + 4, len(lines))):
            if lines[j].strip() and HEADING_RE.match(lines[j]):
                section_titles.append((line_idx, bold_text))
                break

    if len(section_titles) < 5:
        # Try just taking first 5 bold lines after the intro
        intro_end = 12  # After frontmatter + bullet list
        section_titles = [(i, t) for i, t in section_bolds if i > intro_end][:5]

    if len(section_titles) < 5:
        return 0

    # Step 1: Remove ALL existing anchors from ## headings (they're misplaced)
    fixes = 0
    for i, line in enumerate(lines):
        hm = HEADING_RE.match(line)
        if hm:
            cleaned = ANCHOR_RE.sub('', line).rstrip()
            if cleaned != line:
                lines[i] = cleaned
                fixes += 1

    # Step 2: Convert bold section titles to ## headings with correct anchors
    for (line_idx, bold_text), anchor_id in zip(section_titles[:5], SECTION_ANCHORS):
        old_line = lines[line_idx]
        # Build new heading, preserving trailing colon if present
        clean_text = bold_text.strip()
        colon = ':' if old_line.rstrip().endswith(':') else ''
        lines[line_idx] = f'## {clean_text}{colon} {{#{anchor_id}}}'
        fixes += 1

    filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def fix_de_it(filepath):
    """Fix de/it which have all ## headings but no bold section titles.

    The section structure uses ## headings with German text.
    Anchors were placed on first 3 unique-ish headings but Device/Server
    sections have no distinct section title heading.
    Insert ## headings with anchors before the Device and Server sections.
    """
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    existing = set(ANCHOR_RE.findall(text))
    needed = set(SECTION_ANCHORS) - existing
    if not needed:
        return 0

    # Find the SoftwareIssues anchor line
    sw_line = None
    for i, line in enumerate(lines):
        if '{#SoftwareIssues}' in line:
            sw_line = i
            break
    if sw_line is None:
        return 0

    # After SoftwareIssues, scan for content that looks like Device/Server sections
    # In de/it, the "Was Sie prüfen sollten:" heading marks the Device section
    # The last ## heading block marks the Server section

    # Find all ## headings after SoftwareIssues
    post_sw_headings = []
    for i in range(sw_line + 1, len(lines)):
        hm = HEADING_RE.match(lines[i])
        if hm:
            post_sw_headings.append(i)

    fixes = 0

    # For DeviceSettings: should be the "Things to check" heading (unique in the file)
    if 'DeviceSettings' in needed:
        for i in post_sw_headings:
            line = lines[i]
            cleaned = ANCHOR_RE.sub('', line).rstrip()
            # This is likely the "check/prüfen" heading
            if any(kw in cleaned.lower() for kw in ['prüfen', 'check', 'controlla', 'verificar', 'comprovar', '確認', '점검']):
                if '{#' not in line:
                    lines[i] = cleaned + ' {#DeviceSettings}'
                    fixes += 1
                    break

    # For ServerIssues: insert before the last ## heading block
    if 'ServerIssues' in needed and len(post_sw_headings) >= 2:
        # Find where the "Server issues" content starts
        # It's after the Device section — look for the last "How to test" heading
        last_test_heading = None
        for i in reversed(post_sw_headings):
            line_lower = ANCHOR_RE.sub('', lines[i]).lower()
            if any(kw in line_lower for kw in ['test', 'prüfen', 'testen', 'テスト']):
                last_test_heading = i
                break
        if last_test_heading:
            # Insert a Server issues heading before it
            lines.insert(last_test_heading, '')
            lines.insert(last_test_heading, '## {#ServerIssues}')
            fixes += 1

    if fixes > 0:
        filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def fix_nl(filepath):
    """Fix nl which is missing DeviceSettings and ServerIssues."""
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    existing = set(ANCHOR_RE.findall(text))
    if 'DeviceSettings' in existing and 'ServerIssues' in existing:
        return 0

    fixes = 0

    # nl has bold "Oplossingen": that needs to become a heading
    # Find the "Check het volgende" heading with SoftwareIssues — that's the Device section
    # The content after the last ## is the Server section

    # Look for bold lines after the SoftwareIssues anchor
    sw_line = None
    for i, line in enumerate(lines):
        if '{#SoftwareIssues}' in line:
            sw_line = i
            break

    if sw_line is None:
        return 0

    for i in range(sw_line + 1, len(lines)):
        bm = BOLD_LINE_RE.match(lines[i])
        if bm and 'DeviceSettings' not in existing:
            # This bold line is likely a sub-section, but let's check if we need
            # to add a Device settings heading before the "Check" section
            pass

    # Simpler: just scan for content patterns
    # In nl, Device section starts around line 58, Server around line 73
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Look for standalone text lines that are section titles
        if stripped and not HEADING_RE.match(line) and not BOLD_LINE_RE.match(line):
            if i > 50 and not stripped.startswith('-') and not stripped.startswith('*') and len(stripped) < 60:
                # Check if it looks like "Device settings" or "Server issues" equivalent
                pass

    # Fallback: just add empty anchor headings at the right spots
    # Find the line with {#SoftwareIssues} check heading, and add DeviceSettings after its block
    check_line = None
    for i, line in enumerate(lines):
        if '{#SoftwareIssues}' in line:
            check_line = i
            break

    if check_line and 'DeviceSettings' not in existing:
        # Find the next ## heading after SoftwareIssues — that's still part of Software section
        # Then find where Device section content starts
        for i in range(check_line + 1, len(lines)):
            hm = HEADING_RE.match(lines[i])
            if hm and i > check_line + 10:  # Far enough to be a new section
                # Insert DeviceSettings before this heading
                lines.insert(i, '')
                lines.insert(i, '## {#DeviceSettings}')
                fixes += 1
                break

    # Re-scan for ServerIssues
    text2 = '\n'.join(lines)
    if 'ServerIssues' not in ANCHOR_RE.findall(text2):
        # Find the last ## heading — Server section is after it
        last_h = None
        for i, line in enumerate(lines):
            if HEADING_RE.match(line):
                last_h = i
        if last_h:
            # Look for content after the last heading that's the server section
            for i in range(last_h + 1, len(lines)):
                if lines[i].strip() and not lines[i].strip().startswith('-'):
                    lines.insert(i, '')
                    lines.insert(i, '## {#ServerIssues}')
                    fixes += 1
                    break

    if fixes > 0:
        filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def main():
    total_fixes = 0

    for locale in PROBLEM_LOCALES:
        conn_file = I18N / locale / 'docusaurus-plugin-content-docs' / 'current' / 'client' / 'troubleshooting' / 'connection-issues.md'
        if not conn_file.exists():
            continue

        text = conn_file.read_text(encoding='utf-8')
        existing = set(ANCHOR_RE.findall(text))
        missing = set(SECTION_ANCHORS) - existing
        if not missing:
            print(f'  {locale}: ALL ANCHORS PRESENT')
            continue

        # Count bold section titles to determine approach
        bold_count = len(BOLD_LINE_RE.findall(text))

        if locale in ('bg', 'ca', 'sr'):
            fixes = fix_bold_section_locales(conn_file)
        elif locale in ('de', 'it', 'ja'):
            fixes = fix_de_it(conn_file)
        elif locale == 'nl':
            fixes = fix_nl(conn_file)
        else:
            fixes = 0

        if fixes:
            print(f'  {locale}: fixed {fixes} issue(s)')
            total_fixes += fixes
        else:
            print(f'  {locale}: COULD NOT FIX (missing: {sorted(missing)})')

    print(f'\nDone: {total_fixes} total fixes')


if __name__ == '__main__':
    main()
