# Outline Help Center

Help center articles for [Outline VPN](https://getoutline.org), built with [Docusaurus](https://docusaurus.io/).

Live site: https://support.getoutline.org

## Prerequisites

- [Node.js](https://nodejs.org/) >= 20
- [Python 3](https://www.python.org/) with `beautifulsoup4` (for content conversion scripts)

## Getting Started

Install dependencies:

```sh
npm install
```

Start the local development server (English only):

```sh
npm start
```

This opens `http://localhost:3000` with hot-reloading enabled.

To start the dev server in a specific locale:

```sh
npm start -- --locale fr
```

## Building

Build the site for all 65 locales (slow):

```sh
npm run build
```

Build for a single locale (fast, useful for testing):

```sh
npm run build -- --locale en
```

Build a small subset of locales for development (en, fr, ar):

```sh
npm run build:dev
```

Preview the production build locally:

```sh
npm run serve
```

## Deployment

The site deploys to GitHub Pages via the CI workflow on push to `main`. It builds all 65 locales and publishes to the `gh-pages` branch, which is served at https://support.getoutline.org.

## Content Conversion

The original content was exported from Google's GKMS (Knowledge Management System) in HTML format. Conversion scripts in `scripts/` transform this into Markdown:

- `scripts/convert_gkms.py` — Converts English articles from `old-site/` to `docs/`
- `scripts/convert_translations.py` — Converts all non-English translations to `i18n/`
- `scripts/create_placeholder_images.py` — Creates placeholder images (for development)
- `scripts/download_images.py` — Downloads article images from Google Cloud Storage
- `scripts/rename_images.sh` — Renames downloaded images to match expected filenames

To re-run the conversion (requires `pip install beautifulsoup4`):

```sh
python3 scripts/convert_gkms.py
python3 scripts/convert_translations.py
```

## Project Structure

```
docs/                  # English documentation (default locale)
i18n/                  # Translated documentation (64 locales)
  {locale}/
    docusaurus-plugin-content-docs/current/  # Translated articles
  partial-translations/  # Incomplete translations (not built)
old-site/              # Original GKMS HTML exports (source of truth)
scripts/               # Conversion and utility scripts
src/css/               # Custom CSS
static/images/         # Images and logos
```
