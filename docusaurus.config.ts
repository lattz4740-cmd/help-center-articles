import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const SUPPORTED_LOCALES = ['en'];

function buildLocaleConfigs(): Record<string, {label: string; direction: 'ltr' | 'rtl'}> {
  const configs: Record<string, {label: string; direction: 'ltr' | 'rtl'}> = {};
  for (const locale of SUPPORTED_LOCALES) {
    const label = new Intl.DisplayNames([locale], {type: 'language'}).of(locale) ?? locale;
    const {direction} = (new Intl.Locale(locale) as Intl.Locale & {textInfo: {direction: 'ltr' | 'rtl'}}).textInfo;
    configs[locale] = {label, direction};
  }
  return configs;
}

const config: Config = {
  title: 'Outline Help Center',
  tagline: 'Get help with Outline VPN',
  favicon: 'images/outline-favicon.png',

  future: {
    v4: true,
  },

  url: 'https://support.getoutline.org',
  baseUrl: '/',

  organizationName: 'OutlineFoundation',
  projectName: 'help-center-articles',
  deploymentBranch: 'gh-pages',

  onBrokenLinks: 'throw',

  markdown: {
    format: 'detect',
  },

  i18n: {
    defaultLocale: 'en',
    locales: SUPPORTED_LOCALES,
    localeConfigs: buildLocaleConfigs(),
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/',
          editUrl:
            'https://github.com/OutlineFoundation/help-center-articles/edit/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'images/outline-logo.png',
    colorMode: {
      defaultMode: 'light',
      disableSwitch: true,
      respectPrefersColorScheme: false,
    },
    navbar: {
      title: 'Outline Help Center',
      logo: {
        alt: 'Outline Logo',
        src: 'images/outline-logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'helpSidebar',
          label: 'Help',
          position: 'left',
        },
        {
          type: 'search',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Product Info',
          items: [
            {
              label: 'Download Outline',
              href: 'https://getoutline.org/',
            },
            {
              label: 'Terms of Service',
              href: 'https://s3.amazonaws.com/outline-vpn/static_downloads/Outline-Terms-of-Service.html',
            },
            {
              label: 'Data Collection Policy',
              href: 'https://support.getoutline.org/about/data-collection',
            },
          ],
        },
        {
          title: 'Get Help',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/OutlineFoundation/?q=outline',
            },
            {
              label: 'Reddit',
              href: 'https://www.reddit.com/r/outlinevpn/',
            },
            {
              label: 'Developer Docs',
              href: 'https://developer.getoutline.org/',
            },
          ],
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'yaml'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
