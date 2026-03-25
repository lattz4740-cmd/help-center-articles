import Head from '@docusaurus/Head';
import {useEffect} from 'react';

const TARGET = 'https://getoutline.org/policies/data-collection';

export default function Redirect(): JSX.Element {
  useEffect(() => { window.location.replace(TARGET); }, []);
  return (
    <>
      <Head>
        <meta httpEquiv="refresh" content={`0; url=${TARGET}`} />
      </Head>
      <p>Redirecting to <a href={TARGET}>{TARGET}</a>…</p>
    </>
  );
}
