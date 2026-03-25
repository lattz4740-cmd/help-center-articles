---
title: "Kako nastavim omejitve podatkov za ključe za dostop?"
sidebar_label: "Kako nastavim omejitve podatkov za ključe za dostop?"
---

Nastavite lahko omejitev podatkov, ki bo veljala za vse ključe za dostop. Če želite nastaviti omejitev, odprite Upravitelja za Outline in se pomaknite do razdelka Nastavitve. V njem bo prikazan preklopni gumb Omejitve podatkov, ki v položaju za vklop omogoča, da nastavite omejitev.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Ko nastavite omejitev, si lahko na strani s ključi za dostop na paličnem grafikonu, ki prikazuje preneseno količino podatkov v zadnjih 30 dneh, ogledate, kako blizu je vsak uporabnik omejitvi.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Poleg tega, da lahko nastavite omejitev za vse ključe za dostop, lahko omejitev podatkov določite tudi za posamezen ključ. Ta nastavitev bo preglasila katero koli privzeto omejitev podatkov, ki ste jo nastavili, če pa privzete omejitve podatkov niste nastavili, lahko še vedno nastavite omejitev podatkov za kateri koli ključ. 

 Če želite nastaviti omejitev prenosa podatkov za ključ, odprite Upravitelja za Outline, pomaknite se na zavihek Povezave, na katerem je ključ, ki ga želite nastaviti, in kliknite meni na desni strani vrstice ključa. Tam kliknite »Omejitev podatkov«. Če želite spremeniti omejitev podatkov za »Moj ključ za dostop«, kliknite ikono omejitve podatkov ![Slika ni na voljo: Ker nimate pravic, da bi si jo lahko ogledali, ali ker je bila odstranjena iz sistema](/images/data-limits-icon.png).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Izberite možnost »Nastavi omejitev podatkov po meri«. Ko izberete to potrditveno polje, se prikaže polje, v katerem lahko nastavite omejitev podatkov po meri za ta ključ. Ko končate, kliknite gumb SHRANI, da shranite omejitev podatkov.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Ko shranite omejitev prenosa podatkov za izbrani ključ, se ta omejitev prikaže na glavnem zaslonu skupaj s preneseno količino podatkov (v zadnjih 30 dneh) za posamezni ključ.

Če želite odstraniti omejitev podatkov za ključ za dostop, se tako kot prej pomaknite v pogovorno okno Omejitev podatkov za ključ, prekličite izbiro potrditvenega polja Nastavi omejitev podatkov po meri in kliknite gumb SHRANI.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Pogosta vprašanja o omejitvi podatkov
## Kaj je omejitev podatkov na podlagi 30-dnevnega obdobja spremljanja?
 Pri omejitvi prenosa podatkov na podlagi 30-dnevnega obdobja spremljanja se seštevajo prenesene količine podatkov za vsak posamezni ključ v preteklih 30 dneh, pri čemer je zagotovljeno, da prenesena količina podatkov za ključ v zadevnem obdobju ne preseže omejitve. Zato ključ ne more preseči omejitve v nobenem 30-dnevnem obdobju, vključno s koledarskimi meseci, dolgimi 30 dni ali manj. To dejansko pomeni, da se bo količina razpoložljivih podatkov posameznega uporabnika vsak dan povečala za količino, ki jo je prenesel pred 31 dnevi.

## Zakaj Outline uporablja omejitve na podlagi spremljanja?
 Omejitve na podlagi spremljanja zagotavljajo jamstva za 30-dnevno obdobje, kar pomeni, da je njihovo nastavljanje preprostejše kot nastavljanje ponavljajoče se omejitve (na primer prilagodljivega dneva v mesecu), pri čemer zagotavljajo podobna jamstva. Prav tako se ujemajo z obstoječim prikazom prenesene količine podatkov za Outline in običajnimi orodji, kot so analitične storitve in statistični podatki o strežnikih.

## Kateri podatki se upoštevajo pri omejitvi podatkov?
 V skupno količino je vključen izhod iz strežnika pri vsakem ključu za dostop. To se dejansko nanaša na podatke, ki so v imenu ključa poslani iz strežnika in nazaj odjemalcu. Dejansko bi moralo biti to tesno usklajeno s prometom, poslanim iz ključa v strežnik in nazaj, zato upamo, da se bo ujemalo s skupnimi količinami vaših uporabnikov. Izbrali smo izhod, ker to zaračunavajo sodelujoči ponudniki storitev v oblaku.

## Ali bodo uporabniki obveščeni, če bodo prekoračili omejitev podatkov?
 Zaenkrat ne. Številni ponudniki storitev v oblaku ponujajo omejitev, kot je 1 TB, za celoten mesec, ki lahko podpira 10 uporabnikov s prenosom količine 100 GB ali 100 uporabnikov s prenosom količine 10 GB. Te količine so zelo velike, zato pričakujemo, da jih ne bo doseglo veliko uporabnikov. Upamo, da se bodo uporabniki obrnili na skrbnike strežnikov, ko bodo dosegli omejitev. Cenili bomo, če nam boste sporočili, kako bi lahko obvestila pomagala v vašem primeru uporabe, pri čemer se na nas lahko obrnete [tukaj](/about/feedback).

## Ali bodo uporabniki obveščeni, ko se bodo približali omejitvi podatkov?
 Količina novih podatkov, ki jih bo prejel uporabnik, ki se približuje omejitvi, se bo razlikovala glede na posamezen dan, ker omejitev temelji na njegovem prenosu podatkov v predhodnih 30 dneh. Menimo, da bi opozorilo končne uporabnike bolj zmedlo, kot pa jim pomagalo. Cenili bomo, če nam boste povratne informacije o tem vedenju sporočili [tukaj](/about/feedback).

## Ali lahko ponastavim preneseno količino podatkov uporabnika?
 Ne, uporabnikova omejitev vedno vključuje preneseno količino podatkov v zadnjih 30 dneh. Lahko pa povečate omejitev podatkov za njegov ključ ali zanj ustvarite nov ključ.

## Zakaj so nekateri od mojih uporabnikov izgubili dostop takoj, ko je bila omogočena omejitev prenosa podatkov?
 Omejitve podatkov temeljijo na prenosu podatkov uporabnikov v zadnjih 30 dneh, ki se zabeleži ne glede na to, ali so bile omejitve podatkov omogočene ali ne. Možno je, da so zadevni uporabniki presegli omejitev že pred njeno uvedbo. Upoštevajte tudi, da so uveljavljene vse omejitve podatkov, tudi če spremenite omejitev podatkov za en ključ.

## Ali lahko nastavim omejitev za celoten strežnik, na primer »1 TB na vsakih 30 dni«?
 Trenutno ne. Veseli bomo, če nam več informacij o svojem primeru uporabe sporočite [tukaj](/about/feedback).

## Če je na voljo privzeta omejitev podatkov in omejitev podatkov za določen ključ, katera omejitev bo uveljavljena?
 Omejitev podatkov za določen ključ bo preglasila privzeto omejitev podatkov (če ste jo določili).

## Ali lahko nastavim omejitev podatkov za določen ključ, ne da bi nastavil/-a privzeto omejitev podatkov?
 Da. Za nastavitev omejitve podatkov za en ključ ni treba določiti privzete omejitve. Določite lahko na primer omejitev za en ključ, za katerega menite, da se lahko deli s številnimi drugimi osebami, da se zaščitite pred pretiranim prenosom podatkov prek tega ključa.
