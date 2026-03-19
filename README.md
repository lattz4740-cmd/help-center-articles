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

Deploy to GitHub Pages:

```sh
npm run deploy
```

This verifies translations, builds all 65 locales, and pushes to the `gh-pages` branch, which is served at https://support.getoutline.org.