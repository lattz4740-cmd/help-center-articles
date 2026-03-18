#!/usr/bin/env python3
"""Convert translated GKMS HTML exports to Markdown for Docusaurus i18n."""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, Tag

# Import shared converter functions
sys.path.insert(0, str(Path(__file__).parent))
from convert_gkms import (
    WEB_ID_TO_DOC,
    convert_body,
    extract_articles,
    parse_image_snippets,
    read_existing_frontmatter,
    yaml_quote,
)

ROOT = Path(__file__).resolve().parent.parent
OLD_SITE = ROOT / "old-site"
I18N = ROOT / "i18n"

# GKMS locale code → Docusaurus BCP 47 locale code
LOCALE_MAP = {
    "iw": "he",
    "no": "nb",
}

# TOPIC ID → directory path (relative to docs/) for _category_.json
TOPIC_TO_DIR = {
    "15309650": "about",
    "15330318": "manager",
    "15330822": "client",
    "15330823": "client/troubleshooting",
    "15330846": "developers",
    "15331124": "client/getting-started",
    "15331325": "manager/server-management",
    "15331425": "manager/server-setup",
    "15331729": "manager/troubleshooting",
}


def find_webs_file(locale):
    """Find the WEBS HTML file for a given GKMS locale."""
    help_center = OLD_SITE / "Help Center"
    pattern = f"WEBS_*_{locale}.HTML"
    matches = list(help_center.glob(pattern))
    return matches[0] if matches else None


def find_topics_file(locale):
    """Find the TOPICS HTML file for a given GKMS locale."""
    help_center = OLD_SITE / "Help Center"
    pattern = f"TOPICS_*_{locale}.HTML"
    matches = list(help_center.glob(pattern))
    return matches[0] if matches else None


def extract_topics(html_path):
    """Parse TOPICS HTML and return dict of topic_id → translated_title."""
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    topics = {}
    for div in soup.find_all("div", class_="gkms"):
        classes = div.get("class", [])
        text = div.get_text(strip=True)

        if "id" in classes and "notranslate" in classes:
            m = re.match(r"TOPIC:(\d+)", text)
            if m:
                topic_id = m.group(1)
                # Next sibling should be the title div
                sibling = div.next_sibling
                while sibling:
                    if isinstance(sibling, Tag):
                        sib_classes = sibling.get("class", [])
                        if "topic" in sib_classes and "title" in sib_classes:
                            topics[topic_id] = sibling.get_text(strip=True)
                            break
                    sibling = sibling.next_sibling

    return topics


def get_gkms_locales():
    """Get all GKMS locales from WEBS files in Help Center."""
    help_center = OLD_SITE / "Help Center"
    locales = set()
    for f in help_center.glob("WEBS_*.HTML"):
        # Extract locale from filename: WEBS_..._LOCALE.HTML
        m = re.search(r"_([^_]+)\.HTML$", f.name)
        if m:
            locales.add(m.group(1))
    return sorted(locales)


def write_translated_doc(locale_dir, doc_path, title, sidebar_label, body_md):
    """Write a translated doc file."""
    full_path = locale_dir / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
    full_path.parent.mkdir(parents=True, exist_ok=True)

    fm_lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"sidebar_label: {yaml_quote(sidebar_label)}",
        "---",
    ]

    content = "\n".join(fm_lines) + "\n\n" + body_md + "\n"

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


def write_category_json(locale_dir, dir_path, label):
    """Write a _category_.json file with the translated label."""
    import json

    full_path = locale_dir / "docusaurus-plugin-content-docs" / "current" / dir_path / "_category_.json"
    full_path.parent.mkdir(parents=True, exist_ok=True)

    data = {"label": label}

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    image_snippets = parse_image_snippets()

    # Read English sidebar labels to use as fallback
    en_sidebar_labels = {}
    for web_id, doc_path in WEB_ID_TO_DOC.items():
        fm = read_existing_frontmatter(doc_path)
        en_sidebar_labels[web_id] = fm.get("sidebar_label", "")

    gkms_locales = get_gkms_locales()
    print(f"Found {len(gkms_locales)} locales: {', '.join(gkms_locales)}")

    total_articles = 0
    total_locales = 0

    for gkms_locale in gkms_locales:
        if gkms_locale == "en":
            continue

        docusaurus_locale = LOCALE_MAP.get(gkms_locale, gkms_locale)
        locale_dir = I18N / docusaurus_locale

        # Convert articles
        webs_file = find_webs_file(gkms_locale)
        if not webs_file:
            print(f"  WARNING: No WEBS file for locale {gkms_locale}")
            continue

        articles = extract_articles(webs_file)

        locale_count = 0
        for web_id, title, web_content in articles:
            if web_id not in WEB_ID_TO_DOC:
                continue

            doc_path = WEB_ID_TO_DOC[web_id]
            sidebar_label = title  # Use translated title as sidebar label
            body_md = convert_body(web_content, image_snippets)
            write_translated_doc(locale_dir, doc_path, title, sidebar_label, body_md)
            locale_count += 1

        # Convert topic labels to _category_.json
        topics_file = find_topics_file(gkms_locale)
        if topics_file:
            topics = extract_topics(topics_file)
            for topic_id, translated_label in topics.items():
                if topic_id in TOPIC_TO_DIR:
                    write_category_json(locale_dir, TOPIC_TO_DIR[topic_id], translated_label)

        total_articles += locale_count
        total_locales += 1
        print(f"  {docusaurus_locale}: {locale_count} articles")

    print(f"\nDone: {total_articles} articles across {total_locales} locales")


if __name__ == "__main__":
    main()
