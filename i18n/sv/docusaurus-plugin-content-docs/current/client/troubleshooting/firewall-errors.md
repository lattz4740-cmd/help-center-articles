---
title: Problem med brandvägg
sidebar_label: Problem med brandvägg
---

Det kan uppstå tre olika typer av problem med brandväggar:

## Du kanske blockeras av en brandvägg i ett nätverk

Om du försöker installera Outline i ett nätverk som skyddas av en brandvägg, till exempel på en skola eller arbetsplats, ska du testa att utföra installationen i ett annat nätverk.

Om det inte fungerar kontaktar du nätverksadministratören så att han eller hon kan tillåta anslutningar mellan Outline-servern och det nätverk som skyddas av brandväggen. Du måste veta Outline-serverns IP-adress och på vilka portar Outline körs, vilket visas i slutet av installationsskriptet.

## Du kanske blockeras av en brandvägg på en enhet

Om det finns mjukvara på enheten som blockerar utgående anslutningar på icke-standardiserade portar eller mjukvara som inte känns igen (ZoneAlarm från CheckPoint) läser du igenom dokumentationen för enheten eller programvaran för att ta reda på hur du kan skapa ett undantag för Outline.

## Du kanske blockeras av en brandvägg på servern

Molnleverantören du valt kanske kräver att du öppnar de portar Outline körs på genom att skapa undantag för serverns brandvägg manuellt. När du körde installationsskriptet fick du information om vilka två slumpmässigt valda portar som Outline körs på. Det borde räcka med att öppna dessa två portar.

 Om du behöver skapa undantag i serverns brandvägg rekommenderar vi att du läser dokumentationen för UFW och Iptables:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
