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
ENGLISH_PAGES_DIR = PROJECT_ROOT / "src" / "pages"
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

# Docs/pages that only exist in English (no translation expected).
# Includes redirect pages under s/ and the contactsupport page.
ENGLISH_ONLY: set[str] = {
    "s/contactsupport",
    "s/index",
    "s/article/index",
    "s/article/Data-collection",
    "s/article/How-do-I-get-an-access-key",
    "s/article/What-if-my-access-key-doesn-t-work",
    "s/article/Why-can-t-I-connect-to-the-Outline-service",
    "s/topic/index",
}

# --- Homepage translation tiers (by language reach) ---
# Widely spoken languages — all homepage strings translated.
MAJOR_LOCALES: set[str] = {
    "ar", "de", "es", "es-419", "fr", "it", "ja", "ko", "nl", "pl",
    "pt", "pt-BR", "ru", "th", "tr", "uk", "vi", "zh-Hans", "zh-Hant", "zh-HK",
}

# Mid-reach languages — buttons translated, descriptions missing.
SECONDARY_LOCALES: set[str] = {
    "bg", "cs", "da", "el", "en-GB", "fa", "fi",
    "he", "hi", "hr", "hu", "id", "ms", "nb", "ro", "sk", "sl", "sv",
}

# Smaller-reach languages — descriptions and buttons missing.
EMERGING_LOCALES: set[str] = {
    "af", "am", "az", "bn", "bs", "ca", "et", "fil", "hy", "is",
    "ka", "kk", "km", "lo", "lv", "mk", "mn", "mr", "my", "ne",
    "si", "sq", "sr", "sw", "ta", "ur",
}

# Keys missing per tier.
_MISSING_DESCRIPTION_KEYS: set[str] = {
    "homepage.client.description",
    "homepage.developers.description",
    "homepage.manager.description",
}
_MISSING_BUTTON_KEYS: set[str] = {
    "homepage.about.button",
    "homepage.client.button",
    "homepage.developers.button",
    "homepage.manager.button",
}


def _build_known_missing_keys(locale: str) -> set[str]:
    """Return the set of known-missing keys for a given locale."""
    if locale in MAJOR_LOCALES:
        return set()
    if locale in SECONDARY_LOCALES:
        return _MISSING_DESCRIPTION_KEYS
    if locale in EMERGING_LOCALES:
        return _MISSING_DESCRIPTION_KEYS | _MISSING_BUTTON_KEYS
    return set()

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
    ("it", "client/getting-started/available-languages"),  # Was in Lithuanian (lt)
    ("it", "client/troubleshooting/connection-issues"),  # Was in German (de)
    ("it", "manager/server-management/reset-server-id"),  # Was in Lithuanian (lt)
    ("it", "manager/server-setup/available-languages"),  # Was in Lithuanian (lt)
    ("lv", "client/getting-started/install-linux"),  # Was in Lao (lo)
    ("mn", "client/getting-started/system-requirements"),  # Was in Norwegian (nb)
    ("ms", "about/brand-usage"),
    ("ms", "about/getoutline-me-telegram"),
    ("ms", "about/how-outline-works"),
    ("pl", "about/getoutline-me-telegram"),
    ("pt", "about/how-outline-works"),
    ("pt-BR", "client/troubleshooting/firewall-errors"),
    ("ru", "about/access-resources-blocked"),
    ("ru", "client/getting-started/available-languages"),  # Was in Norwegian (nb)
    ("ru", "manager/server-setup/available-languages"),  # Was in Norwegian (nb)
    ("ur", "client/getting-started/system-requirements"),  # Was in Ukrainian (uk)
}


# Threshold for content parity warnings. If the translation's non-code
# content is less than this fraction of the English content length, flag it.
CONTENT_PARITY_THRESHOLD = 0.40
CONTENT_PARITY_THRESHOLD_CJK = 0.20
CJK_LOCALES = {"ja", "ko", "zh-Hans", "zh-Hant", "zh-HK"}



def get_english_doc_paths() -> set[str]:
    """Get all doc paths relative to docs/, without extension."""
    paths = set()
    for f in ENGLISH_DOCS_DIR.rglob("*.md"):
        rel = f.relative_to(ENGLISH_DOCS_DIR).with_suffix("")
        paths.add(str(rel))
    return paths


def get_english_page_paths() -> set[str]:
    """Get all markdown page paths relative to src/pages/, without extension.

    These are pages (not docs) that need translation via
    i18n/{locale}/docusaurus-plugin-content-pages/.
    Only includes .md/.mdx files (TSX pages use code.json for translations).
    """
    paths = set()
    for ext in ("*.md", "*.mdx"):
        for f in ENGLISH_PAGES_DIR.rglob(ext):
            rel = f.relative_to(ENGLISH_PAGES_DIR).with_suffix("")
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
    # Normalize mailto: links — treat security@getoutline.org mailto as
    # equivalent to the getoutline.org website link
    if url.startswith('mailto:') and 'getoutline.org' in url:
        return 'https://getoutline.org/'
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


def find_bare_urls(md_text: str) -> list[str]:
    """Find bare URLs in markdown that aren't inside links or code blocks.

    A proper markdown doc should wrap URLs in [text](url) or <url> syntax.
    Bare URLs are likely conversion artifacts.
    """
    text = strip_code_blocks(md_text)
    # Remove frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    # Remove entire markdown links [text](url) including text
    text = re.sub(r'\[([^\]]*)\]\([^)]+\)', '', text)
    # Remove angle-bracket URLs <url>
    text = re.sub(r'<https?://[^>]+>', '', text)
    # Now find any remaining bare URLs
    bare = re.findall(r'https?://[^\s)\]>]+', text)
    return bare


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
        # section headings (##) as English. Sub-headings (###) may vary
        # since translators may organize content differently.
        en_levels = extract_heading_levels(en_text)
        tr_levels = extract_heading_levels(tr_text)
        en_sections = [l for l in en_levels if l == 2]
        tr_sections = [l for l in tr_levels if l == 2]
        if en_sections != tr_sections:
            issues.append(Issue(
                locale, doc_path, "HEADING_STRUCTURE",
                f"Section headings (h2) differ: English has {len(en_sections)}, "
                f"translation has {len(tr_sections)}"
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

        # Bare URLs (not inside markdown links or code blocks)
        bare_urls = find_bare_urls(tr_text)
        if bare_urls:
            issues.append(Issue(
                locale, doc_path, "BARE_URL",
                f"Found {len(bare_urls)} bare URL(s): {bare_urls[:3]}"
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


    return issues


def _extract_code_json_keys() -> dict[str, str]:
    """Extract required code.json keys and English defaults from source files.

    Finds both static <Translate id="...">Default text</Translate> and
    dynamic IDs assigned to variables like titleId: 'homepage.about.title'.
    Returns {key: english_default}.
    """
    keys: dict[str, str] = {}
    src_dir = PROJECT_ROOT / "src"

    for f in src_dir.rglob("*.tsx"):
        text = f.read_text("utf-8")

        # Static: <Translate id="some.id">Default text</Translate>
        for m in re.finditer(
            r'<Translate\s+id=["\']([^"\']+)["\']>\s*\n?\s*(.+?)\s*\n?\s*</Translate>',
            text, re.DOTALL,
        ):
            keys[m.group(1)] = m.group(2).strip()

        # Dynamic: card definitions with paired Id/default values
        # e.g. titleId: 'homepage.about.title', title: 'About Outline',
        for m in re.finditer(
            r"(\w+)Id:\s*'(homepage\.[^']+)'.*?\1:\s*'([^']+)'",
            text, re.DOTALL,
        ):
            keys[m.group(2)] = m.group(3)

    return keys


def _extract_current_json_keys() -> dict[str, str]:
    """Extract required current.json keys from sidebars.ts.

    Parses category labels and keys to build the Docusaurus translation
    key format: sidebar.<sidebarId>.category.<label|key>
    Returns {key: english_label}.
    """
    keys: dict[str, str] = {}
    sidebars_path = PROJECT_ROOT / "sidebars.ts"
    text = sidebars_path.read_text("utf-8")

    # Find sidebar names and their ranges
    sidebar_pattern = re.compile(r'(\w+Sidebar)\s*:\s*\[')
    sidebar_ranges: list[tuple[str, int, int]] = []
    for m in sidebar_pattern.finditer(text):
        sidebar_ranges.append((m.group(1), m.start(), 0))
    for i in range(len(sidebar_ranges)):
        name, start, _ = sidebar_ranges[i]
        end = sidebar_ranges[i + 1][1] if i + 1 < len(sidebar_ranges) else len(text)
        sidebar_ranges[i] = (name, start, end)

    # For each sidebar section, find categories with label and optional key
    label_pattern = re.compile(r"label:\s*'([^']+)'")
    key_pattern = re.compile(r"key:\s*'([^']+)'")

    for sidebar_name, start, end in sidebar_ranges:
        section = text[start:end]
        cat_blocks = re.finditer(
            r"type:\s*'category'(.*?)items:\s*\[",
            section, re.DOTALL,
        )
        for block in cat_blocks:
            block_text = block.group(1)
            label_m = label_pattern.search(block_text)
            key_m = key_pattern.search(block_text)
            if label_m:
                label = label_m.group(1)
                cat_id = key_m.group(1) if key_m else label
                keys[f"sidebar.{sidebar_name}.category.{cat_id}"] = label

    return keys


def _extract_navbar_json_keys() -> dict[str, str]:
    """Extract required navbar.json keys from docusaurus.config.ts.

    Parses navbar items to find labels that need translation.
    Returns {key: english_label}.
    """
    keys: dict[str, str] = {}
    config_path = PROJECT_ROOT / "docusaurus.config.ts"
    text = config_path.read_text("utf-8")

    navbar_match = re.search(r'navbar:\s*\{.*?items:\s*\[(.*?)\]', text, re.DOTALL)
    if navbar_match:
        items_text = navbar_match.group(1)
        label_pattern = re.compile(r"label:\s*'([^']+)'")
        for m in label_pattern.finditer(items_text):
            label = m.group(1)
            keys[f"item.label.{label}"] = label

    return keys


# Lazily loaded on first use
_required_keys_cache: dict[str, dict[str, str]] = {}


def _get_required_keys(kind: str) -> dict[str, str]:
    """Returns {translation_key: english_default} for the given file type."""
    if kind not in _required_keys_cache:
        if kind == "code.json":
            _required_keys_cache[kind] = _extract_code_json_keys()
        elif kind == "current.json":
            _required_keys_cache[kind] = _extract_current_json_keys()
        elif kind == "navbar.json":
            _required_keys_cache[kind] = _extract_navbar_json_keys()
    return _required_keys_cache[kind]


def _check_json_keys(
    locale: str,
    filename: str,
    json_path: Path,
    required: dict[str, str],
) -> list[Issue]:
    """Check a translation JSON file has all required keys and they're translated.

    Args:
        locale: The locale being checked.
        filename: Display name for the file (e.g. "code.json").
        json_path: Path to the JSON file.
        required: {key: english_default} from source extraction.
    """
    issues: list[Issue] = []

    if not json_path.exists():
        issues.append(Issue(locale, filename, "TRANSLATION_KEY",
                           f"Missing {filename}"))
        return issues

    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        issues.append(Issue(locale, filename, "TRANSLATION_KEY",
                           f"Invalid JSON: {e}"))
        return issues

    known_missing = _build_known_missing_keys(locale)
    for key in required:
        if key not in data:
            if key not in known_missing:
                issues.append(Issue(locale, filename, "TRANSLATION_KEY",
                                   f"Missing key: {key}"))
        elif not data[key].get("message"):
            issues.append(Issue(locale, filename, "TRANSLATION_KEY",
                               f"Empty message: {key}"))

    return issues


def verify_i18n_json(locale: str) -> list[Issue]:
    """Verify code.json, current.json, and navbar.json have all required translation keys."""
    issues = []
    locale_dir = I18N_BASE / locale

    issues.extend(_check_json_keys(
        locale, "code.json",
        locale_dir / "code.json",
        _get_required_keys("code.json"),
    ))

    issues.extend(_check_json_keys(
        locale, "current.json",
        locale_dir / "docusaurus-plugin-content-docs" / "current.json",
        _get_required_keys("current.json"),
    ))

    issues.extend(_check_json_keys(
        locale, "navbar.json",
        locale_dir / "docusaurus-theme-classic" / "navbar.json",
        _get_required_keys("navbar.json"),
    ))

    return issues


def verify_pages(locale: str, english_page_paths: set[str]) -> list[Issue]:
    """Check that markdown pages under src/pages/ have translations."""
    issues = []
    pages_dir = I18N_BASE / locale / "docusaurus-plugin-content-pages"
    for page_path in sorted(english_page_paths - ENGLISH_ONLY):
        # Check for .md or .mdx translation
        found = False
        for ext in (".md", ".mdx"):
            if (pages_dir / (page_path + ext)).exists():
                found = True
                break
        if not found:
            issues.append(Issue(
                locale, f"pages/{page_path}", "PAGE_MISSING",
                "Page translation missing"
            ))
    return issues


def main():
    warn_only = "--warn" in sys.argv

    english_paths = get_english_doc_paths()
    english_page_paths = get_english_page_paths()

    print(f"English docs: {len(english_paths)} files")
    print(f"English pages: {len(english_page_paths)} files")
    print(f"English-only (no translation expected): {len(ENGLISH_ONLY)} files")
    print(f"Locales to verify: {len(LOCALES)}")
    print()

    total_issues = 0
    issues_by_category: dict[str, int] = {}

    # Check English docs for bare URLs
    for doc_path in sorted(english_paths):
        en_text = read_doc(ENGLISH_DOCS_DIR, doc_path)
        bare = find_bare_urls(en_text)
        if bare:
            issue = Issue("en", doc_path, "BARE_URL",
                          f"Found {len(bare)} bare URL(s): {bare[:3]}")
            print(issue)
            issues_by_category["BARE_URL"] = issues_by_category.get("BARE_URL", 0) + 1
            total_issues += 1

    for locale in LOCALES:
        issues = verify_locale(locale, english_paths)
        issues.extend(verify_i18n_json(locale))
        issues.extend(verify_pages(locale, english_page_paths))

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
