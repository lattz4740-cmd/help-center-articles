---
title: Google Cloudi automaatne seadistus
sidebar_label: Google Cloudi automaatne seadistus
---

## Ülevaade

Outline Manager hõlmab funktsiooni, mis võimaldab teil Google Cloudis töötavas serveris automaatselt Outline'i serveri seadistada. Kui otsustate seda funktsiooni kasutada, palub Outline Manager teil oma Google'i kontoga sisse logida, mis annab teie Outline Manageri kohalikule eksemplarile teatud [OAuthi](https://developers.google.com/identity/protocols/oauth2) load, et teie Google Cloudi kontot seadistada.

 Kui te ei soovi neid lube anda, võite järgida Outline Manageris täpsemaid seadistusjuhiseid, et käitada Outline'i teenuses Google Cloud Platform.

## Antavad load

Automatiseeritud seadistuse pakkumiseks vajab Outline Manager teie Google'i kontolt järgmisi lube.

## Google Cloud Platform

- Teie Google Compute Engine'i ressursside vaatamine ja haldamine
- Google Cloudi teenustes teie andmete vaatamine ja teie Google'i konto e-posti aadressi vaatamine

## Konto põhiteave

- Teie peamise Google'i konto e-posti aadressi vaatamine
- Teie ja teie isiklike andmete seostamine Google'is

## Täiendav juurdepääs

- Cloud Platformi projektide haldamine
- Google Cloud Platformi arvelduskontode vaatamine ja haldamine
- Google API teenuse konfiguratsiooni haldamine

Need load võimaldavad meil toetada täpsemaid funktsioone teie Outline'i serverite haldamiseks, sealhulgas järgmisi.

- Õige arvelduskonto valimise võimaldamine
- Uue projekti loomine teie Outline'i serverite korraldamiseks
- Saadaolevate andmekeskuste loetlemine
- Uute virtuaalmasinate loomine Outline'i käitamiseks
- Uue virtuaalmasina seadistamine Outline'iga

## Lubade tühistamine

Võite tühistada Outline Manageri juurdepääsu Google Cloud Platformile, külastades jaotist [Minu konto](https://myaccount.google.com/permissions). Kui tühistate juurdepääsu, jätkavad teie automaatse seadistusega loodud serverid tööd, ent neid ei kuvata enam Outline Manageris. Nendele juurdepääsu taastamiseks looge lihtsalt uuesti ühendus Google Cloud Platformiga, käivitades automaatse seadistuse voo.

## Outline'i projekti korraldamine

Google Cloudi automaatne seadistus kasutab teie Outline'i serverite korraldamiseks üht [Google Cloudi projekti](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Projekt luuakse automaatse seadistuse esmakordsel kasutamisel soovitatava projekti ID-ga, mille alguses on „Outline-“ ja millele järgneb juhuslike tähemärkide jada. Soovi korral võite loomise ajal valida muu projekti ID. Projekti nimeks saab „Outline servers“.

## Arvelduskonto

Google Cloudi projektide jaoks on vaja lingitud arvelduskontot, mis määrab makseteabe. Kui kasutate Google Cloudi automaatset seadistust esimest korda, palutakse teil määrata arvelduskonto, mis seostatakse teie Outline'i serveritega. Mõnikord lakkab server töötamast seetõttu, et arvelduskontoga on probleeme. Sel juhul logige sisse [Google Cloud Console'i](https://console.cloud.google.com/getting-started), leidke Outline'iga seotud Google Cloudi projekt (nimega „Outline servers“) ja värskendage arveldusseadeid.

## Serverite hävitamine

Kui soovite automaatse seadistusega loodud serverid hävitada, on seda kõige lihtsam teha Outline Manageris. Kui aga soovite serverid ise hävitada, võite logida sisse [Google Cloud Console'i](https://console.cloud.google.com/getting-started), leida projekti, mis loodi algseadistuse ajal (nimega „Outline servers“), ja kustutada sealsed resssursid või sulgeda projekti.
