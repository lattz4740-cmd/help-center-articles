---
title: Terminologija
sidebar_label: Terminologija
---

## Kaj je VPN?
 Navidezno zasebno omrežje (VPN) je zasebna povezava med vašimi napravami in gostiteljskim strežnikom. Ko uporabljate VPN, je vaš promet skrit internetnemu ponudniku. VPN boste morda želeli uporabljati v teh primerih:

- za zaščito podatkov pri uporabi javnega omrežja Wi-Fi;
- za ohranjanje zasebnosti podatkov brskanja pred internetnim ponudnikom in vladnimi agencijami;
- za dostop do necenzurirane vsebine iz različnih virov po vsem svetu.

## Kako se Outline razlikuje od tradicionalnih omrežij VPN?
 Internetni ponudniki lahko s prepoznavanjem pogostih varnostnih protokolov in/ali vzorci količine prometa zlahka zaznavajo in blokirajo tradicionalna omrežja VPN. Outline je prožnejši od tradicionalnih omrežij VPN, saj je ustvarjen z uporabo protokola, ki je zasnovan tako, da ga je težko zaznati in posledično težje blokirati. Outline je odporen na zapletene oblike cenzure, kot je blokiranje na podlagi omrežja ali naslovov IP.

## Kaj je strežnik Outline?
 V strežniku Outline deluje omrežje VPN, s katerim se bodo povezali uporabniki, ki imajo za to dovoljenje. Če ustvarjate novo omrežje, lahko kot strežnik Outline uporabite lastni varen strežnik (če ga imate) ali pa ponudnika storitev v oblaku, na primer:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Strežnik boste nastavili v Upravitelju za Outline.

## Kaj je upravitelj storitev? {#servicemanager}
 Upravitelj storitev je oseba, ki je odgovorna za nastavljanje strežnika Outline in deljenje ključev za dostop z uporabniki. Upravitelj storitev je na splošno odgovoren za stroške uporabe strežnika. 

## Kaj je ključ za dostop? {#accesskey}
 Ključ za dostop se uporablja za dostop do obstoječega strežnika Outline in povezavo z omrežjem VPN. [Upravitelj storitev](#servicemanager) vam bo dal ključ za dostop, lahko pa tudi sami[nastavite strežnik Outline](/manager/server-setup/setup-server). Ključ za dostop je videti na primer tako (samo vzorec; ta ključ ne bo deloval): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Kaj je Upravitelj za Outline?
 Upravitelj za Outline je aplikacija za namizne računalnike, s katero lahko upravitelj storitev nastavi strežnik Outline, ustvari [ključe za dostop](#accesskey) ter nastavi omejitve podatkov za posamezen ključ. Najnovejšo različico Upravitelja za Outline lahko prenesete[tukaj](https://getoutline.org/get-started/#step-3) ali[tukaj](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Kaj je odjemalec za Outline?
 Odjemalec za Outline je aplikacija, ki je na voljo za namizne in mobilne naprave ter s katero se lahko povežete s strežnikom Outline in s ključem za dostop dostopate do strežnika VPN. Najnovejšo različico aplikacije odjemalca za Outline lahko prenesete[tukaj](https://getoutline.org/get-started/#step-3) ali[tukaj](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Kaj so omejitve podatkov?
 Upravitelji storitev lahko z Upraviteljem za Outline za ključe za dostop nastavijo omejitev podatkov na podlagi 30-dnevnega obdobja spremljanja, da preprečijo prekomerno uporabo in lažje zagotovijo predvidljivost stroškov. Upravitelji storitev lahko nastavijo privzeto omejitev, ki velja za vsak ključ, poleg tega pa lahko za poljubni ključ nastavijo drugačno omejitev, s katero preglasijo privzeto. Ko je omejitev nastavljena, začne veljati takoj in se uveljavlja vsako uro.

Če upravitelji storitev omogočijo deljenje meritev s podjetjem Jigsaw, morajo prebrati[pravilnik o zbiranju podatkov](/about/data-collection), kjer najdejo podrobnosti o tem, kako bo sistem poročal o uporabi omejitev podatkov.
