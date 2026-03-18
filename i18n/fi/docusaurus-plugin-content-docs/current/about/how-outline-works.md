---
title: Outlinen toiminta
sidebar_label: Outlinen toiminta
---

**Palvelimen asentaminen**

 ​Vaikka Outlinen asentaminen saattaa vaikuttaa yksinkertaiselta, palvelimen asennuksen taustalla on erilaisia monimutkaisia vaiheita. Aina kun Outline asennetaan, asennusskripti suorittaa seuraavat vaiheet:

- Shadowbox-näköistiedoston vakaa versio noudetaan ja tuodaan Dockerin avulla. Näköistiedosto sijaitsee [Quay.io](https://quay.io/)-palvelussa osoitteessa [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Näköistiedosto sisältää Outline-palvelimen ja Management APIn, jolla Outline-palvelimen hallintasovelluksen käyttäjä voi myöhemmin luoda ja poistaa pääsyavaimia, sallia tai kieltää anonyymien tietojen lähettämisen jne.
- [Watchtower](https://github.com/v2tec/watchtower) asennetaan ja määritetään niin, että se tarkistaa näköistiedoston päivitykset tunnin välein. Tämä auttaa varmistamaan, että Outline-palvelimelle on aina asennettu uusimmat ominaisuudet ja tietoturvaparannukset.
- Verkkopalvelin käynnistyy Management APIin pääsyä varten. Palvelin käyttää salaista ja satunnaista porttia sekä satunnaista polkua.
- [Itse allekirjoitettu SSL-varmenne](https://en.wikipedia.org/wiki/Self-signed_certificate) luodaan, jotta Outline-palvelimen hallinta voidaan salata TLS-standardin mukaisesti, vaikka sillä ei ole verkkotunnusta. Tälle varmenteelle luodaan myös yksilöllinen tunnistetiedosto, joka tallennetaan Outline Manager ‑sovellukseen, mikä auttaa ehkäisemään MITM-hyökkäyksiä.

Outlinea ei tarvitse määrittää sen jälkeen, kun se on asennettu.

**Palvelimen tietoturva**

 Outline-ohjelmisto käyttää avointa lähdekoodia, mikä tarkoittaa, että kuka tahansa voi nähdä koodin ja parantaa sitä haavoittuvuuksia havaitessaan. Koodimme on saatavilla [GitHubissa](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Lisäksi kaikki asennetut Outline-palvelimet päivittyvät automaattisesti heti, kun uusi versio julkaistaan. Näin varmistetaan, että yksikään Outline-palvelin ei käytä ohjelmiston vanhoja versioita.

 Outline Manager ‑sovellus on yhteydessä Outline-palvelimen hallintapalveluun palvelimen pääsyavainten hallintaa varten. Hallintapalvelu käyttää sattumanvaraista porttia ja yksilöllistä, salaista polkua. Hallintapalveluun kohdistuvia urkintayrityksiä on vaikeutettu siten, että palvelu ei vastaa kyselyihin, ellei oikeaa salaista polkua ole määritetty. Lisäksi kaikki yhteydenpito hallintapalveluun on salattu [itse allekirjoitetulla SSL-varmenteella](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Outline-palvelin ei tallenna lokeja, joten mahdollisesti vaarantunut käyttäjädata ei paljastu. Lue lisää [täältä](https://support.getoutline.org/s/article/Security-and-privacy). [Radically Open Security](https://radicallyopensecurity.com/) ja [Cure53](https://cure53.de/) auditoivat Outlinen vuonna 2018. Lue niiden raportit [täältä](https://support.getoutline.org/s/article/Security-and-privacy).

**UDP-liikenteen käsitteleminen**

 Outline voi toimia koko järjestelmän kattavana VPN-verkkona, jolloin kaikki UDP-liikenne kulkee Outline-palvelimen kautta.

**DNS-liikenne**

Outline suorittaa kaikki DNS-haut Outline-palvelimen kautta ja suojaa niitä samoilla salausmenetelmillä kuin kaikkea muutakin verkkotoimintaa. DNS-kyselysi lähetetään Outline-palvelimen kautta Dyn Internet Guideen, OpenDNS:ään, Cloudflare DNS:ään tai Quad9 DNS:ään. Outline ei koskaan kirjaa DNS-hakuja.
