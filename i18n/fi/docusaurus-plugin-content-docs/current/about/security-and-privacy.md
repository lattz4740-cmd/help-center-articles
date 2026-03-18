---
title: Outlinen tietoturva ja yksityisyys
sidebar_label: Outlinen tietoturva ja yksityisyys
---

Outlinen tietoturva ja yksityisyys

## Miten Outline suojaa verkkoviestintääsi?

Internetliikennettä on helpointa valvoa, kun se kulkee paikallisen tai kansallisen verkon kautta.

Outline auttaa pitämään viestintäsi yksityisenä salaamalla internetliikenteesi sen kulkiessa kansallisessa verkossa ja pitämällä sen salattuna, kunnes se saapuu Outline-palvelimelle. Kun liikenne salataan Outlinella, verkkoa valvovat tahot eivät voi tarkastella siirtämiäsi tietoja tai verkkosivustoja, joilla vierailet.

Outlinen avulla voit myös päästä käsiksi suojattuihin viestintätyökaluihin, jotka eivät ole muutoin saatavilla maassasi.

## Salausstandardit

Outline suojaa laitteesi ja Outline-palvelimen välisen liikenteen 256-bittisellä AEAD Chacha2020 IETF Poly 1305 ‑salauksella. AEAD-salaus takaa luottamuksellisuuden, eheyden ja aitouden, ja se toimii erinomaisesti nykyaikaisilla laitteilla.

## Tietoturva-auditoinnit

Radically Open Security ja Cure53 ovat riippumattomia tietoturvajärjestöjä, jotka vertaavat ohjelmistoja uusimpiin suojausstandardeihin. Järjestöt auditoivat Outlinen vuonna 2018. Radically Open Security toteutti täydentävän auditoinnin vuonna 2022 ja Cure53 auditoi Outline SDK:n vuonna 2024. Voit lukea raportit täältä:

- [Radically Open Securityn penetraatiotestausraportti (maaliskuu 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Cure53:n penetraatiotestaus- ja auditointiraportti, Jigsaw Outline (joulukuu 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Radically Open Securityn penetraatiotestausraportti (joulukuu 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Cure53:n penetraatiotestausraportti, Jigsaw Outline VPN SDK (tammikuu 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonyymit mittarit ja lokit

Outline valvoo kunkin pääsyavaimen osalta käytettyä kaistanleveyttä siirrettyinä tavuina. Tämän tiedon avulla palvelinten järjestelmänvalvojat voivat vaihtaa pilvipalveluntarjoajalta tilattua kaistanleveyttä tarpeen mukaan, mutta he eivät voi nähdä Outline-palvelimen kautta siirrettyjä tietoja.

Lue lisää Outlinen [datan ja tietojen keruusta](/about/data-collection).

---

## Usein kysyttyä tietoturvasta ja yksityisyydestä

## Voiko Outline tehdä minut anonyymiksi verkossa?

Ei. Outline ei ole anonymisointityökalu. Outline suojaa yksityisyyttäsi potentiaalisilta verkkoa valvovilta tahoilta.

Outline ei takaa täydellistä anonymiteettiä vierailemillasi sivustoilla, sillä ne voivat tunnistaa sinut kirjautuessasi sisään tai esimerkiksi selaimen sormenjäljen perusteella. Useimmissa nykyaikaisissa älypuhelimissa käytetään sovellusliittymää, jonka ansiosta puhelimelle asennetut mobiilisovellukset voivat noutaa sijaintisi laitteen GPS-vastaanottimen avulla välityspalvelimesta riippumatta.

Yleisesti ottaen VPN suojaa erityisesti verkkovalvonnalta, mutta verkossa toimimiseen liittyy aina riskejä. Jos internetpalveluntarjoaja tietää henkilöllisyytesi ennalta ja pystyy valvomaan verkkoliikennettäsi, se saattaa pystyä päättelemään Outline-palvelimesi IP-osoitteen, vaikka käyttäisit VPN:ää. Näiden tietojen perusteella internetpalveluntarjoaja voi estää pääsysi Outline-palvelimelle tai päätellä karkean sijaintisi tai esimerkiksi sen, millaiseen aikaan yleensä käytät verkkoa.

## Näkevätkö muut, että käytän Outlinea?

Mahdollisesti. Käyttämäsi alustat ja palvelut saattavat nähdä, että yhteytesi käyttää pilvipalvelinta. Toisinaan ne voivat päätellä, että käytät VPN:ää, mutta ne eivät voi selvittää internetliikenteesi sisältöä.

## Suojaako Outline minua kaikilta mahdollisilta kyberuhkilta?

Ei. Yksikään työkalu ei yksinään suojaa sinua kaikilta mahdollisilta kyberuhkilta. Outline tarjoaa pääsyn avoimeen internetiin ja parantaa yksityisyyttäsi salaamalla liikenteesi. Suosittelemme kuitenkin, että suojaudut ennakoivasti muilla tavoin muunlaisilta uhkilta, kuten haittaohjelmilta ja tietojenkalastelulta.

Verkkosuojauksesi vahvistamiseksi suosittelemme yhteistyötä organisaation kyberturvallisuusasiantuntijan kanssa. Vaihtoehtoisesti voit pyytää yksilöllistä opastusta [Security Planner](https://securityplanner.org/) ‑sivuston johtavilta tietoturva-asiantuntijoilta. Security Planner tarjoaa ongelmien ratkaisuun selkeät ohjeet ja sopivat kyberturvallisuustyökalut.

Voit myös tutustua muihin [Jigsaw'n](https://jigsaw.google.com/) kyberturvallisuustuotteisiin, kuten [Intraan](https://getintra.org/), [Project Shieldiin](https://g.co/shield) ja [Salasanavaroitukseen](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Onko VPN:n käyttäminen laillista?

Tarkista paikalliset lait ja säädökset sekä valitsemasi pilvipalveluntarjoajan käyttöehdot, ennen kuin alat käyttää Outlinea tai Outline-sovellusta.
