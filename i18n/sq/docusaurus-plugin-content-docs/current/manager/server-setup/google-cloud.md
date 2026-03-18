---
title: Konfigurimi i automatizuar i Google Cloud
sidebar_label: Konfigurimi i automatizuar i Google Cloud
---

## Përmbledhja

Outline Manager përfshin një veçori që të lejon të konfigurosh automatikisht serverin e Outline në një server që ekzekutohet në Google Cloud. Nëse zgjedh të përdorësh këtë veçori, Outline Manager do të të kërkojë të identifikohesh me "Llogarinë tënde të Google", e cila do të japë leje të caktuara të [OAuth](https://developers.google.com/identity/protocols/oauth2) për instalimin tënd lokal të Outline Manager për qëllimet e konfigurimit të llogarisë sate të Google Cloud.

 Nëse nuk dëshiron t'i japësh këto leje, mund të ndjekësh udhëzimet për konfigurimin e përparuar në Outline Manager për ta ekzekutuar Outline në Google Cloud Platform.

## Lejet e dhëna

Për të ofruar konfigurimin e automatizuar, Outline Manager kërkon lejet e mëposhtme nga "Llogaria jote e Google".

## Google Cloud Platform

- Të shikojë dhe të menaxhojë burimet e tua të Google Compute Engine
- Të shikojë të dhënat e tua në shërbimet e Google Cloud dhe të shikojë adresën e email-it të "Llogarisë sate të Google"

## Informacionet bazë të llogarisë

- Të shikojë adresën tënde kryesore të email-it të "Llogarisë së Google"
- Të të lidhë ty me informacionet e tua personale në Google

## Qasja shtesë

- Të menaxhojë projektet e tua të Cloud Platform
- Të shikojë dhe të menaxhojë llogaritë e tua të faturimit të Google Cloud Platform
- Të menaxhojë konfigurimin e shërbimit të API-së së Google

Këto leje na lejojnë të mbështesim funksionalitete të përparuara për menaxhimin e serverëve të tu të Outline, duke përfshirë:

- Të lejojmë që të zgjedhësh llogarinë e saktë të faturimit
- Të krijosh një projekt të ri për të organizuar serverët e tu të Outline
- Të listosh qendrat e disponueshme të të dhënave
- Të krijosh pajisje të reja virtuale për ekzekutimin e Outline
- Të konfigurosh pajisjen e re virtuale me Outline

## Revokimi i lejeve

Mund ta revokosh qasjen te Google Cloud Platform për Outline Manager duke vizituar [Llogaria ime](https://myaccount.google.com/permissions). Nëse e revokon qasjen, çdo server që ke krijuar me konfigurimin e automatizuar do të vazhdojë të ekzekutohet, por nuk do të shfaqet më në Outline Manager. Për të restauruar qasjen tek ato, thjesht rilidhe Google Cloud Platform duke nisur rrjedhën e konfigurimit të automatizuar.

## Organizimi i projektit të Outline

Konfigurimi i automatizuar i Google Cloud përdor [një projekt të vetëm të Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) për të organizuar serverët e tu të Outline. Projekti krijohet gjatë përdorimit të parë të konfigurimit të automatizuar me një ID të sugjeruar projekti që fillon me “Outline-” të ndjekur nga një varg karakteresh të rastësishme. Mund të zgjedhësh një ID tjetër projekti në momentin e krijimit nëse preferon. Projekti do të emërtohet si “Serverët e Outline”.

## Llogaria e faturimit

Projektet e Google Cloud kërkojnë një "llogari të lidhur faturimi" që përcakton informacionet e pagesës. Kur përdor për herë të parë konfigurimin e automatizuar të Google Cloud, do të të kërkohet të japësh një llogari faturimi për ta lidhur me serverët e tu të Outline. Ndonjëherë, një server do të ndalojë së funksionuari sepse ka një problem me llogarinë e faturimit. Në këtë rast, duhet të identifikohesh në [Google Cloud Console](https://console.cloud.google.com/getting-started), të lokalizosh projektin e Google Cloud të lidhur me Outline (me emrin “Serverët e Outline”) dhe të përditësosh cilësimet e faturimit.

## Shkatërrimi i serverëve

Nëse dëshiron të shkatërrosh serverët e krijuar duke përdorur konfigurimin e automatizuar, mënyra më e lehtë është ta bësh këtë nga brenda në Outline Manager. Sidoqoftë, nëse dëshiron t'i shkatërrosh vetë serverët, mund të identifikohesh në [Google Cloud Console](https://console.cloud.google.com/getting-started), të gjesh projektin që është krijuar gjatë konfigurimit fillestar (me emrin “Serverët e Outline”) dhe t'i fshish burimet aty ose ta mbyllësh projektin.
