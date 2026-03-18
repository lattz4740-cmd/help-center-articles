---
title: "Zakaj ne morem vzpostaviti povezave s storitvijo Outline?"
sidebar_label: "Zakaj ne morem vzpostaviti povezave s storitvijo Outline?"
---

Obstaja več razlogov, zakaj morda ne morete vzpostaviti povezave s storitvijo Outline:

- **Povezava naprave**/client/troubleshooting/connection-issues#One[**z internetom je prekinjena**](#Internetissues)[#Internetissues](#Internetissues)**.**V napravi bo omrežna povezava včasih prekinjena in v tem primeru je treba nekoliko počakati, da se posodobijo ikone za omrežje. Prav tako je mogoče, da je naprava povezana z lokalnim omrežjem, vendar internet ne deluje.
- /client/troubleshooting/connection-issues#Two[**Požarni zid omrežja blokira dostop**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[do](#FirewallIssues) strežnika Outline.**To se pogosto zgodi, če uporabljate javno omrežje, na primer šolsko, službeno ali brezplačno brezžično omrežje.
- **V napravi je**/client/troubleshooting/connection-issues#Three[**požarni zid ali protivirusna programska oprema**](#SoftwareIssues),[#SoftwareIssues](#SoftwareIssues)**ki blokira dostop do strežnika Outline.**
- **Morda boste morali spremeniti**[**nastavitve telefona**](#DeviceSettings)**.**
- **Upravitelj storitve je morda**[**uničil strežnik ali pa vašo zahtevo morda blokira ponudnik internetnih storitev**](#ServerIssues).

## Težave z internetno povezavo: {#Internetissues}

## Kako izvesti preizkus:

Izklopite Outline in preverite, ali je povezava z internetom znova vzpostavljena.

- Če je, si spodaj oglejte več možnosti za odpravljanje težave.
- Če ni, počakajte nekaj trenutkov in preverite, ali so se nastavitve povezave samodejno posodobile.

## Kaj je treba popraviti:

Znova vzpostavite povezavo v napravi:

1. V drugi napravi preverite, ali je mogoče vzpostaviti povezavo z istim omrežjem. Če v drugih napravah ni mogoče vzpostaviti povezave, omrežje morda ne deluje, zato boste morali počakati na vnovični začetek delovanja ali odpraviti težavo.
2. Če lahko druge naprave vzpostavijo povezavo z istim omrežjem, lahko poskusite povezavo v svoji napravi vzpostaviti na enega ali več od teh načinov:
   1. V napravi vklopite način za letalo (mobilna naprava)
   2. Znova zaženite napravo
   3. Izklopite napravo, počakajte 2 minuti in znova vklopite napravo

## Težave s požarnim zidom omrežja: {#FirewallIssues}

## Kako izvesti preizkus:

1. Prekinite povezavo s trenutnim omrežjem Wi-FI ali žičnim omrežjem.
2. Vzpostavite povezavo z drugim omrežjem, na primer z mobilnim omrežjem
3. Poskusite znova vzpostaviti povezavo s strežnikom Outline

Če je mogoče povezavo vzpostaviti prek drugega omrežje, je razlog za težavo nedelujoče trenutno omrežje.

## Kaj je treba popraviti:

Obrnite se na upravitelja storitve z zahtevo, da vam omogoči dostop do strežnika Outline, ali namesto tega še naprej uporabljajte drugo omrežje.

**Težave s požarnim zidom ali protivirusno programsko opremo:**

**Kako izvesti preizkus:**

 Povezavo s strežnikom Outline poskusite vzpostaviti v drugi napravi.

Opomba: Če želite strežnik Outline uporabljati v drugi napravi, ne pozabite, da potrebujete ključ za dostop in aplikacijo Outline.

## Kaj je treba popraviti: {#SoftwareIssues}
Preverite nastavitve požarnega zida ali protivirusne programske opreme in se prepričajte, da ne preprečujejo prometa za VPN in Outline.

## Nastavitve naprave: {#DeviceSettings}

## Kaj je treba preveriti: {#DeviceSettings}
V napravah Android:

1. Odprite aplikacijo z nastavitvami.
2. V napravi poiščite razdelek **Nastavitve za VPN** (v nastavitvah za VPN bodo prikazane vse aplikacije VPN, ki imajo trenutno dostop do telefona).
3. Če v nastavitvah za VPN ne vidite aplikacije Outline, jo odmestite in znova namestite. Naprava mora po namestitvi samodejno omogočiti dostop aplikaciji Outline.

Prepričajte se, da v napravi Android nimate nameščene nobene aplikacije za prekrivanje zaslona, saj lahko ta pošlje okno z dovoljenji za Outline v ozadje, tako da ni vidno v ospredju.

 V napravi Android odprite razdelek »Nastavitve« > »Aplikacije« > »Posebni dostop za aplikacije«. Nato se dotaknite možnosti »Prekrivanje drugih aplikacij«. Odstranite lahko dostop do vseh aplikacij, ki omogočajo takšno vedenje.

 V napravah iOS: Preberite[ta članek s pomočjo](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Težave s strežnikom: {#ServerIssues}

## Kako izvesti preizkus: {#ServerIssues}
Če imate dostop do več strežnikov, poskusite vzpostaviti povezavo z enim od drugih strežnikov.

## Kaj je treba popraviti:

Obrnite se na upravitelja storitve in preverite, ali je bil strežnik uničen. V tem primeru ga prosite za[ključ za dostop](/about/terminology) do drugega strežnika.

Če ste strežnik nastavili vi, poskusite povezavo z njim vzpostaviti prek Upravitelja za Outline ali drugega načina, kot je[protokol SSH](https://en.wikipedia.org/wiki/Secure_Shell). Če to ne deluje, lahko preverite konzolo morebitnega ponudnika storitev v oblaku in se prepričate, ali je povezava s strežnikom še vedno vzpostavljena.
