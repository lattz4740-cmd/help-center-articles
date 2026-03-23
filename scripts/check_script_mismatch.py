#!/usr/bin/env python3
"""Detect articles where the title script doesn't match the body script.

For example: Latvian title (Latin) but Lao body (Lao script).
"""

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Map locale to expected Unicode script(s)
LOCALE_SCRIPTS = {
    "ar": {"ARABIC"}, "fa": {"ARABIC"}, "ur": {"ARABIC"},
    "he": {"HEBREW"},
    "am": {"ETHIOPIC"},
    "hi": {"DEVANAGARI"}, "mr": {"DEVANAGARI"}, "ne": {"DEVANAGARI"},
    "bn": {"BENGALI"},
    "ta": {"TAMIL"},
    "si": {"SINHALA"},
    "ka": {"GEORGIAN"},
    "hy": {"ARMENIAN"},
    "my": {"MYANMAR"},
    "km": {"KHMER"},
    "lo": {"LAO"},
    "th": {"THAI"},
    "ja": {"CJK", "HIRAGANA", "KATAKANA"},
    "ko": {"HANGUL", "CJK"},
    "zh-Hans": {"CJK"}, "zh-Hant": {"CJK"}, "zh-HK": {"CJK"},
    "ru": {"CYRILLIC"}, "uk": {"CYRILLIC"}, "bg": {"CYRILLIC"},
    "sr": {"CYRILLIC"}, "mk": {"CYRILLIC"}, "mn": {"CYRILLIC"},
    "kk": {"CYRILLIC"},
    "el": {"GREEK"},
}

# Latin-script locales (everything else)
LATIN_LOCALES = {
    "af", "az", "bs", "ca", "cs", "da", "de", "en-GB", "es", "es-419",
    "et", "fi", "fil", "fr", "hr", "hu", "id", "is", "it", "lv", "ms",
    "nb", "nl", "pl", "pt", "pt-BR", "ro", "sk", "sl", "sq", "sv", "sw",
    "tr", "vi",
}

def get_dominant_script(text):
    """Get the dominant non-Latin, non-Common script in text."""
    script_counts = {}
    for ch in text:
        if ch.isalpha():
            name = unicodedata.name(ch, "UNKNOWN")
            # Extract script from Unicode name
            for script in ["ARABIC", "HEBREW", "ETHIOPIC", "DEVANAGARI", "BENGALI",
                          "TAMIL", "SINHALA", "GEORGIAN", "ARMENIAN", "MYANMAR",
                          "KHMER", "LAO", "THAI", "CJK", "HIRAGANA", "KATAKANA",
                          "HANGUL", "CYRILLIC", "GREEK", "LATIN"]:
                if script in name:
                    script_counts[script] = script_counts.get(script, 0) + 1
                    break
    if not script_counts:
        return None
    # Return dominant non-LATIN script, or LATIN if that's all there is
    non_latin = {k: v for k, v in script_counts.items() if k != "LATIN"}
    if non_latin:
        return max(non_latin, key=non_latin.get)
    return "LATIN"

def get_body_text(filepath):
    """Get body text after frontmatter."""
    text = filepath.read_text("utf-8")
    in_fm = False
    body_lines = []
    for line in text.split("\n"):
        if line.strip() == "---":
            in_fm = not in_fm
            continue
        if not in_fm:
            body_lines.append(line)
    return " ".join(body_lines)[:500]  # First 500 chars of body

issues = []
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir() or locale_dir.name == "partial-translations":
        continue
    docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
    if not docs_dir.exists():
        continue
    loc = locale_dir.name
    expected = LOCALE_SCRIPTS.get(loc)

    for md_file in docs_dir.rglob("*.md"):
        rel = str(md_file.relative_to(docs_dir))
        body = get_body_text(md_file)
        if len(body.strip()) < 20:
            continue

        body_script = get_dominant_script(body)

        if expected:
            # Non-Latin locale: body should contain expected script
            if body_script and body_script not in expected and body_script != "LATIN":
                issues.append((loc, rel, f"Expected {expected}, got {body_script}"))
        elif loc in LATIN_LOCALES:
            # Latin locale: body should be Latin
            if body_script and body_script != "LATIN":
                issues.append((loc, rel, f"Expected LATIN, got {body_script}"))

for loc, rel, msg in sorted(issues):
    print(f"  {loc}/{rel}: {msg}")

print(f"\nTotal issues: {len(issues)}")
