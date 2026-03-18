---
title: "Zašto se ne mogu povezati s uslugom Outline?"
sidebar_label: "Zašto se ne mogu povezati s uslugom Outline?"
---

Do nemogućnosti povezivanja s uslugom Outline može dovesti nekoliko razloga:

- **Vaš uređaj**[/client/troubleshooting/connection-issues#One](/client/troubleshooting/connection-issues#One)[**nije povezan s internetom**](#Internetissues)[#Internetissues](#Internetissues)**.**Na uređaju ponekad može doći do prekida mrežne veze. Ažuriranje mrežnih ikona može potrajati nekoliko trenutaka. Moguće je i da je vaš uređaj povezan s lokalnom mrežom, ali internet ne radi.
- **Vaš**[/client/troubleshooting/connection-issues#Two](/client/troubleshooting/connection-issues#Two)[**mrežni vatrozid blokira pristup**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[#FirewallIssues](#FirewallIssues) Outline poslužitelju.**To se često događa na javnim mrežama, poput školskih, poslovnih ili besplatnih bežičnih mreža.
- **Vaš uređaj ima**[/client/troubleshooting/connection-issues#Three](/client/troubleshooting/connection-issues#Three)[**vatrozid ili antivirusni softver**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**koja blokira pristup vašem Outline poslužitelju.**
- **Vaše**[**postavke uređaja**](#DeviceSettings)**možda se trebaju izmijeniti.**
- **Vaš je upravitelj usluge možda**[**uništio poslužitelj ili vaš ISP blokira vaš zahtjev**](#ServerIssues) .

## Problemi s internetskom vezom: {#Internetissues}

## Postupak testiranja:

Isključite Outline i provjerite je li veza s internetom ponovno uspostavljena.

- Ako jest, pogledajte još prijedloga za rješavanje problema u nastavku.
- Ako nije, pričekajte nekoliko trenutaka da biste vidjeli hoće li se postavke veze same ažurirati.

## Što treba popraviti:

Ponovo povežite uređaj s internetom:

1. Provjerite može li se drugi uređaj povezati s istom mrežom. Ako se drugi uređaji ne mogu povezati s internetom, mreža je možda nedostupna te ćete za rješavanje problema morati pričekati da ponovno bude dostupna.
2. Ako se drugi uređaji mogu povezati s istom mrežom, možete isprobati neki od sljedećih prijedloga da se ponovo povežete s internetom:
   1. Uključite način rada u zrakoplovu (na mobilnom uređaju)
   2. Ponovo pokrenite uređaj
   3. Isključite uređaj, pričekajte dvije minute i ponovo uključite uređaj

## Problemi s mrežnim vatrozidom: {#FirewallIssues}

## Postupak testiranja:

1. Prekinite vezu s trenutačnom Wi-Fi ili žičanom mrežom.
2. Povežite se s drugom mrežom, na primjer mobilnom.
3. Pokušajte ponovo uspostaviti vezu s Outline poslužiteljem

Ako se uspijete povezati s poslužiteljem dok upotrebljavate drugu mrežu, pronašli ste problem.

## Što treba popraviti:

Zatražite od upravitelja usluge da omogući pristup vašem Outline poslužitelju ili nastavite upotrebljavati drugu mrežu.

**Problemi s vatrozidom ili antivirusnim softverom:**

**Postupak testiranja:**

 Pokušajte ponovo uspostaviti vezu s Outlineom s drugog uređaja.

Napomena: ne zaboravite da za upotrebu Outlinea na drugom uređaju trebate imati pristupni ključ i aplikaciju Outline.

## Što treba popraviti:

Provjerite postavke vatrozida ili antivirusnog softvera i uredite ih tako da dopuštaju promet preko VPN-a i Outlinea.

## Postavke uređaja: {#DeviceSettings}

## Što treba provjeriti:

Android:

1. Otvorite aplikaciju Postavke.
2. Potražite **postavke VPN-a** na svojem uređaju (u postavkama VPN-a prikazuju se sve VPN aplikacije koje trenutačno imaju pristup na telefonu).
3. Ako u postavkama VPN-a ne vidite Outline, deinstalirajte Outline i ponovo ga instalirajte. Uređaj bi nakon instalacije automatski trebao dati pristup Outlineu.

Na Android uređaju ne smije biti instalirana aplikacija za preklapanje na zaslonu jer ona možda potiskuje prozor s dopuštenjima za Outlook u pozadinu, zbog čega nije vidljiv u prednjem planu.

 Na Android uređaju otvorite Postavke > Aplikacije > Poseban pristup za aplikacije. Dodirnite Prikaz iznad drugih aplikacija. Možete ukloniti pristup aplikacijama koje dopuštaju to ponašanje.

 iOS: pročitajte [ovaj članak pomoći](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Problemi s poslužiteljem: {#ServerIssues}

## Postupak testiranja:

Ako možete pristupiti više poslužitelja, pokušajte se povezati s drugim poslužiteljem.

## Što treba popraviti:

Obratite se upravitelju usluge i provjerite nije li poslužitelj uništen. Ako jest, zatražite [pristupni ključ](/about/terminology) za drugi poslužitelj.

Ako ste vi postavili poslužitelj, pokušajte se povezati s njim putem Upravitelja Outlinea ili na neki drugi način, na primjer putem [SSH-a](https://en.wikipedia.org/wiki/Secure_Shell). Ako to ne riješi problem, možete provjeriti konzolu davatelja usluga u oblaku (ako postoji) da biste saznali je li poslužitelj i dalje online.
