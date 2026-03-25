---
title: Terminologie
sidebar_label: Terminologie
---

## Wat is een VPN?

Een Virtual Private Network (VPN) is een privéverbinding tussen je apparaten en een hostserver. Als je een VPN gebruikt, is je internetverkeer verborgen voor je provider.

Dit zijn een paar redenen om een VPN te gebruiken:

- Je gegevens beschermen als je een openbaar wifi-netwerk gebruikt.
- Je browsegegevens verborgen houden voor je provider en overheidsinstanties.
- Toegang krijgen tot ongecensureerde content van verschillende bronnen over de hele wereld.

## Hoe verschilt Outline van traditionele VPN's?

Internetproviders kunnen traditionele VPN's makkelijk detecteren en blokkeren door veelgebruikte beveiligingsprotocollen en/of patronen in de hoeveelheid verkeer in kaart te brengen. Outline is veerkrachtiger dan traditionele VPN's, omdat het is gemaakt met een protocol dat moeilijk te detecteren en dus moeilijker te blokkeren is. Outline weerstaat geraffineerde vormen van censuur, inclusief netwerkgebaseerde blokkeringen en IP-blokkeringen.

## Wat is een Outline-server?

Een Outline-server voert het VPN uit waar gebruikers verbinding mee maken.

Als je een nieuw netwerk maakt, kun je je eigen beveiligde server (als je die hebt) gebruiken als Outline-server of een cloudserviceprovider gebruiken, zoals:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Je stelt de server in via Outline Manager.

## Wat is een servicemanager? {#servicemanager}

Een servicemanager is de persoon die de Outline-server instelt en de toegangssleutels deelt met gebruikers. De servicemanager is meestal ook verantwoordelijk voor de kosten van het servergebruik.

## Wat is een toegangssleutel? {#accesskey}

Met een toegangssleutel heb je toegang tot een bestaande Outline-server en maak je verbinding met het VPN. Een [servicemanager](#servicemanager) geeft je een toegangssleutel. Je kunt ook zelf [een Outline-server instellen](/manager/server-setup/setup-server).

Zo ziet een toegangssleutel eruit (deze sleutel is een voorbeeld en werkt niet echt):

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Wat is Outline Manager?

Outline Manager is een desktop-app waarmee servicemanagers een Outline-server kunnen instellen, [toegangssleutels](#accesskey) kunnen maken en een datalimiet kunnen instellen voor het gebruik per sleutel. Download [hier](https://getoutline.org/get-started/#step-3) of [hier](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) de nieuwste versie van Outline Manager.

## Wat is Outline-client?

Outline-client is een app voor desktop en mobiel waarmee je verbinding kunt maken met een Outline-server en toegang krijgt tot het VPN met een toegangssleutel. Download [hier](https://getoutline.org/get-started/#step-3) of [hier](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) de nieuwste versie van Outline-client.

## Wat zijn datalimieten?

In Outline Manager kunnen servicemanagers een verzamellimiet van 30 dagen instellen voor toegangssleutels om overmatig gebruik te voorkomen en de kosten voorspelbaar te houden. Servicemanagers kunnen een standaardlimiet instellen die geldt voor elke sleutel en een andere limiet instellen voor individuele sleutels om de standaardlimiet te overschrijven. Nadat je een limiet instelt, wordt die meteen van kracht en wordt die uurlijks afgedwongen.

Als servicemanagers toestemming geven om statistieken te delen met Jigsaw, moeten ze het [Beleid voor gegevens verzamelen](https://getoutline.org/policies/data-collection) bekijken. Hierin staat hoe het gebruik van datalimieten wordt gemeld.
