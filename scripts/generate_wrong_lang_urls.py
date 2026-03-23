#!/usr/bin/env python3
"""Generate support.google.com links for articles that were in the wrong language.

Maps article filenames to GKMS WEB IDs from the old-site export, then
generates URLs with the locale's hl= parameter.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_SITE = ROOT / "old-site" / "Help Center"

# Read English export to map article titles to WEB IDs
en_file = OLD_SITE / "WEBS_14917423,14919822,15330317,15330818,plus_31_more_en.HTML"
text = en_file.read_text("utf-8")

# Extract WEB ID -> title mapping
web_id_pattern = re.compile(r'WEB:(\d+)')
title_pattern = re.compile(r'<div class="gkms article title">(.+?)</div>')

# Parse sequentially
ids_and_titles = []
current_id = None
for line in text.split("\n"):
    m = web_id_pattern.search(line)
    if m:
        current_id = m.group(1)
    m = title_pattern.search(line)
    if m and current_id:
        ids_and_titles.append((current_id, m.group(1)))
        current_id = None

# Map English titles to doc paths
TITLE_TO_DOC = {
    "How Outline Works": "about/how-outline-works",
    "Terminology": "about/terminology",
    "Security and privacy while using Outline": "about/security-and-privacy",
    "Data and information collection": "about/data-collection",
    "How to send feedback or suggestions": "about/feedback",
    "Am I allowed to use or replicate the Outline brand?": "about/brand-usage",
    "How do I access Outline resources if getoutline.org is blocked?": "about/access-resources-blocked",
    'Do you support "getoutline.me" and the "@OutlineVpnOfficial" Telegram channel?': "about/getoutline-me-telegram",
    "What are the system requirements for running the Outline Client?": "client/getting-started/system-requirements",
    "Connecting your device to an Outline server": "client/getting-started/connecting-device",
    "How do I get an access key?": "client/getting-started/get-access-key",
    "Can I use an access key more than once?": "client/getting-started/access-key-reuse",
    "Installing the Outline Client on Linux": "client/getting-started/install-linux",
    "Available languages": "client/getting-started/available-languages",
    "How do I download the client app when the download link isn't working?": "client/troubleshooting/download-link",
    "Why can't I install the Outline client on Windows?": "client/troubleshooting/windows-install",
    "What can I do if my access key is not working?": "client/troubleshooting/access-key-issues",
    "Why can't I connect to the Outline service?": "client/troubleshooting/connection-issues",
    "Why can't I access the internet when my Outline server connection is active?": "client/troubleshooting/internet-access",
    "Firewall errors": "client/troubleshooting/firewall-errors",
    "How do I set up an Outline server?": "manager/server-setup/setup-server",
    "Google Cloud automated setup": "manager/server-setup/google-cloud",
    "How much does it cost to run Outline?": "manager/server-setup/cost",
    "Setting up multiple Outline servers": "manager/server-setup/multiple-servers",
    "Outline server setup FAQs": "manager/server-setup/setup-faqs",
    "Managing access to an Outline server (using access keys)": "manager/server-management/manage-access-keys",
    "How do I set data limits on access keys?": "manager/server-management/data-limits",
    "How do I reset my server ID?": "manager/server-management/reset-server-id",
    "How do I change the location of my Outline server?": "manager/server-management/change-location",
    "How do I update my Outline server software?": "manager/server-management/update-software",
    "How do I delete my Outline server?": "manager/server-management/delete-server",
    "How do I download the Outline Manager when the download link isn't working?": "manager/troubleshooting/manager-download",
    "Why can't I install the Outline Manager on Windows?": "manager/troubleshooting/windows-install",
    "I'm a developer. Where do I find support integrating the Outline SDK into my application?": "developers/sdk-support",
}

# Build doc -> web_id mapping
doc_to_web_id = {}
for web_id, title in ids_and_titles:
    # Clean HTML entities
    title_clean = title.replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'")
    if title_clean in TITLE_TO_DOC:
        doc_to_web_id[TITLE_TO_DOC[title_clean]] = web_id

# Also handle the available-languages for manager (same article ID)
# Find available-languages IDs
for web_id, title in ids_and_titles:
    title_clean = title.replace("&amp;", "&").replace("&quot;", '"')
    if "Available languages" in title_clean and "manager" not in doc_to_web_id.get("manager/server-setup/available-languages", ""):
        # There should be two "Available languages" articles
        if "client/getting-started/available-languages" in doc_to_web_id:
            doc_to_web_id["manager/server-setup/available-languages"] = web_id

# List of wrong-language articles we found and fixed/deleted
WRONG_LANG_ARTICLES = [
    ("de", "about/brand-usage", "Danish (da) instead of German"),
    ("it", "client/troubleshooting/connection-issues", "German (de) instead of Italian"),
    ("it", "client/getting-started/available-languages", "Lithuanian (lt) instead of Italian"),
    ("it", "manager/server-setup/available-languages", "Lithuanian (lt) instead of Italian"),
    ("it", "manager/server-management/reset-server-id", "Lithuanian (lt) instead of Italian"),
    ("ru", "client/getting-started/available-languages", "Norwegian (nb) instead of Russian"),
    ("ru", "manager/server-setup/available-languages", "Norwegian (nb) instead of Russian"),
    ("lv", "client/getting-started/install-linux", "Lao (lo) instead of Latvian"),
    ("mn", "client/getting-started/system-requirements", "Norwegian (nb) instead of Mongolian"),
    ("ur", "client/getting-started/system-requirements", "Ukrainian (uk) instead of Urdu"),
    ("ar", "about/getoutline-me-telegram", "English title (untranslated), Arabic body"),
]

print("=== Google Support URLs for articles in the wrong language ===\n")
for locale, doc_path, description in WRONG_LANG_ARTICLES:
    web_id = doc_to_web_id.get(doc_path, "???")
    url = f"https://support.google.com/outline/answer/{web_id}?hl={locale}"
    print(f"  {locale}/{doc_path}:")
    print(f"    Issue: {description}")
    print(f"    URL: {url}")
    print()
