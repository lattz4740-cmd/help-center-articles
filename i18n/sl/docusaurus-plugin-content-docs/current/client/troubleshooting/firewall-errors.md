---
title: Napake v zvezi s požarnim zidom
sidebar_label: Napake v zvezi s požarnim zidom
---

Pride lahko do treh vrst težav v zvezi s požarnim zidom:

## Morda vas je blokiral požarni zid omrežja.

Če poskušate Outline namestiti, ko ste povezani z omrežjem, zaščitenim s požarnim zidom, na primer v šoli ali službi, poskusite namestitev izvesti v drugem omrežju.

Če s tem ne odpravite težave, prosite skrbnika omrežja, naj omogoči povezave med omrežjem, zaščitenim s požarnim zidom, in strežnikom Outline. Potrebovali boste naslov IP strežnika Outline in vrata, prek katerih se izvaja Outline, kar je navedeno na koncu skripta za namestitev.

**Morda vas je blokiral požarni zid naprave**.

Če v napravi uporabljate programsko opremo, ki blokira odhodne povezave prek nestandardnih vrat ali neprepoznane programske opreme (na primer ZoneAlarm podjetja CheckPoint), v dokumentaciji za napravo ali programsko opremo poiščite navodila, kako ustvariti izjemo za Outline.

## Morda vas je blokiral požarni zid strežnika.

Pri ponudniku storitev v oblaku, ki ste ga izbrali, je morda treba ročno ustvariti izjeme za požarni zid vašega strežnika, da je mogoče odpreti vrata, prek katerih se izvaja Outline. Po zagonu skripta za namestitev bi se moralo prikazati dvoje naključno izbranih vrat, prek katerih se Outline izvaja v strežniku. Zadostovati bi moralo, da odprete ta vrata.

 Če želite ustvariti izjeme za požarni zid strežnika, priporočamo, da si ogledate dokumentacijo za »ufw« in »iptables«:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
