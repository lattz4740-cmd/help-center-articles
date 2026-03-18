#!/usr/bin/env python3
"""Compare locales available on support.google.com/outline vs our Docusaurus site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Languages listed in the Google Support language dropdown (mapped to BCP 47 codes).
# Scraped from https://support.google.com/outline?hl=en language selector.
GOOGLE_SUPPORT_LOCALES = {
    "af",       # Afrikaans
    "ar",       # العربية
    "bg",       # български
    "bn",       # বাংলা
    "ca",       # català
    "cs",       # čeština
    "de",       # Deutsch
    "el",       # Ελληνικά
    "en-GB",    # English (United Kingdom)
    "es",       # español
    "es-419",   # español (Latinoamérica)
    "et",       # eesti
    "fa",       # فارسی
    "fi",       # suomi
    "fil",      # Filipino
    "fr",       # français
    "he",       # עברית
    "hi",       # हिन्दी
    "hr",       # hrvatski
    "hu",       # magyar
    "hy",       # հայերեն
    "id",       # Indonesia
    "is",       # íslenska
    "it",       # italiano
    "ja",       # 日本語
    "ka",       # ქართული
    "kk",       # қазақ тілі
    "km",       # ខ្មែរ
    "ko",       # 한국어
    "lv",       # latviešu
    "mk",       # македонски
    "mn",       # монгол
    "mr",       # मराठी
    "ms",       # Melayu
    "my",       # မြန်မာ
    "nb",       # norsk
    "nl",       # Nederlands
    "pl",       # polski
    "pt",       # português
    "pt-BR",    # português (Brasil)
    "ro",       # română
    "ru",       # русский
    "sk",       # slovenčina
    "sl",       # slovenščina
    "sq",       # shqip
    "sr",       # српски
    "sv",       # svenska
    "sw",       # Kiswahili
    "ta",       # தமிழ்
    "th",       # ไทย
    "tr",       # Türkçe
    "uk",       # українська
    "vi",       # Tiếng Việt
    "zh-Hans",  # 中文（简体）
    "zh-Hant",  # 中文（繁體）
}
# Note: Google also lists "svenska (Sverige)" and "Ελληνικά (Ελλάδα)" which
# appear to be duplicates of sv and el respectively. Excluded.

# Our Docusaurus locales (from docusaurus.config.ts)
OUR_LOCALES = [
    "af", "am", "ar", "ar-EG", "as", "az", "be", "bg", "bn", "bs",
    "ca", "cs", "cy", "da", "de", "de-CH", "el", "en-AU", "en-CA", "en-GB",
    "en-IN", "en-SG", "es", "es-419", "et", "eu", "fa", "fi", "fil", "fr",
    "fr-CA", "ga", "gl", "gu", "ha", "he", "hi", "hr", "hu", "hy", "id",
    "is", "it", "ja", "ka", "kk", "km", "kn", "ko", "ky", "lo", "lt", "lv",
    "mk", "ml", "mn", "mr", "ms", "my", "nb", "ne", "nl", "or", "pa", "pl",
    "pt", "pt-BR", "ro", "ru", "si", "sk", "sl", "sq", "sr", "sv", "sw",
    "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "yo", "zh-Hans",
    "zh-Hant", "zh-HK", "zu",
]


def count_translated_docs(locale):
    """Count how many translated docs exist for a locale."""
    locale_dir = I18N / locale / "docusaurus-plugin-content-docs" / "current"
    if not locale_dir.exists():
        return 0
    return len(list(locale_dir.rglob("*.md")))


def main():
    our_set = set(OUR_LOCALES)
    google_set = GOOGLE_SUPPORT_LOCALES

    on_google = our_set & google_set
    not_on_google = our_set - google_set

    print(f"Our locales: {len(our_set)}")
    print(f"Google support locales: {len(google_set)}")
    print(f"Overlap: {len(on_google)}")
    print(f"Only in our site (not on Google): {len(not_on_google)}")
    print()

    # Show locales not on Google with their doc counts
    print("=== Locales NOT on Google Support (candidates for partial-translations/) ===")
    print(f"{'Locale':<10} {'Docs':>5}  Notes")
    print("-" * 50)
    for locale in sorted(not_on_google):
        count = count_translated_docs(locale)
        print(f"{locale:<10} {count:>5}")

    print()
    print("=== Locales on Google Support (keep in i18n/) ===")
    print(f"{'Locale':<10} {'Docs':>5}")
    print("-" * 50)
    for locale in sorted(on_google):
        count = count_translated_docs(locale)
        print(f"{locale:<10} {count:>5}")


if __name__ == "__main__":
    main()
