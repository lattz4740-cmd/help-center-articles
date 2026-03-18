#!/usr/bin/env python3
"""Fix connection-issues.md heading structure across all locales.

The English version has 5 section headings with anchor IDs:
  ## Internet connection issues: {#Internetissues}
  ## Network firewall issues: {#FirewallIssues}
  ## Firewall or antivirus software issues: {#SoftwareIssues}
  ## Device settings: {#DeviceSettings}
  ## Server issues: {#ServerIssues}

In some translations, these section titles appear as:
  - **Bold text** (not a heading at all)
  - #### Title (wrong heading level)
  - ## Title (correct level but may be missing anchor)

This script identifies the 5 section titles by distinguishing them from
repeated sub-section headings (like "How to test:", "Things to fix:") and
ensures they are all ## headings with the correct anchor IDs.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

SECTION_ANCHORS = ['Internetissues', 'FirewallIssues', 'SoftwareIssues', 'DeviceSettings', 'ServerIssues']

# Regex patterns for heading-like lines
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)(?:\s*\{#[^}]+\})?\s*$')
BOLD_LINE_RE = re.compile(r'^\*\*(.+?)\*\*\s*$')
ANCHOR_RE = re.compile(r'\{#([^}]+)\}')


def analyze_structure(text):
    """Analyze the heading/bold structure of a connection-issues file.

    Returns a list of (line_number, line_text, line_type, heading_level)
    where line_type is 'heading' or 'bold'.
    """
    elements = []
    for i, line in enumerate(text.split('\n')):
        hm = HEADING_RE.match(line)
        if hm:
            elements.append((i, line, 'heading', len(hm.group(1)), hm.group(2).strip()))
            continue
        bm = BOLD_LINE_RE.match(line)
        if bm:
            elements.append((i, line, 'bold', 0, bm.group(1).strip()))
    return elements


def identify_section_titles(elements):
    """Identify which elements are section titles (not sub-section titles).

    Sub-section titles like "How to test:", "Things to fix:" repeat multiple times.
    Section titles are unique. We also skip the intro bullet list items.
    """
    # Count occurrences of each heading text (normalized)
    text_counts = {}
    for _, _, _, _, text in elements:
        # Normalize: strip trailing colons and whitespace
        norm = text.rstrip(':').rstrip().lower()
        text_counts[norm] = text_counts.get(norm, 0) + 1

    # Section titles appear only once (or rarely); sub-section titles repeat
    # Also, section titles tend to come before sub-section titles
    section_candidates = []
    for elem in elements:
        line_num, line, etype, level, text = elem
        norm = text.rstrip(':').rstrip().lower()

        # Skip if this text appears more than once (it's a sub-section title)
        if text_counts.get(norm, 0) > 1:
            continue

        # Skip lines that are clearly sub-sections even if unique
        # (some translations have slightly different wording each time)
        # Heuristic: if it's a very short heading that matches common sub-section patterns, skip
        skip_patterns = ['test', 'fix', 'check', 'verify', 'correct', 'repair',
                         'tester', 'corriger', 'vérifier', 'probar', 'corregir',
                         'prüfen', 'beheben', 'überprüfen']
        if any(p in norm for p in skip_patterns) and len(norm) < 30:
            continue

        section_candidates.append(elem)

    return section_candidates


def fix_file(filepath):
    """Fix the heading structure of a connection-issues.md file."""
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    # Check if already fully correct
    existing_anchors = set(ANCHOR_RE.findall(text))
    if set(SECTION_ANCHORS).issubset(existing_anchors):
        return 0

    elements = analyze_structure(text)
    section_titles = identify_section_titles(elements)

    # We expect exactly 5 section titles
    if len(section_titles) < 5:
        # Try a fallback: look at ALL unique headings/bolds, sorted by line number
        # and take the first 5 that aren't in the intro bullet list area
        # The intro ends around line 13 (after frontmatter + bullet list)
        frontmatter_end = 0
        for i, line in enumerate(lines):
            if i > 0 and line.strip() == '---':
                frontmatter_end = i + 1
                break

        # Find first non-empty, non-list line after frontmatter
        content_start = frontmatter_end
        for i in range(frontmatter_end, len(lines)):
            if lines[i].startswith('- ') or lines[i].startswith('  ') or not lines[i].strip():
                continue
            if HEADING_RE.match(lines[i]) or BOLD_LINE_RE.match(lines[i]):
                content_start = i
                break

        section_titles = [e for e in elements if e[0] >= content_start]
        section_titles = identify_section_titles(section_titles)

    if len(section_titles) < 5:
        # Still not enough — try taking all unique heading/bold elements after the intro
        # and pick the ones that look most like section titles
        return 0

    # Take exactly 5 section titles (the first 5 unique ones after intro)
    section_titles = section_titles[:5]

    # Now fix each section title to be a ## heading with the correct anchor
    fixes = 0
    for (line_num, old_line, etype, level, title_text), anchor_id in zip(section_titles, SECTION_ANCHORS):
        # Check if this line already has the correct anchor
        if f'{{#{anchor_id}}}' in old_line:
            continue

        # Build the new line
        # Strip any existing anchor from the title text
        clean_text = ANCHOR_RE.sub('', title_text).strip()
        # Remove bold markers if present
        clean_text = clean_text.strip('*').strip()

        new_line = f'## {clean_text} {{#{anchor_id}}}'

        if lines[line_num] != new_line:
            lines[line_num] = new_line
            fixes += 1

    if fixes > 0:
        filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def main():
    total_fixes = 0
    total_files = 0

    for locale_dir in sorted(I18N.iterdir()):
        if not locale_dir.is_dir() or locale_dir.name == 'partial-translations':
            continue

        conn_file = locale_dir / 'docusaurus-plugin-content-docs' / 'current' / 'client' / 'troubleshooting' / 'connection-issues.md'
        if not conn_file.exists():
            continue

        locale = locale_dir.name
        fixes = fix_file(conn_file)
        if fixes > 0:
            print(f'  {locale}: fixed {fixes} section heading(s)')
            total_fixes += fixes
            total_files += 1

    print(f'\nDone: {total_fixes} fixes in {total_files} files')


if __name__ == '__main__':
    main()
