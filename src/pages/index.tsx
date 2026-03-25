import React, {useCallback} from 'react';
import Layout from '@theme/Layout';
import Translate from '@docusaurus/Translate';
import Link from '@docusaurus/Link';

function BrowseTopics() {
  const cards = [
    {
      image: '/images/landing-guides.png',
      titleId: 'homepage.about.title',
      title: 'About Outline',
      descriptionId: 'homepage.about.description',
      description: 'Learn how Outline works, its security model, and more.',
      buttonId: 'homepage.about.button',
      button: 'Learn more',
      to: '/about/how-outline-works',
    },
    {
      image: '/images/outline-client.svg',
      titleId: 'homepage.client.title',
      title: 'Outline Client',
      descriptionId: 'homepage.client.description',
      description: 'Get started with connecting your device and troubleshooting.',
      buttonId: 'homepage.client.button',
      button: 'Get started',
      to: '/client/getting-started/system-requirements',
    },
    {
      image: '/images/outline-manager.svg',
      titleId: 'homepage.manager.title',
      title: 'Outline Manager',
      descriptionId: 'homepage.manager.description',
      description: 'Set up and manage your Outline server.',
      buttonId: 'homepage.manager.button',
      button: 'Set up a server',
      to: '/manager/server-setup/setup-server',
    },
    {
      image: '/images/landing-reference.png',
      titleId: 'homepage.developers.title',
      title: 'For Developers',
      descriptionId: 'homepage.developers.description',
      description: 'Integrate the Outline SDK into your application.',
      buttonId: 'homepage.developers.button',
      button: 'Explore the SDK',
      to: 'https://developer.getoutline.org/',
    },
  ];

  return (
    <section className="browse-topics">
      <h2 className="browse-topics__heading">
        <Translate id="homepage.browseTopics">Browse help topics</Translate>
      </h2>
      <div className="browse-topics__list">
        {cards.map((card) => (
          <div key={card.to} className="browse-topics__card">
            <img src={card.image} alt="" className="browse-topics__card-image" />
            <h3 className="browse-topics__card-title">
              <Translate id={card.titleId}>{card.title}</Translate>
            </h3>
            <p className="browse-topics__card-description">
              <Translate id={card.descriptionId}>{card.description}</Translate>
            </p>
            <Link className="browse-topics__card-button" to={card.to}>
              <Translate id={card.buttonId}>{card.button}</Translate>
            </Link>
          </div>
        ))}
      </div>
    </section>
  );
}

export default function Home(): React.ReactElement {
  const openSearch = useCallback(() => {
    const btn = document.querySelector('.DocSearch-Button') as HTMLButtonElement;
    if (btn) btn.click();
  }, []);

  return (
    <Layout title="Outline Help Center">
      <div className="hero-search">
        <div className="hero-search__content">
          <h1 className="hero-search__title">
            <Translate id="homepage.hero.title">How can we help you?</Translate>
          </h1>
          <button
            type="button"
            className="hero-search__input"
            onClick={openSearch}>
            <img src="/images/search-icon.svg" alt="" width="20" height="20" aria-hidden="true" />
            <span>
              <Translate id="homepage.hero.searchPlaceholder">
                Search for help...
              </Translate>
            </span>
          </button>
        </div>
      </div>
      <BrowseTopics />
    </Layout>
  );
}
