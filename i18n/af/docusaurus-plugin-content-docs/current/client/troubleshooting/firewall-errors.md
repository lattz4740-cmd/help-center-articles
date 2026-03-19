---
title: Brandmuurfoute
sidebar_label: Brandmuurfoute
---

Jy kan drie tipes brandmuurfoute teëkom:

## Jy kan deur ’n netwerkbrandmuur geblokkeer word.

Indien jy Outline probeer installeer terwyl jy aan ’n brandmuurnetwerk gekoppel is, byvoorbeeld by ’n skool of werkplek, moet jy eerder probeer om dit op ’n ander netwerk te installeer.

Indien dit nie werk nie, moet jy asseblief jou netwerkadmin kontak om verbindings tussen die brandmuurnetwerk en jou Outline-bediener toe te laat. Jy sal jou Outline-bediener se IP-adres moet ken, asook die poorte waardeur Outline loop. Dit word aan die einde van die installasieskrip aangedui.

## Jy kan deur ’n toestelbrandmuur geblokkeer word.

Indien jy sagteware op jou toestel het wat uitgaande verbindings op nie-standaardpoorte blokkeer, of sagteware wat nie herken word nie (CheckPoint se ZoneAlarm), moet jy jou toestel of sagteware se dokumente raadpleeg om uit te vind hoe om ’n uitsondering vir Outline te skep.

## Jy kan deur ’n bedienerbrandmuur geblokkeer word.

Die wolkverskaffer wat jy gekies het, kan van jou verwag om handmatig uitsonderings tot jou bedienerbrandmuur te skep om die poorte waardeur Outline loop, oop te maak. Ná jy die installasieskrip laat loop het, behoort jy twee lukraak gekose poorte te kry waar Outline op jou bediener loop. Dit behoort te werk as hierdie twee poorte oopgemaak word.

 Om uitsonderings op jou bedienerbrandmuur te skep, beveel ons aan dat jy na die dokumente vir “ufw” en “iptables” kyk:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
