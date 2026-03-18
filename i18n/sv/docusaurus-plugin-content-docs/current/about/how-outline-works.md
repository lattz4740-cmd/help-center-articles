---
title: Så här fungerar Outline
sidebar_label: Så här fungerar Outline
---

**Serverinstallation**

 ​Även om det kan verka enkelt att installera Outline sker flera komplexa steg bakom kulisserna när servern installeras. När Outline installeras kör ett installationsskript följande steg:

- Den stabila versionen av Shadowbox-avbildningen hämtas och importeras med hjälp av Docker. Bilden finns på [Quay.io](https://quay.io/), i [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Bilden innehåller Outline-servern och Management API som senare används av Outline Server Management-appen för att skapa och ta bort åtkomstnycklar, välja att rapportera anonyma mätvärden eller inte osv.
- [Watchtower](https://github.com/v2tec/watchtower) installeras och konfigureras för att söka efter uppdateringar av avbildningen varje timme. På så sätt är alla Outline-servrar alltid uppdaterade med de senaste funktionerna och säkerhetsförbättringarna.
- En webbserver som används för åtkomst till Management-API:et startas på en slumpmässig port på en hemlig och slumpmässig sökväg.
- Ett [självsignerat SSL-certifikat](https://en.wikipedia.org/wiki/Self-signed_certificate) skapas så att hanteringen av Outline-servern kan krypteras med hjälp av TLS även om det inte finns ett domännamn. En unik signatur för det här certifikatet skapas också och lagras i Outline Manager-appen för att förhindra man-i-mitten-attacker.

Installationen av Outline behöver inte konfigureras efter installationen

**Serversäkerhet**

 Outline-mjukvaran har öppen källkod, vilket innebär att alla kan se koden och förbättra den om de upptäcker brister. Vår kod lagras på [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Dessutom uppdateras alla Outline-servrar automatiskt när en ny version lanseras, så att ingen Outline-server körs med tidigare programvaruversioner.

 I syfte att hantera åtkomstnycklar på servern interagerar Outline Manager-appen med en hanteringstjänst på Outline-servern. Hanteringstjänsten körs via en slumpmässig port och en hemlig och unik sökväg. Själva hanteringstjänsten är avläsningsskyddad eftersom den inte svarar på förfrågningar om inte den hemliga sökvägen anges. Slutligen krypteras all kommunikation med hanteringstjänsten med ett [självsignerat SSL-certifikat](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Dessutom lagras inga loggar på Outline-servern, så även om vi skulle utsättas för intrång skulle ingen data avslöjas. Läs mer [här](https://support.getoutline.org/s/article/Security-and-privacy). Outline granskades av [Radically Open Security](https://radicallyopensecurity.com/) och [Cure53](https://cure53.de/) under 2018. Läs rapporterna [här](https://support.getoutline.org/s/article/Security-and-privacy).

**Hantera UDP-trafik**

 Outline kan fungera som ett VPN för hela systemet, vilket innebär att UDP-trafiken körs via Outline-servern.

**DNS-trafik**

Outline gör DNS-uppslagningar via Outline-servern och skyddar dessa med samma kryptering som används för all annan nätverksaktivitet. Dina DNS-förfrågningar går via Outline-servern till Dyn Internet Guide, OpenDNS, Cloudflare DNS eller Quad9 DNS. Outline loggar aldrig DNS-uppslagningar.
