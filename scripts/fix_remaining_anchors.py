#!/usr/bin/env python3
"""Fix remaining broken anchor issues across all locales.

1. Add {#servicemanager} and {#accesskey} to terminology headings that are
   missing them (matches the 4th and 5th ## headings, which correspond to
   "What is a service manager?" and "What is an access key?").
2. Remap #One/#Two/#Three anchors in connection-issues links to the correct
   heading IDs (#Internetissues/#FirewallIssues/#SoftwareIssues).
3. Fix remaining lowercase/localized anchor references.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)(?:\s*\{#[^}]+\})?\s*$', re.MULTILINE)


def fix_terminology_anchors(filepath):
    """Add {#servicemanager} and {#accesskey} to terminology headings.

    Handles two cases:
    - ## headings: adds anchor ID to the 4th and 5th ## heading
    - **bold** paragraphs: converts the 4th and 5th bold-only line to ## headings with anchors
    """
    text = filepath.read_text(encoding="utf-8")

    # Already has both anchors?
    if '{#servicemanager}' in text and '{#accesskey}' in text:
        return 0

    fixes = 0
    new_text = text

    # Check if file uses ## headings or **bold** paragraphs
    h2_headings = list(HEADING_RE.finditer(text))
    h2_only = [(i, m) for i, m in enumerate(h2_headings) if len(m.group(1)) == 2]

    bold_re = re.compile(r'^\*\*(.+?)\*\*\s*$', re.MULTILINE)
    bold_lines = list(bold_re.finditer(text))

    if len(h2_only) >= 5:
        # Has ## headings — add anchor to 4th and 5th
        anchor_map = {3: 'servicemanager', 4: 'accesskey'}
        for h2_idx in sorted(anchor_map.keys(), reverse=True):
            anchor_id = anchor_map[h2_idx]
            if f'{{#{anchor_id}}}' in new_text:
                continue
            if h2_idx >= len(h2_only):
                continue
            _, m = h2_only[h2_idx]
            if '{#' in m.group(0):
                continue
            heading_prefix = m.group(1)
            heading_text = m.group(2).strip()
            new_line = f"{heading_prefix} {heading_text} {{#{anchor_id}}}"
            new_text = new_text[:m.start()] + new_line + new_text[m.end():]
            fixes += 1
    elif len(bold_lines) >= 5:
        # Has **bold** paragraphs — convert 4th and 5th to ## headings with anchors
        anchor_map = {3: 'servicemanager', 4: 'accesskey'}
        for bold_idx in sorted(anchor_map.keys(), reverse=True):
            anchor_id = anchor_map[bold_idx]
            if f'{{#{anchor_id}}}' in new_text:
                continue
            if bold_idx >= len(bold_lines):
                continue
            m = bold_lines[bold_idx]
            bold_text = m.group(1)
            new_line = f"## {bold_text} {{#{anchor_id}}}"
            new_text = new_text[:m.start()] + new_line + new_text[m.end():]
            fixes += 1

    if fixes > 0:
        filepath.write_text(new_text, encoding="utf-8")
    return fixes


def fix_connection_issues_anchors(filepath):
    """Fix #One/#Two/#Three and other broken anchor references."""
    text = filepath.read_text(encoding="utf-8")
    new_text = text

    # Map old anchors to correct ones
    replacements = {
        # Old Google support section anchors
        '#One)': '#Internetissues)',
        '#Two)': '#FirewallIssues)',
        '#Three)': '#SoftwareIssues)',
        # Lowercase variants
        '#devicesettings)': '#DeviceSettings)',
        '#devsettings)': '#DeviceSettings)',
        '#Devicesettings)': '#DeviceSettings)',
        '#internetissues)': '#Internetissues)',
        '#firewallissues)': '#FirewallIssues)',
        '#softwareissues)': '#SoftwareIssues)',
        '#serverissues)': '#ServerIssues)',
        '#Serverissues)': '#ServerIssues)',
        # Afrikaans localized anchors (headings now use English IDs)
        '#Internetkwessies)': '#Internetissues)',
        '#BrandmuurKwessies)': '#FirewallIssues)',
        '#SagtewareKwessies)': '#SoftwareIssues)',
        '#ToestelInstellings)': '#DeviceSettings)',
        '#BedienerKwessies)': '#ServerIssues)',
        # Malay localized anchors
        '#MasalahInternet)': '#Internetissues)',
        '#MasalahTembokApi)': '#FirewallIssues)',
        '#MasalahPerisian)': '#SoftwareIssues)',
        '#TetapanPeranti)': '#DeviceSettings)',
        '#MasalahPelayan)': '#ServerIssues)',
    }

    fixes = 0
    for old, new in replacements.items():
        count = new_text.count(old)
        if count > 0:
            new_text = new_text.replace(old, new)
            fixes += count

    # Also fix full-path anchors like /locale/client/troubleshooting/connection-issues#One
    for old_anchor, new_anchor in [('#One)', '#Internetissues)'), ('#Two)', '#FirewallIssues)'), ('#Three)', '#SoftwareIssues)')]:
        # These appear as absolute paths
        old_frag = old_anchor.rstrip(')')
        new_frag = new_anchor.rstrip(')')
        pattern = re.compile(r'connection-issues' + re.escape(old_frag) + r'\)')
        count = len(pattern.findall(new_text))
        if count > 0:
            new_text = pattern.sub(f'connection-issues{new_frag})', new_text)
            fixes += count

    if fixes > 0 and new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
    return fixes


def fix_terminology_refs(filepath):
    """Fix #servicemanager%E2%80%AB (with RTL mark) and similar."""
    text = filepath.read_text(encoding="utf-8")
    new_text = text

    # Fix URL-encoded RTL marks in anchors
    new_text = new_text.replace('#servicemanager%E2%80%AB)', '#servicemanager)')
    new_text = new_text.replace('#accesskey%E2%80%AB)', '#accesskey)')

    fixes = 0
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        fixes = text.count('%E2%80%AB)')

    return fixes


def main():
    total_fixes = 0
    total_files = 0

    for locale_dir in sorted(I18N.iterdir()):
        if not locale_dir.is_dir() or locale_dir.name == 'partial-translations':
            continue

        docs_dir = locale_dir / 'docusaurus-plugin-content-docs' / 'current'
        if not docs_dir.exists():
            continue

        locale = locale_dir.name

        # Fix terminology anchors
        term_file = docs_dir / 'about' / 'terminology.md'
        if term_file.exists():
            fixes = fix_terminology_anchors(term_file)
            if fixes:
                print(f"  {locale}/about/terminology: added {fixes} heading anchor(s)")
                total_fixes += fixes
                total_files += 1

            fixes = fix_terminology_refs(term_file)
            if fixes:
                print(f"  {locale}/about/terminology: fixed {fixes} RTL anchor ref(s)")
                total_fixes += fixes
                total_files += 1

        # Fix connection-issues anchors
        conn_file = docs_dir / 'client' / 'troubleshooting' / 'connection-issues.md'
        if conn_file.exists():
            fixes = fix_connection_issues_anchors(conn_file)
            if fixes:
                print(f"  {locale}/client/troubleshooting/connection-issues: fixed {fixes} anchor ref(s)")
                total_fixes += fixes
                total_files += 1

        # Also check internet-access which links to connection-issues anchors
        inet_file = docs_dir / 'client' / 'troubleshooting' / 'internet-access.md'
        if inet_file.exists():
            fixes = fix_connection_issues_anchors(inet_file)
            if fixes:
                print(f"  {locale}/client/troubleshooting/internet-access: fixed {fixes} anchor ref(s)")
                total_fixes += fixes
                total_files += 1

    print(f"\nDone: {total_fixes} fixes in {total_files} files")


if __name__ == '__main__':
    main()
