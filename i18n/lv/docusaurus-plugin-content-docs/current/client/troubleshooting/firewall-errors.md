---
title: Ugunsmūra kļūdas
sidebar_label: Ugunsmūra kļūdas
---

Tālāk ir raksturoti trīs iespējamie ugunsmūra problēmu veidi.

## Bloķēšanu var veikt tīkla ugunsmūris.

Ja mēģināt instalēt programmatūru Outline, kad ir izveidots savienojums ar tīklu, kuru aizsargā ugunsmūris, piemēram, skolā vai darbavietā, mēģiniet veikt instalēšanu citā tīklā.

Ja tas nedarbojas, sazinieties ar tīkla administratoru, lai nodrošinātu atļauju savienojuma izveidei starp ugunsmūra aizsargātu tīklu un Outline serveri. Jums būs jāzina sava Outline servera IP adrese un porti, kuros darbojas programmatūra Outline — tie ir norādīti instalācijas skripta beigās.

**Bloķēšanu var veikt ierīces ugunsmūris**.

Ja ierīcē ir programmatūra, kas bloķē nestandarta portu vai neatzītas programmatūras (CheckPoint ZoneAlarm) izejošos savienojumus, skatiet ierīces vai programmatūras dokumentāciju, lai uzzinātu, kā izveidot izņēmumu programmatūrai Outline.

## Bloķēšanu var veikt servera ugunsmūris.

Jūsu izvēlētais mākoņpakalpojumu sniedzējs var pieprasīt izņēmumu manuālu izveidi servera ugunsmūrim, lai atvērtu portus, kuros darbojas programmatūra Outline. Pēc instalēšanas skripta palaišanas jums bija jābūt piešķirtiem diviem nejauši atlasītiem portiem, kuros serverī darbojas programmatūra Outline. Būtu jāpietiek ar šo abu portu atvēršanu.

 Lai izveidotu izņēmumus servera ugunsmūrim, iesakām skatīt tālāk norādīto dokumentāciju un meklēt “ufw” un “iptables”.

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
