---
title: Hoe Outline werk
sidebar_label: Hoe Outline werk
---

## Bedienerinstallering
 ​Hoewel Outline-installering eenvoudig lyk, is daar ’n komplekse stel stappe wat agter die skerms plaasvind om jou bediener te installeer. Wanneer Outline geïnstalleer word, loop ’n installeringskrip deur die volgende stappe:

- Die stabiele weergawe van die Shadowbox-stelselkopie word verkry en deur Docker ingevoer. Die stelselkopie word gehuisves op [Quay.io](https://quay.io/) in [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Hierdie stelselkopie bevat die Outline-bediener en Management API wat later deur die Outline-bedienerbestuur-app gebruik gaan word om toegangsleutels te skep en te verwyder, intekening te aanvaar vir of te onttrek aan die rapportering van anonieme maatstawwe, ens.
- [Watchtower](https://github.com/v2tec/watchtower) is geïnstalleer en opgestel om uurliks vir stelselkopie-opdaterings te kyk om te help verseker dat elke Outline-bediener deurlopend op datum gehou word met die nuutste kenmerke en sekuriteitverbeterings.
- ’n Webbediener wat gebruik word om toegang tot die Management API te kry, word op ’n lukrake poort op ’n geheime en lukrake pad begin.
- ’n [Selfondertekende SSL-sertifikaat](https://en.wikipedia.org/wiki/Self-signed_certificate) word geskep sodat die bestuur van die Outline-bediener geënkripteer kan word deur TLS te gebruik al het dit nie ’n domeinnaam nie. ’n Unieke vingerafdruk van hierdie sertifikaat word ook gegenereer en gestoor in die Outline Manager-app en dit help om MITM-aanvalle te keer.

Die Outline-installering hoef nie ná installering opgestel te word nie.

## Bedienersekuriteit
 Outline-sagteware is oopbron, wat beteken dat enigiemand die kode kan sien en dit kan verbeter as daar enige kwesbaarhede ontdek word. Ons kode word gehuisves op [GitHub](https://github.com/search?q=org%3AOutline-Foundation+outline&unscoped_q=outline).

 Verder word alle geïnstalleerde Outline-bedieners outomaties opgedateer wanneer ’n nuwe weergawe vrygestel word om te verseker dat geen Outline-bediener ou weergawes van die sagteware gebruik nie.

 Om die toegangsleutels op die bediener te bestuur, is daar interaksie tussen die Outline Manager-app en die bestuurdiens op die Outline-bediener. Die bestuurdiens loop op ’n lukrake poort op ’n geheime en unieke pad. Die bestuurdiens self kan nie ondersoek word nie, aangesien dit nie reageer op vrae behalwe as die toepaslike geheime pad gespesifiseer word nie. Ten slotte word alle kommunikasie aan die bestuurdiens geënkripteer met ’n [selfondertekende SSL-sertifikaat](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Die Outline-bediener stoor ook nie enige loglêers nie, so al word dit gekompromitteer, sal geen gebruikerdata openbaar gemaak word nie. Kry [hier](/about/security-and-privacy) meer inligting. Outline is in 2018 deur [Radically Open Security](https://radicallyopensecurity.com/) en [Cure53](https://cure53.de/) geoudit. Lees die verslae [hier](/about/security-and-privacy).

## Hantering van UDP-verkeer
 Outline kan as ’n stelselwye VPN werk, wat beteken dat alle UDP-vervoer deur die Outline-bediener getonnel word.

## DNS-verkeer
Outline voer alle DNS-soektogte deur die Outline-bediener uit en beskerm hulle deur dieselfde enkripsie te gebruik wat vir alle ander netwerkaktiwiteite gebruik word. Jou DNS-navrae sal deur die Outline-bediener na die Dyn Internet Guide, OpenDNS, Cloudflare DNS of Quad9 DNS gaan. Outline hou nie ’n loglêer van jou DNS-soektogte nie.
