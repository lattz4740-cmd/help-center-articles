#!/usr/bin/env python3
"""Fix remaining admonition patterns not caught by first pass."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

total_fixes = 0

# Fix 1: connecting-device.md — *word*: pattern (colon OUTSIDE asterisks)
connecting_device = "docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md"

for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connecting_device
    if not f.exists():
        continue
    text = f.read_text("utf-8")
    if ":::warning" in text:
        continue  # Already fixed

    lines = text.split("\n")
    new_lines = []
    fixed = False
    for line in lines:
        # Match *SomeWord*: rest  (colon outside asterisks)
        m = re.match(r'^\*([^*]+)\*[:：]\s*(.+)$', line)
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

# Fix 2: connection-issues.md — remaining Note-like patterns
# Read each file, find the line between "Try connecting" and the next "### Things to fix"
connection_issues = "docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# Known Note prefixes in various languages
NOTE_PREFIXES = [
    "Let wel", "ملاحظة", "মনে রাখবেন", "نکته", "ध्यान दें",
    "Megjegyzés", "Athugaðu", "注", "შენიშვნა", "Ескертпе",
    "ໝາຍເຫດ", "Санамж", "टीप", "Merk", "ख्याल गर्नुहोस्",
    "Rețineți", "සටහන", "Напомена", "கவனத்திற்கு", "نوٹ",
    "Lưu ý", "備註", "หมายเหตุ", "Anmärkning", "Merk",
    "Pastaba", "Piezīme", "Märkus", "Σημείωση", "Хуулбар",
    "Нота", "Тэмдэглэл",
    # Already handled in first pass but just in case
    "Note", "Nota", "Hinweis", "Remarque", "Примечание", "メモ",
    "참고", "注意", "Catatan", "Napomena", "Забележка", "টীকা",
    "Qeyd", "Shënim", "Забелешка", "नोट", "Tandaan", "Huomautus",
    "Athugasemd", "Uwaga", "Observação", "Notă", "Poznámka",
    "Opomba", "Opmerking", "Notat", "Kumbuka", "הערה",
]

for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connection_issues
    if not f.exists():
        continue
    text = f.read_text("utf-8")
    if ":::note" in text:
        continue  # Already fixed

    lines = text.split("\n")
    new_lines = []
    fixed = False

    for line in lines:
        matched = False
        for prefix in NOTE_PREFIXES:
            # Match: PREFIX: content  or  PREFIX： content
            pattern = re.escape(prefix) + r'[:：]\s+(.+)$'
            m = re.match(pattern, line)
            if m:
                content = m.group(1).strip()
                new_lines.append(":::note")
                new_lines.append(content)
                new_lines.append(":::")
                fixed = True
                matched = True
                break
        if not matched:
            new_lines.append(line)

    if fixed:
        f.write_text("\n".join(new_lines), "utf-8")
        print(f"  FIXED {locale_dir.name}/connection-issues.md (Note → :::note)")
        total_fixes += 1

print(f"\nDone: {total_fixes} files fixed")
