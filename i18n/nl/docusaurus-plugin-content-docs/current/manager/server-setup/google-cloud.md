---
title: Overzicht
sidebar_label: Overzicht
---

Outline Manager bevat een functie waarmee je Outline Server automatisch kunt instellen op een server die wordt uitgevoerd in Google Cloud. Als je ervoor kiest deze functie te gebruiken, vraagt Outline Manager je in te loggen met je Google-account. Daarmee krijg je bepaalde [OAuth](https://developers.google.com/identity/protocols/oauth2)-rechten voor de lokale installatie van Outline Manager om je Google Cloud-account in te stellen.

Als je deze rechten niet wilt geven, kun je de geavanceerde installatie-instructies volgen in Outline Manager om Outline uit te voeren via Google Cloud Platform.

## Toegewezen rechten

Outline Manager heeft de volgende rechten nodig in je Google-account voor automatische installatie.

## Google Cloud Platform

- Bronnen voor Google Compute Engine bekijken en beheren
- Je gegevens in Google Cloud-services bekijken en het e-mailadres van je Google-account zien

## Algemene accountgegevens

- Het primaire e-mailadres van je Google-account bekijken
- Je koppelen aan je persoonlijke informatie bij Google

## Aanvullende toegang

- Je Cloud Platform-projecten beheren
- Je Google Cloud Platform-factureringsaccounts bekijken en beheren
- De Google API-serviceconfiguratie beheren

Met deze rechten kunnen we je geavanceerde functies bieden om je Outline-servers te beheren, zoals:

- Je toestaan het juiste factureringsaccount te selecteren
- Een nieuw project maken om je Outline-servers te ordenen
- Beschikbare datacenters vermelden
- Nieuwe virtuele machines maken om Outline op uit te voeren
- Outline instellen op een nieuwe virtuele machine

## Rechten intrekken

Je kunt de toegang tot Google Cloud Platform voor Outline Manager intrekken via [Mijn account](https://myaccount.google.com/permissions). Als je de toegang intrekt, blijven servers die je hebt gemaakt met de automatische installatie actief, maar worden ze niet meer weergegeven in Outline Manager. Je kunt de toegang herstellen door opnieuw te koppelen met Google Cloud Platform. Dit doe je door het automatische instelproces te starten.

## Outline-projectorganisatie

De automatische installatie via Google Cloud gebruikt één [Google Cloud-project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) om je Outline-servers te ordenen. Het project wordt gemaakt als je de automatische installatie voor het eerst gebruikt en heeft een voorgestelde project-ID die begint met 'Outline-', gevolgd door een reeks willekeurige tekens. Je kunt ook een andere project-ID kiezen als je het project maakt. Het project heet 'Outline servers'.

## Factureringsaccount

Voor Google Cloud-projecten is een gekoppeld factureringsaccount vereist waarin je betalingsgegevens staan. Als je de automatische installatie van Google Cloud voor het eerst gebruikt, wordt je gevraagd een factureringsaccount op te geven dat kan worden gekoppeld aan je Outline-servers. Soms werkt een server niet meer omdat er een probleem is met het factureringsaccount. Je moet dan inloggen bij de [Google Cloud Console](https://console.cloud.google.com/getting-started), het Google Cloud-project zoeken dat is gekoppeld aan Outline (met de naam 'Outline servers') en de factureringsinstellingen updaten.

## Servers vernietigen

Als je servers wilt vernietigen die zijn gemaakt met de automatische installatie, kun je dit het makkelijkst doen in Outline Manager. Als je de servers liever zelf wilt vernietigen, kun je inloggen bij de [Google Cloud Console](https://console.cloud.google.com/getting-started), het project zoeken dat is gemaakt tijdens de eerste installatie (met de naam 'Outline servers') en daar de resources verwijderen of het project beëindigen.
