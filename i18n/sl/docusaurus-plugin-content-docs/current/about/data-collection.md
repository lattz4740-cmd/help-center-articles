---
title: Zbiranje podatkov
sidebar_label: Zbiranje podatkov
---

Outline ne zbira osebnih podatkov, razen če to omogočite. Outline prav tako ne zbira podatkov o spletnih mestih, ki jih obiščete, in o tem, s kom ali o čem komunicirate.

 Če pri ponudniku storitev v oblaku ustvarite račun ali se vanj prijavite prek Upravitelja za Outline, ne pridobimo nobenih podatkov, ki jih posredujete takemu ponudniku, kot so e-poštni naslov, ime, podatki za obračunavanje in podrobnosti o plačilu.

## Podatki, ki jih pridobimo samodejno
 Samodejno zbiramo dve vrsti podatkov.

 1. Naslov IP strežnika

 Naslove IP strežnika Outline zbira [Quay.io](https://quay.io/), pri čemer dostop do teh naslovov pridobimo, ko se strežnik samodejno posodobi za najnovejše izboljšave glede varnosti in funkcij. Prek naslova IP strežnika je morda mogoče prepoznati ponudnika strežnika v oblaku in mesto, v katerem je nastavljen strežnik Outline, vendar na podlagi teh podatkov ni mogoče ugotoviti, kdo upravlja strežnik in kdo dostopa do njega.

 2. Tehnični podatki, ki ne omogočajo osebne prepoznave

 Če se Outline zruši ali pride do usodne izjeme oziroma če ročno pošljete povratne informacije prek aplikacije Outline, se pri tem sporočijo podatki, navedeni spodaj. Ti podatki so uporabljeni samo za lažje ugotavljanje in odpravljanje težav glede stabilnosti ali delovanja.

- Država
- Jezik
- Datum in ura zrušitve/izjeme in do 100 predhodnih dogodkov (npr. uporabnik je odprl razdelek z vizitko)
- Statično prevedena sporočila o izjemi
- Ime in različica operacijskega sistema
- Model telefona (če je primerno)
- Čas zagona aplikacije
- Brskalnik
- Arhitektura
- Različica in številka gradnje aplikacije Outline

Ti podatki so prek protokola HTTPS preneseni podjetju Sentry ([sentry.io](https://sentry.io/)), ki je zunanji ponudnik odprtokodne storitve sledenja napakam. Sentry uporablja različne standardne panožne tehnologije in storitve, s katerimi preprečuje nepooblaščen dostop do vaših podatkov ter njihovo razkritje, uporabo in izgubo. Če imate morebitna vprašanja glede pravilnikov za Sentry, obiščite [https://sentry.io/security/](https://sentry.io/security/) in [https://sentry.io/privacy/](https://sentry.io/privacy/) ali se obrnite na [security@sentry.io](mailto:security@sentry.io). Dostop do vseh podatkov o storitvi Outline, ki jih shrani Sentry, je omejen, pri čemer lahko do njih dostopajo samo člani ekipe za Outline.

## Podatki, ki jih pridobimo samo, če v to privolite
 Ko uporabnik privoli v zbiranje podatkov, začne Outline te podatke pošiljati ekipi za Outline.

 1. Meritve o uporabi

 Vsak strežnik Outline samodejno zbira podatke o številu prenesenih bajtov, količini časa, ko je bil uporabnik povezan s strežnikom, državah in avtonomnih sistemih izvora uporabljenih poverilnic, ter podatke, ali je bila katera koli funkcija omogočena ali onemogočena, pri čemer to zbiranje zajema uporabo v zadnji uri in se izvaja na podlagi ključa za dostop. Vsebina komunikacije in metapodatki, ki omogočajo osebno prepoznavo (npr. podatki za prijavo, e-poštni naslovi, ID-ji naprav itn.), se ne beležijo. Vse meritve so povezane z ID-jem strežnika. Navodila za spreminjanje ID-ja strežnika so na voljo [tukaj](/manager/server-management/reset-server-id).

 Strežniki Outline privzeto ne posredujejo teh meritev ekipi za Outline. Če skrbnik strežnika izrecno omogoči deljenje meritev o uporabi, se ti podatki varno pošiljajo ekipi za Outline vsako uro. Po 60 dneh so meritve o uporabi združene na ravni države. Skrbniki strežnikov lahko nastavitve deljenja meritev o uporabi kadar koli spremenijo prek menija z nastavitvami v Upravitelju za Outline.

 Anonimne meritve o uporabi strežnika uporabljamo za ugotavljanje trendov uporabe in izboljševanje izdelka, zato cenimo, če nam jih posredujete.

 Če skrbnik strežnika na primer omogoči deljenje meritev o uporabi z nami, lahko prejmemo podatke, ki kažejo, da je bil strežnik z ID-jem 12345 včeraj v uporabi več kot 3 ure prek treh ključev, ki so vsi uporabljeni v Združenih državah in Kanadi, pri čemer je prenesel skupno 500 megabajtov podatkov, funkcija za omejitev podatkov pa je bila omogočena.

 2. Vaši komentarji in e-poštni naslov, če pošljete povratne informacije

 V aplikacijah Outline in Upravitelj za Outline lahko ekipi pošljete povratne informacije. Priporočamo, da vanje ne vključite podatkov, ki omogočajo osebno prepoznavo, pri čemer imate na voljo tudi neobvezno polje za e-poštni naslov, ki ga lahko izpolnite, če želite prejeti odgovor ekipe. Prav tako samodejno zbiramo nekatere osnovne podatke za boljše razumevanje vaših povratnih informacij. Podatki, ki jih zbiramo, so opisani v zgornjem razdelku »Podatki, ki jih pridobimo samodejno« pod 2. točko. Več o naših postopkih za zagotavljanje varnosti in zasebnosti v storitvi Outline je na voljo [tukaj](/about/security-and-privacy).

 Če uporabljate različico beta aplikacije Outline v napravi Android, bomo za zbiranje podatkov za odpravljanje napak, na podlagi katerih lahko lažje zaznamo težave in izboljšamo Outline, morda uporabili Googlovo storitev [Firebase](https://firebase.google.com/). Več o pravilnikih storitve Firebase glede zasebnosti in varnosti je na voljo na njenem spletnem mestu: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Če želite, da Outline teh podatkov ne pošilja prek storitve Firebase, uporabite produkcijsko različico aplikacije.
