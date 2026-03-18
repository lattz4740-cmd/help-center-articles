#!/usr/bin/env python3
"""Fix link issues in translated markdown files.

Fixes:
1. Self-referencing links: where translations link to their own doc path
   (from old Salesforce URLs), replace with the English link at the same position.
2. Less-specific links: where English has a more specific URL on the same domain,
   use the English version.
3. http → https normalization for all links.

Does NOT fix:
- Link reordering/swapping
- Anchor differences (#step-1 vs #step-3)
- Count mismatches (different number of links)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

LOCALES = [
    "af", "am", "ar", "az", "bg", "bn", "bs",
    "ca", "cs", "da", "de", "el", "en-GB",
    "es", "es-419", "et", "fa", "fi", "fil", "fr",
    "he", "hi", "hr", "hu", "hy", "id",
    "is", "it", "ja", "ka", "kk", "km", "ko", "lo", "lv",
    "mk", "mn", "mr", "ms", "my", "nb", "ne", "nl", "pl",
    "pt", "pt-BR", "ro", "ru", "si", "sk", "sl", "sq", "sr", "sv", "sw",
    "ta", "th", "tr", "uk", "ur", "vi", "zh-Hans",
    "zh-Hant", "zh-HK",
]

# Regex to match markdown links: [text](url)
LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')


def extract_links_with_positions(text):
    """Extract all markdown links with their positions. Returns [(start, end, text, url)]."""
    results = []
    for m in LINK_RE.finditer(text):
        results.append((m.start(), m.end(), m.group(1), m.group(2)))
    return results


def is_self_link(url, doc_path):
    """Check if a URL is a self-referencing link to the same doc."""
    # Internal path like /about/how-outline-works
    normalized = "/" + doc_path
    if url == normalized or url.startswith(normalized + "#") or url.startswith(normalized + "?"):
        return True
    return False


def is_more_specific(english_url, translation_url):
    """Check if English URL is a more specific version of the translation URL (same domain, longer path)."""
    # Both must be external URLs
    if not english_url.startswith("http") or not translation_url.startswith("http"):
        return False

    # Strip protocol for comparison
    en_clean = re.sub(r'^https?://', '', english_url).rstrip('/')
    tr_clean = re.sub(r'^https?://', '', translation_url).rstrip('/')

    # Same domain, English has longer/more specific path
    en_parts = en_clean.split('/', 1)
    tr_parts = tr_clean.split('/', 1)

    if en_parts[0] == tr_parts[0]:  # Same domain
        en_path = en_parts[1] if len(en_parts) > 1 else ''
        tr_path = tr_parts[1] if len(tr_parts) > 1 else ''
        if len(en_path) > len(tr_path) and en_path.startswith(tr_path):
            return True
    return False


def upgrade_http(url):
    """Upgrade http:// to https:// for known safe domains."""
    if url.startswith("http://"):
        # Don't upgrade localhost or IP addresses
        after = url[7:]
        if after.startswith("localhost") or re.match(r'\d+\.\d+\.\d+\.\d+', after):
            return url
        return "https://" + after
    return url


def fix_file(en_path, tr_path, doc_path):
    """Fix links in a translation file. Returns (fixes_made, content) or None if no changes."""
    en_text = en_path.read_text(encoding="utf-8")
    tr_text = tr_path.read_text(encoding="utf-8")

    en_links = extract_links_with_positions(en_text)
    tr_links = extract_links_with_positions(tr_text)

    # Build replacement map: offset -> new_url
    replacements = []
    fixes = {"self_link": 0, "more_specific": 0, "http_upgrade": 0}

    # For pairwise comparison, only when counts match
    if len(en_links) == len(tr_links):
        for (_, _, _, en_url), (tr_start, tr_end, tr_link_text, tr_url) in zip(en_links, tr_links):
            new_url = tr_url

            # Fix 1: self-referencing links → use English URL
            if is_self_link(tr_url, doc_path) and not is_self_link(en_url, doc_path):
                new_url = en_url
                fixes["self_link"] += 1

            # Fix 2: English is more specific → use English URL
            elif is_more_specific(en_url, new_url):
                new_url = en_url
                fixes["more_specific"] += 1

            # Fix 3: http → https
            upgraded = upgrade_http(new_url)
            if upgraded != new_url:
                new_url = upgraded
                fixes["http_upgrade"] += 1

            if new_url != tr_url:
                replacements.append((tr_start, tr_end, tr_link_text, tr_url, new_url))
    else:
        # Count mismatch: still do http→https and self-link fixes on all translation links
        for tr_start, tr_end, tr_link_text, tr_url in tr_links:
            new_url = tr_url

            # Fix self-referencing links (replace with just removing the link? No, we don't know the English URL)
            # For count mismatches we can't do positional comparison, so skip self-link fixes

            # Fix 3: http → https
            upgraded = upgrade_http(new_url)
            if upgraded != new_url:
                new_url = upgraded
                fixes["http_upgrade"] += 1

            if new_url != tr_url:
                replacements.append((tr_start, tr_end, tr_link_text, tr_url, new_url))

    if not replacements:
        return None

    # Apply replacements in reverse order to preserve positions
    new_text = tr_text
    for start, end, link_text, old_url, new_url in reversed(replacements):
        old_link = f"[{link_text}]({old_url})"
        new_link = f"[{link_text}]({new_url})"
        new_text = new_text[:start] + new_link + new_text[end:]

    total = sum(fixes.values())
    return total, fixes, new_text


def main():
    total_fixes = 0
    total_files = 0
    fix_counts = {"self_link": 0, "more_specific": 0, "http_upgrade": 0}

    for locale in LOCALES:
        locale_dir = I18N / locale / "docusaurus-plugin-content-docs" / "current"
        if not locale_dir.exists():
            continue

        for tr_file in sorted(locale_dir.rglob("*.md")):
            doc_path = str(tr_file.relative_to(locale_dir).with_suffix(""))
            en_file = DOCS / f"{doc_path}.md"

            if not en_file.exists():
                continue

            result = fix_file(en_file, tr_file, doc_path)
            if result is None:
                continue

            count, fixes, new_text = result
            tr_file.write_text(new_text, encoding="utf-8")

            print(f"  {locale}/{doc_path}: {count} fix(es) "
                  f"(self={fixes['self_link']}, specific={fixes['more_specific']}, "
                  f"https={fixes['http_upgrade']})")

            total_fixes += count
            total_files += 1
            for k, v in fixes.items():
                fix_counts[k] += v

    print(f"\nDone: {total_fixes} fixes in {total_files} files")
    print(f"  Self-link fixes: {fix_counts['self_link']}")
    print(f"  More-specific fixes: {fix_counts['more_specific']}")
    print(f"  HTTP→HTTPS upgrades: {fix_counts['http_upgrade']}")


if __name__ == "__main__":
    main()
