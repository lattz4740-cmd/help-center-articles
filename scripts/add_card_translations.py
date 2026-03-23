#!/usr/bin/env python3
"""Add card description and button translations to all code.json files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Translation keys and their values per locale
# Format: {key: {locale: message}}
TRANSLATIONS = {
    "homepage.about.description": {
        "en": "Learn how Outline works, its security model, and more.",
        "af": "Leer hoe Outline werk, sy sekuriteitsmodel, en meer.",
        "am": "Outline እንዴት እንደሚሰራ፣ የደህንነት ሞዴሉ፣ እና ሌሎችን ይወቁ።",
        "ar": "تعرَّف على آلية عمل Outline ونموذج الأمان والمزيد.",
        "az": "Outline-ın necə işlədiyini, təhlükəsizlik modelini və daha çoxunu öyrənin.",
        "bg": "Научете как работи Outline, неговия модел за сигурност и др.",
        "bn": "Outline কীভাবে কাজ করে, এর নিরাপত্তা মডেল এবং আরও জানুন।",
        "bs": "Saznajte kako Outline radi, njegov sigurnosni model i više.",
        "ca": "Apreneu com funciona Outline, el seu model de seguretat i molt més.",
        "cs": "Zjistěte, jak Outline funguje, jaký má model zabezpečení a další.",
        "da": "Lær hvordan Outline fungerer, sikkerhedsmodellen og mere.",
        "de": "Erfahren Sie, wie Outline funktioniert, und mehr über das Sicherheitsmodell.",
        "el": "Μάθετε πώς λειτουργεί το Outline, το μοντέλο ασφαλείας του και πολλά άλλα.",
        "en-GB": "Learn how Outline works, its security model, and more.",
        "es": "Descubre cómo funciona Outline, su modelo de seguridad y más.",
        "es-419": "Descubre cómo funciona Outline, su modelo de seguridad y más.",
        "et": "Siit saate teada, kuidas Outline töötab, selle turvamudeli ja palju muud.",
        "fa": "درباره نحوه کار Outline، مدل امنیتی آن و موارد دیگر بیاموزید.",
        "fi": "Lue, miten Outline toimii, sen tietoturvamalli ja paljon muuta.",
        "fil": "Alamin kung paano gumagana ang Outline, ang security model nito, at higit pa.",
        "fr": "Découvrez le fonctionnement d'Outline, son modèle de sécurité et plus encore.",
        "he": "למידע על אופן הפעולה של Outline, מודל האבטחה שלו ועוד.",
        "hi": "जानें कि Outline कैसे काम करता है, इसका सुरक्षा मॉडल और बहुत कुछ।",
        "hr": "Saznajte kako Outline funkcionira, njegov sigurnosni model i više.",
        "hu": "Tudja meg, hogyan működik az Outline, annak biztonsági modellje és egyebek.",
        "hy": "Իմացեք, թե ինչպես է աշխատում Outline-ը, նրա անվտանգության մոդելը և այլն:",
        "id": "Pelajari cara kerja Outline, model keamanannya, dan lainnya.",
        "is": "Lærðu hvernig Outline virkar, öryggislíkan þess og fleira.",
        "it": "Scopri come funziona Outline, il suo modello di sicurezza e molto altro.",
        "ja": "Outline の仕組み、セキュリティ モデルなどについて説明します。",
        "ka": "გაიგეთ, როგორ მუშაობს Outline, მისი უსაფრთხოების მოდელი და სხვა.",
        "kk": "Outline қалай жұмыс істейтінін, оның қауіпсіздік үлгісін және т.б. біліңіз.",
        "km": "ស្វែងយល់​ពី​របៀប​ដំណើរការ​របស់ Outline គំរូ​សុវត្ថិភាព និង​ច្រើន​ទៀត។",
        "ko": "Outline의 작동 방식, 보안 모델 등을 알아보세요.",
        "lo": "ຮຽນຮູ້ວິທີການເຮັດວຽກຂອງ Outline, ຮູບແບບຄວາມປອດໄພ ແລະ ອື່ນໆ.",
        "lv": "Uzziniet, kā darbojas Outline, tā drošības modeli un daudz ko citu.",
        "mk": "Дознајте како функционира Outline, неговиот безбедносен модел и повеќе.",
        "mn": "Outline хэрхэн ажилладаг, аюулгүй байдлын загвар зэргийг мэдэж аваарай.",
        "mr": "Outline कसे कार्य करते, त्याचे सुरक्षा मॉडेल आणि बरेच काही जाणून घ्या.",
        "ms": "Ketahui cara Outline berfungsi, model keselamatannya dan banyak lagi.",
        "my": "Outline အလုပ်လုပ်ပုံ၊ လုံခြုံရေးပုံစံနှင့် အခြားအရာများကို လေ့လာပါ။",
        "nb": "Lær hvordan Outline fungerer, sikkerhetsmodellen og mer.",
        "ne": "Outline कसरी काम गर्छ, यसको सुरक्षा मोडेल र थप जान्नुहोस्।",
        "nl": "Lees hoe Outline werkt, over het beveiligingsmodel en meer.",
        "pl": "Dowiedz się, jak działa Outline, poznaj model zabezpieczeń i nie tylko.",
        "pt": "Saiba como o Outline funciona, o modelo de segurança e muito mais.",
        "pt-BR": "Saiba como o Outline funciona, o modelo de segurança e muito mais.",
        "ro": "Aflați cum funcționează Outline, modelul de securitate și multe altele.",
        "ru": "Узнайте, как работает Outline, о модели безопасности и многом другом.",
        "si": "Outline ක්‍රියා කරන ආකාරය, එහි ආරක්‍ෂණ ආකෘතිය සහ තවත් දේ ගැන ඉගෙන ගන්න.",
        "sk": "Zistite, ako Outline funguje, aký má model zabezpečenia a ďalšie informácie.",
        "sl": "Preberite, kako deluje Outline, njegov varnostni model in več.",
        "sq": "Mësoni se si funksionon Outline, modelin e sigurisë dhe më shumë.",
        "sr": "Сазнајте како Outline функционише, његов безбедносни модел и још много тога.",
        "sv": "Läs om hur Outline fungerar, dess säkerhetsmodell och mycket mer.",
        "sw": "Jifunze jinsi Outline inavyofanya kazi, muundo wake wa usalama, na mengine zaidi.",
        "ta": "Outline எவ்வாறு செயல்படுகிறது, அதன் பாதுகாப்பு மாதிரி மற்றும் பலவற்றை அறிக.",
        "th": "เรียนรู้วิธีการทำงานของ Outline รูปแบบความปลอดภัย และอื่นๆ",
        "tr": "Outline'ın nasıl çalıştığını, güvenlik modelini ve daha fazlasını öğrenin.",
        "uk": "Дізнайтеся, як працює Outline, його модель безпеки тощо.",
        "ur": "جانیں کہ Outline کیسے کام کرتا ہے، اس کا سیکیورٹی ماڈل، اور مزید۔",
        "vi": "Tìm hiểu cách Outline hoạt động, mô hình bảo mật và nhiều hơn nữa.",
        "zh-Hans": "了解 Outline 的工作原理、安全模型等。",
        "zh-Hant": "瞭解 Outline 的運作方式、安全模型等。",
        "zh-HK": "瞭解 Outline 的運作方式、安全模型等。",
    },
    "homepage.about.button": {
        "en": "Learn more",
    },
    "homepage.client.description": {
        "en": "Get started with connecting your device and troubleshooting.",
    },
    "homepage.client.button": {
        "en": "Get started",
    },
    "homepage.manager.description": {
        "en": "Set up and manage your Outline server.",
    },
    "homepage.manager.button": {
        "en": "Set up a server",
    },
    "homepage.developers.description": {
        "en": "Integrate the Outline SDK into your application.",
    },
    "homepage.developers.button": {
        "en": "Explore the SDK",
    },
}

# Simple button/description translations
BUTTON_TRANSLATIONS = {
    "homepage.about.button": {
        "de": "Mehr erfahren", "fr": "En savoir plus", "es": "Más información",
        "es-419": "Más información", "it": "Scopri di più", "ja": "詳細",
        "ko": "자세히 알아보기", "pt": "Saiba mais", "pt-BR": "Saiba mais",
        "ru": "Подробнее", "zh-Hans": "了解详情", "zh-Hant": "瞭解詳情", "zh-HK": "瞭解詳情",
        "ar": "مزيد من المعلومات", "nl": "Meer informatie", "pl": "Dowiedz się więcej",
        "tr": "Daha fazla bilgi", "th": "เรียนรู้เพิ่มเติม", "vi": "Tìm hiểu thêm",
        "uk": "Дізнатися більше", "sv": "Läs mer", "da": "Læs mere", "nb": "Les mer",
        "fi": "Lue lisää", "cs": "Zjistit více", "el": "Μάθετε περισσότερα",
        "hu": "Tudjon meg többet", "ro": "Aflați mai multe", "bg": "Научете повече",
        "hr": "Saznajte više", "sk": "Zistite viac", "sl": "Več informacij",
        "he": "מידע נוסף", "hi": "और जानें", "fa": "اطلاعات بیشتر",
        "id": "Pelajari lebih lanjut", "ms": "Ketahui lebih lanjut",
    },
    "homepage.client.button": {
        "de": "Erste Schritte", "fr": "Commencer", "es": "Empezar",
        "es-419": "Empezar", "it": "Inizia", "ja": "使ってみる",
        "ko": "시작하기", "pt": "Começar", "pt-BR": "Começar",
        "ru": "Начать", "zh-Hans": "开始使用", "zh-Hant": "開始使用", "zh-HK": "開始使用",
        "ar": "البدء", "nl": "Aan de slag", "pl": "Rozpocznij",
        "tr": "Başlayın", "th": "เริ่มต้นใช้งาน", "vi": "Bắt đầu",
        "uk": "Почати", "sv": "Kom igång", "da": "Kom i gang", "nb": "Kom i gang",
        "fi": "Aloita", "cs": "Začít", "el": "Ξεκινήστε",
        "hu": "Első lépések", "ro": "Începeți", "bg": "Започнете",
        "hr": "Započnite", "sk": "Začať", "sl": "Začnite",
        "he": "תחילת העבודה", "hi": "शुरू करें", "fa": "شروع کنید",
        "id": "Mulai", "ms": "Mulakan",
    },
    "homepage.manager.button": {
        "de": "Server einrichten", "fr": "Configurer un serveur", "es": "Configurar un servidor",
        "es-419": "Configurar un servidor", "it": "Configura un server", "ja": "サーバーを設定",
        "ko": "서버 설정", "pt": "Configurar servidor", "pt-BR": "Configurar servidor",
        "ru": "Настроить сервер", "zh-Hans": "设置服务器", "zh-Hant": "設定伺服器", "zh-HK": "設定伺服器",
        "ar": "إعداد خادم", "nl": "Server instellen", "pl": "Skonfiguruj serwer",
        "tr": "Sunucu kurun", "th": "ตั้งค่าเซิร์ฟเวอร์", "vi": "Thiết lập máy chủ",
        "uk": "Налаштувати сервер", "sv": "Konfigurera server", "da": "Konfigurer server", "nb": "Sett opp server",
        "fi": "Määritä palvelin", "cs": "Nastavit server", "el": "Ρύθμιση διακομιστή",
        "hu": "Szerver beállítása", "ro": "Configurați serverul", "bg": "Настройване на сървър",
        "hr": "Postavi poslužitelj", "sk": "Nastaviť server", "sl": "Nastavite strežnik",
        "he": "הגדרת שרת", "hi": "सर्वर सेट अप करें", "fa": "راه‌اندازی سرور",
        "id": "Siapkan server", "ms": "Sediakan pelayan",
    },
    "homepage.developers.button": {
        "de": "SDK erkunden", "fr": "Explorer le SDK", "es": "Explorar el SDK",
        "es-419": "Explorar el SDK", "it": "Esplora l'SDK", "ja": "SDKを見る",
        "ko": "SDK 살펴보기", "pt": "Explorar o SDK", "pt-BR": "Explorar o SDK",
        "ru": "Изучить SDK", "zh-Hans": "探索 SDK", "zh-Hant": "探索 SDK", "zh-HK": "探索 SDK",
        "ar": "استكشاف SDK", "nl": "SDK verkennen", "pl": "Poznaj SDK",
        "tr": "SDK'yı keşfedin", "th": "สำรวจ SDK", "vi": "Khám phá SDK",
        "uk": "Дослідити SDK", "sv": "Utforska SDK", "da": "Udforsk SDK", "nb": "Utforsk SDK",
        "fi": "Tutustu SDK:hon", "cs": "Prozkoumat SDK", "el": "Εξερευνήστε το SDK",
        "hu": "SDK felfedezése", "ro": "Explorați SDK-ul", "bg": "Разгледайте SDK",
        "hr": "Istražite SDK", "sk": "Preskúmajte SDK", "sl": "Raziščite SDK",
        "he": "גלה את ה-SDK", "hi": "SDK का अन्वेषण करें", "fa": "کاوش SDK",
        "id": "Jelajahi SDK", "ms": "Terokai SDK",
    },
    "homepage.client.description": {
        "de": "Verbinden Sie Ihr Gerät und beheben Sie Probleme.",
        "fr": "Connectez votre appareil et résolvez les problèmes.",
        "es": "Conecta tu dispositivo y soluciona problemas.",
        "es-419": "Conecta tu dispositivo y soluciona problemas.",
        "it": "Collega il tuo dispositivo e risolvi i problemi.",
        "ja": "デバイスの接続とトラブルシューティングを始めましょう。",
        "ko": "기기를 연결하고 문제를 해결하세요.",
        "pt": "Conecte o seu dispositivo e resolva problemas.",
        "pt-BR": "Conecte seu dispositivo e resolva problemas.",
        "ru": "Подключите устройство и устраните неполадки.",
        "zh-Hans": "连接设备并排除故障。",
        "zh-Hant": "連線裝置並排解問題。",
        "zh-HK": "連線裝置並排解問題。",
        "ar": "ابدأ بتوصيل جهازك واستكشاف الأخطاء وإصلاحها.",
        "nl": "Sluit uw apparaat aan en los problemen op.",
        "pl": "Połącz urządzenie i rozwiąż problemy.",
        "tr": "Cihazınızı bağlayın ve sorunları giderin.",
        "th": "เริ่มต้นเชื่อมต่ออุปกรณ์และแก้ไขปัญหา",
        "vi": "Bắt đầu kết nối thiết bị và khắc phục sự cố.",
        "uk": "Підключіть пристрій і усуньте несправності.",
    },
    "homepage.manager.description": {
        "de": "Richten Sie Ihren Outline-Server ein und verwalten Sie ihn.",
        "fr": "Configurez et gérez votre serveur Outline.",
        "es": "Configura y administra tu servidor Outline.",
        "es-419": "Configura y administra tu servidor Outline.",
        "it": "Configura e gestisci il tuo server Outline.",
        "ja": "Outline サーバーを設定して管理します。",
        "ko": "Outline 서버를 설정하고 관리하세요.",
        "pt": "Configure e faça a gestão do seu servidor Outline.",
        "pt-BR": "Configure e gerencie seu servidor Outline.",
        "ru": "Настройте сервер Outline и управляйте им.",
        "zh-Hans": "设置和管理您的 Outline 服务器。",
        "zh-Hant": "設定及管理您的 Outline 伺服器。",
        "zh-HK": "設定及管理您的 Outline 伺服器。",
        "ar": "قم بإعداد وإدارة خادم Outline الخاص بك.",
        "nl": "Stel uw Outline-server in en beheer deze.",
        "pl": "Skonfiguruj serwer Outline i zarządzaj nim.",
        "tr": "Outline sunucunuzu kurun ve yönetin.",
        "th": "ตั้งค่าและจัดการเซิร์ฟเวอร์ Outline ของคุณ",
        "vi": "Thiết lập và quản lý máy chủ Outline của bạn.",
        "uk": "Налаштуйте сервер Outline і керуйте ним.",
    },
    "homepage.developers.description": {
        "de": "Integrieren Sie das Outline SDK in Ihre Anwendung.",
        "fr": "Intégrez le SDK Outline dans votre application.",
        "es": "Integra el SDK de Outline en tu aplicación.",
        "es-419": "Integra el SDK de Outline en tu aplicación.",
        "it": "Integra l'SDK di Outline nella tua applicazione.",
        "ja": "Outline SDK をアプリケーションに統合しましょう。",
        "ko": "Outline SDK를 애플리케이션에 통합하세요.",
        "pt": "Integre o SDK do Outline na sua aplicação.",
        "pt-BR": "Integre o SDK do Outline ao seu aplicativo.",
        "ru": "Интегрируйте Outline SDK в ваше приложение.",
        "zh-Hans": "将 Outline SDK 集成到您的应用中。",
        "zh-Hant": "將 Outline SDK 整合到您的應用程式中。",
        "zh-HK": "將 Outline SDK 整合到您的應用程式中。",
        "ar": "ادمج حزمة Outline SDK في تطبيقك.",
        "nl": "Integreer de Outline SDK in uw applicatie.",
        "pl": "Zintegruj Outline SDK ze swoją aplikacją.",
        "tr": "Outline SDK'yı uygulamanıza entegre edin.",
        "th": "รวม Outline SDK เข้ากับแอปพลิเคชันของคุณ",
        "vi": "Tích hợp Outline SDK vào ứng dụng của bạn.",
        "uk": "Інтегруйте Outline SDK у свій додаток.",
    },
}

# Merge button translations into TRANSLATIONS
for key, locales in BUTTON_TRANSLATIONS.items():
    if key not in TRANSLATIONS:
        TRANSLATIONS[key] = {"en": ""}
    TRANSLATIONS[key].update(locales)

DESCRIPTIONS = {
    "homepage.about.description": "Description for the About Outline card on the homepage",
    "homepage.about.button": "Button text for the About Outline card on the homepage",
    "homepage.client.description": "Description for the Outline Client card on the homepage",
    "homepage.client.button": "Button text for the Outline Client card on the homepage",
    "homepage.manager.description": "Description for the Outline Manager card on the homepage",
    "homepage.manager.button": "Button text for the Outline Manager card on the homepage",
    "homepage.developers.description": "Description for the For Developers card on the homepage",
    "homepage.developers.button": "Button text for the For Developers card on the homepage",
}

total = 0
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    code_path = locale_dir / "code.json"
    if not code_path.exists():
        continue

    locale = locale_dir.name
    data = json.loads(code_path.read_text("utf-8"))

    for key, locales in TRANSLATIONS.items():
        message = locales.get(locale, locales.get("en", ""))
        data[key] = {
            "message": message,
            "description": DESCRIPTIONS.get(key, ""),
        }

    code_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", "utf-8")
    total += 1

print(f"Updated {total} code.json files with card translations")
