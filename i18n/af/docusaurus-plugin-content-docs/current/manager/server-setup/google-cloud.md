---
title: Google Cloud se geoutomatiseerde opstelling
sidebar_label: Google Cloud se geoutomatiseerde opstelling
---

## Oorsig

Outline Manager sluit ’n kenmerk in wat jou toelaat om outomaties ’n Outline-bediener op te stel op ’n bediener wat in die Google Cloud gebruik word. Indien jy kies om hierdie kenmerk te gebruik, sal Outline Manager jou vra om met jou Google-rekening aan te meld. Dit sal sekere [OAuth](https://developers.google.com/identity/protocols/oauth2)-toestemmings aan jou plaaslike installasie van Outline Manager verleen om jou Google Cloud-rekening op te stel.

 Indien jy nie hierdie toestemmings wil verskaf nie, kan jy die gevorderde installeringinstruksies in die Outline Manager volg om Outline op Google Cloud Platform te laat loop.

## Toestemmings gegee

Om ’n outomatiese opstelling te verskaf, het Outline Manager die volgende toestemmings van jou Google-rekening af nodig.

## Google Cloud Platform

- Bekyk en bestuur jou Google Compute Engine-hulpbronne
- Bekyk jou data in alle Google Cloud-dienste en sien die e-posadres van jou Google-rekening

## Basiese rekeninginligting

- Sien jou Google-rekening se primêre e-posadres
- Assosieer jou met jou persoonlike inligting op Google

## Bykomende toegang

- Bestuur jou Cloud Platform-projekte
- Bekyk en bestuur jou Google Cloud Platform-faktureringrekeninge
- Bestuur jou Google-API-diensopstelling

Hierdie toestemmings laat ons toe om gevorderde funksionaliteit te ondersteun vir die bestuur van jou Outline-bedieners, insluitend om:

- Jou in staat te stel om die korrekte faktureringrekening te kies
- ’n Nuwe projek te skep om jou Outline-bedieners te organiseer
- Alle beskikbare datasentrums te lys
- Nuwe, virtuele masjiene te skep om op Outline te werk
- Die nuwe virtuele masjien met Outline op te stel

## Herroep toestemmings

Jy kan [My rekening](https://myaccount.google.com/permissions) besoek om toegang tot Google Cloud Platform vir die Outline Manager te herroep. Indien jy toegang herroep, sal enige bedieners wat jy met die outomatiseerde opstelling geskep het, aanhou loop, maar sal nie in die Outline Manager verskyn nie. Om toegang tot hulle te herstel, kan jy eenvoudig weer aan Google Cloud Platform koppel deur die geoutomatiseerde opstelvloei te begin.

## Outline-projekorganisasie

Google Cloud se geoutomatiseerde opstelling gebruik ’n enkele [Google Cloud-projek](https://cloud.google.com/resource-manager/docs/creating-managing-projects) om jou Outline-bedieners te organiseer. Die projek word geskep gedurende die eerste keer wat die outomatisering-opstelling gebruik word, met ’n voorgestelde projek-ID wat begin met “Outline-” gevolg deur ’n string lukrake karakters. Jy kan ’n ander projek-ID kies wanneer die projek geskep word indien jy sou verkies. Die projek sal “Outline-bedieners” genoem wees.

## Faktureringrekening

Google Cloud-projekte benodig ’n gekoppelde “faktureringrekening” wat die betaalinligting definieer. Wanneer jy die eerste keer Google Wolk se geoutomatiseerde opstelling gebruik, moet jy ’n faktureringrekening verskaf wat met jou Outline-bedieners geassosieer sal word. Soms sal ’n bediener ophou loop omdat daar ’n probleem met die faktureringrekening is. In so ’n geval moet jy aanmeld by die [Google Cloud Console](https://console.cloud.google.com/getting-started), die Google Cloud Console opspoor wat met die projek in Outline (genaamd “Outline-bedieners”) geassosieer word, en die faktureringinstellings opdateer.

## Om bedieners uit te wis

Indien jy die bedieners wat met die outomatiseerde opstelling geskep is wil uitwis, is die maklikste manier om dit te doen deur Outline Manager te gebruik. Indien jy self hierdie bedieners wil vernietig, kan jy by die [Google Cloud Console](https://console.cloud.google.com/getting-started) aanmeld, ’n projek vind wat gedurende die oorspronklike opstelling geskep is (genaamd “Outline-bedieners”), en die hulpbronne daar uitvee óf die projek beëindig.
