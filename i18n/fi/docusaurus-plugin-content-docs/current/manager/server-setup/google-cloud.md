---
title: Google Cloudin automaattinen käyttöönotto
sidebar_label: Google Cloudin automaattinen käyttöönotto
---

## Yleiskatsaus

Outline Managerissa on ominaisuus, jonka avulla voit määrittää Outline-palvelimen automaattisesti Google Cloudia käyttävällä palvelimella. Jos käytät tätä ominaisuutta, Outline Manager pyytää sinua kirjautumaan sisään Google-tililläsi, jotta paikallinen Outline Manager ‑järjestelmä saa tietyt [OAuth](https://developers.google.com/identity/protocols/oauth2)-luvat Google Cloud ‑tilisi määrittämistä varten.

 Jos et halua antaa näitä lupia, voit suorittaa Outlinen Google Cloud Platformissa Outline Managerin edistyneen käyttöönoton ohjeiden mukaisesti.

## Luvat

Automaattista määritystä varten Outline Manager tarvitsee Google-tililtäsi seuraavat luvat.

## Google Cloud Platform

- Google Compute Engine ‑materiaalien näkeminen ja ylläpito
- Datasi tarkastaminen kaikissa Google Cloud ‑palveluissa ja Google-tilisi sähköpostiosoitteen tarkastaminen

## Tilin perustiedot

- Google-tilin ensisijaisen sähköpostiosoitteen näkeminne
- Sinun yhdistämisesi Googlessa näkyviin henkilökohtaisiin tietoihin, jotka olet määrittänyt julkisiksi

## Lisäpääsyoikeudet

- Cloud Platform ‑projektien ylläpito
- Google Cloud Platform ‑laskutustilien näkeminen ja ylläpito
- Google API ‑palvelukokoonpanon hallinnointi

Nämä luvat mahdollistavat Outline-palvelintesi ylläpitoa koskevien lisätoimintojen tukemisen. Näitä ovat esimerkiksi seuraavat:

- Oikean laskutustilin valitsemismahdollisuus
- Uuden projektin luominen Outline-palvelinten järjestämistä varten
- Käytettävissä olevien palvelinkeskusten luettelointi
- Uusien virtuaalikoneiden luominen Outlinea varten
- Uuden virtuaalikoneen määrittäminen Outlinella

## Käyttöoikeuksien peruminen

Voit perua Outline Managerin pääsyn Google Cloud Platformiin [Oma tili](https://myaccount.google.com/permissions) ‑sivulla. Jos perut pääsyn, automaattisen määrityksen kautta luomasi palvelimet pysyvät käytössä mutta ne eivät enää näy Outline Managerissa. Jos haluat palauttaa pääsyn niihin, muodosta uusi yhteys Google Cloud Platformiin aloittamalla automaattisen määrityksen käyttö.

## Outline-projektien järjestäminen

Google Cloudin automaattinen määritys järjestää Outline-palvelimesi yksittäisen [Google Cloud ‑projektin](https://cloud.google.com/resource-manager/docs/creating-managing-projects) avulla. Projekti luodaan, kun automaattista määritystä käytetään ensimmäisen kerran, ja sille ehdotettu projektitunnus koostuu sanasta “Outline-” ja sitä seuraavasta satunnaisten merkkien jonosta. Halutessasi voit valita luomisvaiheessa jonkin muun projektitunnuksen. Projektin nimeksi tulee “Outline servers” (Outline-palvelimet).

## Laskutustili

Google Cloud ‑projekteissa on oltava linkitetty "laskutustili", joka määrittää maksutiedot. Kun käytät Google Cloudin automaattista määritystä ensimmäisen kerran, sinua pyydetään lisäämään Outline-palvelimiisi yhdistettävä laskutustili. Joskus palvelin lakkaa toimimasta, koska laskutustilissä on jokin ongelma. Jos näin käy, sinun kannattaa kirjautua [Google Cloud Consoleen](https://console.cloud.google.com/getting-started), etsiä Outlineen yhdistetty Google Cloud ‑projekti (nimeltään "Outline servers") ja päivittää laskutusasetukset.

## Palvelinten tuhoaminen

Jos haluat tuhota automaattisen käyttöönoton kautta luodut palvelimet, voit tehdä sen helpoiten Outline Managerissa. Jos kuitenkin haluat tuhota palvelimet itse, voit kirjautua [Google Cloud Consoleen](https://console.cloud.google.com/getting-started), etsiä alkumäärityksen aikana luodun projektin (nimeltään "Outline servers") ja joko poistaa resurssit sieltä tai lopettaa projektin.
