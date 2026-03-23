import React, {useCallback} from 'react';
import Layout from '@theme/Layout';
import Translate from '@docusaurus/Translate';

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
    </Layout>
  );
}
