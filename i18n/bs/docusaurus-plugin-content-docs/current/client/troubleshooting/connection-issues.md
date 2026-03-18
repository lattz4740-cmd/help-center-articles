---
title: "Zašto se ne mogu povezati s uslugom Outline?"
sidebar_label: "Zašto se ne mogu povezati s uslugom Outline?"
---

Postoji nekoliko mogućih razloga zašto se ne možete povezati s uslugom Outline:

- **Prekinuta je**[/client/troubleshooting/connection-issues#One](/client/troubleshooting/connection-issues#One)[**veza uređaja s internetom**](#Internetissues)[#Internetissues](#Internetissues)**.**Ponekad će na vašem uređaju doći do prekida mrežne veze i može malo potrajati da se ažuriraju ikone mreže. Možda je i uređaj povezan s lokalnom mrežom, ali nema veze s internetom.
- **Vaš**[/client/troubleshooting/connection-issues#Two](/client/troubleshooting/connection-issues#Two)[**zaštitni zid mreže blokira pristup**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[O](#FirewallIssues)utline serveru.**Ovo se često događa kada ste na javnoj mreži, npr. školskoj, poslovnoj ili besplatnoj bežičnoj mreži.
- **Uređaj ima**[/client/troubleshooting/connection-issues#Three](/client/troubleshooting/connection-issues#Three)[**zaštitni zid ili antivirusni softver**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**koji blokira pristup Outline serveru.**
- **Vaše**[**postavke telefona**](#DeviceSettings)**se možda trebaju promijeniti.**
- **Vaš upravitelj usluge je možda**[**eliminirao server ili ISP blokira vaš zahtjev**](#ServerIssues) .

## Problemi s internetskom vezom: {#Internetissues}

## Kako testirati:

Isključite Outline i provjerite je li vraćena veza s internetom.

- Ako jeste, pogledajte više opcija rješavanja problema ispod.
- Ako nije, pričekajte nekoliko trenutaka da vidite hoće li se postavke veze samostalno ažurirati.

## Trebate riješiti sljedeće:

Vratite uređaj online:

1. Provjerite može li se drugi uređaj povezati s istom mrežom. Ako i drugi uređaji nisu online, mreža možda ne funkcionira i morate pričekati da se ponovo uspostavi veza s njom ili riješiti probleme s njom.
2. Ako se drugi uređaji mogu povezati s istom mrežom, možete pokušati nešto od sljedećeg da vratite uređaj online:
   1. Postavite uređaj u način rada u avionu (mobilni uređaj)
   2. Ponovo pokrenite uređaj
   3. Isključite uređaj, pričekajte 2 minute, a zatim ga ponovo uključite

## Problemi sa zaštitnim zidom mreže: {#FirewallIssues}

## Kako testirati:

1. Prekinite vezu s trenutnim WiFi-jem ili žičanom mrežom.
2. Povežite se s drugom mrežom, npr. mobilnom
3. Pokušajte se ponovo povezati s Outline serverom

Ako se možete povezati kada ste na drugoj mreži, onda je u tome problem.

## Trebate riješiti sljedeće:

Obratite se upravitelju usluge i zatražite da vam dozvoli pristup Outline serveru ili nastavite koristiti drugu mrežu.

**Problemi sa zaštitnim zidom ili antivirusnim softverom:**

**Kako testirati:**

 Pokušajte se povezati s Outlineom s drugog uređaja.

Napomena: ne zaboravite da vam trebaju pristupni ključ i aplikacija Outline da koristite Outline na drugom uređaju.

## Trebate riješiti sljedeće:

Provjerite jesu li postavke zaštitnog zida ili antivirusnog softvera postavljene tako da dozvoljavaju protok VPN i Outline saobraćaja.

## Postavke uređaja: {#DeviceSettings}

## Šta trebate provjeriti:

Za Android:

1. Otvorite aplikaciju Postavke.
2. Potražite **Postavke VPN-a** na uređaju. (Postavke VPN-a će prikazati sve VPN aplikacije koje trenutno imaju pristup na vašem telefonu.)
3. Ako ne vidite Outline u postavkama VPN-a, deinstalirajte Outline i ponovo ga instalirajte. Uređaj bi nakon instaliranja trebao automatski dati pristup Outlineu.

Provjerite da na Android uređaju nemate neku aplikaciju za preklapanje ekrana jer bi ona mogla slati prozor s odobrenjima za Outline u pozadinu tako da se ne vidi u prvom planu.

 Na Android uređaju idite u Postavke > Aplikacije > Poseban pristup aplikaciji. Zatim dodirnite opciju Prikaži preko drugih aplikacija. Možete ukloniti pristup svim aplikacijama koje dozvoljavaju ovakvo ponašanje.

 Za iOS: pročitajte[ovaj članak podrške](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Problemi sa serverom: {#ServerIssues}

## Kako testirati:

Ako imate pristup većem broju servera, pokušajte se povezati s nekim od njih.

## Trebate riješiti sljedeće:

Obratite se upravitelju usluge da provjerite je li server eliminiran. Ako jeste, zatražite[pristupni ključ](/about/terminology) za drugi server.

Ako ste vi postavili server, pokušajte se povezati s njim putem Outline Managera ili na neki drugi način, kao što je[SSH](https://en.wikipedia.org/wiki/Secure_Shell). Ako to ne funkcionira, pokušajte provjeriti konzolu pružaoca usluge oblaka, ako postoji, da provjerite je li server i dalje online.
