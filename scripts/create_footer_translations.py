#!/usr/bin/env python3
"""Create footer.json translation files for all locales.

Pulls existing translations from ~/Projects/developer-documentation
and adds "Privacy Policy" translations for all locales.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
DEV_DOCS = Path.home() / "Projects" / "developer-documentation" / "i18n"

# Map developer-documentation locale codes to our locale codes
LOCALE_MAP = {
    "zh-CN": "zh-Hans",
    "zh-TW": "zh-Hant",
}

# Read all existing footer translations from developer-documentation
dev_footers = {}
if DEV_DOCS.exists():
    for locale_dir in DEV_DOCS.iterdir():
        if not locale_dir.is_dir():
            continue
        footer_path = locale_dir / "docusaurus-theme-classic" / "footer.json"
        if footer_path.exists():
            locale = LOCALE_MAP.get(locale_dir.name, locale_dir.name)
            dev_footers[locale] = json.loads(footer_path.read_text("utf-8"))

print(f"Found {len(dev_footers)} footer translations in developer-documentation:")
print(f"  Locales: {', '.join(sorted(dev_footers.keys()))}")

# "Privacy Policy" translations per locale
PRIVACY_POLICY = {
    "af": "Privaatheidsbeleid",
    "am": "የግላዊነት መመሪያ",
    "ar": "سياسة الخصوصية",
    "az": "Məxfilik Siyasəti",
    "bg": "Правила за поверителност",
    "bn": "গোপনীয়তা নীতি",
    "bs": "Politika privatnosti",
    "ca": "Política de privadesa",
    "cs": "Zásady ochrany soukromí",
    "da": "Fortrolighedspolitik",
    "de": "Datenschutzerklärung",
    "el": "Πολιτική απορρήτου",
    "en-GB": "Privacy Policy",
    "es": "Política de privacidad",
    "es-419": "Política de privacidad",
    "et": "Privaatsuspoliitika",
    "fa": "خط‌مشی رازداری",
    "fi": "Tietosuojakäytäntö",
    "fil": "Patakaran sa Privacy",
    "fr": "Règles de confidentialité",
    "he": "מדיניות פרטיות",
    "hi": "निजता नीति",
    "hr": "Pravila o privatnosti",
    "hu": "Adatvédelmi irányelvek",
    "hy": "Գաdelays",
    "id": "Kebijakan Privasi",
    "is": "Persónuverndarstefna",
    "it": "Informativa sulla privacy",
    "ja": "プライバシー ポリシー",
    "ka": "კონფიდენციალურობის დებულება",
    "kk": "Құпиялылық саясаты",
    "km": "គោលការណ៍​ភាពឯកជន",
    "ko": "개인정보처리방침",
    "lo": "ນະໂຍບາຍຄວາມເປັນສ່ວນຕົວ",
    "lv": "Privātuma politika",
    "mk": "Правила за приватност",
    "mn": "Нууцлалын бодлого",
    "mr": "गोपनीयता धोरण",
    "ms": "Dasar Privasi",
    "my": "ကိုယ်ရေးကိုယ်တာ မူဝါဒ",
    "nb": "Personvern",
    "ne": "गोपनीयता नीति",
    "nl": "Privacybeleid",
    "pl": "Polityka prywatności",
    "pt": "Política de Privacidade",
    "pt-BR": "Política de Privacidade",
    "ro": "Politica de confidențialitate",
    "ru": "Политика конфиденциальности",
    "si": "රහස්‍යතා ප්‍රතිපත්තිය",
    "sk": "Pravidlá ochrany súkromia",
    "sl": "Pravilnik o zasebnosti",
    "sq": "Politika e privatësisë",
    "sr": "Политика приватности",
    "sv": "Integritetspolicy",
    "sw": "Sera ya Faragha",
    "ta": "தனியுரிமைக் கொள்கை",
    "th": "นโยบายความเป็นส่วนตัว",
    "tr": "Gizlilik Politikası",
    "uk": "Політика конфіденційності",
    "ur": "رازداری کی پالیسی",
    "vi": "Chính sách quyền riêng tư",
    "zh-Hans": "隐私权政策",
    "zh-Hant": "隱私權政策",
    "zh-HK": "私隱政策",
}

# Fix Armenian
PRIVACY_POLICY["hy"] = "Գաղտնիության քաղաքականություն"

ENGLISH_DEFAULTS = {
    "link.title.Product Info": "Product Info",
    "link.title.Get Help": "Get Help",
    "link.item.label.Download Outline": "Download Outline",
    "link.item.label.Terms of Service": "Terms of Service",
    "link.item.label.Privacy Policy": "Privacy Policy",
    "link.item.label.GitHub": "GitHub",
    "link.item.label.Reddit": "Reddit",
    "link.item.label.Developer Docs": "Developer Docs",
}

DESCRIPTIONS = {
    "link.title.Product Info": "The title of the footer links column with title=Product Info in the footer",
    "link.title.Get Help": "The title of the footer links column with title=Get Help in the footer",
    "link.item.label.Download Outline": "The label of footer link with label=Download Outline linking to https://getoutline.org/",
    "link.item.label.Terms of Service": "The label of footer link with label=Terms of Service linking to https://s3.amazonaws.com/outline-vpn/static_downloads/Outline-Terms-of-Service.html",
    "link.item.label.Privacy Policy": "The label of footer link with label=Privacy Policy linking to https://s3.amazonaws.com/outline-vpn/static_downloads/Outline-Privacy-Policy.html",
    "link.item.label.GitHub": "The label of footer link with label=GitHub linking to https://github.com/OutlineFoundation/?q=outline",
    "link.item.label.Reddit": "The label of footer link with label=Reddit linking to https://www.reddit.com/r/outlinevpn/",
    "link.item.label.Developer Docs": "The label of footer link with label=Developer Docs linking to https://developer.getoutline.org/",
}

KEY_ORDER = [
    "link.title.Product Info",
    "link.title.Get Help",
    "link.item.label.Download Outline",
    "link.item.label.Terms of Service",
    "link.item.label.Privacy Policy",
    "link.item.label.GitHub",
    "link.item.label.Reddit",
    "link.item.label.Developer Docs",
]

total = 0
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
    if not docs_dir.exists():
        continue

    locale = locale_dir.name
    dev_data = dev_footers.get(locale, {})

    footer = {}
    for key in KEY_ORDER:
        if key in dev_data:
            message = dev_data[key]["message"]
        elif key == "link.item.label.Privacy Policy":
            message = PRIVACY_POLICY.get(locale, "Privacy Policy")
        else:
            message = ENGLISH_DEFAULTS[key]

        footer[key] = {
            "message": message,
            "description": DESCRIPTIONS[key],
        }

    theme_dir = locale_dir / "docusaurus-theme-classic"
    theme_dir.mkdir(exist_ok=True)
    (theme_dir / "footer.json").write_text(
        json.dumps(footer, ensure_ascii=False, indent=2) + "\n", "utf-8"
    )
    total += 1

print(f"\nCreated {total} footer.json files")
