---
title: "Ako nastavím dátové limity pre prístupové kľúče?"
sidebar_label: "Ako nastavím dátové limity pre prístupové kľúče?"
---

Môžete nastaviť dátový limit, ktorý bude platiť pre všetky prístupové kľúče. Ak ho chcete nastaviť, otvorte Outline Manager a prejdite do Nastavení. Uvidíte v nich prepínač Dátové limity, ktorý vám po povolení umožňuje nastaviť limit.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Po nastavení limitu budete na stránke prístupového kľúča vidieť, ako blízko sa nachádzajú jednotliví používatelia k jeho dosiahnutiu. Pruhový graf zobrazuje spotrebu dát za posledných 30 dní.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Okrem možnosti nastaviť limit pre všetky prístupové kľúče môžete teraz každému kľúču prideliť vlastný dátový limit. Toto nastavenie prepíše predvolený dátový limit, ktorý ste nastavili, ale ak ste žiadny nenastavili, môžete ho stále nakonfigurovať pre ktorýkoľvek kľúč.

 Ak chcete nastaviť limit dátových prenosov kľúča, otvorte Outline Manager a prejdite na kartu Pripojenia s tým kľúčom, ktorý chcete nastaviť. Kliknite na ponuku napravo od riadka kľúča. Kliknite v nej na Dátový limit. Ak chcete zmeniť dátový limit kľúča v sekcii Môj prístupový kľúč, kliknite na ikonu Dátové limity ![Tento obrázok nie je k dispozícii, pretože: nemáte oprávnenia na jeho zobrazenie alebo bol zo systému odstránený](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Vyberte Nastaviť vlastný dátový limit. Keď ste začiarkli toto políčko, zobrazí sa pole, v ktorom budete môcť nastaviť vlastný dátový limit daného kľúča. Po dokončení nastavenia dátového limitu kliknite na tlačidlo ULOŽIŤ.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Po uložení sa bude limit dátových prenosov vybraného kľúča zobrazovať na hlavnej obrazovke spolu so spotrebou dát (za posledných 30 dní).

Ak chcete dátový limit odstrániť z prístupového kľúča, prejdite na jeho dialógové okno Dátový limit tak, ako predtým, zrušte začiarknutie políčka Nastaviť vlastný dátový limit a kliknite na tlačidlo ULOŽIŤ.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Časté otázky o dátovom limite****

****Čo je to 30‑dňový kĺzavý dátový limit?****

 30‑dňový kĺzavý dátový limit spočíta používanie každého kľúča za posledných 30 dní a na dané obdobie obmedzí používanie kľúča tak, aby tento limit neprekročil. Výsledkom je, že kľúč nemôže presiahnuť limit počas ľubovoľného 30‑dňového obdobia vrátane kalendárnych mesiacov s najviac 30 dňami. V praxi to znamená, že dostupné dáta každého používateľa sa každý deň zvýšia o množstvo dát, ktoré daný používateľ použil pred 31 dňami.

**Prečo Outline využíva kĺzavé limity?**

 Kĺzavé limity poskytujú záruku na každé 30‑dňové obdobie. Znamená to, že sa konfigurujú jednoduchšie než opakovaný limit (napríklad prispôsobiteľný deň mesiaca), no zároveň poskytujú podobnú záruku. Okrem toho zodpovedajú existujúcemu zobrazeniu používania dát v službe Outline, ale aj bežným nástrojom, ako sú analytické služby a štatistiky servera.

**Aké dáta sa započítavajú do dátového limitu?**

 Zahŕňajú sa dáta každého prístupového kľúča odchádzajúce zo servera. V presnom slova zmysle ide o dáta odoslané v mene kľúča zo servera, ako aj späť ku klientovi. V praxi by mali tieto dáta relatívne presne zodpovedať prenosu dát z kľúča na server a naspäť. Dúfame preto, že tento údaj bude zodpovedať záznamom vašich používateľov. Vybrali sme odchádzajúce dáta, pretože ide o parameter, ktorý účtujú nami oslovení poskytovatelia cloudu.

**Dostanú používatelia upozornenie, keď prekročia dátový limit?**

 Momentálne nie. Mnoho cloudových poskytovateľov zahŕňa limit napríklad 1 TB na celý mesiac, čo postačuje pre 10 používateľov po 100 GB alebo 100 používateľov po 10 GB. Ide o relatívne vysoké čísla, preto neočakávame, že limit dosiahne veľa používateľov. Dúfame, že používatelia po dosiahnutí limitu kontaktujú správcov servera. Oceníme však vaše poznatky o tom, ako môžu upozornenia pomôcť vo vašom prípade použitia. Môžete nás[kontaktovať tu](https://support.getoutline.org/s/contactsupport).

**Dostanú používatelia upozornenie, keď sa priblížia k dátovému limitu?**

 Množstvo nových dát, ktoré používateľ blížiaci sa k limitu dostane, sa bude denne líšiť, pretože sa zakladá na jeho používaní spred 30 dní. Myslíme si, že upozornenie koncových používateľov skôr mätie, než im pomáha. Radi si prečítame vašu spätnú väzbu k tomuto správaniu, keď ju odošlete na [tejto stránke](https://support.getoutline.org/s/contactsupport).

**Môžem resetovať spotrebu dát používateľa?**

 Nie, limit používateľa vždy zahŕňa posledných 30 dní spotreby dát. Môžete však zvýšiť dátový limit jeho kľúča alebo pre neho vytvoriť nový kľúč.

**Prečo niektorí moji používatelia prišli po aktivácii dátových limitov o prístup?**

 Dátové limity sa zakladajú na používateľových posledných 30 dňoch dátových prenosov, ktoré sú zaznamenané bez ohľadu na to, či boli dátové limity aktivované. Je možné, že dotyční používatelia už prekročili daný limit skôr, ako bol zavedený. Okrem toho pripomíname, že sú presadzované všetky dátové limity, aj keď meníte dátový limit jediného kľúča.

**Môžem nastaviť limit na úrovni servera, napríklad 1 TB na 30 dní?**

 Momentálne nie. Radi sa dozvieme viac o vašom prípade použitia na [tejto stránke](https://support.getoutline.org/s/contactsupport).

**Ak je nastavený predvolený dátový limit aj dátový limit konkrétneho kľúča, ktorý bude presadzovaný?**

 Dátový limit príslušného kľúča prepíše akýkoľvek predvolený dátový limit (ak existuje), ktorý ste nastavili.

**Môžem nastaviť dátový limit konkrétneho kľúča bez konfigurácie predvoleného dátového limitu?**

 Áno. Ak chcete nastaviť dátový limit jedného kľúča, nemusíte definovať predvolený. Môžete napríklad nastaviť limit jedného kľúča, o ktorom si myslíte, že môže byť široko zdieľaný, aby ste sa chránili pred nadmerným dátovým prenosom prostredníctvom daného kľúča.
