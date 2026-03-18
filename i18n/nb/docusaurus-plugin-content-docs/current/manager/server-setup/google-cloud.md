---
title: Automatisk konfigurering av Google Cloud
sidebar_label: Automatisk konfigurering av Google Cloud
---

## Oversikt

Outline-administrator inneholder en funksjon du kan bruke til å konfigurere Outline-tjeneren automatisk på tjenere som kjører i Google Cloud. Hvis du velger å bruke denne funksjonen, ser du en forespørsel i Outline-administrator om å logge på med Google-kontoen din, noe som betyr at visse [OAuth](https://developers.google.com/identity/protocols/oauth2)-tillatelser blir tildelt den lokale installasjonen din av Outline-administrator, med det formålet å konfigurere Google Cloud-kontoen din.

 Hvis du ikke vil gi disse tillatelsene, kan du følge veiledningen om avansert konfigurering i Outline-administrator for å kjøre Outline på Google Cloud Platform.

## Tildelte tillatelser

For å kunne utføre automatisk konfigurering trenger Outline-administrator følgende tillatelser fra Google-kontoen din.

## Google Cloud Platform

- Se og administrer Google Compute Engine-ressurser
- se dataene dine i alle Google Cloud-tjenester samt e-postadressen for Google-kontoen din

## Grunnleggende kontoinformasjon

- Se den primære e-postadressen for Google-kontoen din
- knytte deg til personopplysninger på Google

## Annen tilgang

- Administrer Cloud Platform-prosjektene dine
- Se og administrer faktureringskontoene dine for Google Cloud Platform
- administrere konfigurering av Google API-tjenestene dine

Med disse tillatelsene kan vi støtte avansert funksjonalitet for administrering av Outline-tjenerne dine, inkludert følgende:

- gi deg mulighet til å velge riktig faktureringskonto
- opprette nye prosjekter for å organisere Outline-tjenerne dine
- generere lister over tilgjengelige datasentre
- opprette nye virtuelle maskiner for kjøring av Outline
- konfigurere den nye virtuelle maskinen med Outline

## Oppheving av tillatelser

Du kan oppheve tilgangen til Google Cloud Platform for Outline-administrator ved å gå til [kontooversikten din](https://myaccount.google.com/permissions). Hvis du opphever tilgangen, kommer eventuelle tjenere du har opprettet med den automatiske konfigureringen, til å fortsette å kjøre, men de vises ikke lenger i Outline-administrator. For å gjenopprette tilgangen kan du koble til Google Cloud Platform på nytt ved å starte flyten for automatisk konfigurering.

## Organisering av Outline-prosjekter

Ved automatisk konfigurering av Google Cloud brukes ett enkelt [Google Cloud-prosjekt](https://cloud.google.com/resource-manager/docs/creating-managing-projects) til å organisere Outline-tjenerne dine. Prosjektet opprettes den første gangen du bruker den automatiske konfigureringen, med en foreslått prosjekt-ID som begynner med «Outline-», etterfulgt av en streng med tilfeldige tegn. Hvis du vil, kan du velge en annen prosjekt-ID når prosjektet opprettes. Prosjektet får navnet «Outline-tjener».

## Faktureringskonto

Google Cloud-prosjekter krever en tilknyttet «faktureringskonto» med betalingsopplysninger. Den første gangen du bruker automatisk konfigurering for Google Cloud, blir du bedt om å oppgi en faktureringskonto som skal tilknyttes Outline-tjenerne dine. Noen ganger kan tjenere slutte å kjøre på grunn av problemer med faktureringskontoen. I slike tilfeller må du logge på [Google Cloud Console](https://console.cloud.google.com/getting-started), finne Google Cloud-prosjektet som er tilknyttet Outline (kalt «Outline-tjener»), og oppdatere faktureringsinnstillingene.

## Tilintetgjøring av tjenere

Hvis du vil tilintetgjøre tjenerne du har opprettet ved hjelp av automatisk konfigurering, er det enklest å gjøre dette via Outline-administrator. Hvis du imidlertid vil tilintetgjøre tjenerne selv, kan du logge på[Google Cloud Console](https://console.cloud.google.com/getting-started), finne prosjektet som ble opprettet under den innledende konfigureringen (kalt «Outline-tjener»), og enten slette ressursene der eller avvikle prosjektet.
