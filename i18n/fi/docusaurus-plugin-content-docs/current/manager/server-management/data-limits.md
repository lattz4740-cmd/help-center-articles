---
title: "Miten voin asettaa datarajoja pääsyavaimiin?"
sidebar_label: "Miten voin asettaa datarajoja pääsyavaimiin?"
---

Voit asettaa datarajan, jota käytetään kaikissa pääsyavaimissa. Aseta raja Outline Managerin asetuksissa. Voit asettaa rajan Datarajat-valitsimella, kun se on otettu käyttöön.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Kun raja on asetettu, näet pääsyavainsivulta, miten lähellä rajaa kukin käyttäjä on. Pääsyavainsivun pylväskaaviossa näkyy datan käyttö 30 viime päivän ajalta.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Voit asettaa yhteisen rajan kaikille pääsyavaimille ja oman datarajan kullekin yksittäiselle avaimelle. Tämä asetus ohittaa datarajalle asetetun oletusarvon. Jos et kuitenkaan ole asettanut oletusdatarajaa, voit silti asettaa datarajan mille tahansa avaimelle. 

 Voit asettaa avaimelle datansiirtorajan Outline Managerissa. Siirry Yhteydet-välilehdelle, jolta löydät haluamasi avaimen, ja klikkaa avaimen rivin oikealla puolella olevaa valikkoa. Klikkaa sitten "Dataraja". Voit muuttaa "Oma pääsyavaimeni" ‑kohdassa olevaa datarajaa klikkaamalla Datarajat-kuvaketta ![Datarajat-kuvake](/images/data-limits-icon.png).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Valitse "Aseta oma dataraja". Kun tämä ruutu on merkitty valituksi, näytöllä näkyy kenttä, jossa voit asettaa oman datarajan kyseiselle avaimelle. Kun olet valmis, tallenna dataraja klikkaamalla TALLENNA-painiketta.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Kun olet tallentanut datansiirtorajan valitsemallesi avaimelle, raja näkyy päänäkymässä kunkin avaimen datan käytön (30 viime päivän ajalta) vieressä.

Voit poistaa pääsyavaimen datarajan siirtymällä avaimen Dataraja-valintaikkunaan edellä kuvatulla tavalla, poistamalla valinnan "Aseta oma dataraja" ‑ruudusta ja klikkaamalla TALLENNA-painiketta.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Usein kysyttyä datarajoista
## Mikä on 30 päivän palautuva dataraja?
 30 päivän palautuva dataraja laskee datan käytön kunkin pääsyavaimen osalta 30 päivän ajalta. Datan käyttö pääsyavaimella ei voi ylittää rajaa kyseisellä ajanjaksolla. Tämä tarkoittaa sitä, että datan käyttö pääsyavaimella ei voi ylittää rajoitusta 30-päiväisten tai sitä lyhyempien kalenterikuukausien eikä minkään muun 30 päivän jakson aikana. Käytännössä tämä tarkoittaa sitä, että käyttäjän datarajaan päivittäin vapautuva määrä vastaa 31 päivää aiemmin käytetyn datan määrää.

## Miksi Outline käyttää palautuvia rajoja?
 Palautuva raja takaa datan enimmäiskäytön minkä tahansa 30 päivän jakson aikana. Tämä tarkoittaa, että se on helpompi määrittää kuin toistuva rajoitus (esimerkiksi vapaavalintainen päivä kuukaudessa) mutta dataa on silti käytettävissä samankaltainen määrä. Lisäksi palautuva dataraja vastaa nykyistä Outline-datan käytön esitystapaa sekä analytiikkapalveluita, palvelintilastoja ja muita yleisiä työkaluja.

## Millainen data lasketaan mukaan datarajaan?
 Kullakin pääsyavaimella palvelimelta lähetetty data sisältyy laskelmaan. Tällä tarkoitetaan dataa, joka lähetetään palvelimelta pääsyavaimen pyynnöstä, sekä takaisin asiakassovellukselle lähetettyä dataa. Tämän pitäisi käytännössä olla lähes yhtä suuri kuin pääsyavaimelta palvelimelle ja takaisin lähetetyn datan määrä, joten toivomme, että laskelmat vastaavat käyttäjiesi odotuksia. Laskelmamme perustuvat lähetettyyn dataan, koska kyselyihimme vastanneet pilvipalveluntarjoajat laskuttavat sen mukaan.

## Ilmoitetaanko käyttäjille datarajan ylittymisestä?
 Ei tällä hetkellä. Monien pilvipalveluntarjoajien raja on esimerkiksi 1 Tt kuukaudessa, mikä vastaa esim. 100 Gt:n käyttöä 10 käyttäjältä tai 10 Gt:n käyttöä 100 käyttäjältä. Luvut ovat suurehkoja ja pidämme niiden ylittymistä melko epätodennäköisenä. Toivomme, että datarajan saavuttaneet käyttäjät ottavat yhteyttä palvelimensa ylläpitäjään. Olisimme kuitenkin kiitollisia, jos voisit kertoa, miten ilmoituksista olisi hyötyä omassa käyttötapauksessasi. Voit ottaa meihin yhteyttä [täällä](/about/feedback).

## Ilmoitetaanko käyttäjille datarajan saavuttamisesta?
 Käyttäjille palautuvan uuden datan määrä vaihtelee päivittäin, koska määrä perustuu 30 päivän takaiseen datan käyttöön. Mielestämme ilmoitukset saattaisivat pikemminkin hämmentää loppukäyttäjiä tällaisissa tapauksissa. Pyydämme antamaan palautetta tällaisesta toimintamallista [täällä](/about/feedback).

## Voinko nollata käyttäjän datan käytön?
 Et voi. Käyttäjän raja sisältää aina datan käytön kuluneiden 30 päivän ajalta. Voit kuitenkin nostaa avaimen datarajaa tai luoda käyttäjälle uuden avaimen.

## Otin datarajat käyttöön. Miksi osalla käyttäjistä ei enää ole pääsyoikeutta?
 Datarajat perustuvat käyttäjien datan käyttöön kuluneiden 30 päivän ajalta. Datankäyttö kirjataan, olivatpa datarajat otettu käyttöön tai ei. On mahdollista, että kyseiset käyttäjät ovat ylittäneet rajansa jo ennen toiminnon käyttöönottoa. Huomaathan myös, että kaikki datarajat ovat pakotettuja, vaikka muuttaisit vain yksittäisen avaimen datarajaa.

## Voinko asettaa koko palvelinta koskevan rajan, esim. "1 Tt 30 päivän aikana"?
 Et tällä hetkellä. Pyydämme sinua kertomaan omasta käyttötapauksestasi [täällä](/about/feedback).

## Jos käytössä on oletusdataraja tai tietyllä avaimella on oma dataraja, kumpi pakotetaan käyttöön?
 Tietyn avaimen dataraja ohittaa kaikki asettamasi oletusdatarajat.

## Voinko asettaa datarajan tietylle avaimelle määrittämättä oletusdatarajaa?
 Kyllä. Datarajan asettaminen tietylle avaimelle ei edellytä oletusdatarajan määrittämistä. Voit esimerkiksi asettaa rajan tietylle avaimelle, jonka olet jakanut useille käyttäjille. Näin voit estää liiallisen datankäytön kyseisen avaimen kautta.
