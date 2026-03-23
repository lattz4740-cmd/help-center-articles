#!/usr/bin/env python3
"""Fix remaining admonition patterns that weren't caught by previous passes."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

total_fixes = 0

def fix_file(rel_path, find_and_replace_fn):
    """Fix a specific file using a custom find-and-replace function."""
    global total_fixes
    f = I18N / rel_path
    if not f.exists():
        print(f"  SKIP {rel_path} (not found)")
        return
    text = f.read_text("utf-8")
    new_text = find_and_replace_fn(text)
    if new_text != text:
        f.write_text(new_text, "utf-8")
        locale = rel_path.split("/")[0]
        print(f"  FIXED {locale}/{rel_path.split('/')[-1]}")
        total_fixes += 1

CD = "docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md"
CI = "docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# === connecting-device remaining ===

# hy: *Կարևոր է*․ content
def fix_hy_cd(text):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        if line.startswith("*") and "Outline" in line and ":::warning" not in text:
            # Extract label and content - pattern: *label*. content
            m = re.match(r'^\*(.+?)\*[.\u2024\u0589]\s*(.+)$', line)
            if m:
                new_lines.append(f":::warning[{m.group(1)}]")
                new_lines.append(m.group(2))
                new_lines.append(":::")
                continue
        new_lines.append(line)
    return "\n".join(new_lines)

fix_file(f"hy/{CD}", fix_hy_cd)

# ru: no prefix, just content on last line
def fix_ru_cd(text):
    if ":::warning" in text:
        return text
    lines = text.split("\n")
    # Find last non-empty line
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() and not lines[i].startswith("#") and not lines[i].startswith("-") and not lines[i].startswith("---"):
            lines[i] = f":::warning\n{lines[i]}\n:::"
            break
    return "\n".join(lines)

fix_file(f"ru/{CD}", fix_ru_cd)

# === connection-issues remaining ===

# For these locales, find the Note line by position
# It's always on the line after "Try connecting to Outline from another device"

def fix_note_by_position(text, note_prefixes=None):
    """Find the Note line after 'try connecting' and wrap in :::note."""
    if ":::note" in text:
        return text
    lines = text.split("\n")
    new_lines = []
    found_try = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Look for "Try connecting to Outline from another device" line
        if not found_try and stripped and "Outline" in stripped and not stripped.startswith("#"):
            # Check if previous non-empty was a "How to test:" heading
            prev = ""
            for j in range(i - 1, -1, -1):
                if lines[j].strip():
                    prev = lines[j].strip()
                    break
            if prev.startswith("###"):
                found_try = True
                new_lines.append(line)
                continue

        # The line after "try connecting" (with possible blank line between)
        if found_try and stripped:
            # This is the Note line - wrap it
            # Strip any prefix like "ማስታወሻ፦" etc.
            content = stripped
            if note_prefixes:
                for prefix in note_prefixes:
                    if stripped.startswith(prefix):
                        content = stripped[len(prefix):].lstrip(":").lstrip("：").lstrip("፦").lstrip("៖").strip()
                        break

            new_lines.append(":::note")
            new_lines.append(content)
            new_lines.append(":::")
            found_try = False
            # Add remaining lines
            for remaining in lines[i+1:]:
                new_lines.append(remaining)
            return "\n".join(new_lines)

        new_lines.append(line)

    return "\n".join(new_lines)

# am: ማስታወሻ፦ content
fix_file(f"am/{CI}", lambda t: fix_note_by_position(t, ["ማስታወሻ፦", "ማስታወሻ"]))

# he: no prefix (line 52)
fix_file(f"he/{CI}", lambda t: fix_note_by_position(t))

# hy: no prefix (line 51)
fix_file(f"hy/{CI}", lambda t: fix_note_by_position(t))

# km: ចំណាំ៖ content
fix_file(f"km/{CI}", lambda t: fix_note_by_position(t, ["ចំណាំ៖", "ចំណាំ"]))

# my: no prefix (line 51)
fix_file(f"my/{CI}", lambda t: fix_note_by_position(t))

# ru: Обратите внимание, content (line 53)
fix_file(f"ru/{CI}", lambda t: fix_note_by_position(t))

# uk: Примітка. content (line 51)
fix_file(f"uk/{CI}", lambda t: fix_note_by_position(t, ["Примітка.", "Примітка"]))

print(f"\nDone: {total_fixes} files fixed")
