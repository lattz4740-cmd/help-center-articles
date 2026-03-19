---
title: Svona virkar Outline
sidebar_label: Svona virkar Outline
---

## Uppsetning þjóns
 ​Jafnvel þótt uppsetning Outline virðist einföld fer flókið ferli fram bakvið tjöldin til að ljúka uppsetningu þjónsins. Þegar Outline er sett upp keyrir uppsetningarskrifta eftirfarandi skref:

- Stöðug útgáfa Shadowbox-myndar er sótt og flutt inn með Docker. Myndin er hýst á [Quay.io](https://quay.io/), á [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Þessi mynd inniheldur Outline-þjóninn og forritaskil stjórnunar sem þjónsstjórnunarforrit Outline notar síðan til að búa til og fjarlægja aðgangslykla, samþykkja/hafna skráningu nafnlausra mæligilda o.s.frv.
- [Watchtower](https://github.com/v2tec/watchtower) er sett upp og stillt á að athuga með myndauppfærslur á klukkustundarfresti í því skyni að tryggja að hver einasti Outline-þjónn sé alltaf uppfærður með nýjustu eiginleikunum og öryggisúrbótunum.
- Vefþjónn, sem er notaður til að fá aðgang að forritaskilum stjórnunar, er ræstur á handahófsvalinni gátt á leynilegri og handahófsvalinni slóð.
- [Sjálfundirritað SSL-vottorð](https://en.wikipedia.org/wiki/Self-signed_certificate) er búið til svo að hægt sé að dulkóða stjórnun Outline-þjónsins með TLS þrátt fyrir að ekkert lénsheiti sé fyrir hendi. Einkvæmt fingrafar þessa vottorðs er einnig búið til og vistað í Outline Manager-forritinu í því skyni að koma í veg fyrir MITM-árásir.

Uppsetning Outline krefst engra grunnstillinga eftir uppsetningu.

## Öryggi þjóns
 Hugbúnaður Outline er með opinn kóða. Það þýðir að hver sem er getur skoðað kóðann og gert endurbætur á honum ef veikleikar uppgötvast. Kóðinn okkar er hýstur á [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Enn fremur skal þess getið að allir uppsettir Outline-þjónar eru uppfærðir um leið og ný útgáfa býðst. Þannig er tryggt að enginn Outline-þjónn keyri gamlar útgáfur hugbúnaðarins.

 Til að stjórna aðgangslyklum á þjóninum á Outline Manager-forritið í samskiptum við stjórnunarþjónustu á Outline-þjóninum. Stjórnunarþjónustan keyrir á handahófsvalinni gátt og á leynilegri og einkvæmri slóð. Ekki er hægt að eiga við stjórnunarþjónustuna sjálfa þar sem hún svarar ekki fyrirspurnum nema viðeigandi leynileg slóð sé tilgreind. Að lokum skal þess getið að öll samskipti við stjórnunarþjónustuna eru dulkóðuð með [sjálfundirrituðu SSL-vottorði](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Auk þess vistar Outline-þjónninn enga annála, svo jafnvel þótt árás yrði gerð á hann myndu engin notkunargögn verða gefin upp. Nánar [hér](/about/security-and-privacy). Árið 2018 gekkst Outline undir endurskoðanir [Radically Open Security](https://radicallyopensecurity.com/) og [Cure53](https://cure53.de/). Skýrslurnar má finna [hér](/about/security-and-privacy).

## Meðhöndlun UDP-umferðar
 Outline getur keyrt sem VPN í öllu kerfinu sem þýðir að allri UDP-umferð er beint um göng í gegnum Outline-þjóninn

## DNS-umferð
Outline framkvæmir allar DNS-uppflettingar í gegnum Outline-þjóninn og ver þær með sömu dulkóðun og er notuð fyrir alla aðra netvirkni. DNS-fyrirspurnir fara í gegnum Outline-þjóninn yfir í Dyn Internet Guide, OpenDNS, Cloudflare DNS eða Quad9 DNS. Outline skráir aldrei DNS-uppflettingar.
