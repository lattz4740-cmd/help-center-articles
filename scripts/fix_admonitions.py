#!/usr/bin/env python3
"""Convert *Important:* and Note: patterns to Docusaurus admonitions across all translations."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

total_fixes = 0

# Fix 1: connecting-device.md — *Important:* → :::warning[Important]
# Pattern: line starting with *Important:* (or translated equivalent with italic markers)
# The italic markers may vary: *...:* or *...:* etc.
connecting_device = "docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md"

for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connecting_device
    if not f.exists():
        continue

    text = f.read_text("utf-8")
    lines = text.split("\n")
    new_lines = []
    fixed = False

    for line in lines:
        # Match *Important:* or *<translated>:* at start of line
        # The pattern is: *SomeWord:* followed by the rest of the content
        m = re.match(r'^\*([^*]+?)[:：]\*\s*(.+)$', line)
        if m:
            label = m.group(1).strip()
            content = m.group(2).strip()
            new_lines.append(f":::warning[{label}]")
            new_lines.append(content)
            new_lines.append(":::")
            fixed = True
        else:
            new_lines.append(line)

    if fixed:
        f.write_text("\n".join(new_lines), "utf-8")
        print(f"  FIXED {locale_dir.name}/connecting-device.md (Important → :::warning)")
        total_fixes += 1

# Fix 2: connection-issues.md — Note: → :::note
connection_issues = "docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connection_issues
    if not f.exists():
        continue

    text = f.read_text("utf-8")
    lines = text.split("\n")
    new_lines = []
    fixed = False

    for line in lines:
        # Match "Note:" or translated equivalent at start of line
        # Common patterns: "Note:", "Nota:", "注:", "注意:", "참고:", etc.
        # We look for a short word/phrase followed by colon, then the actual content
        # But we need to be careful not to match headings like "### How to test:"
        if line.startswith("#"):
            new_lines.append(line)
            continue

        # Try to match Note-like prefix patterns
        # English: "Note: ..."
        # We'll match any line that starts with a short word + colon that corresponds
        # to the "Note:" line in the English source (it appears right after "Try connecting...")
        m = re.match(r'^(Note|Nota|Hinweis|Remarque|Примечание|メモ|참고|注意|備註|หมายเหตุ|Catatan|Napomena|Забележка|টীকা|Qeyd|Shënim|Забелешка|Тэмдэглэл|नोट|Tandaan|Huomautus|Athugasemd|Uwaga|Observação|Notă|Poznámka|Opomba|Opmerking|Anmärkning|Notat|Kumbuka|Piezīme|Märkus|Σημείωση|Eskualdaketa|ملاحظه|הערה)[:：]\s*(.+)$', line)
        if m:
            content = m.group(2).strip()
            new_lines.append(":::note")
            new_lines.append(content)
            new_lines.append(":::")
            fixed = True
        else:
            new_lines.append(line)

    if fixed:
        f.write_text("\n".join(new_lines), "utf-8")
        print(f"  FIXED {locale_dir.name}/connection-issues.md (Note → :::note)")
        total_fixes += 1

print(f"\nDone: {total_fixes} files fixed")
