---
title: Kako deluje Outline
sidebar_label: Kako deluje Outline
---

## Namestitev strežnika
 ​Čeprav se namestitev strežnika Outline morda zdi preprosta, se v ozadju izvede zapleteno zaporedje korakov za njegovo namestitev. Pri nameščanju strežnika Outline skript za namestitev izvede naslednje korake:

- Pridobi in uvozi se stabilna različica slike Shadowbox, pri čemer se uporabi Docker. Sliko gosti [Quay.io](https://quay.io/) v shrambi [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Slika vsebuje strežnik Outline in API za upravljanje, ki ga pozneje uporabi aplikacija za upravljanje strežnika Outline, da ustvari in odstrani ključe za dostop, omogoči/onemogoči sporočanje anonimnih meritev itd.
- Namesti in konfigurira se knjižnica [Watchtower](https://github.com/containrrr/watchtower), ki vsako uro preveri, ali so na voljo posodobitve slike, ter tako pomaga zagotavljati, da so vsi strežniki Outline stalno posodobljeni z najnovejšimi funkcijami in varnostnimi izboljšavami.
- Prek naključnih vrat ter skrivne in naključne poti se zažene spletni strežnik, ki se uporablja za dostop do API-ja za upravljanje.
- Ustvari se [samopodpisano potrdilo SSL](https://en.wikipedia.org/wiki/Self-signed_certificate), tako da je mogoče upravljanje strežnika Outline šifrirati s standardom TLS, kljub temu da ni na voljo imena domene. Ustvari se tudi edinstveni prstni odtis tega potrdila, ki se shrani v aplikaciji Upravitelj za Outline in pomaga preprečevati napade s posrednikom.

Po namestitvi strežnika Outline ni potrebna konfiguracija.

## Varnost strežnika
 Programska oprema Outline je odprtokodna, kar pomeni, da si lahko kdor koli ogleda kodo in jo izboljša, če so odkrite ranljivosti. Našo kodo gosti storitev [GitHub](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline).

 Poleg tega se nameščeni strežniki Outline samodejno posodobijo ob vsaki izdaji nove različice, kar zagotavlja, da se v nobenem strežniku Outline ne izvajajo stare različice programske opreme.

 Za upravljanje ključev za dostop v strežniku aplikacija Upravitelj za Outline komunicira s storitvijo za upravljanje v strežniku Outline. Storitev za upravljanje se izvaja prek naključnih vrat ter skrivne in enolične poti. Storitev za upravljanje sama zmanjšuje tveganje, saj se ne odzove na poizvedbe, razen če je navedena ustrezna skrivna pot. Prav tako je vsa komunikacija s storitvijo za upravljanje šifrirana s [samopodpisanim potrdilom SSL](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Poleg tega strežnik Outline ne shranjuje nobenih dnevnikov, zato se tudi v primeru ogroženega strežnika uporabniški podatki ne razkrijejo. Več o tem preberite [tukaj](/about/security-and-privacy). Outline sta leta 2018 pregledali podjetji [Radically Open Security](https://radicallyopensecurity.com/) in [Cure53](https://cure53.de/). Poročila lahko preberete [tukaj](/about/security-and-privacy).

## Obravnavanje prometa UDP
 Outline lahko deluje kot sistemski VPN, kar pomeni, da je ves promet UDP preusmerjen prek strežnika Outline.

## Promet DNS
Outline vsa iskanja DNS izvaja prek strežnika Outline, pri čemer njihovo varnost zagotovi z enakim šifriranjem kot pri vsej drugi omrežni dejavnosti. Poizvedbe DNS bodo prek strežnika Outline poslane v storitev Dyn Internet Guide, OpenDNS, Cloudflare DNS ali Quad9 DNS. Outline nikoli ne beleži vaših iskanj DNS.
