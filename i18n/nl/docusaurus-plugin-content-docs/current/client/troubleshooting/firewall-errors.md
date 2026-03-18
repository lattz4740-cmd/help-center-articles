---
title: Firewallfouten
sidebar_label: Firewallfouten
---

Je kunt drie soorten firewallproblemen tegenkomen:

## Je wordt wellicht geblokkeerd door een netwerkfirewall.

Als je Outline probeert te installeren wanneer je verbinding hebt met een netwerk met een firewall, zoals op school of op het werk, kun je proberen Outline te installeren via een ander netwerk.

 Als dit niet werkt, kun je je netwerkbeheerder vragen verbindingen met je Outline-server via het netwerk met de firewall toe te staan. Je moet hiervoor het IP-adres van je Outline-server en de poorten waarop Outline wordt uitgevoerd weten. Deze staan onderaan het installatiescript.

## Je wordt wellicht geblokkeerd door een apparaatfirewall.

Als je software op je apparaat hebt waarmee uitgaande verbindingen op niet-standaardpoorten of niet-herkende software worden geblokkeerd (zoals ZoneAlarm van Checkpoint), kijk je in de documentatie van je apparaat of software hoe je een uitzondering kunt maken voor Outline.

## Je wordt wellicht geblokkeerd door een serverfirewall.

De cloudprovider die je hebt gekozen, vereist wellicht dat je handmatig uitzonderingen maakt op je serverfirewall om de poorten te openen die door Outline worden gebruikt. Nadat je het installatiescript had uitgevoerd, heb je als het goed is twee willekeurige poorten gekregen die door Outline worden gebruikt op je server. Als je deze twee poorten opent, zou dit genoeg moeten zijn.

 Als je uitzonderingen wilt maken op je serverfirewall, raden we je aan de documentatie van UFW en Iptables te bekijken:

- UFW: [https://help.ubuntu.com/community/UFW](/client/troubleshooting/firewall-errors)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](/client/troubleshooting/firewall-errors)
