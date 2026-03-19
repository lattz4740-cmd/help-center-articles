---
title: "Miks ma ei saa Outline'i teenusega ühendust luua?"
sidebar_label: "Miks ma ei saa Outline'i teenusega ühendust luua?"
---

Järgnevalt on toodud mõned põhjused, miks te ei pruugi saada Outline'i teenusega ühendust luua.

- **Teie seadmel**[**puudub internetiühendus**](#Internetissues)**.**Mõnikord katkeb teie seadme võrguühendus ja võrguikoonide värskendamiseks võib kuluda pisut aega. Samuti on võimalik, et teie seade on ühendatud kohaliku võrguga, ent internet ei tööta.
- **Teie**[**võrgu tulemüür blokeerib juurdepääsu**](#FirewallIssues)**teie Outline'i serverile.**See juhtub tavaliselt siis, kui kasutate avalikku võrku, nt kooli, töökoha või tasuta juhtmeta võrku.
- **Teie seadmel on**[**tulemüüri- või viirusetõrjetarkvara**](#SoftwareIssues),**mis blokeerib juurdepääsu Outline'i serverile.**
- **Teie**[**telefoni seadme seadeid**](#DeviceSettings)**tuleb võib-olla muuta.**
- **Teie teenusehaldur võis**[**hävitada serveri või teie internetiteenuse pakkuja võib blokeerida teie päringut**](#ServerIssues).

## Internetiühenduse probleemid {#Internetissues}

### Testimine

Lülitage Outline välja ja vaadake, kas teie internetiühendus taastub.

- Kui taastub, vaadake allpool muid veaotsingu valikuid.
- Kui ei taastu, siis oodake mõni hetk ja vaadake, kas ühenduse seaded värskendavad end.

### Parandamine

Looge seadmes uuesti võrguühendus.

1. Kontrollige, kas teine seade saab sama võrguga ühenduse luua. Kui teised seadmed ei saa võrguühendust luua, on võrk võib-olla maas ja teil tuleb oodata, kuni see taas tööle hakkab, või teha veaotsing.
2. Kui teistes seadmetes õnnestub sama võrguga ühendus luua, võite võrguühenduse taastamiseks proovida järgmisi lahendusi.
   1. Lülitage seadmes sisse lennukirežiim (mobiilseadme puhul).
   2. Taaskäivitage seade.
   3. Lülitage seade välja, oodake 2 minutit ja seejärel lülitage seade uuesti sisse.

## Võrgu tulemüüri probleemid {#FirewallIssues}

### Testimine

1. Katkestage ühendus praeguse WiFi- või juhtmega võrguga.
2. Looge ühendus muu võrguga, näiteks mobiilsidevõrguga.
3. Proovige Outline'i serveriga uuesti ühendus luua.

Kui saate muus võrgus ühenduse luua, on probleem leitud.

### Parandamine

Võtke ühendust teenusehalduriga ja paluge, et ta lubaks juurdepääsu teie Outline'i serverile, või jätkake teise võrgu kasutamist.

## Tulemüüri- või viirusetõrjetarkvara probleemid {#SoftwareIssues}
### Testimine
 Proovige luua ühendus Outline'iga muu seadme kaudu.

Märkus. Pidage meeles, et teil on teises seadmes Outline'i kasutamiseks vaja pääsuvõtit ja Outline'i rakendust.

### Parandamine
Kontrollige tulemüüri- või viirusetõrjetarkvara seadeid ja veenduge, et need laseksid läbi VPN-i ja Outline'i liikluse.

## Seadme seaded {#DeviceSettings}

## Kontrollimine {#ServerIssues}
Androidis

1. Avage rakendus Seaded.
2. Otsige oma seadmes jaotist **VPN-i seaded** (VPN-i seadetes kuvatakse kõik VPN-i rakendused, millel on praegu teie telefonis juurdepääs).
3. Kui VPN-i seadetes Outline'i ei kuvata, desinstallige Outline ja installige see uuesti. Pärast installimist peaks seade Outline'ile automaatselt juurdepääsu andma.

Veenduge, et teil poleks Androidi seadmessse installitud ekraani ülekatte rakendust, kuna see võib saata Outline'i õiguste akna taustale, et see poleks esiplaanil nähtav.

 Tehke Androidi seadmes valikud Seaded > Rakendused > Rakenduste erijuurdepääs. Seejärel puudutage valikut „Kuva teiste rakenduste peal“. Saate eemaldada juurdepääsu rakendustele, mis lubavad sellist käitumist.

 iOS-is: lugege [seda toeartiklit](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Serveriprobleemid

### Testimine
Kui teil on juurdepääs mitmele serverile, proovige luua ühendus muu serveriga.

### Parandamine

Võtke ühendust oma teenusehalduriga ja uurige, kas server on hävitatud. Kui see on hävitatud, küsige temalt mõne muu serveri [pääsuvõtit](/about/terminology).

Kui seadistasite serveri ise, proovige sellega ühendust luua Outline Manageri või muu meetodi, näiteks [SSH](https://en.wikipedia.org/wiki/Secure_Shell) kaudu. Kui see ei tööta, võite pilveteenuste pakkuja konsooli (kui see on saadaval) kaudu uurida, kas server on võrgus.
