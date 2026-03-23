#!/usr/bin/env python3
"""Generate CSV of wrong-language articles with Google Support URLs."""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_SITE = ROOT / "old-site" / "Help Center"

# Read English export to map article titles to WEB IDs
en_file = OLD_SITE / "WEBS_14917423,14919822,15330317,15330818,plus_31_more_en.HTML"
text = en_file.read_text("utf-8")

web_id_pattern = re.compile(r'WEB:(\d+)')
title_pattern = re.compile(r'<div class="gkms article title">(.+?)</div>')

ids_and_titles = []
current_id = None
for line in text.split("\n"):
    m = web_id_pattern.search(line)
    if m:
        current_id = m.group(1)
    m = title_pattern.search(line)
    if m and current_id:
        ids_and_titles.append((current_id, m.group(1).replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'")))
        current_id = None

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

# Build doc -> (web_id, english_title) mapping
doc_to_info = {}
seen_available = False
for web_id, title in ids_and_titles:
    if title in TITLE_TO_DOC:
        doc_to_info[TITLE_TO_DOC[title]] = (web_id, title)
    # Handle second "Available languages" for manager
    if title == "Available languages":
        if not seen_available:
            seen_available = True
        else:
            doc_to_info["manager/server-setup/available-languages"] = (web_id, title)

# Wrong-language articles: (intended_locale, doc_path, actual_lang_code)
WRONG_LANG = [
    ("de", "about/brand-usage", "da"),
    ("it", "client/troubleshooting/connection-issues", "de"),
    ("it", "client/getting-started/available-languages", "lt"),
    ("it", "manager/server-setup/available-languages", "lt"),
    ("it", "manager/server-management/reset-server-id", "lt"),
    ("ru", "client/getting-started/available-languages", "nb"),
    ("ru", "manager/server-setup/available-languages", "nb"),
    ("lv", "client/getting-started/install-linux", "lo"),
    ("mn", "client/getting-started/system-requirements", "nb"),
    ("ur", "client/getting-started/system-requirements", "uk"),
]

output_path = ROOT / "wrong-language-articles.csv"
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["english_title", "intended_language_code", "actual_language_code", "support_google_com_link"])

    for intended_locale, doc_path, actual_lang in WRONG_LANG:
        info = doc_to_info.get(doc_path)
        if info:
            web_id, en_title = info
            url = f"https://support.google.com/outline/answer/{web_id}?hl={intended_locale}"
        else:
            en_title = doc_path
            url = "N/A"

        writer.writerow([en_title, intended_locale, actual_lang, url])

print(f"CSV written to: {output_path}")
print(f"Total wrong-language articles: {len(WRONG_LANG)}")
