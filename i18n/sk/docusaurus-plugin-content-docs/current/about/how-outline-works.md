---
title: Ako Outline funguje
sidebar_label: Ako Outline funguje
---

## Inštalácia servera
 Aj keď inštalácia servera Outline môže pôsobiť jednoducho, spočíva v komplexnej skupine krokov, pomocou ktorých sa server inštaluje. Keď sa Outline inštaluje, inštalačný skript spustí tieto kroky:

- Pomocou služby Docker sa načíta a importuje stabilná verzia obrazu služby Shadowbox. Obraz je hostený na [Quay.io](https://quay.io/) ([https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags)). Tento obraz obsahuje server Outline a rozhranie Management API, ktoré neskôr používa aplikácia na správu servera Outline na vytváranie a odstraňovanie prístupových kľúčov, prihlasovanie a odhlasovanie sa z reportovania anonymných metrík atď.
- Nainštaluje sa nástroj [Watchtower](https://github.com/v2tec/watchtower) a nakonfiguruje sa tak, aby každú hodinu kontroloval dostupnosť aktualizácií obrazu, čo pomáha zabezpečiť, že každý server Outline je vždy aktuálny a má najnovšie funkcie a zlepšenia zabezpečenia.
- Webový server používaný na prístup k rozhraniu Management API sa spustí na náhodnom porte na tajnej a náhodnej ceste.
- Vytvorí sa [certifikát SSL s vlastným podpisom](https://en.wikipedia.org/wiki/Self-signed_certificate), aby bolo možné správu servera Outline šifrovať pomocou protokolu TLS, hoci nemá názov domény. Vygeneruje sa aj jedinečný digitálny odtlačok tohto certifikátu, ktorý sa uloží v aplikácii Správca Outline, čo pomáha brániť útokom MITM.

Outline po inštalácii netreba konfigurovať.

## Zabezpečenie servera
 Softvér Outline má licenciu open source. Znamená to, že ktokoľvek si môže pozrieť jeho kód a zlepšiť ho, ak objaví akékoľvek nedostatky zabezpečenia. Náš kód je hostený na [GitHub](https://github.com/search?q=org%3AOutline-Foundation+outline&unscoped_q=outline).

 Všetky nainštalované servery Outline sú navyše automaticky aktualizované vždy, keď je vydaná nová verzia, čím sa zabezpečuje, že žiadny server Outline ďalej nepoužíva staré verzie softvéru.

 Aplikácia Správca Outline interaguje so službou správy na serveri Outline, čo umožňuje spravovať prístupové kľúče na serveri. Služba správy sa prevádzkuje na náhodnom porte na tajnej a jedinečnej ceste Samotná služba správy je odolná proti preskúmaniu, keďže neodpovedá na dopyty, pokiaľ nie je uvedená príslušná tajná cesta. Všetka komunikácia so službou správy je navyše šifrovaná [certifikátom SSL s vlastným podpisom](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Server Outline neukladá žiadne denníky, takže ani v prípade jeho napadnutia nedôjde k zverejneniu žiadnych údajov používateľov. [Ďalšie informácie](/about/security-and-privacy) V roku 2018 prešiel Outline auditom organizácií [Radically Open Security](https://radicallyopensecurity.com/) a [Cure53](https://cure53.de/). Reporty [nájdete tu](/about/security-and-privacy).

## Riešenie premávky UDP
 Outline dokáže fungovať ako VPN pre celý systém. Znamená to, že všetka premávka UDP bude tunelovaná cez server Outline.

## Premávka DNS
Outline vykonáva všetky vyhľadávania DNS cez server Outline a chráni ich rovnakým šifrovaním, aké sa používa na všetku ostatnú aktivitu siete. Vaše dopyty DNS budú prechádzať cez server Outline do služby Dyn Internet Guide, OpenDNS, Cloudflare DNS alebo Quad9 DNS. Outline vaše vyhľadávania DNS nikdy nezaznamenáva.
