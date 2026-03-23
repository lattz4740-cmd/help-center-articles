#!/usr/bin/env python3
"""Add 'Browse help topics' translation to all code.json files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

BROWSE = {
    "af": "Blaai deur hulponderwerpe",
    "am": "የእገዛ ርዕሶችን ያስሱ",
    "ar": "تصفّح مواضيع المساعدة",
    "az": "Yardım mövzularına baxın",
    "bg": "Преглед на помощните теми",
    "bn": "সাহায্যের বিষয়গুলি ব্রাউজ করুন",
    "bs": "Pregledajte teme za pomoć",
    "ca": "Navega pels temes d'ajuda",
    "cs": "Procházet témata nápovědy",
    "da": "Gennemse hjælpeemner",
    "de": "Hilfethemen durchsuchen",
    "el": "Περιήγηση σε θέματα βοήθειας",
    "en-GB": "Browse help topics",
    "es": "Explorar temas de ayuda",
    "es-419": "Explorar temas de ayuda",
    "et": "Sirvi abiteemesid",
    "fa": "مرور موضوعات راهنما",
    "fi": "Selaa ohjeaiheita",
    "fil": "Mag-browse ng mga paksa ng tulong",
    "fr": "Parcourir les sujets d'aide",
    "he": "עיון בנושאי עזרה",
    "hi": "सहायता विषय ब्राउज़ करें",
    "hr": "Pregledajte teme za pomoć",
    "hu": "Súgótémák böngészése",
    "hy": "Զnnnn delays",
    "id": "Jelajahi topik bantuan",
    "is": "Skoða hjálparefni",
    "it": "Sfoglia gli argomenti di assistenza",
    "ja": "ヘルプトピックを見る",
    "ka": "დახმარების თემების დათვალიერება",
    "kk": "Анықтама тақырыптарын шолу",
    "km": "រុករក​ប្រធានបទ​ជំនួយ",
    "ko": "도움말 주제 찾아보기",
    "lo": "ເບິ່ງຫົວຂໍ້ຄວາມຊ່ວຍເຫຼືອ",
    "lv": "Pārlūkot palīdzības tēmas",
    "mk": "Прегледајте теми за помош",
    "mn": "Тусламжийн сэдвүүдийг үзэх",
    "mr": "मदत विषय ब्राउझ करा",
    "ms": "Semak imbas topik bantuan",
    "my": "အကူအညီခေါင်းစဉ်များ ရှာဖွေပါ",
    "nb": "Se gjennom hjelpeemner",
    "ne": "मद्दत विषयहरू ब्राउज गर्नुहोस्",
    "nl": "Hulponderwerpen bekijken",
    "pl": "Przeglądaj tematy pomocy",
    "pt": "Explorar tópicos de ajuda",
    "pt-BR": "Explorar tópicos de ajuda",
    "ro": "Răsfoiți subiectele de ajutor",
    "ru": "Обзор тем справки",
    "si": "උදව් මාතෘකා බ්‍රවුස් කරන්න",
    "sk": "Prehľadávať témy pomocníka",
    "sl": "Brskanje po temah pomoči",
    "sq": "Shfletoni temat e ndihmës",
    "sr": "Прегледајте теме помоћи",
    "sv": "Bläddra bland hjälpämnen",
    "sw": "Vinjari mada za usaidizi",
    "ta": "உதவி தலைப்புகளை உலாவுக",
    "th": "เรียกดูหัวข้อความช่วยเหลือ",
    "tr": "Yardım konularına göz atın",
    "uk": "Перегляд тем довідки",
    "ur": "مدد کے موضوعات براؤز کریں",
    "vi": "Duyệt các chủ đề trợ giúp",
    "zh-Hans": "浏览帮助主题",
    "zh-Hant": "瀏覽說明主題",
    "zh-HK": "瀏覽說明主題",
}

# Fix Armenian
BROWSE["hy"] = "Զննել օգնության թեմաները"

total = 0
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    code_path = locale_dir / "code.json"
    if not code_path.exists():
        continue

    locale = locale_dir.name
    data = json.loads(code_path.read_text("utf-8"))
    data["homepage.browseTopics"] = {
        "message": BROWSE.get(locale, "Browse help topics"),
        "description": "The heading for the browse topics section on the homepage"
    }
    code_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", "utf-8")
    total += 1

print(f"Updated {total} code.json files")
