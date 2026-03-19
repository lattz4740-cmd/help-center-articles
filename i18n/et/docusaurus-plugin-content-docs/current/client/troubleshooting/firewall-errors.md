---
title: Tulemüüri vead
sidebar_label: Tulemüüri vead
---

Teil võib tulemüüriga seoses ilmneda kolme tüüpi probleeme.

## Teid võib blokeerida võrgu tulemüür.

Kui üritate installida Outline'i ja olete ühendatud tulemüüriga võrguga, näiteks koolis või töökohas, proovige installida muu võrgu kaudu.

Kui see ei toimi, võtke ühendust oma võrguadministraatoriga, et lubada ühendused tulemüüriga võrgu ja teie Outline'i serveri vahel. Teil on vaja teada oma Outline'i serveri IP-aadressi ja porte, kus Outline töötab, mis on märgitud installiskripti lõpus.

## Teid võib blokeerida seadme tulemüür.

Kui teie seadmes on tarkvara, mis blokeerib mittestandardsete portide väljaminevad ühendused või tundmatu tarkvara (CheckPointi ZoneAlarm), vaadake seadme või tarkvara dokumentidest teavet Outline'i jaoks erandi loomise kohta.

## Teid võib blokeerida serveri tulemüür.

Teie valitud pilveteenuste pakkuja võib nõuda, et looksite serveri tulemüüri jaoks käsitsi erandid, et avada pordid, milles Outline töötab. Pärast installiskripti käitamist esitati teile kaks juhuslikult valitud porti, milles Outline teie serveris töötab. Nende kahe pordi avamisest peaks piisama.

 Serveri tulemüüri erandi loomiseks soovitame teil vaadata programmide „UFW“ ja „iptables“ dokumentatsiooni:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
