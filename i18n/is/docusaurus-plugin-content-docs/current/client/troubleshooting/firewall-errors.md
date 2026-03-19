---
title: Vandamál tengd eldvegg
sidebar_label: Vandamál tengd eldvegg
---

Þrjár gerðir vandamála sem tengjast eldvegg geta komið upp:

## Eldveggur netkerfis kann að hafa lokað á þig.

Ef þú reynir að setja upp Outline í gegnum netkerfi sem er á bakvið eldvegg, t.d. skóla- eða vinnunet, skaltu prófa að tengjast öðru neti til að setja upp Outline.

Ef það virkar ekki skaltu hafa samband við kerfisstjórann þinn og óska eftir leyfi fyrir tengingu á milli netkerfisins sem er á bakvið eldvegg og Outline-þjónsins þíns. Þú þarft að gefa upp IP-tölu Outline-þjónsins og gáttirnar sem Outline er keyrt í en þær eru tilgreindar í lok uppsetningarskriftunnar.

## Eldveggur tækis kann að hafa lokað á þig.

Ef þú ert með hugbúnað í tækinu þínu sem lokar á tengingar á útleið í óstöðluðum gáttum eða á óþekkan hugbúnað (ZoneAlarm frá CheckPoint) skaltu skoða fylgiskjöl tækisins eða hugbúnaðarins til að kynna þér hvernig hægt er að gera undantekningu fyrir Outline.

## Eldveggur þjóns kann að hafa lokað á þig.

Skýjaþjónustan sem þú valdir kann að fara fram á að þú búir handvirkt til undantekningar fyrir eldvegg þjónsins til að opna fyrir gáttirnar sem Outline keyrir í. Þegar þú hefur keyrt uppsetningarskriftuna ættu handahófsvöldu gáttirnar tvær sem Outline keyrir í á þjóninum þínum að birtast. Það ætti að nægja að opna þessar tvær gáttir.

 Til að búa til undantekningar fyrir eldvegg þjónsins mælum við með að þú kynnir þér fylgiskjöl fyrir „ufw“ og „iptables“:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
