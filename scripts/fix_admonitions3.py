#!/usr/bin/env python3
"""Fix remaining admonition patterns with varied punctuation and stripped labels."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
DOCS = ROOT / "docs"

total_fixes = 0

# === connecting-device.md ===
# The Important admonition is always the LAST line of the file.
# Patterns seen:
# 1. *Label:* content  → already handled
# 2. *Label*: content  → already handled
# 3. *Label!* content  (da, lv, sv)
# 4. *Label.* content  (et, hy, uk)
# 5. *Label-* content  (my)
# 6. *Label፦* content  (am)
# 7. *Label៖* content  (km)
# 8. Label: content     (fa, ja, zh-Hant) — no asterisks
# 9. : content          (de, es, fr, it, ko, pl, pt-BR, th, tr) — label stripped
# 10. ：content          (zh-Hans) — full-width colon, label stripped
# 11. content only       (ru) — completely stripped

connecting_device = "docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md"

# Read English to get the content for comparison
en_file = DOCS / "client/getting-started/connecting-device.md"
en_text = en_file.read_text("utf-8")

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

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            new_lines.append(line)
            continue

        # Pattern 3: *Label!* content
        m = re.match(r'^\*([^*]+)!\*\s*(.+)$', stripped)
        if m:
            new_lines.append(f":::warning[{m.group(1).strip()}]")
            new_lines.append(m.group(2).strip())
            new_lines.append(":::")
            fixed = True
            continue

        # Pattern 4/5: *Label.* or *Label-* or *Label፦* or *Label៖* content
        m = re.match(r'^\*([^*]+?)[.\-፦៖․]\*\s*(.+)$', stripped)
        if m:
            new_lines.append(f":::warning[{m.group(1).strip()}]")
            new_lines.append(m.group(2).strip())
            new_lines.append(":::")
            fixed = True
            continue

        # Pattern 8: Label: content (no asterisks) — known labels
        m = re.match(r'^(مهم|重要|重要事項)[:：]\s*(.+)$', stripped)
        if m:
            new_lines.append(f":::warning[{m.group(1).strip()}]")
            new_lines.append(m.group(2).strip())
            new_lines.append(":::")
            fixed = True
            continue

        # Pattern 9/10: starts with : or ：(label was stripped)
        # Only match the last non-empty content line
        if (stripped.startswith(':') or stripped.startswith('：')) and i >= len(lines) - 3:
            content = stripped.lstrip(':').lstrip('：').strip()
            if content:
                new_lines.append(":::warning")
                new_lines.append(content)
                new_lines.append(":::")
                fixed = True
                continue

        # Pattern 11: ru — no prefix at all, just content as last line
        # Only apply if this is the last non-empty line and locale is ru
        if locale_dir.name == "ru" and i == len(lines) - 1 and "Outline" in stripped and not stripped.startswith("#"):
            new_lines.append(":::warning")
            new_lines.append(stripped)
            new_lines.append(":::")
            fixed = True
            continue

        new_lines.append(line)

    if fixed:
        f.write_text("\n".join(new_lines), "utf-8")
        print(f"  FIXED {locale_dir.name}/connecting-device.md")
        total_fixes += 1

# === connection-issues.md ===
# The Note line appears right after "Try connecting to Outline from another device."
# Remaining patterns use: !, ., ፦, ៖, space before :, or no prefix at all

connection_issues = "docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# For each remaining locale, we know the Note line position from the check output
# Strategy: find the "Try connecting..." line, then the next non-empty line is the Note
REMAINING_NOTE_LOCALES = {
    "am", "da", "et", "fi", "fil", "fr", "he", "hy", "km",
    "lv", "my", "ru", "sq", "sv", "tr", "uk"
}

for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir() or locale_dir.name not in REMAINING_NOTE_LOCALES:
        continue
    f = locale_dir / connection_issues
    if not f.exists():
        continue
    text = f.read_text("utf-8")
    if ":::note" in text:
        continue

    lines = text.split("\n")
    new_lines = []
    fixed = False
    # Find "How to test:" section for firewall, then the Note line
    in_firewall_test = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect the "How to test:" section under Firewall heading
        if stripped.startswith("### ") and ("test" in stripped.lower() or "prüfen" in stripped.lower() or "tester" in stripped.lower() or "测" in stripped.lower() or "테스트" in stripped.lower() or "ทดสอบ" in stripped.lower() or "проверить" in stripped.lower() or "проверка" in stripped.lower() or "перевірити" in stripped.lower() or "тест" in stripped.lower() or "ፈተና" in stripped.lower() or "prøve" in stripped.lower() or "testida" in stripped.lower() or "testata" in stripped.lower() or "test" in stripped.lower()):
            in_firewall_test = True
            new_lines.append(line)
            continue

        # If we found a "Things to fix" heading, we've passed the Note
        if stripped.startswith("### ") and in_firewall_test and "test" not in stripped.lower():
            in_firewall_test = False

        if in_firewall_test and not fixed and stripped and not stripped.startswith("#"):
            # Skip the "Try connecting..." line itself
            if i > 0 and new_lines:
                prev_non_empty = ""
                for j in range(len(new_lines) - 1, -1, -1):
                    if new_lines[j].strip():
                        prev_non_empty = new_lines[j].strip()
                        break

                # The Note line comes after the "Try connecting" line
                # Check if previous non-empty line was "Try connecting..."
                # or if this line matches known Note patterns
                is_note_line = False

                # Check various Note-like prefixes with varied punctuation
                note_patterns = [
                    r'^(ማስታወሻ|Bemærk|Märkus|Huom|Paalala|Remarque|Piezīme|Obs|Not|Примітка|Shënim|ចំណាំ)[!.፦៖:]?\s*[:：]?\s*(.+)$',
                ]
                for pat in note_patterns:
                    m = re.match(pat, stripped)
                    if m:
                        content = m.group(2).strip()
                        new_lines.append(":::note")
                        new_lines.append(content)
                        new_lines.append(":::")
                        fixed = True
                        is_note_line = True
                        in_firewall_test = False
                        break

                if is_note_line:
                    continue

                # he, hy, my, ru — no prefix, just content after "Try connecting" line
                # These are trickier — check if prev line was about trying to connect
                if not fixed:
                    try_keywords = ["connect", "חבר", "подключ", "підключ", "ချိတ်ဆက်", "միdelays", "миан"]
                    if any(kw in prev_non_empty.lower() for kw in try_keywords):
                        # This is the Note content without a prefix
                        new_lines.append(":::note")
                        new_lines.append(stripped)
                        new_lines.append(":::")
                        fixed = True
                        in_firewall_test = False
                        continue

        new_lines.append(line)

    if fixed:
        f.write_text("\n".join(new_lines), "utf-8")
        print(f"  FIXED {locale_dir.name}/connection-issues.md")
        total_fixes += 1
    else:
        print(f"  SKIP  {locale_dir.name}/connection-issues.md (no pattern matched)")

print(f"\nDone: {total_fixes} files fixed")
