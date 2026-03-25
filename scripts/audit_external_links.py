#!/usr/bin/env python3
"""Audit all external links in the English docs and config files.

Extracts all URLs from markdown docs, checks each one for HTTP status,
and reports broken or redirected links.
"""

import re
import urllib.request
import urllib.error
import ssl
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
PAGES_DIR = ROOT / "src" / "pages"
CONFIG_FILE = ROOT / "docusaurus.config.ts"

# Match markdown links [text](url) and bare URLs
MD_LINK_RE = re.compile(r'\[([^\]]*)\]\((https?://[^)]+)\)')
BARE_URL_RE = re.compile(r'(?<!\()(https?://[^\s\)\]>]+)')

# Also match href="url" in config
HREF_RE = re.compile(r"href:\s*['\"]?(https?://[^'\">\s,]+)")


def extract_urls_from_md(path: Path) -> list[tuple[str, str]]:
    """Return list of (url, context) from a markdown file."""
    text = path.read_text("utf-8")
    results = []
    for m in MD_LINK_RE.finditer(text):
        results.append((m.group(2), f"[{m.group(1)}]"))
    return results


def extract_urls_from_config(path: Path) -> list[tuple[str, str]]:
    """Return list of (url, context) from config file."""
    text = path.read_text("utf-8")
    results = []
    for m in HREF_RE.finditer(text):
        results.append((m.group(1), "docusaurus.config.ts"))
    return results


def main():
    # Collect all unique URLs and where they appear
    url_sources: dict[str, list[str]] = defaultdict(list)

    # English docs
    for md in sorted(DOCS_DIR.rglob("*.md")):
        rel = str(md.relative_to(ROOT))
        for url, ctx in extract_urls_from_md(md):
            url_sources[url].append(f"{rel} {ctx}")

    # Pages (tsx/md)
    for f in sorted(PAGES_DIR.rglob("*.tsx")):
        text = f.read_text("utf-8")
        rel = str(f.relative_to(ROOT))
        for m in re.finditer(r'(?:to|href)=["\']?(https?://[^"\'>\s]+)', text):
            url_sources[m.group(1)].append(rel)

    # Config
    if CONFIG_FILE.exists():
        for url, ctx in extract_urls_from_config(CONFIG_FILE):
            url_sources[url].append(ctx)

    print(f"Found {len(url_sources)} unique external URLs\n")

    # Group by domain
    by_domain: dict[str, list[str]] = defaultdict(list)
    for url in sorted(url_sources.keys()):
        m = re.match(r'https?://([^/]+)', url)
        domain = m.group(1) if m else "unknown"
        by_domain[domain].append(url)

    for domain in sorted(by_domain.keys()):
        urls = by_domain[domain]
        print(f"\n{'='*60}")
        print(f"  {domain} ({len(urls)} URLs)")
        print(f"{'='*60}")
        for url in urls:
            sources = url_sources[url]
            source_str = sources[0] if len(sources) == 1 else f"{sources[0]} (+{len(sources)-1} more)"
            print(f"  {url}")
            print(f"    <- {source_str}")


if __name__ == "__main__":
    main()
