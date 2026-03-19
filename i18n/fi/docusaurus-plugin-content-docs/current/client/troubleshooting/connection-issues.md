---
title: "Miksi en voi muodostaa yhteyttä Outline-palveluun?"
sidebar_label: "Miksi en voi muodostaa yhteyttä Outline-palveluun?"
---

Jos et voi muodostaa yhteyttä Outline-palveluun, siihen voi olla useita syitä:

- **Laite**[**ei ole yhteydessä internetiin**](#Internetissues)**.**Joskus laitteen verkkoyhteys voi katketa ja voi mennä hetki, ennen kuin verkkokuvakkeet päivittyvät. On myös mahdollista, että laitteesi on yhdistetty lähiverkkoon, mutta internetyhteys ei toimi.
- [**Verkon palomuuri estää yhteyden**](#FirewallIssues)**Outline-palvelimeen.**Tämä on yleistä, jos käytät julkista verkkoa, kuten oppilaitoksen tai työpaikan verkkoa tai maksutonta langatonta verkkoa.
- **Laitteessasi on**[**palomuuri tai virustorjuntaohjelma,**](#SoftwareIssues)**joka estää yhteyden Outline-palvelimeen.**
- **Puhelimesi**[**laiteasetuksia**](#DeviceSettings)**on ehkä muutettava.**
- **Palvelun hallinnoija on saattanut**[**poistaa palvelimen, tai internetpalveluntarjoaja saattaa estää pyyntösi.**](#ServerIssues)

## Internetyhteysongelmat: {#Internetissues}

### Testaaminen:

Laita Outline pois päältä ja katso, alkaako internetyhteys toimia uudelleen.

- Jos näin tapahtuu, katso lisää ohjeita ongelmatilanteisiin alta.
- Jos näin ei tapahdu, odota hetki ja katso, päivittyvätkö yhteysasetukset itsestään.

### Korjattavat asiat:

Palauta laitteen verkkoyhteys:

1. Kokeile, voitko muodostaa yhteyden kyseiseen verkkoon jollain muulla laitteella. Jos et voi muodostaa yhteyttä muilla laitteilla, verkon toiminnassa voi olla häiriö. Odota, kunnes häiriö poistuu tai suorita vianetsintä.
2. Jos voit muodostaa yhteyden muilla laitteilla kyseiseen verkkoon, voit yrittää palauttaa laitteen verkkoyhteyden yhdellä tai useammalla seuraavista tavoista:
   1. Aseta laite lentokonetilaan (mobiili).
   2. Käynnistä laite uudestaan.
   3. Sammuta laite, odota kaksi minuuttia ja käynnistä laite sitten uudestaan.

## Verkon palomuurin ongelmat: {#FirewallIssues}

### Testaaminen:

1. Katkaise yhteys nykyiseen Wi-Fi-verkkoon tai langalliseen verkkoon.
2. Muodosta yhteys toiseen verkkoon, kuten mobiiliverkkoon.
3. Yritä muodostaa yhteys Outline-palvelimeen uudelleen.

Jos yhteyden muodostaminen onnistuu toisessa verkossa, olet löytänyt ongelman syyn.

### Korjattavat asiat:

Pyydä palvelun hallinnoijaa sallimaan yhteyden muodostaminen Outline-palvelimeen. Voit myös jatkaa toisen verkon käyttämistä.

## Palomuurin tai virustorjuntaohjelman ongelmat: {#SoftwareIssues}
### Testaaminen:
 Yritä muodostaa yhteys Outlineen toisella laitteella.

Huom. Tarvitset pääsyavaimen ja Outline-sovelluksen, jotta voit käyttää Outlinea toisella laitteella.

### Korjattavat asiat:
Tarkista palomuurin tai virustorjuntaohjelman asetukset varmistaaksesi, että ne sallivat VPN- ja Outline-liikenteen.

## Laiteasetukset: {#DeviceSettings}

## Tarkistettavat asiat: {#ServerIssues}
Android:

1. Avaa Asetukset-sovellus.
2. Etsi laitteen **VPN-asetukset**. Ne näyttävät kaikki VPN-sovellukset, joilla on pääsyoikeus puhelimessa.
3. Jos Outlinea ei näy VPN-asetuksissa, poista sen asennus ja asenna se uudelleen. Laitteen tulisi antaa Outlinelle pääsyoikeus automaattisesti asennuksen yhteydessä.

Varmista, ettei Android-laitteeseen ole asennettu näyttöä peittäviä sovelluksia. Sellaiset saattavat siirtää Outlinen lupaikkunan taustalle, jolloin se ei näy näytöllä.

 Valitse Android-laitteessa Asetukset > Sovellukset > Sovellusten erikoiskäyttö. Valitse sitten "Näytä sovellusten päällä". Poista pääsy sellaisiin sovelluksiin, jotka sallivat näyttämisen päällimmäisenä.

 iOS: Lue [tämä tukiartikkeli](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Palvelinongelmat:

### Testaaminen:
Jos käytössäsi on useampia palvelimia, yritä muodostaa yhteys toiseen palvelimeen.

### Korjattavat asiat:

Kysy palvelun hallinnoijalta, onko palvelin poistettu. Jos näin on, pyydä [pääsyavainta](/about/terminology) toiselle palvelimelle.

Jos otit palvelimen käyttöön itse, yritä muodostaa siihen yhteys Outline Managerin kautta tai esimerkiksi käyttämällä [SSH:ta](https://en.wikipedia.org/wiki/Secure_Shell). Jos tämä ei auta, voit yrittää katsoa pilvipalveluntarjoajan konsolista, onko palvelin yhä online-tilassa.
