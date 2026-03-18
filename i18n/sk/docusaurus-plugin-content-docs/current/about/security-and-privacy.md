---
title: Zabezpečenie a ochrana súkromia pri používaní služby Outline
sidebar_label: Zabezpečenie a ochrana súkromia pri používaní služby Outline
---

Zabezpečenie a ochrana súkromia pri používaní služby Outline

## Ako Outline chráni vašu online komunikáciu

Internetová premávka je najviac vystavená riziku monitorovania, keď prechádza miestnou alebo národnou sieťou.

Outline pomáha zachovať súkromie vašej komunikácie tým, že internetovú premávku počas prenosu v národnej sieti šifruje, až kým sa nedostane na server služby Outline. Pri šifrovaní premávky cez Outline sledovatelia siete nemôžu kontrolovať weby, ktoré navštevujete, ani informácie, ktoré prenášate.

Outline vám tiež pomôže získať prístup k nástrojom na bezpečnú komunikáciu end-to-end, ktoré vo vašej krajine inak nemusia byť dostupné.

## Šifrovacie štandardy

Outline šifruje komunikáciu medzi vaším zariadením a serverom Outline pomocou 256‑bitovej šifry AEAD Chacha2020 IETF Poly 1305. Šifry AEAD poskytujú dôvernosť, integritu a overenie pravosti a pri použití na modernom hardvéri dosahujú skvelý výkon.

## Audity zabezpečenia

V roku 2018 prešla služba Outline auditom dvoch nezávislých organizácií Radically Open Security a Cure53 zameraných na digitálnu bezpečnosť, ktoré kontrolujú, či softvér spĺňa najnovšie bezpečnostné normy. Organizácia Radically Open Security vykonala ďalší audit v roku 2022 a firma Cure53 vykonala audit súpravy Outline SDK v roku 2024. Reporty si môžete pozrieť v týchto zdrojoch:

- [Radically Open Security Penetration Test Report (Správa o prienikovom teste zostavená firmou Radically Open Security), marec 2018](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (Správa o prienikovom teste a audite softvéru Jigsaw Outline zostavená firmou Cure53), december 2018](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (Report o penetračnom teste od firmy Radically Open Security) (december 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (Správa firmy Cure53 o prienikovom teste softvéru Jigsaw Outline VPN SDK, január 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonymné metriky a denníky

Outline sleduje použitú rýchlosť pripojenia, a to vo forme prenesených bajtov pre jednotlivé prístupové kľúče. Tieto informácie umožňujú správcom servera upraviť u poskytovateľov cloudového servera odoberanú rýchlosť pripojenia podľa potreby, no neumožňujú im zobraziť si konkrétne informácie, ktoré prešli cez server služby Outline.

Prečítajte si viac o tom, ako Outline [zhromažďuje údaje a informácie](/about/data-collection).

---

## Časté otázky o zabezpečení a ochrane súkromia

## Zabezpečí mi Outline anonymitu na internete?

Nie, Outline nie je nástroj na anonymizáciu. Chráni vaše súkromie pred potenciálnymi sledovateľmi siete.

Outline vám na weboch, ktoré navštevujete, nezabezpečuje úplnú anonymitu, pretože tie vás aj tak môžu identifikovať, keď sa prihlásite, prípadne pomocou techník, ako sú digitálne stopy v prehliadači. V prípade mobilných aplikácií disponuje väčšina moderných smartfónov rozhraniami API, ktoré umožňujú inštalovaným aplikáciám získavať polohu nezávisle od vášho proxy servera, pretože môžu využiť integrované GPS.

Siete VPN vo všeobecnosti ponúkajú dôležité nástroje na ochranu, najmä pred monitorovaním internetu, no to neznamená, že vám online nič nehrozí. Ak poskytovateľ internetu pozná vašu totožnosť a môže sledovať vašu sieťovú premávku, dokáže určiť adresu IP vášho servera Outline, dokonca aj keď používate VPN. Tieto informácie sa dajú použiť na blokovanie prístupu k serveru Outline alebo na identifikovanie vzorcov používania, napríklad kedy ste zvyčajne online, a teoreticky aj vašej približnej polohy.

## Dá sa zistiť, či používam Outline?

Teoreticky áno. Platformy a služby, ku ktorým pristupujete, pravdepodobne budú vedieť rozpoznať, že vaše pripojenie pochádza z cloudového servera. Občas vedia vydedukovať, že používate VPN, no ani vtedy nevidia obsah vašej internetovej premávky.

## Chráni ma Outline pred všetkými možnými kybernetickými hrozbami?

Nie. Pred všetkými možnými kybernetickými hrozbami vás neochráni žiaden nástroj. Outline vám umožňuje prístup k otvorenému internetu a šifrovaním sieťovej premávky zlepšuje ochranu vášho súkromia. Aj napriek tomu vám odporúčame chrániť sa proti iným typom útokov, napríklad malvéru alebo phishingu, aj ďalšími spôsobmi.

Skúste sa obrátiť na odborníka na kybernetickú bezpečnosť vo svojej organizácii, ktorý vám pomôže chrániť sa online lepšie. Prípadne môžete využiť prispôsobené rady od popredných odborníkov na zabezpečenie na webe [Security Planner](https://securityplanner.org/). Ide o web, ktorý vám poskytne jasné pokyny na výber nástrojov kybernetickej bezpečnosti zodpovedajúcich vašim potrebám.

Môžete si pozrieť aj ďalšie služby kybernetickej bezpečnosti od firmy [Jigsaw](https://jigsaw.google.com/), ako sú [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) a [Ochrana hesla](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Je legálne používať VPN?

Než začnete prevádzkovať Outline alebo používať aplikáciu, pozrite si miestne zákony a nariadenia a tiež zmluvné podmienky poskytovateľa cloudu, ktorého plánujete využívať.
