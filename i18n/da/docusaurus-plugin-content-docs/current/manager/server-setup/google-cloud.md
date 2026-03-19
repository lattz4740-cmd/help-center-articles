---
title: Automatisk konfiguration af Google Cloud
sidebar_label: Automatisk konfiguration af Google Cloud
---

## Oversigt

Outline Manager har en funktion, der giver dig mulighed for automatisk at konfigurere Outline-server på en server, der kører på Google Cloud. Hvis du vælger at bruge denne funktion, beder Outline Manager dig om at logge ind med din Google-konto, som giver visse [OAuth-tilladelser](https://developers.google.com/identity/protocols/oauth2) til din lokale installation af Outline Manager med det formål at konfigurere din Google Cloud-konto.

 Hvis du ikke vil give disse tilladelser, kan du følge den avancerede konfigurationsvejledning i Outline Manager for at køre Outline på Google Cloud Platform.

## Tilladelser, der skal gives

Outline Manager kræver følgende tilladelser fra din Google-konto for at foretage automatisk konfiguration.

## Google Cloud Platform

- Se og administrere dine ressourcer i Google Compute Engine
- Se dine data i Google Cloud-tjenester og se mailadressen for din Google-konto

## Grundlæggende kontooplysninger

- Se den primære mailadresse på din Google-konto
- Knytte dig til dine personlige oplysninger på Google

## Yderligere adgang

- Administrere dine Cloud Platform-projekter
- Se og administrere dine faktureringskonti på Google Cloud Platform
- Administrere din Google API-tjenestekonfiguration

Disse tilladelser giver os mulighed for at understøtte avanceret funktionalitet til administration af dine Outline-servere, herunder:

- Give dig mulighed for at vælge den korrekte faktureringskonto
- Oprette et nyt projekt for at organisere dine Outline-servere
- Angive tilgængelige datacentre
- Oprette nye virtuelle maskiner til kørsel af Outline
- Konfigurere den nye virtuelle maskine med Outline

## Tilbagekaldelse af tilladelser

Du kan tilbagekalde adgangen til Google Cloud Platform for Outline Manager ved at gå til [Min konto](https://myaccount.google.com/permissions). Hvis du tilbagekalder adgangen, kører alle servere, du har oprettet med den automatiske konfiguration, stadig, men de vises ikke længere i Outline Manager. Hvis du vil genoprette adgangen til dem, skal du blot genoprette forbindelsen til Google Cloud Platform ved at påbegynde den automatiske konfigurationsproces.

## Organisation af Outline-projekt

Den automatiske konfiguration af Google Cloud bruger et enkelt [Google Cloud-projekt](https://cloud.google.com/resource-manager/docs/creating-managing-projects) til at organisere dine Outline-servere. Projektet oprettes i forbindelse med den første brug af den automatiske konfiguration med et foreslået projekt-id, der starter med "Outline" efterfulgt af en streng med tilfældige tegn. Du kan vælge et andet projekt-id ved oprettelsen, hvis du foretrækker det. Projektet får navnet "Outline-servere".

## Faktureringskonto

Google Cloud-projekter kræver en tilknyttet "faktureringskonto", der definerer betalingsoplysninger. Når du bruger automatisk konfiguration af Google Cloud, bliver du bedt om at angive en faktureringskonto, der skal tilknyttes dine Outline-servere. Nogle gange stopper en server med at køre, fordi der er et problem med faktureringskontoen. I så fald skal du logge ind på [Google Cloud Console](https://console.cloud.google.com/getting-started), finde det Google Cloud-projekt, der er knyttet til Outline (kaldet "Outline-servere"), og opdatere faktureringsindstillingerne.

## Destruktion af servere

Hvis du vil destruere dine servere, der er oprettet ved hjælp af den automatiske konfiguration, er det nemmest at gøre det i Outline Manager. Hvis du selv vil destruere serverne, kan du logge ind på [Google Cloud Console](https://console.cloud.google.com/getting-started), finde det projekt, der blev oprettet under den indledende konfiguration (kaldet "Outline-servere"), og enten slette ressourcerne der eller lukke projektet.
