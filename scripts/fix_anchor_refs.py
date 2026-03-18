#!/usr/bin/env python3
"""Fix anchor references in translated docs to match the heading anchor IDs.

After fix_heading_anchors.py adds English anchor IDs to translated headings,
the links within those docs may reference different casing or typos.
This script fixes the link references to match the actual heading anchors.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

ANCHOR_HEADING_RE = re.compile(r'^#{1,6}\s+.*\{#([^}]+)\}', re.MULTILINE)

# Known anchor typos/variants in translations → correct anchor ID
ANCHOR_TYPOS = {
    "internetissues": "Internetissues",
    "firewallissues": "FirewallIssues",
    "softwareissues": "SoftwareIssues",
    "softwareissuesss": "SoftwareIssues",
    "devicesettings": "DeviceSettings",
    "serverissues": "ServerIssues",
    "internetissues1": "Internetissues",
    "serivcemanager": "servicemanager",
}


def fix_file(filepath):
    """Fix anchor references in a file. Returns number of fixes."""
    text = filepath.read_text(encoding="utf-8")

    # Extract actual heading anchor IDs in this file
    heading_anchors = set(ANCHOR_HEADING_RE.findall(text))

    fixes = 0
    new_text = text

    # Fix links that reference typo/variant anchors
    for typo, correct in ANCHOR_TYPOS.items():
        if correct in heading_anchors:
            # Replace (#typo) with (#correct) — but only in link targets, not headings
            pattern = re.compile(r'\(#' + re.escape(typo) + r'\)', re.IGNORECASE)
            count = len(pattern.findall(new_text))
            if count > 0:
                new_text = pattern.sub(f'(#{correct})', new_text)
                fixes += count

            # Also fix bare #typo in link targets like [text](#typo)
            pattern2 = re.compile(r'\]\(#' + re.escape(typo) + r'\)', re.IGNORECASE)
            # Already covered by the above

    if fixes > 0 and new_text != text:
        filepath.write_text(new_text, encoding="utf-8")

    return fixes


def main():
    total_fixes = 0
    total_files = 0

    for locale_dir in sorted(I18N.iterdir()):
        if not locale_dir.is_dir() or locale_dir.name == "partial-translations":
            continue
        docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
        if not docs_dir.exists():
            continue

        for md_file in sorted(docs_dir.rglob("*.md")):
            fixes = fix_file(md_file)
            if fixes > 0:
                rel = f"{locale_dir.name}/{md_file.relative_to(docs_dir)}"
                print(f"  {rel}: {fixes} fix(es)")
                total_fixes += fixes
                total_files += 1

    print(f"\nDone: {total_fixes} anchor reference fixes in {total_files} files")


if __name__ == "__main__":
    main()
