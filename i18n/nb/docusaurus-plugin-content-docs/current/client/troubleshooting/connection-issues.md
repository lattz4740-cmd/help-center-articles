---
title: "Hvorfor kan jeg ikke koble til Outline-tjenesten?"
sidebar_label: "Hvorfor kan jeg ikke koble til Outline-tjenesten?"
---

Det finnes flere grunner til at du kanskje ikke kan koble til Outline-tjenesten:

- **Enheten din er**[**koblet fra internett**](#Internetissues)**.**Noen ganger kan nettverkstilkoblingen for enheten din bli brutt, og da kan det ta litt tid før nettverksikonene blir oppdatert. Det er også mulig at enheten din er koblet til det lokale nettverket, men at internett er nede.
- [**Brannmuren for nettverket ditt blokkerer tilgangen**](#FirewallIssues)**til Outline-tjeneren.**Dette er vanlig når du bruker et offentlig nettverk, for eksempel et skole- eller jobbnettverk eller et kostnadsfritt trådløst nettverk.
- **Enheten har**[**en brannmur eller antivirusprogramvare**](#SoftwareIssues)**som blokkerer tilgangen til Outline-tjeneren.**
- **Det er mulig at**[**innstillingene for telefonen**](#DeviceSettings)**må endres.**
- **Tjenesteadministratoren din kan ha**[**slettet tjeneren, eller nettleverandøren din blokkerer forespørselen**](#ServerIssues).

## Problemer med internettilkoblingen: {#Internetissues}

### Slik tester du det:

Slå av Outline og se om internettilkoblingen er gjenopprettet.

- Hvis den er det, kan du se flere alternativer for feilsøking nedenfor.
- Hvis den ikke er det, kan du vente litt for å se om tilkoblingsinnstillingene oppdateres av seg selv.

### Ting du bør fikse:

Få enheten din på nettet igjen:

1. Sjekk en annen enhet for å se om den får koblet til det samme nettverket. Hvis andre enheter ikke får opprettet nettilkobling, kan det hende at nettverket er nede. Da må du vente til det er oppe igjen før du kan fortsette feilsøkingen.
2. Hvis andre enheter kan koble seg til det samme nettverket, kan du prøve én eller flere av disse løsningene for å få enheten din på nett igjen:
   1. Sett enheten i flymodus (mobilenheter).
   2. Start enheten på nytt.
   3. Slå av enheten, vent i to minutter, og slå den på igjen.

## Brannmurproblemer for nettverket: {#FirewallIssues}

### Slik tester du det:

1. Koble fra det gjeldende wifi-nettverket eller nettverket med ledning.
2. Koble til et annet nettverk, for eksempel et mobilnettverk.
3. Prøv å koble til Outline-tjeneren på nytt.

Hvis du kan koble til mens du er på det andre nettverket, er det dette som er problemet ditt.

### Ting du bør fikse:

Kontakt tjenesteadministratoren og be om at tilgang til Outline-tjeneren din tillates, eller fortsett å bruke det andre nettverket.

## Problemer med brannmur eller antivirusprogramvare: {#SoftwareIssues}
### Slik tester du det:
 Prøv å koble til Outline fra en annen enhet.

Merk: Husk at du trenger en tilgangsnøkkel og Outline-appen for å kunne bruke Outline på en annen enhet.

### Ting du bør fikse:
Sjekk innstillingene for brannmuren din eller antivirusprogrammet ditt for å forsikre deg om at de slipper gjennom VPN- og Outline-trafikk.

## Enhetsinnstillinger: {#DeviceSettings}

## Ting du bør sjekke: {#ServerIssues}
Android:

1. Åpne Innstillinger-appen.
2. Finn **VPN-innstillingene** på enheten din (i VPN-innstillingene kan du se alle VPN-appene som har tilgang til telefonen din i øyeblikket).
3. Hvis du ikke finner Outline i VPN-innstillingene, avinstallerer du Outline og installerer den på nytt. Outline bør automatisk få tilgang av enheten, så snart den er installert.

Sørg for at du ikke har en app for skjermoverlegg installert på Android-enheten din, da dette kan sende vinduet for Outline-tillatelse til bakgrunnen slik at det ikke er synlig i forgrunnen.

 På Android-enheten din går du til Innstillinger > Apper > Spesiell apptilgang. Trykk deretter på «Vis over andre apper». Du kan fjerne tilgangen til enhver app som tillater dette.

 iOS: Les [denne brukerstøtteartikkelen](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Tjenerproblemer:

### Slik tester du det:
Hvis du har tilgang til mer enn én tjener, kan du prøve å koble til den andre.

### Ting du bør fikse:

Kontakt tjenesteadministratoren for å sjekke om tjeneren er slettet. Hvis den er det, kan du be om å få en [tilgangsnøkkel](/about/terminology) til en annen tjener.

Når du har konfigurert tjeneren, kan du prøve å koble til via Outline-administratoren eller en annen metode, for eksempel [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Hvis det ikke fungerer, kan du prøve å sjekke konsollen til nettskyleverandøren, hvis du har en, for å se om tjeneren fortsatt er på nett.
