---
title: Terminológia
sidebar_label: Terminológia
---

**Čo je VPN?**

 Virtuálna súkromná sieť (VPN) je súkromné pripojenie vašich zariadení k hostiteľskému serveru. Keď používate VPN, vaša návštevnosť je pred poskytovateľom internetu skrytá. VPN odporúčame používať, keď chcete:

- chrániť svoje údaje pri používaní verejnej siete Wi‑Fi;
- uchovávať svoje dáta prehliadania v súkromí, aby ich nevidel poskytovateľ internetu ani orgány verejnej správy;
- získavať prístup k necenzurovanému obsahu z rôznych zdrojov po celom svete.

**Čím sa Outline líši od tradičných sietí VPN?**

 Poskytovatelia internetu môžu ľahko zaznamenávať a blokovať tradičné siete VPN rozpoznávaním bežných bezpečnostných protokolov a vzorov objemu návštevnosti. Služba Outline je odolnejšia než tradičné siete VPN, pretože bola vytvorená pomocou protokolu navrhnutého tak, aby ho bolo náročné rozpoznať, a teda ťažšie blokovať. Služba Outline je odolná voči sofistikovaným formám cenzúry vrátane blokovania na základe siete a blokovania adresy IP.

**Čo je server Outline?**

 Server Outline prevádzkuje sieť VPN, ku ktorej sa budú pripájať povolení používatelia. Ak vytvárate novú sieť, môžete ako server Outline použiť vlastný zabezpečený server (ak nejaký máte), prípadne môžete použiť poskytovateľa cloudových služieb, ako sú:

- DigitalOcean,
- Google Cloud Platform (GCP),
- Amazon Web Services (AWS).

Server nastavíte v Správcovi Outline.

**Čo je správca služby?**

 Správca služby je osoba zodpovedná za nastavenie servera Outline a zdieľanie prístupových kľúčov s používateľmi. Obvykle zodpovedá za náklady na používanie servera. 

**Čo je prístupový kľúč?**

 Prístupový kľúč slúži na prístup k existujúcemu serveru Outline a pripojenie k sieti VPN. Poskytne vám ho [správca služby](#servicemanager) alebo môžete [nastaviť server Outline](/manager/server-setup/setup-server) svojpomocne. Prístupový kľúč vyzerá napríklad takto (ide o nefunkčnú ukážku): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Čo je Správca Outline?**

 Správca Outline je aplikácia pre počítače, ktorá správcovi služby umožňuje nastaviť server Outline, vygenerovať [prístupové kľúče](#accesskey) a nakonfigurovať pre každý z nich dátový limit používania. Najnovšiu verziu Správcu Outline si môžete [stiahnuť tu](https://getoutline.org/get-started/#step-3) alebo na [tejto stránke](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Čo je to Outline Client?**

 Outline Client je aplikácia dostupná pre počítače a mobilné zariadenia, ktorá vám umožňuje pripojiť sa k serveru Outline a získať prístup k sieti VPN pomocou prístupového kľúča. Najnovšiu verziu aplikácie Outline Client si môžete [stiahnuť tu](https://getoutline.org/get-started/#step-3) alebo na [tejto stránke](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Čo sú dátové limity?**

 Správca Outline umožňuje správcom služieb nastaviť v prípade prístupových kľúčov kĺzavý 30-dňový dátový limit, ktorý zabráni nadmernému používaniu a pomôže predvídať náklady. Správcovia služieb môžu nastaviť jednotný predvolený limit na všetky kľúče alebo rôzne limity pre jednotlivé kľúče, ktoré predvolený limit prepíšu. Keď nastavíte limit, začne platiť okamžite a bude sa uplatňovať každú hodinu.

Ak sa správcovia služieb prihlásia na zdieľanie metrík so službou Jigsaw, mali by si prečítať [pravidlá zhromažďovania údajov](/about/data-collection). Nájdu v nich podrobnosti o tom, ako bude reportované používanie dátových limitov.
