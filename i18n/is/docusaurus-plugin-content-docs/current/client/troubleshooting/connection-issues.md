---
title: "Hvers vegna get ég ekki tengst Outline-þjóni?"
sidebar_label: "Hvers vegna get ég ekki tengst Outline-þjóni?"
---

Nokkrar ástæður gætu valdið því að þú getur ekki tengst Outline-þjóni:

- **Tækið þitt**/client/troubleshooting/connection-issues#One[**aftengdist netinu**](#Internetissues)[#Internetissues](#Internetissues)**.**Stundum rofnar nettenging tækisins og smástund getur liðið áður en netkerfistáknin uppfærast. Einnig er mögulegt að tækið þitt sé tengt staðarnetinu en að netið liggi niðri.
- **Mögulega**/client/troubleshooting/connection-issues#Two[**lokar eldveggur netkerfisins á aðgang**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[a](#FirewallIssues)ð Outline-þjóninum.**Þetta er algengt ef þú tengist skóla- eða vinnuneti eða gjaldfrjálsu, þráðlausu neti.
- **Tækið þitt er með**/client/troubleshooting/connection-issues#Three[**eldvegg eða vírusvarnarhugbúnað**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**sem loka á aðgang að Outline-þjóninum.**
- **Það gæti**[**þurft að breyta stillingum**](#DeviceSettings)**símtækisins þíns.**
- **Þjónustustjórinn gæti hafa**[**eyðilagt þjóninn eða hugsanlega lokar netþjónustan þín á beiðnina**](#ServerIssues) .

## Vandamál varðandi nettengingu: {#Internetissues}

### Svona er prófun gerð:

Slökktu á Outline og athugaðu hvort netið tengist á ný.

- Ef svo er má finna fleiri úrræðaleitarkosti hér að neðan.
- Ef svo er ekki skaltu hinkra í augnablik til að sjá hvort tengingarstillingarnar uppfærist sjálfkrafa.

### Atriði sem þarf að laga:

Tengdu tækið aftur við netið:

1. Athugaðu hvort annað tæki getur tengst sama neti. Ef önnur tæki geta ekki tengst netinu er hugsanlegt að netið liggi niðri og þú þurfir að bíða þar til tenging kemst aftur á eða leita frekari úrræða.
2. Ef önnur tæki geta tengst sama neti geturðu reynt eitt eða fleiri eftirfarandi ráða til að tengjast netinu á ný:
   1. Sett tækið í flugstillingu (snjalltæki)
   2. Endurræst tækið
   3. Slökkt á tækinu, beðið í 2 mínútur og kveikt svo aftur á því

## Vandamál varðandi eldvegg netkerfis: {#FirewallIssues}

### Svona er prófun gerð:

1. Aftengstu núverandi WiFi-neti eða netinu sem þú tengist með snúru.
2. Tengstu öðru neti, t.d. farsímaneti
3. Prófaðu að tengjast Outline-þjóninum aftur

Þetta er vandamálið ef þú getur tengst á öðru neti.

### Atriði sem þarf að laga:

Hafðu samband við þjónustustjórann og biddu hann um að leyfa aðgang að Outline-þjóninum þínum eða haltu áfram að nota annað net.

## Vandamál varðandi eldvegg eða vírusvarnarhugbúnað: {#SoftwareIssues}
### Svona er prófun gerð:
 Prófaðu að tengjast Outline í öðru tæki.

Athugaðu: Mundu að þú þarft aðgangslykil og Outline-forritið til að nota Outline í öðru tæki.

### Atriði sem þarf að laga:
Athugaðu stillingar eldveggsins eða vírusvarnarhugbúnaðarins til að ganga úr skugga að þær séu stilltar þannig að VPN- og Outline-umferð sé hleypt í gegn.

## Tækjastillingar: {#DeviceSettings}

## Atriði til að athuga: {#ServerIssues}
Í Android:

1. Opnaðu stillingaforritið.
2. Finndu **VPN-stillingar** í tækinu (VPN-stillingarnar sýna öll VPN-forrit sem eru með aðgang að símanum eins og stendur.)
3. Ef þú finnur ekki Outline í VPN-stillingunum skaltu fjarlægja Outline og setja það upp aftur. Tækið ætti að veita Outline aðgang sjálfkrafa þegar það er uppsett.

Gakktu úr skugga um að engin forrit fyrir skjáyfirlögn séu uppsett í Android-tækinu þar sem það kann að senda Outline-heimildagluggann í bakgrunninn og koma í veg fyrir að hann sjáist í forgrunninum.

 Opnaðu „Stillingar > Forrit > Sérstakur aðgangur forrits“ í Android-tækinu. Ýttu síðan á „Sýna yfir öðrum forritum“. Þú getur fjarlægt aðgang að öllum forritum sem leyfa slíka virkni.

 Fyrir iOS: Lestu[þessa hjálpargrein](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Vandamál varðandi þjón:

### Svona er prófun gerð:
Ef þú ert með aðgang að fleiri en einum þjóni skaltu prófa að tengjast hinum þjóninum.

### Atriði sem þarf að laga:

Hafðu samband við þjónustustjóra til að athuga hvort þjóninn hafi verið eyðilagður. Ef svo er skaltu biðja viðkomandi um [aðgangslykil](/about/terminology) að öðrum þjóni.

Ef þú settir þjóninn upp skaltu prófa að tengja hann í gegnum Outline Manager eða með öðrum hætti, t.d. með [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Ef það virkar ekki geturðu prófað að skoða stjórnborð skýjaþjónustunnar, ef það er til staðar, til að athuga hvort þjónninn sé ennþá á netinu.
