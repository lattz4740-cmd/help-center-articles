---
title: Hoe Outline werkt
sidebar_label: Hoe Outline werkt
---

## Serverinstallatie

Hoewel de installatie van Outline eenvoudig lijkt, is de installatie van de server achter de schermen zeer complex.

Wanneer Outline wordt geïnstalleerd, voert een installatiescript de volgende stappen uit:

- De stabiele versie van de Shadowbox-image wordt opgehaald en geïmporteerd met Docker. De image wordt gehost op [Quay.io](https://quay.io/), op [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Deze image bevat de Outline-server en Management API, die later wordt gebruikt door de Server Management-app van Outline om toegangssleutels te maken en verwijderen, aan of af te melden voor het verzenden van anonieme statistieken enzovoort.
- [Watchtower](https://github.com/v2tec/watchtower) wordt geïnstalleerd en geconfigureerd om elk uur te controleren op image-updates, zodat elke Outline-server steeds de nieuwste functies en beveiligingsupdates bevat.
- Een webserver, die wordt gebruikt om toegang te krijgen tot de Management API, wordt gestart op een willekeurige poort met een geheim, willekeurig pad.
- Er wordt een [zelfondertekend SSL-certificaat](https://en.wikipedia.org/wiki/Self-signed_certificate) gemaakt, zodat het beheer van de Outline-server kan worden versleuteld met TLS, ook al is er geen domeinnaam. Er wordt ook een unieke vingerafdruk van dit certificaat gemaakt en opgeslagen in de Outline Manager-app, zodat MITM-aanvallen worden voorkomen.

Na de installatie hoeft Outline niet meer te worden geconfigureerd.

## Serverbeveiliging

De Outline-software is open source. Dit betekent dat iedereen de code kan zien en deze kan verbeteren als er kwetsbaarheden worden ontdekt. De code wordt gehost op [GitHub](https://github.com/search?q=org%3AOutline-Foundation+outline&unscoped_q=outline).

Daarnaast worden alle geïnstalleerde Outline-servers automatisch geüpdatet wanneer er een nieuwe versie wordt vrijgegeven. Zo worden er nooit oude versies van de software gebruikt op Outline-servers.

De Outline Manager-app communiceert met een beheerservice op de Outline-server om de toegangssleutels op de server te beheren. De beheerservice wordt uitgevoerd op een willekeurige poort, via een uniek, geheim pad. De beheerservice zelf is niet gevoelig voor probes, omdat deze alleen reageert op zoekopdrachten als het juiste geheime pad wordt opgegeven. Als laatste wordt alle communicatie met de beheerservice versleuteld via een [SSL](https://en.wikipedia.org/wiki/Self-signed_certificate) .

De Outline-server slaat geen logboeken op. Zelfs als de server wordt gehackt, worden er dus geen gebruikersgegevens vrijgegeven. Kijk [here](/about/security-and-privacy) voor meer informatie.

In 2018 is Outline gecontroleerd door [Radically Open Security](https://radicallyopensecurity.com/) en [Cure53](https://cure53.de/) . Bekijk de rapporten. [→](/about/security-and-privacy).

## UDP-verkeer

Outline kan worden gebruikt als systeembrede VPN. Dit betekent dat al het UDP-verkeer door de Outline-server wordt gestuurd.

## DNS-Traffic

In Outline erfolgen alle DNS-Lookups über den Outline-Server. Dabei wird dieselbe Verschlüsselung verwendet wie bei allen anderen Netzwerkaktivitäten. Alle Ihre DNS-Abfragen werden über den Outline-Server an den Dyn Internet Guide oder an OpenDNS weitergeleitet.

Ihre DNS-Lookups werden zu keiner Zeit von Outline protokolliert.
