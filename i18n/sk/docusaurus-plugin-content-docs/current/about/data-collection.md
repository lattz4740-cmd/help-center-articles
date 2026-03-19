---
title: Zhromažďovanie údajov a informácií
sidebar_label: Zhromažďovanie údajov a informácií
---

Outline nezhromažďuje osobné údaje, kým s tým nevyjadríte súhlas. Nezhromažďuje ani informácie o weboch, ktoré navštívite, ani s kým a o čom komunikujete.

 Ak cez Správcu Outline vytvárate účet u poskytovateľa cloudu tretej strany alebo sa doň prihlasujete, nezískame žiadne informácie, ktoré mu poskytnete, napríklad vašu e‑mailovú adresu, meno, fakturačné údaje ani platobné údaje.

## Informácie, ktoré získavame automaticky
 Automaticky zhromažďujeme dva typy informácií.

 1. Adresu IP servera

 Adresa IP servera Outline sa získava cez [Quay.io](https://quay.io/) a je nám sprístupnená, keď sa server automaticky aktualizuje využitím najnovších zlepšení zabezpečenia a funkcií. Adresa IP servera môže identifikovať poskytovateľa cloudového servera a mesto, v ktorom bol server Outline nastavený, no neposkytuje informácie o tom, kto server prevádzkuje alebo k nemu má prístup.

 2. Technické údaje neumožňujúce zistenie totožnosti

 V prípade spadnutia služby Outline, výskytu závažnej výnimky alebo manuálneho odoslania spätnej väzby cez aplikáciu Outline budú nahlásené informácie uvedené nižšie. Tieto informácie sa použijú iba na pomoc pri identifikovaní a riešení problémov so stabilitou alebo výkonom.

- Krajina
- Miestne nastavenie
- Dátum a čas zlyhania alebo výnimky a najviac 100 predchádzajúcich udalostí, ako napríklad otvorenie sekcie Informácie používateľom
- Staticky kompilované správy o výnimkách
- Názov a verzia operačného systému
- Model telefónu (ak je to relevantné)
- Čas spustenia aplikácie
- Prehliadač
- Architektúra
- Číslo verzie a zostavy aplikácie Outline

Tieto informácie sa prenášajú pomocou protokolu HTTPS do služby Sentry ([sentry.io](https://sentry.io/)), čo je open source služba tretej strany na sledovanie chýb. Sentry na zabezpečenie vašich údajov pred neautorizovaným prístupom, zverejnením, použitím a stratou používa rôzne technológie a služby zodpovedajúce odvetvovým normám. Ak máte akékoľvek otázky týkajúce sa pravidiel služby Sentry, prejdite na [https://sentry.io/security/](https://sentry.io/security/) a [https://sentry.io/privacy/](https://sentry.io/privacy/), prípadne kontaktujte podporu na [security@sentry.io](mailto:security@sentry.io). Všetky údaje služby Outline ukladané službou Sentry sú obmedzené tak, že k nim majú prístup iba členovia tímu služby Outline.

## Informácie, ktoré získavame iba po vyjadrení súhlasu
 Outline po vyjadrení súhlasu nahlasuje tímu Outline nasledujúce informácie.

 1. Metriky používania

 Každý server Outline automaticky zhromažďuje počet prenesených bajtov za poslednú hodinu na základe prístupového kľúča, čas, počas ktorého bol používateľ pripojený k serveru, krajiny a autonómne systémy pôvodu použitých prihlasovacích údajov a informácie o tom, či boli nejaké funkcie zapnuté alebo vypnuté. Obsah komunikácie ani metadáta umožňujúce zistenie totožnosti (napr. prihlasovacie údaje, e‑mailové adresy, identifikátory zariadení atď.) sa nezaznamenávajú. Všetky metriky sú prepojené s identifikátorom servera. Pokyny na zmenu identifikátora servera [nájdete tu](/manager/server-management/reset-server-id).

 Servery Outline tieto metriky predvolene nezdieľajú s tímom Outline. Ak správca servera explicitne vyjadrí súhlas so zdieľaním metrík používania, tieto informácie budú bezpečne odosielané tímu Outline každú hodinu. Po 60 dňoch budú metriky používania agregované na úrovni krajiny. Správcovia servera môžu svoje predvoľby zdieľania metrík používania kedykoľvek zmeniť v ponuke Nastavenia v Správcovi Outline.

 Oceňujeme, že s nami anonymné metriky o používaní servera zdieľate, keďže ich používame na meranie trendov používania a zlepšovanie služby.

 Ak napríklad správca servera aktivuje zdieľanie metrík používania, budeme môcť získať informácie uvádzajúce, že server s identifikátorom 12345 sa včera používal 3 hodiny a celkovo došlo k prenosu 500 megabajtov dát z troch kľúčov, ktoré sa používali v USA a Kanade, pričom bola aktivovaná funkcia dátových limitov.

 2. Vaše komentáre a e‑mailová adresa, ak odošlete spätnú väzbu

 Aplikácie Správca Outline a Outline umožňujú odoslať tímu spätnú väzbu. Odporúčame neuvádzať údaje umožňujúce zistenie totožnosti, no pole e‑mailovej adresy je k dispozícii, ak chcete od tímu dostať odpoveď. Automaticky tiež zbierame niektoré základné informácie, ktoré nám pomôžu vašu spätnú väzbu lepšie pochopiť. Pozrite si 2. bod v časti Informácie, ktoré získavame automaticky, kde nájdete, ktoré údaje zhromažďujeme. Prečítajte si viac [o zabezpečení a spôsoboch ochrany súkromia služby Outline](/about/security-and-privacy).

 Ak používate beta verziu aplikácie Outline v Androide, môžeme použiť platformu [Firebase od Googlu](https://firebase.google.com/) na zhromažďovanie informácií pre ladenie, ktoré nám pomôžu detegovať problémy a zlepšovať Outline. Viac o pravidlách ochrany súkromia a zabezpečenia platformy Firebase sa dozviete na jej webe: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Ak nechcete, aby aplikácia Outline tieto informácie prostredníctvom služby Firebase odosielala, používajte jej finálnu verziu.
