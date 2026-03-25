---
title: Terminologia
sidebar_label: Terminologia
---

## Mikä on VPN?
 VPN eli virtuaalinen yksityisverkko on yksityinen yhteys laitteen ja isäntäpalvelimen välillä. VPN-yhteyttä käyttäessäsi liikenne salataan internetpalveluntarjoajalta. VPN-yhteyttä voi käyttää esimerkiksi

- datan suojaamiseen julkista Wi-Fi-verkkoa käytettäessä
- selausdatan salaamiseen internetpalveluntarjoajalta ja viranomaisilta
- sensuroidun sisällön käyttämiseen eri puolilta maailmaa.

## Miten Outline eroaa perinteisistä VPN:istä?
 Internetpalveluntarjoajat voivat havaita ja estää perinteiset VPN:t helposti tunnistamalla yleisiä suojausprotokollia ja/tai liikennemääriä. Outline on perinteisiä VPN:iä luotettavampi, koska se perustuu protokollaan, joka on vaikea havaita ja estää. Outline on tehokas tapa kiertää kehittyneitä sensuurimenetelmiä, kuten verkkoon perustuvia estoja ja IP-estoja.

## Mikä Outline-palvelin on?
 Kun hyväksytty käyttäjä yhdistää VPN:ään, hän muodostaa yhteyden VPN:n Outline-palvelimeen. Jos luot uutta verkkoa, voit halutessasi käyttää omaa suojattua palvelintasi Outline-palvelimena tai valita esimerkiksi jonkin seuraavista pilvipalveluntarjoajista:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Voit ottaa palvelimen käyttöön Outline Managerin kautta.

## Mikä palvelun ylläpitäjä on? {#servicemanager}
 Palvelun ylläpitäjä on käyttäjä, joka vastaa Outline-palvelimen käyttöönotosta ja pääsyavainten jakamisesta käyttäjille. Yleensä palvelun ylläpitäjä vastaa palvelimen käyttökustannuksista. 

## Mikä pääsyavain on? {#accesskey}
 Pääsyavain mahdollistaa pääsyn Outline-palvelimeen sekä VPN:ään. Saat pääsyavaimen [palvelun ylläpitäjältä](#servicemanager) tai voit [ottaa Outline-palvelimen käyttöön](/manager/server-setup/setup-server) itse. Tässä on esimerkki pääsyavaimesta (ei-toimiva malli): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Mikä Outline Manager on?
 Outline Manager on työpöytäsovellus, jonka avulla palvelun ylläpitäjä voi ottaa Outline-palvelimen käyttöön, luoda [pääsyavaimia](#accesskey) ja asettaa avainkohtaisen datarajan. Voit ladata Outline Managerin uusimman version [tästä](https://getoutline.org/get-started/#step-3) tai [tästä](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Mikä Outline-asiakassovellus on?
 Outline-asiakassovellus on tietokoneille ja mobiililaitteille saatavilla oleva sovellus, jonka kautta voit yhdistää Outline-palvelimeen ja VPN:ään pääsyavaimen avulla. Voit ladata Outline-asiakassovelluksen uusimman version [tästä](https://getoutline.org/get-started/#step-3) tai [tästä](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Mitä datarajat ovat?
 Outline Managerin avulla palvelun ylläpitäjä voi asettaa pääsyavaimille 30 päivän palautuvan datarajan, jotta käyttö ja kustannukset pysyvät kurissa. Palvelun ylläpitäjä voi asettaa kaikkia avaimia koskevan oletusrajan tai oletusrajasta poikkeavan rajan yksittäisille avaimille. Rajan muutokset ovat voimassa heti. Datankäyttö tarkistetaan tunneittain.

Jos palvelun ylläpitäjä päättää jakaa mittarit Jigsaw'lle, hänen kannattaa katsoa [datankeruun käytännöstä](https://getoutline.org/policies/data-collection), miten datarajojen käytöstä raportoidaan.
