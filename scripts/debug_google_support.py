#!/usr/bin/env python3
"""Debug script to inspect the HTML structure of a Google support page.

Fetches a single article and prints all div classes that might contain
article content, plus the h1 title.
"""

import subprocess
import sys
from bs4 import BeautifulSoup


def main():
    url = "https://support.google.com/outline/answer/14917423?hl=fr"
    print(f"Fetching {url}")

    result = subprocess.run(
        ["curl", "-s", "-L", "--max-time", "10",
         "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
         "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
         "-H", "Accept-Language: fr,en;q=0.5",
         url],
        capture_output=True, text=True, timeout=15,
    )
    html = result.stdout
    soup = BeautifulSoup(html, "html.parser")

    # Check for h1
    h1 = soup.find("h1")
    print(f"h1: {h1.get_text(strip=True) if h1 else None}")

    # Check <title>
    title = soup.find("title")
    print(f"title: {title.get_text(strip=True) if title else None}")

    # Check meta description (often has article content)
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        print(f"meta description: {meta_desc.get('content', '')[:200]}")

    print()

    # Look for embedded JSON data (Google often embeds page data in scripts)
    print("=== Script tags with potential article data ===")
    for script in soup.find_all("script"):
        text = script.string or ""
        if any(kw in text[:500] for kw in ["articleBody", "answer", "hcfe"]):
            print(f"  Script (first 300 chars): {text[:300]}")
            print()

    # Check for any visible text content at all
    body = soup.find("body")
    if body:
        all_text = body.get_text(strip=True)
        print(f"Total body text length: {len(all_text)}")
        print(f"Body text preview: {all_text[:300]}")
    print()

    # Check for noscript content
    noscript = soup.find("noscript")
    if noscript:
        print(f"=== noscript content (first 500 chars) ===")
        print(noscript.get_text(strip=True)[:500])


if __name__ == "__main__":
    main()
