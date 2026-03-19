---
title: "Hoekom kan ek nie aan die Outline-diens koppel nie?"
sidebar_label: "Hoekom kan ek nie aan die Outline-diens koppel nie?"
---

Daar is ’n paar redes hoekom jy dalk nie aan die Outline-diens kan koppel nie:

- **Jou toestel is**/client/troubleshooting/connection-issues#One[**nie aan die internet gekoppel nie**](#Internetissues)[#Internetkwessies](#Internetissues)**.**Soms sal jou toestel ’n onderbreking van die netwerkverbinding ondervind en kan dit ’n rukkie neem om die netwerkikone op te dateer. Dis ook moontlik dat jou toestel aan die plaaslike netwerk gekoppel is, maar dat die internet nie werk nie.
- **Jou**/client/troubleshooting/connection-issues#Two[**netwerkbrandmuur blokkeer tans toegang**](#FirewallIssues)[#BrandmuurKwessies](#FirewallIssues)**[#BrandmuurKwessies](#FirewallIssues)tot jou Outline-bediener.**Dit is algemeen as jy ’n publieke netwerk, soos ’n skool-, werk- of gratis draadlose netwerk, gebruik.
- **Jou toestel het ’n**/client/troubleshooting/connection-issues#Three[**brandmuur of antivirussagteware**](#SoftwareIssues)[#SagtewareKwessies](#SoftwareIssues)**wat toegang tot jou Outline-bediener blokkeer.**
- **Jou**[**foontoestelinstellings**](#DeviceSettings)**moet dalk verander word.**
- **Jou diensbestuurder het dalk**[**die bediener vernietig, of jou internetdiensverskaffer blokkeer dalk jou versoek**](#ServerIssues) .

## Internetverbindingkwessies: {#Internetissues}

### Toets dit só:

Skakel Outline af en kyk of jou verbinding aan die internet dan herstel is.

- Indien wel, kan jy hier onder nog foutsporingopsies sien.
- Indien nie, moet jy ’n rukkie wag om te kyk of jou verbindinginstellings self opdateer.

### Dinge om reg te maak:

Kry jou toestel weer aanlyn:

1. Kyk of ’n ander toestel aan dieselfde netwerk kan koppel. Indien ander toestelle nie aan die internet kan koppel nie, is die netwerk dalk af en moet jy wag vir dit om terug te keer of dit foutspoor.
2. Indien ander toestelle aan dieselfde netwerk kan koppel, kan jy een of meer van die volgende probeer om dit weer aanlyn te kry:
   1. Sit die toestel in vliegtuigmodus (selfoon)
   2. Herbegin die toestel
   3. Skakel die toestel af, wag 2 minute, en skakel die toestel weer aan

## Netwerkbrandmuurkwessies: {#FirewallIssues}

### Toets dit só:

1. Ontkoppel van jou huidige wi-fi of bedrade netwerk
2. Koppel aan ’n ander netwerk, soos ’n selnetwerk
3. Probeer om die Outline-bediener te herkoppel

As jy kan koppel wanneer jy op die ander netwerk is, is dit die fout.

### Dinge om reg te maak:

Kontak die diensbestuurder en vra hulle om toegang tot jou Outline-bediener toe te laat, of hou aan om eerder die ander netwerk te gebruik.

## Brandmuur- of antivirussagtewarekwessies: {#SoftwareIssues}
### Toets dit só:
 Probeer om van ’n ander toestel af aan Outline te koppel.

Let wel: Onthou dat jy ’n toegangsleutel en die Outline-app nodig het om Outline op ’n ander toestel te gebruik.

### Dinge om reg te maak:
Gaan jou brandmuur of antivirussagteware se instellings na om seker te maak dat dit gestel is om VPN- en Outline-verkeer deur te laat.

## Toestelinstellings: {#DeviceSettings}

## Dinge om na te gaan: {#ServerIssues}
Vir Android:

1. Maak die Instellings-app oop.
2. Soek die **VPN-instellings** op jou toestel. (Die VPN-instellings sal gewys word vir al die VPN-apps wat tans tot jou foon toegang het.)
3. Deïnstalleer en herinstalleer Outline as jy dit nie in die VPN-instellings kan sien nie. Outline behoort outomaties toegang van die toestel af te ontvang sodra dit geïnstalleer is.

Maak seker dat daar nie ’n skermoorleggerapp op jou Android-toestel geïnstalleer is nie, omdat dit die Outline-toestemmingsvenster na die agtergrond kan stuur sodat dit nie op die voorgrond sigbaar is nie.

 Gaan op jou Android-toestel na Instellings > Apps > Spesiale apptoegang. Tik dan op “Wys bo-oor ander apps”. Jy kan toegang tot enige apps wat hierdie gedrag toelaat, verwyder.

 Vir iOS: Lees[hierdie steundiensartikel](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Bedienerkwessies:

### Toets dit só:
Indien jy toegang tot meer as een bediener het, moet jy probeer om aan die ander een te koppel.

### Dinge om reg te maak:

Kontak jou diensbestuurder om te sien of die bediener vernietig is. Indien wel, kan jy hulle vir ’n [toegangsleutel](/about/terminology) tot ’n ander bediener vra.

Indien jy die bediener opgestel het, moet jy probeer om deur die Outline Manager of ’n ander metode, soos [SSH](https://en.wikipedia.org/wiki/Secure_Shell), daaraan te koppel. As dit nie werk nie, moet jy die wolkverskafferkonsole, indien enige, probeer nagaan om te kyk of die bediener nog aanlyn is.
