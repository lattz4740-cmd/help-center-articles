---
title: Palomuurivirheet
sidebar_label: Palomuurivirheet
---

Palomuurivirheitä on kolmea tyyppiä:

## Verkon palomuuri saattaa estää käytön.

Jos yrität asentaa Outlinen ollessasi yhteydessä verkkoon, jossa on palomuuri (esimerkiksi ollessasi koulun tai työpaikan verkossa), yritä asentaa Outline toisessa verkossa.

Jos tämä ei onnistu, ota yhteyttä verkon järjestelmänvalvojaan ja pyydä häntä sallimaan yhteydet palomuuritetun verkon ja Outline-palvelimen välillä. Selvitä etukäteen Outline-palvelimesi IP-osoite ja portit, joita Outline käyttää. Outlinen käyttämät portit löydät asennusohjeen lopusta.

**Laitteen palomuuri saattaa estää käytön**.

Jos laitteellasi on ohjelmisto, joka estää lähtevät yhteydet ei-vakiomuotoisiin portteihin tai ei-tunnettuihin ohjelmistoihin (esim. CheckPointin ZoneAlarm), tarkista laitteen tai ohjelmiston ohjeista, miten Outlinea varten luodaan poikkeus.

## Palvelimen palomuuri saattaa estää käytön.

Valitsemasi pilvipalveluntarjoaja saattaa edellyttää, että luot palvelimen palomuurille manuaalisesti poikkeuksia, jotta voit avata Outlinen käyttämät portit. Kun suoritat asennusskriptin, näkyviin tulee kaksi satunnaisesti valittua palvelimesi porttia, joita Outline käyttää. Näiden kahden portin avaamisen pitäisi riittää.

 Katso "ufw"- ja "iptables"-ohjeista, miten voit luoda poikkeuksia palvelimesi palomuuriin:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
