---
title: "Prečo sa nemôžem pripojiť k službe Outline?"
sidebar_label: "Prečo sa nemôžem pripojiť k službe Outline?"
---

Existuje niekoľko možných dôvodov, prečo sa nemôžete pripojiť k službe Outline:

- **Vaše zariadenie**[/client/troubleshooting/connection-issues#One](/client/troubleshooting/connection-issues#Internetissues)[**nie je pripojené k internetu**](#Internetissues)[#Internetissues](#Internetissues)**.**Niekedy môže vo vašom zariadení dôjsť k prerušeniu pripojenia k sieti a aktualizácia ikon siete môže chvíľu trvať. Je tiež možné, že vaše zariadenie je pripojené k miestnej sieti, no internet nefunguje.
- **Vaša**[/client/troubleshooting/connection-issues#Two](/client/troubleshooting/connection-issues#FirewallIssues)[**brána firewall siete blokuje**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[prístup](#FirewallIssues) k vášmu serveru Outline.**Ide o bežný problém, keď používate verejnú sieť, napríklad školskú, pracovnú alebo bezplatnú bezdrôtovú sieť.
- **Vaše zariadenie má**[/client/troubleshooting/connection-issues#Three](/client/troubleshooting/connection-issues#SoftwareIssues)[**bránu firewall alebo antivírusový softvér**](#SoftwareIssues),[#SoftwareIssues](#SoftwareIssues)**ktorý blokuje prístup k vášmu serveru Outline.**
- **Vaše**[**nastavenia telefónneho zariadenia**](#DeviceSettings)**možno bude potrebné zmeniť.**
- **Váš správca služby možno**[**zničil príslušný server alebo váš poskytovateľ internetu možno blokuje vašu požiadavku**](#ServerIssues) .

## Problémy s internetovým pripojením: {#Internetissues}

## Ako otestovať:

Vypnite Outline a skontrolujte, či sa obnoví vaše pripojenie na internet.

- Ak áno, prečítajte si ďalšie možnosti riešenia problémov nižšie.
- Ak nie, chvíľu počkajte a zistite, či sa nastavenia pripojenia aktualizujú.

## Čo treba opraviť:

Znova pripojte svoje zariadenie na internet:

1. Skontrolujte, či sa na rovnakú sieť dokáže pripojiť iné zariadenie. Ak sa iné zariadenia nedokážu pripojiť, sieť môže mať výpadok. Možno bude potrebné, aby ste počkali, než bude znova fungovať, alebo vyriešili problém so sieťou.
2. Ak sa k rovnakej sieti môžu pripojiť iné zariadenia, vyskúšajte jeden alebo viacero nasledujúcich krokov na opätovné spustenie internetu:
   1. Prepnite zariadenie do režimu v lietadle (mobilné zariadenie).
   2. Reštartujte zariadenie.
   3. Vypnite zariadenie, počkajte 2 minúty a znova ho zapnite.

## Problémy s bránou firewall siete: {#FirewallIssues}

## Ako otestovať:

1. Odpojte sa od aktuálne používanej siete Wi‑Fi alebo káblovej siete.
2. Pripojte sa k inej sieti, napríklad k mobilnej.
3. Skúste sa znova pripojiť k serveru Outline.

Ak sa dokážete pripojiť z inej siete, ide o problém na vašej strane.

## Čo treba opraviť:

Kontaktujte správcu služieb a požiadajte ho, aby povolil prístup k vášmu serveru Outline, alebo namiesto toho používajte ďalej túto inú sieť.

**Problémy s bránou firewall alebo antivírusovým softvérom:**

**Ako otestovať:**

 Skúste sa pripojiť k službe Outline v inom zariadení.

Poznámka: Pamätajte, že ak chcete používať Outline v inom zariadení, budete potrebovať prístupový kľúč a aplikáciu Outline.

## Čo treba opraviť: {#SoftwareIssues}
Skontrolujte si nastavenia firewallu alebo antivírusového softvéru a ubezpečte sa, že povoľujú návštevnosť cez VPN a Outline.

## Nastavenia zariadenia: {#DeviceSettings}

## Čo treba skontrolovať: {#DeviceSettings}
Postup pre Android:

1. Otvorte aplikáciu Nastavenia.
2. Vyhľadajte vo svojom zariadení **nastavenia siete VPN**. (V nastaveniach siete VPN uvidíte všetky aplikácie VPN, ktoré majú momentálne prístup vo vašom telefóne).
3. Ak Outline v nastaveniach siete VPN nevidíte, odinštalujte službu Outline a preinštalujte ju. Zariadenie by malo službe Outline po inštalácii automaticky udeliť prístup.

Uistite sa, že vo svojom zariadení s Androidom nemáte nainštalovanú žiadnu aplikáciu s prekrývajúcimi prvkami, pretože môže okno s povoleniami pre službu Outline odosielať do pozadia, takže nebude viditeľné na popredí.

 Prejdite vo svojom zariadení s Androidom do sekcie Nastavenia > Aplikácie > Špeciálny prístup aplikácií. Potom klepnite na Zobrazovať cez iné aplikácie. Môžete odstrániť prístup všetkých aplikácií, ktoré toto správanie povoľujú.

 Postup pre iOS: prečítajte si [tento článok podpory](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Problémy so serverom: {#ServerIssues}

## Ako otestovať: {#ServerIssues}
Ak máte prístup k viac než jednému serveru, skúste sa pripojiť k inému.

## Čo treba opraviť:

Kontaktujte svojho správcu služieb a zistite, či bol server zničený. Ak áno, požiadajte ho o [prístupový kľúč](/about/terminology) k inému serveru.

Ak ste server nastavili, skúste sa k nemu pripojiť cez Správcu Outline alebo iným spôsobom, napríklad pomocou [protokolu SSH](https://en.wikipedia.org/wiki/Secure_Shell). Ak to nebude fungovať, skúste skontrolovať v konzole poskytovateľa cloudu (ak existuje), či je daný server stále online.
