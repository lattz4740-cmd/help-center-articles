import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  aboutSidebar: [
    'about/how-outline-works',
    'about/terminology',
    'about/security-and-privacy',
    'about/feedback',
    'about/brand-usage',
    'about/access-resources-blocked',
    'about/getoutline-me-telegram',
  ],
  clientSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'client/getting-started/system-requirements',
        'client/getting-started/connecting-device',
        'client/getting-started/get-access-key',
        'client/getting-started/access-key-reuse',
        'client/getting-started/install-linux',
        'client/getting-started/available-languages',
      ],
    },
    {
      type: 'category',
      label: 'Troubleshooting',
      key: 'client-troubleshooting',
      items: [
        'client/troubleshooting/download-link',
        'client/troubleshooting/windows-install',
        'client/troubleshooting/access-key-issues',
        'client/troubleshooting/connection-issues',
        'client/troubleshooting/internet-access',
        'client/troubleshooting/firewall-errors',
      ],
    },
  ],
  managerSidebar: [
    {
      type: 'category',
      label: 'Server Setup',
      items: [
        'manager/server-setup/setup-server',
        'manager/server-setup/google-cloud',
        'manager/server-setup/cost',
        'manager/server-setup/multiple-servers',
        'manager/server-setup/setup-faqs',
        'manager/server-setup/available-languages',
      ],
    },
    {
      type: 'category',
      label: 'Server Management',
      items: [
        'manager/server-management/manage-access-keys',
        'manager/server-management/data-limits',
        'manager/server-management/reset-server-id',
        'manager/server-management/change-location',
        'manager/server-management/update-software',
        'manager/server-management/delete-server',
      ],
    },
    {
      type: 'category',
      label: 'Troubleshooting',
      key: 'manager-troubleshooting',
      items: [
        'manager/troubleshooting/manager-download',
        'manager/troubleshooting/windows-install',
      ],
    },
  ],
};

export default sidebars;
