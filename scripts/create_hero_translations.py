#!/usr/bin/env python3
"""Create code.json files with 'How can we help you?' translations for all locales."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Standard translations of "How can we help you?"
TRANSLATIONS = {
    "af": "Hoe kan ons jou help?",
    "am": "እንዴት ልንረዳዎ እንችላለን?",
    "ar": "كيف يمكننا مساعدتك؟",
    "az": "Sizə necə kömək edə bilərik?",
    "bg": "Как можем да ви помогнем?",
    "bn": "আমরা কীভাবে আপনাকে সাহায্য করতে পারি?",
    "bs": "Kako vam možemo pomoći?",
    "ca": "Com et podem ajudar?",
    "cs": "Jak vám můžeme pomoci?",
    "da": "Hvordan kan vi hjælpe dig?",
    "de": "Wie können wir helfen?",
    "el": "Πώς μπορούμε να σας βοηθήσουμε;",
    "en-GB": "How can we help you?",
    "es": "¿Cómo podemos ayudarte?",
    "es-419": "¿Cómo podemos ayudarte?",
    "et": "Kuidas saame teid aidata?",
    "fa": "چگونه می‌توانیم به شما کمک کنیم؟",
    "fi": "Miten voimme auttaa?",
    "fil": "Paano ka namin matutulungan?",
    "fr": "Comment pouvons-nous vous aider ?",
    "he": "איך נוכל לעזור לך?",
    "hi": "हम आपकी कैसे मदद कर सकते हैं?",
    "hr": "Kako vam možemo pomoći?",
    "hu": "Hogyan segíthetünk?",
    "hy": "Ինչպե՞ delays delays",
    "id": "Bagaimana kami dapat membantu Anda?",
    "is": "Hvernig getum við aðstoðað þig?",
    "it": "Come possiamo aiutarti?",
    "ja": "お困りですか？",
    "ka": "როგორ შეგვიძლია დაგეხმაროთ?",
    "kk": "Сізге қалай көмектесе аламыз?",
    "km": "តើ​យើង​អាច​ជួយ​អ្នក​ដោយ​របៀប​ណា?",
    "ko": "무엇을 도와드릴까요?",
    "lo": "ພວກເຮົາຊ່ວຍທ່ານໄດ້ແນວໃດ?",
    "lv": "Kā mēs varam jums palīdzēt?",
    "mk": "Како можеме да ви помогнеме?",
    "mn": "Бид танд хэрхэн туслах вэ?",
    "mr": "आम्ही तुम्हाला कशी मदत करू शकतो?",
    "ms": "Bagaimana kami boleh membantu anda?",
    "my": "ကျွန်ုပ်တို့ ဘယ်လိုကူညီပေးရမလဲ?",
    "nb": "Hvordan kan vi hjelpe deg?",
    "ne": "हामी तपाईंलाई कसरी मद्दत गर्न सक्छौं?",
    "nl": "Hoe kunnen we je helpen?",
    "pl": "Jak możemy Ci pomóc?",
    "pt": "Como podemos ajudar?",
    "pt-BR": "Como podemos ajudar você?",
    "ro": "Cum vă putem ajuta?",
    "ru": "Чем мы можем вам помочь?",
    "si": "අපට ඔබට උදව් කළ හැක්කේ කෙසේද?",
    "sk": "Ako vám môžeme pomôcť?",
    "sl": "Kako vam lahko pomagamo?",
    "sq": "Si mund t'ju ndihmojmë?",
    "sr": "Како вам можемо помоћи?",
    "sv": "Hur kan vi hjälpa dig?",
    "sw": "Tunawezaje kukusaidia?",
    "ta": "நாங்கள் உங்களுக்கு எப்படி உதவ முடியும்?",
    "th": "เราช่วยคุณได้อย่างไร",
    "tr": "Size nasıl yardımcı olabiliriz?",
    "uk": "Як ми можемо вам допомогти?",
    "ur": "ہم آپ کی کس طرح مدد کر سکتے ہیں؟",
    "vi": "Chúng tôi có thể giúp gì cho bạn?",
    "zh-Hans": "我们可以为您提供什么帮助？",
    "zh-Hant": "我們可以為您提供什麼協助？",
    "zh-HK": "我們可以為您提供什麼協助？",
}

# Fix Armenian
TRANSLATIONS["hy"] = "Ինչպե՞ delays hy"  # placeholder, fix below

# Actually let me use the correct Armenian
TRANSLATIONS["hy"] = "Ինչպե՞ս կարող ենք օգնել ձեզ:"

SEARCH_PLACEHOLDER = {
    "af": "Soek vir hulp...",
    "am": "እገዛ ፈልግ...",
    "ar": "ابحث عن مساعدة...",
    "az": "Kömək axtarın...",
    "bg": "Търсене на помощ...",
    "bn": "সাহায্য খুঁজুন...",
    "bs": "Pretraži pomoć...",
    "ca": "Cerca ajuda...",
    "cs": "Hledejte pomoc...",
    "da": "Søg efter hjælp...",
    "de": "Hilfe suchen...",
    "el": "Αναζήτηση βοήθειας...",
    "en-GB": "Search for help...",
    "es": "Buscar ayuda...",
    "es-419": "Buscar ayuda...",
    "et": "Otsi abi...",
    "fa": "جستجوی راهنما...",
    "fi": "Hae ohjeita...",
    "fil": "Maghanap ng tulong...",
    "fr": "Rechercher de l'aide...",
    "he": "חיפוש עזרה...",
    "hi": "सहायता खोजें...",
    "hr": "Pretraži pomoć...",
    "hu": "Segítség keresése...",
    "hy": "Որոնել օգնություն...",
    "id": "Cari bantuan...",
    "is": "Leita að hjálp...",
    "it": "Cerca assistenza...",
    "ja": "ヘルプを検索...",
    "ka": "დახმარების ძიება...",
    "kk": "Көмек іздеу...",
    "km": "ស្វែងរក​ជំនួយ...",
    "ko": "도움말 검색...",
    "lo": "ຊອກຫາຄວາມຊ່ວຍເຫຼືອ...",
    "lv": "Meklēt palīdzību...",
    "mk": "Пребарувајте помош...",
    "mn": "Тусламж хайх...",
    "mr": "मदत शोधा...",
    "ms": "Cari bantuan...",
    "my": "အကူအညီရှာပါ...",
    "nb": "Søk etter hjelp...",
    "ne": "मद्दत खोज्नुहोस्...",
    "nl": "Zoek naar hulp...",
    "pl": "Szukaj pomocy...",
    "pt": "Pesquisar ajuda...",
    "pt-BR": "Pesquisar ajuda...",
    "ro": "Căutați ajutor...",
    "ru": "Поиск справки...",
    "si": "උදව් සොයන්න...",
    "sk": "Hľadať pomoc...",
    "sl": "Išči pomoč...",
    "sq": "Kërko ndihmë...",
    "sr": "Претражите помоћ...",
    "sv": "Sök efter hjälp...",
    "sw": "Tafuta msaada...",
    "ta": "உதவி தேடுங்கள்...",
    "th": "ค้นหาความช่วยเหลือ...",
    "tr": "Yardım arayın...",
    "uk": "Пошук довідки...",
    "ur": "مدد تلاش کریں...",
    "vi": "Tìm kiếm trợ giúp...",
    "zh-Hans": "搜索帮助...",
    "zh-Hant": "搜尋說明...",
    "zh-HK": "搜尋說明...",
}

total = 0
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
    if not docs_dir.exists():
        continue

    locale = locale_dir.name
    title = TRANSLATIONS.get(locale, "How can we help you?")
    placeholder = SEARCH_PLACEHOLDER.get(locale, "Search for help...")

    code_data = {
        "homepage.hero.title": {
            "message": title,
            "description": "The hero title on the homepage"
        },
        "homepage.hero.searchPlaceholder": {
            "message": placeholder,
            "description": "The search placeholder on the homepage"
        }
    }

    code_path = locale_dir / "code.json"
    code_path.write_text(json.dumps(code_data, ensure_ascii=False, indent=2) + "\n", "utf-8")
    total += 1

print(f"Created {total} code.json files")
