---
title: Automatisk konfiguration av Google Cloud
sidebar_label: Automatisk konfiguration av Google Cloud
---

## Översikt

Outline Manager innehåller en funktion som gör att du automatiskt kan konfigurera Outline-servern på en server som körs på Google Cloud. Om du väljer att använda den här funktionen ber Outline Manager dig att logga in med ditt Google-konto, vilket ger vissa[OAuth](https://developers.google.com/identity/protocols/oauth2)-behörigheter för din lokala installation av Outline Manager, så att du kan konfigurera ditt Google Cloud-konto.

 Om du inte vill tillhandahålla dessa behörigheter kan du följa anvisningarna för avancerad konfigurering i Outline Manager och köra Outline på Google Cloud Platform.

## Behörigheter beviljade

Outline Manager kräver följande behörigheter från ditt Google-konto för att kunna tillhandahålla automatisk konfigurering.

## Google Cloud Platform

- Visa och hantera dina resurser i Google Compute Engine
- Visa din data för Google Cloud-tjänster och se e-postadressen för ditt Google-konto

## Grundläggande kontoinformation

- Se den primära e-postadressen för ditt Google-konto
- Koppla dig till dina personliga uppgifter på Google

## Ytterligare åtkomst

- Hantera dina projekt på Cloud Platform
- Visa och hantera dina faktureringskonton på Google Cloud Platform
- Hantera konfigureringen av Googles API-tjänster

Genom dessa behörigheter kan vi stödja avancerade funktioner för att hantera dina Outline-servrar, så att du till exempel kan

- välja rätt faktureringskonto
- skapa ett nytt projekt för att organisera dina Outline-servrar
- lista tillgängliga datacenter
- skapa nya virtuella datorer för att köra Outline
- konfigurera den nya virtuella datorn med Outline.

## Återkalla behörigheter

Du kan återkalla åtkomsten till Google Cloud Platform för Outline Manager genom att besöka[Mitt konto](https://myaccount.google.com/permissions). Om du återkallar åtkomsten fortsätter alla servrar som du har skapat med den automatiska konfigurationen att köras, men visas inte längre i Outline Manager. Om du vill återställa åtkomsten till dem, så ansluter du bara till Google Cloud Platform igen genom att påbörja det automatiska konfigurationsflödet.

## Ordna Outline-projekt

Google Clouds automatiska konfiguration använder ett och samma[Google Cloud-projekt](https://cloud.google.com/resource-manager/docs/creating-managing-projects) för att organisera dina Outline-servrar. Projektet skapas under den första användningen av den automatiska konfigurationen, med ett projekt-id som börjar med ”Outline-” följt av en sträng med slumpmässiga tecken. Om du vill kan du välja ett annat projekt-id vid skapandet. Projektet får namnet ”Outline-servrar”.

## Faktureringskonto

För Google Cloud-projekt krävs ett länkat faktureringskonto som definierar betalningsuppgifter. Första gången du använder automatisk konfiguration i Google Cloud blir du ombedd att ange ett faktureringskonto som ska kopplas till dina Outline-servrar. Ibland slutar en server att köras eftersom det finns ett problem med faktureringskontot. I så fall loggar du in på[Google Cloud Console](https://console.cloud.google.com/getting-started), letar upp det Google Cloud-projekt som är kopplat till Outline (kallat ”Outline-servrar”) och uppdaterar faktureringsinställningarna.

## Förstöra servrar

Det enklaste sättet att förstöra dina servrar skapade med den automatiska konfigurationen är att göra det i Outline Manager. Om du vill förstöra servrarna själv kan du istället logga in på[Google Cloud Console](https://console.cloud.google.com/getting-started), leta upp projektet som skapades under den första konfigurationen (kallat ”Outline-servrar”) och antingen radera resurserna där eller stänga av projektet.
