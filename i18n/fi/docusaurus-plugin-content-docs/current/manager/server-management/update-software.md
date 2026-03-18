---
title: "Miten päivitän Outline-palvelinohjelmiston?"
sidebar_label: "Miten päivitän Outline-palvelinohjelmiston?"
---

Outline-palvelimille asennetaan uusimmat tietoturvapäivitykset automaattisesti, joten käytössäsi on aina ajantasainen Outline-tekniikka. Automaattinen päivittäminen perustuu avoimen lähdekoodin [Watchtower](https://github.com/v2tec/watchtower)-kirjastoon. Se tarkistaa säännöllisesti docker-tiedoston, joka sisältää Outline-ohjelmiston, ja päivittää sen tarvittaessa.

Kun asennat Outlinen käyttämällä Outline Manageria, sille otetaan käyttöön cron-tehtävä, joka päivittää palvelimen ohjelmiston automaattisesti ja käynnistää sen tarvittaessa uudelleen [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) ‑ominaisuuden (Ubuntu) avulla. Huomaa, että näin ei tehdä, jos edistynyt tila on käytössä, jotta käytössä olevat määritykset voidaan säilyttää. Tämä johtuu siitä oletuksesta, että isäntää käytetään Outlinen lisäksi muihin tarkoituksiin.
