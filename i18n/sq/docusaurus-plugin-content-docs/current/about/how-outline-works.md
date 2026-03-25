---
title: Si funksionon Outline
sidebar_label: Si funksionon Outline
---

## Instalimi i serverit
 ​Megjithëse instalimi i Outline mund të duket i thjeshtë, në fakt janë një grup hapash të ndërlikuar që kryhen në prapaskenë për instalimin e serverit tënd. Sa herë që instalohet Outline, një skript instalimi ekzekuton hapat e mëposhtëm:

- Versioni i qëndrueshëm i imazhit të Shadowbox merret dhe importohet duke përdorur Docker. Imazhi strehohet në [Quay.io](https://quay.io/), në [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Ky imazh përfshin serverin e Outline dhe API-në e menaxhimit, të cilat përdoren më vonë nga aplikacioni Outline Server Management për të krijuar dhe për të hequr çelësat e qasjes, për të zgjedhur ose për t'u tërhequr nga raportimi i metrikave anonime etj.
- [Watchtower](https://github.com/v2tec/watchtower) instalohet dhe konfigurohet për të kontrolluar çdo orë për përditësime të imazhit, çka ndihmon për të siguruar që çdo server i Outline të jetë vazhdimisht i përditësuar me përmirësimet më të fundit të veçorive dhe të sigurisë.
- Një server uebi, i cili përdoret për qasjen tek API-ja e menaxhimit, niset në një portë të rastësishme në një shteg sekret dhe të rastësishëm.
- Krijohet një [certifikatë SSL me nënshkrim automatik](https://en.wikipedia.org/wiki/Self-signed_certificate), në mënyrë që menaxhimi i serverit të Outline të mund të enkriptohet duke përdorur protokollin TLS, pavarësisht se nuk ka një emër domeni. Një gjurmë gishti unike për këtë certifikatë krijohet dhe ruhet po ashtu në aplikacionin Outline Manager, duke ndihmuar në parandalimin e sulmeve MITM.

Instalimi i Outline nuk ka nevojë për konfigurim pas instalimit.

## Siguria e serverit
 Softueri i Outline është me burim të hapur, që do të thotë se çdo person mund ta shikojë kodin dhe ta përmirësojë atë nëse ka dobësi të zbuluara. Kodi ynë strehohet në [GitHub](https://github.com/search?q=org%3AOutline-Foundation+outline&unscoped_q=outline).

 Për më tepër, të gjithë serverët e instaluar të Outline përditësohen automatikisht sa herë që publikohet një version i ri, duke siguruar që asnjë server i Outline të mos lihet të ekzekutojë versionet e vjetra të softuerit.

 Për të menaxhuar çelësat e qasjes në server, aplikacioni Outline Manager ndërvepron me një shërbim menaxhimi në serverin e Outline. Shërbimi i menaxhimit ekzekutohet në një portë të rastësishme dhe në një shteg sekret dhe unik. Shërbimi i menaxhimit në vetvete është rezistent ndaj kontrolleve pasi nuk i përgjigjet kërkesave, përveçse nëse specifikohet shtegu përkatës sekret. Si përfundim, të gjitha komunikimet me shërbimin e menaxhimit janë të enkriptuara me një [certifikatë SSL me nënshkrim automatik](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Gjithashtu, serveri i Outline nuk ruan asnjë evidencë, kështu që nuk do të zbulohen të dhëna të përdoruesve edhe nëse ai komprometohet. Mëso më shumë [këtu](/about/security-and-privacy). Outline është audituar nga [Radically Open Security](https://radicallyopensecurity.com/) dhe [Cure53](https://cure53.de/) në vitin 2018. Shiko raportet [këtu](/about/security-and-privacy).

## Administrimi i trafikut të protokollit UDP
 Outline mund të veprojë si një rrjet VPN në të gjithë sistemin, që do të thotë se i gjithë trafiku i protokollit UDP kanalizohet nëpërmjet serverit të Outline.

## Trafiku i DNS-së
Outline i kryen të gjitha kërkimet e DNS-së nëpërmjet serverit të Outline dhe i mbron ato duke përdorur të njëjtin enkriptim që përdoret për të gjitha aktivitetet e tjera të rrjetit. Kërkesat e tua të DNS-së do të kalojnë nëpërmjet serverit të Outline te Dyn Internet Guide, OpenDNS, Cloudflare DNS ose Quad9 DNS. Outline nuk i regjistron asnjëherë kërkimet e tua të DNS-së.
