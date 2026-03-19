#!/usr/bin/env python3
"""
Verify translated documentation files against their English equivalents.

Checks:
1. Every English doc has a translation for every locale (no missing files).
2. No extra translation files exist that don't correspond to an English doc.
3. Frontmatter keys match the English source.
4. Code blocks in translations are identical to the English source.
5. Link URLs in translations are identical to the English source.
6. Heading structure (anchor IDs) matches between English and translations.
7. Content parity: translations aren't significantly shorter than English.
8. Category metadata (_category_.json) exists for translated directories.
"""

import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
ENGLISH_DOCS_DIR = PROJECT_ROOT / "docs"
I18N_BASE = PROJECT_ROOT / "i18n"

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

# Docs that only exist in English (no translation expected).
ENGLISH_ONLY: set[str] = {
    "index",  # Root redirect page
}

# Known missing translations that don't exist on support.google.com.
# These were never translated in the original system.
# Format: (locale, doc_path)
KNOWN_MISSING: set[tuple[str, str]] = {
    ("en-GB", "client/troubleshooting/firewall-errors"),
    ("en-GB", "client/troubleshooting/internet-access"),
    ("en-GB", "manager/server-setup/cost"),
    ("en-GB", "manager/server-setup/multiple-servers"),
    ("en-GB", "manager/server-setup/setup-faqs"),
    ("es", "about/access-resources-blocked"),
    ("es", "client/troubleshooting/firewall-errors"),
    ("ms", "about/brand-usage"),
    ("ms", "about/getoutline-me-telegram"),
    ("ms", "about/how-outline-works"),
    ("pl", "about/getoutline-me-telegram"),
    ("pt", "about/how-outline-works"),
    ("pt-BR", "client/troubleshooting/firewall-errors"),
    ("ru", "about/access-resources-blocked"),
}

# Heading anchors that only exist in the English version (manually added
# post-conversion). Translations won't have these.
KNOWN_ENGLISH_ONLY_ANCHORS: dict[str, set[str]] = {}

# Known link count differences between English and translations.
# Docs where link count differences are accepted because the GKMS source
# translations had structurally different links than English.
# The verify script will skip count-mismatch checks for these docs.
KNOWN_LINK_COUNT_DIFF_DOCS: set[str] = {
    "client/troubleshooting/connection-issues",  # EN has duplicate anchor links
    "about/how-outline-works",  # Translations lost external URLs (were self-links)
    "about/feedback",  # Translations have extra/missing links
    "client/getting-started/connecting-device",  # Translations lost the link
    "client/troubleshooting/windows-install",  # Missing a feedback link
    "manager/server-management/delete-server",  # Extra link in translations
    "manager/server-management/update-software",  # Extra link in translations
    "about/terminology",  # en-GB missing a link
    "manager/troubleshooting/manager-download",  # Extra link
    "manager/server-setup/cost",  # Extra link
    "manager/server-management/data-limits",  # Extra link
}

# Known heading structure differences where translators intentionally
# organized content differently. Format: (locale, doc_path)
KNOWN_HEADING_DIFFS: set[tuple[str, str]] = {
    # google-cloud: translators added extra heading splitting "Additional access"
    ("es", "manager/server-setup/google-cloud"),
    ("tr", "manager/server-setup/google-cloud"),
    ("zh-Hans", "manager/server-setup/google-cloud"),
    ("zh-Hant", "manager/server-setup/google-cloud"),
}

# Threshold for content parity warnings. If the translation's non-code
# content is less than this fraction of the English content length, flag it.
CONTENT_PARITY_THRESHOLD = 0.40
CONTENT_PARITY_THRESHOLD_CJK = 0.20
CJK_LOCALES = {"ja", "ko", "zh-Hans", "zh-Hant", "zh-HK"}

# Directories that should have _category_.json in translations.
CATEGORY_DIRS = [
    "about",
    "client",
    "client/getting-started",
    "client/troubleshooting",
    "developers",
    "manager",
    "manager/server-management",
    "manager/server-setup",
    "manager/troubleshooting",
]


def get_english_doc_paths() -> set[str]:
    """Get all doc paths relative to docs/, without extension."""
    paths = set()
    for f in ENGLISH_DOCS_DIR.rglob("*.md"):
        rel = f.relative_to(ENGLISH_DOCS_DIR).with_suffix("")
        paths.add(str(rel))
    return paths


def get_translated_doc_paths(locale: str) -> set[str]:
    """Get all doc paths for a locale, without extension."""
    locale_dir = I18N_BASE / locale / "docusaurus-plugin-content-docs" / "current"
    if not locale_dir.exists():
        return set()
    paths = set()
    for f in locale_dir.rglob("*.md"):
        rel = f.relative_to(locale_dir).with_suffix("")
        paths.add(str(rel))
    return paths


def read_doc(base_dir: Path, doc_path: str) -> str:
    """Read a doc file and return its contents."""
    f = base_dir / f"{doc_path}.md"
    return f.read_text(encoding="utf-8")


def extract_frontmatter_keys(text: str) -> set[str]:
    """Extract the set of frontmatter key names from markdown."""
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return set()
    keys = set()
    for line in m.group(1).split('\n'):
        km = re.match(r'^(\w[\w_-]*):', line)
        if km:
            keys.add(km.group(1))
    return keys


def extract_code_blocks(md_text: str) -> list[str]:
    """Extract all fenced code blocks from markdown."""
    blocks = []
    lines = md_text.split('\n')
    i = 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        fence_match = re.match(r'^(`{3,})(\w*)', stripped)
        if fence_match:
            fence = fence_match.group(1)
            lang = fence_match.group(2)
            indent = len(lines[i]) - len(stripped)
            code_lines = []
            i += 1
            while i < len(lines):
                close_stripped = lines[i].lstrip()
                if close_stripped.startswith(fence) and close_stripped.strip() == fence:
                    break
                if indent > 0 and lines[i][:indent].strip() == '':
                    code_lines.append(lines[i][indent:])
                else:
                    code_lines.append(lines[i])
                i += 1
            code = '\n'.join(code_lines)
            blocks.append(f"```{lang}\n{code}\n```")
        i += 1
    return blocks


def strip_code_blocks(md_text: str) -> str:
    """Remove all fenced code blocks from markdown."""
    result = []
    lines = md_text.split('\n')
    i = 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        fence_match = re.match(r'^(`{3,})', stripped)
        if fence_match:
            fence = fence_match.group(1)
            i += 1
            while i < len(lines):
                close_stripped = lines[i].lstrip()
                if close_stripped.startswith(fence) and close_stripped.strip() == fence:
                    break
                i += 1
        else:
            result.append(lines[i])
        i += 1
    return '\n'.join(result)


def strip_non_content(md_text: str) -> str:
    """Strip frontmatter, code blocks, and markup. Returns only prose."""
    text = re.sub(r'^---\n.*?\n---\n', '', md_text, flags=re.DOTALL)
    text = strip_code_blocks(text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\{#[^}]+\}', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def normalize_link_url(url: str) -> str:
    """Normalize a link URL for comparison."""
    if url.startswith(('http://', 'https://', 'mailto:', '#')):
        # Normalize http to https
        if url.startswith('http://'):
            url = 'https://' + url[7:]
        # Strip language query params (?hl=XX, ?language=XX)
        url = re.sub(r'[?&](hl|language)=[^&#]*', '', url)
        # Clean up leftover ? or & at end
        url = re.sub(r'[?&]$', '', url)
        # Normalize Wikipedia: locale subdomains, localized paths, and article names
        # e.g. https://cs.wikipedia.org/wiki/Certifikát → WIKIPEDIA
        #      https://zh.wikipedia.org/zh-hk/Article → WIKIPEDIA
        if re.match(r'https://[a-z]{2,3}(-[A-Za-z]+)?\.wikipedia\.org/', url):
            return 'WIKIPEDIA'
        # Normalize trailing slash and /en/ locale paths
        url = re.sub(r'/en/?$', '/', url)
        url = re.sub(r'([^/])$', r'\1/', url)
        return url
    anchor = ''
    url_path = url
    if '#' in url:
        url_path, anchor_text = url.split('#', 1)
        anchor = '#' + anchor_text
    if url_path.endswith('.md'):
        url_path = url_path[:-3]
    return url_path + anchor


def extract_link_urls(md_text: str) -> list[str]:
    """Extract all link URLs from markdown in document order."""
    text = strip_code_blocks(md_text)
    all_matches = []
    for m in re.finditer(r'(?<!!)\[((?:[^\]\\]|\\.)*)\]\(([^)]+)\)', text):
        all_matches.append((m.start(), m.group(2)))
    for m in re.finditer(r'<(https?://[^>]+)>', text):
        all_matches.append((m.start(), m.group(1)))
    all_matches.sort(key=lambda x: x[0])
    return [url for _, url in all_matches]


def extract_heading_anchors(md_text: str) -> list[str]:
    """Extract heading anchor IDs ({#id}) from markdown."""
    anchors = []
    for m in re.finditer(r'^#{1,6}\s+.*?\{#([^}]+)\}\s*$', md_text, re.MULTILINE):
        anchors.append(m.group(1))
    return anchors


def extract_heading_levels(md_text: str) -> list[int]:
    """Extract the sequence of heading levels (e.g. [2, 2, 3, 2]) from markdown."""
    levels = []
    for m in re.finditer(r'^(#{1,6})\s+', md_text, re.MULTILINE):
        levels.append(len(m.group(1)))
    return levels


def extract_bold_only_lines(md_text: str) -> list[str]:
    """Extract standalone bold-only lines that may be misformatted headings."""
    results = []
    for m in re.finditer(r'^(\*{2,4})(.+?)\1\s*$', md_text, re.MULTILINE):
        results.append(m.group(2).strip())
    return results


class Issue:
    """A verification issue."""
    def __init__(self, locale: str, doc_path: str, category: str, message: str):
        self.locale = locale
        self.doc_path = doc_path
        self.category = category
        self.message = message

    def __str__(self):
        return f"  [{self.category}] {self.locale}/{self.doc_path}: {self.message}"


def verify_locale(locale: str, english_paths: set[str]) -> list[Issue]:
    """Verify all translations for a single locale."""
    issues = []
    locale_dir = I18N_BASE / locale / "docusaurus-plugin-content-docs" / "current"
    translated_paths = get_translated_doc_paths(locale)
    expected_paths = english_paths - ENGLISH_ONLY

    # Check for missing translations
    missing = expected_paths - translated_paths
    for doc_path in sorted(missing):
        if (locale, doc_path) in KNOWN_MISSING:
            continue
        issues.append(Issue(locale, doc_path, "MISSING", "Translation file missing"))

    # Check for extra translations
    extra = translated_paths - english_paths
    for doc_path in sorted(extra):
        issues.append(Issue(locale, doc_path, "EXTRA", "No corresponding English doc"))

    # Check each translated file against English
    for doc_path in sorted(translated_paths & english_paths):
        en_text = read_doc(ENGLISH_DOCS_DIR, doc_path)
        tr_text = read_doc(locale_dir, doc_path)

        # Frontmatter keys
        en_keys = extract_frontmatter_keys(en_text)
        tr_keys = extract_frontmatter_keys(tr_text)
        if en_keys and not tr_keys:
            issues.append(Issue(locale, doc_path, "FRONTMATTER", "Missing frontmatter"))
        elif en_keys and tr_keys and en_keys != tr_keys:
            missing_k = en_keys - tr_keys
            extra_k = tr_keys - en_keys
            detail = []
            if missing_k:
                detail.append(f"missing keys: {missing_k}")
            if extra_k:
                detail.append(f"extra keys: {extra_k}")
            issues.append(Issue(
                locale, doc_path, "FRONTMATTER",
                f"Frontmatter keys differ: {'; '.join(detail)}"
            ))

        # Code blocks
        en_blocks = extract_code_blocks(en_text)
        tr_blocks = extract_code_blocks(tr_text)
        if len(en_blocks) != len(tr_blocks):
            issues.append(Issue(
                locale, doc_path, "CODE_BLOCKS",
                f"Count mismatch: English has {len(en_blocks)}, "
                f"translation has {len(tr_blocks)}"
            ))
        else:
            for idx, (en_block, tr_block) in enumerate(zip(en_blocks, tr_blocks)):
                # Normalize whitespace for comparison (indentation may differ
                # when code blocks are inside vs outside list items)
                en_norm = "\n".join(l.strip() for l in en_block.strip().split("\n"))
                tr_norm = "\n".join(l.strip() for l in tr_block.strip().split("\n"))
                if en_norm != tr_norm:
                    issues.append(Issue(
                        locale, doc_path, "CODE_BLOCKS",
                        f"Block {idx + 1} differs from English"
                    ))

        # Link URLs
        en_links = [normalize_link_url(u) for u in extract_link_urls(en_text)]
        tr_links = [normalize_link_url(u) for u in extract_link_urls(tr_text)]
        if len(en_links) != len(tr_links):
            if doc_path in KNOWN_LINK_COUNT_DIFF_DOCS:
                pass
            else:
                issues.append(Issue(
                    locale, doc_path, "LINKS",
                    f"Count mismatch: English has {len(en_links)}, "
                    f"translation has {len(tr_links)}"
                ))
        else:
            # Check if links differ only in order (valid for RTL/different word order)
            if sorted(en_links) == sorted(tr_links):
                pass  # Same links, different order — acceptable
            else:
                for idx, (en_url, tr_url) in enumerate(zip(en_links, tr_links)):
                    if en_url != tr_url:
                        issues.append(Issue(
                            locale, doc_path, "LINKS",
                            f"Link {idx + 1} differs: "
                            f"English={en_url!r}, translation={tr_url!r}"
                        ))

        # Heading anchors
        en_anchors = set(extract_heading_anchors(en_text))
        tr_anchors = set(extract_heading_anchors(tr_text))
        known_en_only = KNOWN_ENGLISH_ONLY_ANCHORS.get(doc_path, set())
        en_anchors -= known_en_only
        missing_anchors = en_anchors - tr_anchors
        extra_anchors = tr_anchors - en_anchors
        if missing_anchors:
            issues.append(Issue(
                locale, doc_path, "HEADINGS",
                f"Missing heading anchors: {sorted(missing_anchors)}"
            ))
        if extra_anchors:
            issues.append(Issue(
                locale, doc_path, "HEADINGS",
                f"Extra heading anchors: {sorted(extra_anchors)}"
            ))

        # Heading level structure: translations should have the same
        # sequence of heading levels as English
        en_levels = extract_heading_levels(en_text)
        tr_levels = extract_heading_levels(tr_text)
        if en_levels != tr_levels:
            if (locale, doc_path) not in KNOWN_HEADING_DIFFS:
                issues.append(Issue(
                    locale, doc_path, "HEADING_STRUCTURE",
                    f"Heading levels differ: English={en_levels}, "
                    f"translation={tr_levels}"
                ))

        # Bold-only lines that should be headings: translations should not
        # have standalone **bold** lines if English doesn't
        en_bolds = extract_bold_only_lines(en_text)
        tr_bolds = extract_bold_only_lines(tr_text)
        if tr_bolds and not en_bolds:
            issues.append(Issue(
                locale, doc_path, "BOLD_AS_HEADING",
                f"Translation has {len(tr_bolds)} bold-only line(s) that "
                f"may be misformatted headings: {[b[:40] for b in tr_bolds[:3]]}"
            ))

        # Content parity
        en_content = strip_non_content(en_text)
        tr_content = strip_non_content(tr_text)
        if len(en_content) > 100:
            threshold = (
                CONTENT_PARITY_THRESHOLD_CJK
                if locale in CJK_LOCALES
                else CONTENT_PARITY_THRESHOLD
            )
            ratio = len(tr_content) / len(en_content)
            if ratio < threshold:
                issues.append(Issue(
                    locale, doc_path, "CONTENT_PARITY",
                    f"Translation is {ratio:.0%} of English length "
                    f"({len(tr_content)} vs {len(en_content)} chars)"
                ))

    # Check _category_.json files
    for cat_dir in CATEGORY_DIRS:
        cat_json = locale_dir / cat_dir / "_category_.json"
        if not cat_json.exists():
            issues.append(Issue(
                locale, f"{cat_dir}/_category_.json", "CATEGORY_MISSING",
                "Category label translation missing"
            ))
        else:
            try:
                data = json.loads(cat_json.read_text(encoding="utf-8"))
                if "label" not in data:
                    issues.append(Issue(
                        locale, f"{cat_dir}/_category_.json", "CATEGORY_INVALID",
                        "Missing 'label' key"
                    ))
            except json.JSONDecodeError as e:
                issues.append(Issue(
                    locale, f"{cat_dir}/_category_.json", "CATEGORY_INVALID",
                    f"Invalid JSON: {e}"
                ))

    return issues


def main():
    warn_only = "--warn" in sys.argv

    english_paths = get_english_doc_paths()

    print(f"English docs: {len(english_paths)} files")
    print(f"English-only (no translation expected): {len(ENGLISH_ONLY)} files")
    print(f"Locales to verify: {len(LOCALES)}")
    print()

    total_issues = 0
    issues_by_category: dict[str, int] = {}

    for locale in LOCALES:
        issues = verify_locale(locale, english_paths)

        if issues:
            print(f"FAIL {locale}: {len(issues)} issue(s)")
            for issue in issues:
                print(issue)
                issues_by_category[issue.category] = (
                    issues_by_category.get(issue.category, 0) + 1
                )
            total_issues += len(issues)
        else:
            print(f"OK   {locale}")

    print()
    if total_issues:
        print(f"Summary: {total_issues} issue(s) across {len(LOCALES)} locales")
        for cat, count in sorted(issues_by_category.items()):
            print(f"  {cat}: {count}")
        if warn_only:
            print("\n--warn: exiting with status 0 despite issues")
            sys.exit(0)
        sys.exit(1)
    else:
        print("PASSED: All translations verified")
        sys.exit(0)


if __name__ == "__main__":
    main()
