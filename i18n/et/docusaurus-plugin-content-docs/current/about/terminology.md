---
title: Terminoloogia
sidebar_label: Terminoloogia
---

## Mis on VPN?
 Virtuaalne privaatvõrk (VPN) on privaatne ühendus teie seadme(te) ja hostserveri vahel. VPN-i kasutamise korral on teie liiklus internetiteenuse pakkuja eest peidetud. VPN-i soovite võib-olla kasutada järgmistel juhtudel.

- Oma andmete kaitsmiseks, kui kasutate avalikku WiFi-võrku
- Oma sirvimisandmete internetiteenuse pakkuja ja riigiasutuste eest privaatsena hoidmiseks
- Tsenseerimata sisule juurdepääsuks erinevatest maailma allikatest

## Mille poolest erineb Outline tavalistest VPN-idest?
 Internetiteenuse pakkujad saavad hõlpsasti tuvastada ja blokeerida tavalised VPN-id, tundes ära levinud turvaprotokollid ja/või liikluse mahu mustrid. Outline on töökindlam kui tavalised VPN-id, kuna selle puhul on kasutatud protokolli, mida on keeruline tuvastada ja seetõttu ka raskem blokeerida. Outline suudab kaitsta keeruliste tsenseerimisvormide eest, nagu IP või võrgupõhine blokeerimine.

## Mis on Outline'i server?
 Outline'i server käitab VPN-i, millega kasutajad, kellel on vastav luba, loovad ühenduse. Kui loote uut võrku, saate oma Outline'i serverina kasutada oma turvalist võrku, kui teil on see olemas, või kasutada mõnda pilveteenuste pakkujat:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Serveri seadistamine toimub Outline Manageris.

## Kes on teenusehaldur? {#servicemanager}
 Teenusehaldur on isik, kes vastutab Outline'i serveri seadistamise ja kasutajatele pääsuvõtmete jagamise eest. Tavaliselt vastutab teenusehaldur serveri kasutamise kulude eest. 

## Mis on pääsuvõti? {#accesskey}
 Pääsuvõtit kasutatakse olemasolevale Outline'i serverile juurdepääsemiseks ja VPN-iga ühenduse loomiseks. Pääsuvõtme annab teile [teenusehaldur](#servicemanager) või saate [Outline'i serveri seadistada](/manager/server-setup/setup-server) ka ise. Siin on näide sellest, milline näeb välja pääsuvõti (ainult näidis, mis ei tööta): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Mis on Outline Manager?
 Outline Manager on töölauarakendus, mis võimaldab teenusehalduril seadistada Outline'i serveri, luua [pääsuvõtmed](#accesskey) ja määrata kasutuse andmepiirangud võtme kohta. Outline Manageri uusima versiooni saate alla laadida [siit](https://getoutline.org/get-started/#step-3) või [siit](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Mis on Outline'i klient?
 Outline'i klient on lauaarvuti ja mobiilseadme jaoks saadaolev rakendus, mis võimaldab teil luua ühenduse Outline'i serveriga ja pääseda VPN-ile juurde pääsuvõtme abil. Outline'i kliendi uusima versiooni saate alla laadida [siit](https://getoutline.org/get-started/#step-3) või [siit](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Mis on andmepiirangud?
 Outline Manager võimaldab teenusehalduritel määrata pääsuvõtmetele jooksva 30-päevase andmepiirangu, et vältida liigset kasutamist ja tagada kulude prognoositavus. Teenusehaldurid saavad määrata vaikepiirangu, mis kehtib kõigi võtmete puhul, ning määrata mis tahes võtmele muu piirangu, mis alistab vaikepiirangu. Pärast piirangu määramist jõustub see kohe ja seda jõustatakse kord tunnis.

Kui teenusehaldurid lubavad mõõdikute jagamise Jigsaw'ga, peaksid nad vaatama [andmete kogumise eeskirjadest](/about/data-collection) üksikasjalikku teavet selle kohta, kuidas andmepiirangute kasutamisest teatatakse.
