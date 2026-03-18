---
title: Sådan fungerer Outline
sidebar_label: Sådan fungerer Outline
---

**Serverinstallation**

 ​Selvom installationen af Outline kan virke simpel, foregår der faktisk komplekse processer bag kulisserne, når serveren installeres. Når Outline installeres, køres der et installationsscript, der udfører følgende trin:

- Den stabile version af Shadowbox-imagefilen hentes og importeres ved hjælp af Docker. Billedet hostes på [Quay.io](https://quay.io/) i [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Dette billede indeholder Outline-serveren og Management API, som senere bruges af Outline Server Management-programmet til at oprette og fjerne adgangsnøgler, tilvælge/fravælge rapportering af anonyme metrics osv.
- [Watchtower](https://github.com/v2tec/watchtower) installeres og konfigureres til at søge efter opdateringer af imagefilen en gang i timen, hvilket er med til at sikre, at alle Outline-servere er konstant opdateret med de nyeste forbedringer af funktioner og sikkerhed.
- En webserver, der bruges til at få adgang til Management API'en, startes på en tilfældig port på en hemmelig og tilfældig sti.
- Der oprettes et [selvunderskrevet SSL-certifikat](https://en.wikipedia.org/wiki/Self-signed_certificate), så administrationen af Outline-serveren kan krypteres ved hjælp af TLS, selvom den ikke har et domænenavn. Der genereres også et unikt fingeraftryk af dette certifikat, som gemmes i programmet Outline Manager for at hjælpe med at forhindre mellemmandsangreb.

Outline-installationen skal ikke konfigureres, efter den er udført.

**Serversikkerhed**

 Outline-softwaren er open source, hvilket betyder, at alle kan se koden og forbedre den, hvis der findes sikkerhedsbrister. Vores kode hostes på [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Desuden opdateres alle installerede Outline-servere automatisk, når der udgives en ny version, hvilket sikrer, at ingen Outline-servere kører med gamle versioner af softwaren.

 Med henblik på at administrere adgangsnøglerne på serveren kommunikerer programmet Outline Manager med en administrationstjeneste på Outline-serveren. Administrationstjenesten kører på en tilfældig port og på en hemmelig og unik sti. Selve administrationstjenesten kan modstå sondering, da den ikke reagerer på forespørgsler, medmindre den korrekte hemmelige sti er angivet. Al kommunikation til administrationstjenesten er desuden krypteret med et [selvunderskrevet SSL-certifikat](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Der gemmes ikke logfiler på Outline-serveren, så selv hvis den bliver kompromitteret, er der ingen brugerdata at afsløre. Få flere oplysninger [her](https://support.getoutline.org/s/article/Security-and-privacy). Outline blev auditeret af [Radically Open Security](https://radicallyopensecurity.com/) og [Cure53](https://cure53.de/) i 2018. Se rapporterne [her](https://support.getoutline.org/s/article/Security-and-privacy).

**Håndtering af UDP-trafik**

 Outline kan fungere som et VPN for hele systemet, hvilket betyder, at al UDP-trafik føres gennem Outline-serveren.

**DNS-trafik**

Outline udfører alle DNS-opslag via Outline-serveren og beskytter dem ved hjælp af den samme kryptering, der anvendes til al anden netværksaktivitet. Dine DNS-forespørgsler går gennem Outline-serveren til Dyn Internet Guide, OpenDNS, Cloudflare DNS eller Quad9 DNS. Outline logfører aldrig dine DNS-opslag.
