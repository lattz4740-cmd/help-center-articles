---
title: Sikkerhet og personvern ved bruk av Outline
sidebar_label: Sikkerhet og personvern ved bruk av Outline
---

Sikkerhet og personvern ved bruk av Outline

## Slik beskytter Outline kommunikasjonen din på nettet

Internettrafikk er mest utsatt for overvåking mens den går over det lokale eller nasjonale nettverket.

Outline bidrar til å holde kommunikasjonen din privat ved å kryptere internettrafikken din mens den går over det nasjonale nettverket, og hele veien frem til Outline-tjeneren. Når trafikken er kryptert med Outline, kan ikke uvedkommende på nettverket dekryptere den og se hvilke nettsteder du besøker, eller hvilken informasjon som blir overført.

Med Outline kan det også være mulig å få tilgang til sikre ende-til-ende-kommunikasjonsverktøy som kanskje ikke er tilgjengelige i landet ditt.

## Krypteringsstandarder

Outline krypterer kommunikasjon mellom enheten din og Outline-tjeneren med chifferet AEAD 256-biters Chacha2020 IETF Poly 1305. AEAD-chiffere sørger for konfidensialitet, integritet og autentisitet, og de fungerer ypperlig på nyere maskinvare.

## Sikkerhetsrevisjoner

I 2018 ble Outline revidert av Radically Open Security og Cure53, to uavhengige leverandører av cybersikkerhet som reviderer programvare i henhold til de nyeste sikkerhetsstandardene. Radically Open Security utførte enda en revisjon i 2022, og Cure53 utførte en revisjon av Outline SDK i 2024. Du kan lese rapportene her:

- [Radically Open Security Penetration Test Report (mars 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (desember 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (desember 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (januar 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonyme verdier og logger

Outline sporer båndbredden som brukes, som «bytes transferred» (overførte byter) for hver tilgangsnøkkel. Med denne informasjonen kan administratorer av Outline-tjenere bestemme om de trenger å skaffe mer båndbredde fra nettskyleverandøren sin. De kan imidlertid ikke se den faktiske informasjonen som er sendt via Outline-tjeneren.

Finn ut mer om [innsamling av data og informasjon](/about/data-collection) i Outline.

---

## Vanlige spørsmål om sikkerhet og personvern

## Kan Outline gjøre meg anonym på nettet?

Nei, Outline er ikke et anonymiseringsverktøy. Outline ivaretar personvernet ditt og beskytter deg mot innsyn fra uvedkommende.

Outline gir deg ikke fullstendig anonymitet på nettstedene du besøker, da nettstedene fortsatt kan identifisere deg når du logger på, eventuelt via teknikker som nettleser-fingeravtrykk. Når det gjelder mobilapper, har de fleste moderne smarttelefoner API-er som gjør det mulig for installerte apper å innhente posisjonen din uavhengig av proxy-tjeneren din, da de kan bruke den innebygde GPS-en.

VPN-nettverk er generelt svært sikre og gir spesielt god beskyttelse mot internettovervåking, men det er likevel aldri helt risikofritt å være på nettet. Selv om du bruker et VPN, kan en nettleverandør finne IP-adressen til Outline-tjeneren din hvis vedkommende allerede kjenner identiteten din og også kan observere nettverkstrafikken din. Denne informasjonen kan brukes til å blokkere tilgangen til tjeneren eller overvåke den for å få innsikt i bruksmønstrene dine, og kanskje også den omtrentlige posisjonen din.

## Er det mulig å se om jeg bruker Outline?

Kanskje. Sannsynligvis kan plattformene og tjenestene du bruker, registrere at tilkoblingen din kommer fra en nettskytjener. De kan i noen tilfeller slutte seg til at du bruker VPN, men de kan ikke se innholdet i internettrafikken din.

## Kan Outline beskytte meg mot alle mulige cybertrusler?

Nei. Det finnes ikke ett enkelt verktøy som kan beskytte deg mot alle mulige cybertrusler. Outline gir deg tilgang til det åpne internettet og sørger for bedre personvern ved å kryptere trafikken din, men vi anbefaler at du tar andre forholdsregler i tillegg for å beskytte deg mot andre typer angrep, som for eksempel skadelig programvare og nettfisking.

Søk råd hos eksperter på cybersikkerhet i organisasjonen din hvis du vil ha bedre beskyttelse på nettet. Du kan eventuelt få personlig veiledning fra ledende sikkerhetseksperter på nettstedet [Security Planner](https://securityplanner.org/). Formålet med dette nettstedet er å vise deg hvordan du velger de sikkerhetsverktøyene som passer best for deg.

Du kan også ta en titt på de andre cybersikkerhetsproduktene fra [Jigsaw](https://jigsaw.google.com/), blant annet [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) og [Passordvarsel](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Er det lovlig å bruke VPN?

Sjekk lokale lover og regler, i tillegg til vilkårene for bruk av nettskyleverandøren du planlegger å bruke, før du begynner å bruke Outline eller appen.
