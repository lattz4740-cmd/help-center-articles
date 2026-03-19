---
title: Innsamling av data og informasjon
sidebar_label: Innsamling av data og informasjon
---

Outline samler ikke inn personopplysninger med mindre du selv velger å oppgi dem. Outline samler heller ikke inn informasjon om nettstedene du besøker, eller hvem eller hva du kommuniserer med.

 Hvis du oppretter eller logger på en konto hos en tredjeparts nettskyleverandør via Outline-administratoren, innhenter ikke vi noen av opplysningene du gir til nettskyleverandøren, for eksempel e-postadresse, navn, faktureringsinformasjon eller betalingsopplysninger.

## Informasjon vi samler inn automatisk
 Vi samler inn to typer informasjon automatisk.

 1. 
IP-adressen til Outline-tjeneren innhentes av [Quay.io](https://quay.io/) og gjøres tilgjengelig for oss når tjeneren blir oppdatert automatisk med de nyeste sikkerhets- og funksjonsforbedringene. IP-adressen til tjeneren kan identifisere nettskyleverandøren samt byen der Outline-tjeneren er installert, men det oppgis ingen informasjon om hvem som kjører tjeneren eller hvem som bruker den.

 2. Teknisk informasjon som ikke er personlig identifiserende

 Hvis Outline krasjer eller et uopprettelig unntak inntreffer, eller hvis du sender tilbakemelding manuelt via Outline-appen, blir informasjonen nedenfor rapportert. Denne informasjonen blir kun brukt til å identifisere og løse stabilitets- eller ytelsesproblemer.

- Land
- Lokalitet
- Dato og klokkeslett for krasjet/unntaket, og opptil 100 tidligere hendelser, for eksempel det at en bruker har åpnet delen «About»
- Statistisk kompilerte unntaksmeldinger
- OS-navn og -versjon
- Telefonmodell (hvis aktuelt)
- Starttid for appen
- Nettleser
- Arkitektur
- Outline-versjon og delversjonsnummer

Denne informasjonen overføres via HTTPS til Sentry ([sentry.io](https://sentry.io/)), som er en tredjepartsleverandør av feilsporing basert på åpen kildekode. Sentry bruker en rekke ulike teknologier og tjenester som følger bransjestandarder, for å beskytte dataene dine mot uautorisert tilgang, avsløring, bruk og tap. Hvis du har spørsmål om retningslinjene til Sentry, kan du gå til [https://sentry.io/security/](https://sentry.io/security/) og [https://sentry.io/privacy/](https://sentry.io/privacy/) eller kontakte [security@sentry.io](mailto:security@sentry.io). Alle Outline-data som lagres av Sentry, er begrenset slik at kun medlemmer av Outline-teamet har tilgang til dem.

## Informasjon vi samler inn kun etter å ha innhentet samtykke
 Outline formidler følgende informasjon til Outline-teamet når vi har innhentet samtykke.

 1. Bruksverdier

 Hver Outline-tjener samler automatisk inn – for den siste timen og fordelt på tilgangsnøkler – antallet byte som overføres, hvor lang tid en bruker var koblet til serveren, opprinnelseslandene og de autonome systemene for legitimasjonen som brukes, og hvorvidt funksjoner er slått av eller på. Verken innholdet i kommunikasjonen eller personlig identifiserende metadata (f.eks. pålogginger, e-poster, enhets-ID-er osv.) blir logget. Alle beregninger knyttes til en tjener-ID. [Her](/manager/server-management/reset-server-id) finner du ut hvordan du endrer tjener-ID-en.

 Som standard deler ikke Outline-tjenerne disse verdiene med Outline-teamet. Hvis tjeneradministratoren uttrykkelig samtykker i å dele bruksverdier, blir denne informasjonen sendt på en sikker måte til Outline-teamet hver time. Etter 60 dager blir bruksverdiene aggregert på landsnivå. Tjeneradministratorer kan endre innstillingen for deling av bruksverdier når som helst ved å gå til Settings-menyen i Outline-administratoren.

 Vi setter pris på at du deler anonyme verdier angående tjenerbruken din med oss, da vi bruker dem til å måle brukstrender og lage et best mulig produkt.

 Hvis en tjeneradministrator for eksempel velger å dele bruksverdier med oss, kan vi motta informasjon som indikerer at en tjener med ID-en 12345 ble brukt i mer enn tre timer i går og overførte totalt 500 MB data fra tre nøkler som ble brukt i USA og Canada, med funksjonen for datagrenser slått på.

 2. Kommentarer og e-postadresse hvis du sender inn tilbakemeldinger

 Via appen for Outline-administrator og Outline-appen kan du sende tilbakemeldinger til teamet. Vi anbefaler at du ikke tar med personlig identifiserende informasjon, men det finnes et felt der du kan velge å skrive inn e-postadressen din hvis du ønsker å få svar fra teamet. Vi samler også automatisk inn noe grunnleggende informasjon, slik at vi kan tolke tilbakemeldingen din på riktig måte. Du finner mer informasjon om hvilke data vi samler inn i del 2 over, under «Informasjon vi samler inn automatisk». [Her](/about/security-and-privacy) finner du ut mer om retningslinjene for sikkerhet og personvern for Outline.

 Hvis du bruker en betaversjon av Outline-appen på Android, kan vi bruke Googles [Firebase](https://firebase.google.com/)-tjeneste til å samle inn feilsøkingsinformasjon som kan bidra til at vi kan oppdage problemer og gjøre Outline enda bedre. Du kan finne ut mer om retningslinjene for personvern og sikkerhet for Firebase ved å gå til nettstedet deres: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Hvis du ikke vil at Outline skal sende denne informasjonen gjennom Firebase, kan du bruke produksjonsversjonen av appen.
