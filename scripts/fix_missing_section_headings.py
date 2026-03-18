#!/usr/bin/env python3
"""Fix missing DeviceSettings and ServerIssues section headings in connection-issues.md.

In many locales, the "Device settings" and "Server issues" section titles
are plain text lines (not headings), so they didn't get anchor IDs.
This script finds these plain-text section titles by looking for non-heading,
non-bold, non-empty lines that appear between the last sub-section heading
of one section and the first sub-section heading of the next section.

Also fixes cases where anchors were placed on the wrong heading (sub-section
instead of section title).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

ANCHOR_RE = re.compile(r'\{#([^}]+)\}')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')


def fix_file(filepath):
    """Fix missing DeviceSettings and ServerIssues anchors."""
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    # Check which anchors are missing
    existing = set(ANCHOR_RE.findall(text))
    needed = {}
    if 'DeviceSettings' not in existing:
        needed['DeviceSettings'] = True
    if 'ServerIssues' not in existing:
        needed['ServerIssues'] = True

    if not needed:
        return 0

    # Find the line with {#SoftwareIssues} — DeviceSettings section starts after that section
    software_line = None
    for i, line in enumerate(lines):
        if '{#SoftwareIssues}' in line:
            software_line = i
            break

    if software_line is None:
        return 0

    # After the SoftwareIssues heading, find the next ## sub-section headings
    # then find the plain text line(s) between sections
    fixes = 0

    # Strategy: scan forward from SoftwareIssues, looking for plain text lines
    # that appear between heading blocks. These are the section titles.
    # The pattern is:
    #   ## Sub-heading (last of Software section)
    #   [content]
    #   Plain text: Device settings section title   <-- NEEDS TO BE ## heading
    #   ## Sub-heading (first of Device section)
    #   [content]
    #   Plain text: Server issues section title     <-- NEEDS TO BE ## heading
    #   ## Sub-heading (first of Server section)

    section_titles_found = []  # (line_index, line_text)

    i = software_line + 1
    in_heading_block = False
    last_heading_line = software_line

    while i < len(lines):
        line = lines[i].strip()
        hm = HEADING_RE.match(lines[i])

        if hm:
            last_heading_line = i
            in_heading_block = True
        elif line and not line.startswith('-') and not line.startswith('*') and not line.startswith('1.'):
            # Non-empty, non-list, non-heading line
            # Check if it's between heading blocks (potential section title)
            if in_heading_block:
                # We just left a heading block — this could be content or a section title
                # Look ahead to see if next non-empty line is a heading
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and HEADING_RE.match(lines[j]):
                    # This line is between two heading blocks — it's a section title
                    section_titles_found.append((i, line))
                    in_heading_block = False
        elif not line:
            pass  # Skip empty lines

        i += 1

    # Assign anchors to found section titles
    anchor_order = ['DeviceSettings', 'ServerIssues']
    anchor_idx = 0

    for line_idx, title_text in section_titles_found:
        if anchor_idx >= len(anchor_order):
            break
        anchor_id = anchor_order[anchor_idx]
        if anchor_id not in needed:
            anchor_idx += 1
            if anchor_idx >= len(anchor_order):
                break
            anchor_id = anchor_order[anchor_idx]
            if anchor_id not in needed:
                continue

        # Convert plain text to ## heading with anchor
        clean = title_text.strip().rstrip(':').strip()
        lines[line_idx] = f'## {title_text.strip()} {{#{anchor_id}}}'
        fixes += 1
        anchor_idx += 1

    # Also handle cases where {#DeviceSettings} is on a sub-section heading
    # but the actual section title is plain text above it
    if 'DeviceSettings' in existing and 'ServerIssues' in needed:
        # DeviceSettings exists but ServerIssues doesn't
        # Find the DeviceSettings heading line
        ds_line = None
        for i, line in enumerate(lines):
            if '{#DeviceSettings}' in line:
                ds_line = i
                break
        if ds_line:
            # Scan forward from DeviceSettings for plain text section title
            for i in range(ds_line + 1, len(lines)):
                line = lines[i].strip()
                if not line:
                    continue
                hm = HEADING_RE.match(lines[i])
                if hm:
                    continue
                if line.startswith('-') or line.startswith('*') or line.startswith('1.'):
                    continue
                # Found a non-heading, non-list line — check if next non-empty is a heading
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and HEADING_RE.match(lines[j]):
                    lines[i] = f'## {line} {{#ServerIssues}}'
                    fixes += 1
                    break

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
