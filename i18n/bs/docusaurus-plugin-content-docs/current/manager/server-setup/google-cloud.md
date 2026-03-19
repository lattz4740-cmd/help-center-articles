---
title: Automatsko postavljanje na Google Cloudu
sidebar_label: Automatsko postavljanje na Google Cloudu
---

## Pregled

Outline Manager uključuje funkciju koja vam omogućava da automatski konfigurirate Outline server na serveru koji se pokreće na Google Cloudu. Ako odaberete da koristite ovu funkciju, Outline Manager će od vas tražiti da se prijavite pomoću Google računa, koji će dati određena [OAuth](https://developers.google.com/identity/protocols/oauth2) odobrenja lokalnoj instalaciji Outline Managera u svrhu konfiguriranja Google Cloud računa.

 Ako ne želite dati ova odobrenja, možete slijediti uputstva za napredno postavljanje u Outline Manageru da pokrenete Outline na Google Cloud Platformu.

## Dodijeljena odobrenja

Outline Manager zahtijeva sljedeća odobrenja s Google računa za pružanje automatskog postavljanja.

## Google Cloud Platform

- Pregled vaših izvora Google Compute Enginea i upravljanje njima
- Pregled vaših podataka na svim Google Cloud uslugama i pregled adrese e-pošte Google računa

## Osnovne informacije o računu

- Pregled vaše primarne adrese e-pošte Google računa
- Povezivanje vas i vaših ličnih informacija na Googleu

## Dodatni pristup

- Upravljanje projektima na Cloud Platformu
- Pregled vaših računa za naplatu na Google Cloud Platformu i upravljanje njima
- Upravljanje konfiguracijom usluga Google API-ja

Ova odobrenja nam omogućavaju da podržavamo napredne funkcije za upravljanje Outline serverima, uključujući:

- omogućavanje da odaberete tačan račun za naplatu
- kreiranje novog projekta za organizaciju vaših Outline servera
- navođenje dostupnih centara za podatke
- kreiranje novih virtuelnih mašina za pokretanje Outlinea
- konfiguraciju nove virtuelne mašine uz Outline

## Opoziv odobrenja

Možete opozvati pristup Outline Managera Google Cloud Platformu u opciji [Moj račun](https://myaccount.google.com/permissions). Ako opozovete pristup, serveri koje ste kreirali pomoću automatskog postavljanja će nastaviti s radom, ali se neće više pojavljivati u Outline Manageru. Ako im želite vratiti pristup, jednostavno ponovo povežite Google Cloud Platform pokretanjem toka automatskog postavljanja.

## Organizacija Outline projekta

Automatsko postavljanje Google Clouda koristi jedan [Google Cloud projekat](https://cloud.google.com/resource-manager/docs/creating-managing-projects) za organizaciju vaših Outline servera. Taj projekat se kreira tokom prvog korištenja automatskog postavljanja uz predloženi ID projekta koji počinje na "Outline-" nakon čega slijedi niz nasumičnih znakova. Ako želite, prilikom kreiranja možete odabrati i drugi ID projekta. Naziv projekta će biti "Outline serveri".

## Račun za naplatu

Za Google Cloud projekte neophodan je povezani "račun za naplatu" na kojem se navode podaci o plaćanju. Prilikom prvog korištenja automatskog postavljanja Google Clouda, od vas će se tražiti da navedete račun za naplatu koji će se povezati s Outline serverima. Ponekad će doći do prekida rada servera zbog problema s računom za naplatu. U tom slučaju, prijavite se na [konzolu Google Cloud](https://console.cloud.google.com/getting-started), pronađite Google Cloud projekat povezan s Outlineom (pod nazivom "Outline serveri") i ažurirajte postavke naplate.

## Eliminacija servera

Ako želite eliminirati servere koji su kreirani pomoću automatskog postavljanja, najjednostavnije je da to uradite iz Outline Managera. Međutim, ako želite sami eliminirati servere, možete se prijaviti na [konzolu Google Cloud](https://console.cloud.google.com/getting-started), pronaći projekat koji je kreiran tokom početnog postavljanja (pod nazivom "Outline serveri") i izbrisati izvore u njemu ili isključiti projekat.
