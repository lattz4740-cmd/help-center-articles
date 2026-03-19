---
title: Automatsko postavljanje Google Clouda
sidebar_label: Automatsko postavljanje Google Clouda
---

## Pregled

Upravitelj Outlinea sadrži značajku koja vam omogućuje da automatski konfigurirate poslužitelj Outlinea na poslužitelju koji se pokreće na Google Cloudu. Ako odlučite upotrebljavati tu značajku, Upravitelj Outlinea tražit će da se prijavite svojim Google računom. Na taj će se način dodijeliti određena dopuštenja za [OAuth](https://developers.google.com/identity/protocols/oauth2) u vašoj lokalnoj instalaciji Upravitelja Outlinea radi konfiguracije Google Cloud računa.

 Ako ne želite dati ta dopuštenja, možete slijediti upute za napredno postavljanje u Upravitelju Outlinea da biste pokrenuli Outline na Google Cloud Platformi.

## Dodijeljena dopuštenja

Upravitelj Outlinea zahtijeva sljedeća dopuštenja na vašem Google računu radi omogućavanja automatskog postavljanja.

## Google Cloud Platform

- Prikaz resursa za Google Compute Engine i upravljanje njima
- Uvid u vaše podatke na uslugama Google Clouda i e-adresu vašeg Google računa

## Osnovni podaci o računu

- Pregled primarne e-adrese vašeg Google računa
- Vaše povezivanje s vašim osobnim podacima na Googleu

## Dodatni pristup

- Upravljanje projektima na Cloud Platformu
- Prikaz računa za naplatu za Google Cloud Platform i upravljanje njima
- Upravljanje konfiguracijom usluga Google API-ja

Ta nam dopuštenja omogućuju podršku za napredne funkcije za upravljanje poslužiteljima Outlinea, uključujući:

- mogućnost da odaberete odgovarajući račun za naplatu
- izradu novog projekta radi organiziranja poslužitelja Outlinea
- popis dostupnih podatkovnih centara
- izradu novih virtualnih uređaja za pokretanje Outlinea
- konfiguraciju novog virtualnog računala s Outlineom

## Opozivanje dopuštenja

Pristup Google Cloud Platformu za Upravitelj Outlinea možete opozvati u odjeljku [Moj račun](https://myaccount.google.com/permissions). Ako opozovete pristup, svi poslužitelji koje ste izradili uz automatsko postavljanje i dalje će se pokretati, ali više se neće prikazivati u Upravitelju Outlinea. Da biste vratili pristup, jednostavno se ponovno povežite s Google Cloud Platformom pokretanjem automatskog postavljanja.

## Organizacija projekta Outlinea

Za automatsko postavljanje na Google Cloudu upotrebljava se jedan [projekt Google Clouda](https://cloud.google.com/resource-manager/docs/creating-managing-projects) za organizaciju poslužitelja Outlinea. Projekt se izrađuje tijekom prve upotrebe automatskog postavljanja uz predloženi ID projekta koji počinje riječju Outline- i nizom nasumičnih znakova. Ako želite, pri izradi možete odabrati drugi ID projekta. Naziv projekta bit će Poslužitelji Outlinea.

## Račun za naplatu

Za projekte na Google Cloudu potreban je povezani račun za naplatu na kojem su definirani podaci o plaćanju. Kada prvi put upotrijebite automatsko postavljanje Google Clouda, morat ćete navesti račun za naplatu koji ćete povezati sa svojim poslužiteljima Outlinea. Ponekad će poslužitelj prestati raditi jer postoji problem s računom za naplatu. U tom se slučaju trebate prijaviti na [Google Cloud Console](https://console.cloud.google.com/getting-started), pronaći projekt Google Clouda povezan s Outlineom (naziva Poslužitelji Outlinea) i ažurirati postavke naplate.

## Uništavanje poslužitelja

Ako želite uništiti poslužitelje izrađene pomoću automatskog postavljanja, najjednostavnije je da to učinite putem Upravitelja Outlinea. Međutim, ako želite sami uništiti poslužitelje, možete se prijaviti na [Google Cloud Console](https://console.cloud.google.com/getting-started), pronaći projekt koji ste izradili tijekom početnog postavljanja (naziva Poslužitelji Outlinea) i izbrisati resurse ili isključiti projekt.
