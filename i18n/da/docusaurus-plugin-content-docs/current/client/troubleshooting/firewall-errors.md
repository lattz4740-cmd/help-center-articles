---
title: Firewallfejl
sidebar_label: Firewallfejl
---

Du kan støde på tre typer firewallproblemer:

## Du kan blive blokeret af en firewall på et netværk.

Hvis du forsøger at installere Outline, mens du har forbindelse til et netværk, der er beskyttet af en firewall, f.eks. i skolen eller på din arbejdsplads, kan du prøve at installere, mens du har forbindelse til et andet netværk.

Hvis det ikke virker, kan du kontakte din netværksadministrator, som kan tillade forbindelser mellem det netværk, der er beskyttet af en firewall, og din Outline-server. Du skal kende din Outline-servers IP-adresse og de porte, som Outline anvender. De angives til sidst i installationsscriptet.

## Du kan blive blokeret af en firewall på en enhed.

Hvis du har software på din enhed, der blokerer for udgående forbindelser på ikke-standardporte, eller software, der ikke genkendes (f.eks. CheckPoints ZoneAlarm), kan du læse dokumentationen til enheden eller softwaren for at få flere oplysninger om, hvordan du opretter en undtagelse for Outline.

## Du kan blive blokeret af en firewall på en server.

Den cloududbyder, du har valgt, kan kræve, at du manuelt opretter undtagelser i din servers firewall for at åbne de porte, Outline bruger. Når du kører installationsscriptet, bør du få vist de to tilfældigt udvalgte porte, som Outline bruger på din server. Det burde være tilstrækkeligt at åbne disse to porte.

 Hvis du vil oprette undtagelser i din servers firewall, anbefaler vi, at du læser dokumentationen til "ufw" og "iptables":

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
