#!/usr/bin/env python3
"""Clean up spurious link artifacts in connection-issues.md bullet lists.

The GKMS converter left behind:
1. Bare self-referencing paths like /client/troubleshooting/connection-issues#One
2. Duplicate/fragment anchor links on the same bullet line

Each bullet should have exactly ONE section anchor link. Extra anchor links
to the same target are removed (replaced with just their text content).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# The 5 valid section anchors in order
SECTION_ANCHORS = ['Internetissues', 'FirewallIssues', 'SoftwareIssues',
                   'DeviceSettings', 'ServerIssues']

# Pattern: bare self-referencing paths
BARE_PATH_RE = re.compile(r'/client/troubleshooting/connection-issues#\w+\s*')

# Pattern: any markdown link to a section anchor
ANCHOR_LINK_RE = re.compile(r'\[([^\]]*)\]\(#(' + '|'.join(SECTION_ANCHORS) + r')\)')


def fix_file(filepath):
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')
    fixes = 0

    for i, line in enumerate(lines):
        if not line.startswith('- '):
            continue

        new_line = line

        # Step 1: Remove bare self-referencing paths
        new_line = BARE_PATH_RE.sub('', new_line)

        # Step 2: For anchor links, keep only the FIRST one per anchor target.
        # Any subsequent links to the same anchor get replaced with just text.
        seen_anchors = set()
        result_parts = []
        last_end = 0

        for m in ANCHOR_LINK_RE.finditer(new_line):
            anchor = m.group(2)
            link_text = m.group(1)
            if anchor in seen_anchors:
                # Duplicate — replace with just the text content
                result_parts.append(new_line[last_end:m.start()])
                result_parts.append(link_text)
                last_end = m.end()
            else:
                seen_anchors.add(anchor)
                # Keep the first link as-is
                result_parts.append(new_line[last_end:m.end()])
                last_end = m.end()

        if result_parts:
            result_parts.append(new_line[last_end:])
            new_line = ''.join(result_parts)

        if new_line != line:
            lines[i] = new_line
            fixes += 1

    if fixes > 0:
        filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def main():
    total = 0
    for d in sorted(I18N.iterdir()):
        if not d.is_dir() or d.name == "partial-translations":
            continue
        f = d / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
        if not f.exists():
            continue
        n = fix_file(f)
        if n:
            print(f"  {d.name}: fixed {n} line(s)")
            total += n

    print(f"\nDone: {total} fixes")


if __name__ == "__main__":
    main()
