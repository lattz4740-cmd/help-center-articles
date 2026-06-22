# Outline Help Center

Help center articles for [Outline VPN](https://getoutline.org), built with [Docusaurus](https://docusaurus.io/).

Live site: https://support.getoutline.org

## Prerequisites

- [Node.js](https://nodejs.org/) >= 20

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

Build a small subset of locales for development (en, fr, ar):

```sh
npm run build:dev
```

Preview the production build locally:

```sh
npm run serve
```

## Deployment

The site is hosted on [Cloudflare Pages](https://pages.cloudflare.com/) with the
Git integration enabled. Deployment is automatic:

- Merging to `main` triggers a production deploy to https://support.getoutline.org.
- Opening a pull request creates a preview deployment with its own URL.

Cloudflare Pages builds with `npm run build` (output in `build/`) on the Node
version pinned in `.nvmrc`. There is no manual deploy step.

Translations are verified in CI on every pull request. To run the same check
locally:

```sh
npm run verify
```