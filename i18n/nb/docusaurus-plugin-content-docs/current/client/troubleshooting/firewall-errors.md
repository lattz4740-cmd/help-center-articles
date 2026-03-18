---
title: Brannmurfeil
sidebar_label: Brannmurfeil
---

Du kan støte på tre typer brannmurfeil:

## Du kan bli blokkert av en nettverksbrannmur.

Hvis du prøver å installere Outline mens du er koblet til et brannmurbeskyttet nettverk, for eksempel på skolen eller jobben, kan du prøve å installere mens du er koblet til et annet nettverk.

Hvis dette ikke virker, kan du be nettverksadministratoren om å tillate tilkoblinger mellom det brannmurbeskyttede nettverket og Outline-tjeneren din. Du må vite hva Outline-tjenerens IP-adresse er, og hvilke porter Outline bruker. Dette står på slutten av installasjonsskriptet.

**Du kan bli blokkert av en enhetsbrannmur**.

Hvis du har programvare på enheten din som blokkerer utgående tilkoblinger på annet enn standardporter, eller har ukjent programvare (for eksempel ZoneAlarm fra CheckPoint), kan du slå opp i dokumentasjonen for enheten eller programvaren for å finne ut hvordan du oppretter et unntak for Outline.

## Du kan bli blokkert av en tjenerbrannmur.

Nettskyleverandøren du har valgt, kan kreve at du legger til unntak manuelt i tjenerbrannmuren for å åpne portene Outline bruker. Etter at du kjørte installasjonsskriptet, skal du ha fått oppgitt de to tilfeldig valgte portene der Outline kjører på tjeneren din. Det skal være tilstrekkelig å åpne disse to portene.

 For å legge til unntak i tjenerbrannmuren anbefaler vi at du ser på dokumentasjonen for «ufw» og «iptables»:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
