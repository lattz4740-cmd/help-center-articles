---
title: "Varför går det inte att ansluta till Outline-tjänsten?"
sidebar_label: "Varför går det inte att ansluta till Outline-tjänsten?"
---

Att du inte kan ansluta till Outline-tjänsten kan bero på några olika anledningar:

- **Enheten är**[**inte ansluten till internet**](#Internetissues)**.**Ibland förlorar enheten kontakten med nätverket och det kan ta en stund innan den har uppdaterat nätverksikonerna. Det är också möjligt att enheten är ansluten till det lokala nätverket men att internetanslutningen är nere.
- **Nätverkets**[**brandvägg blockerar åtkomsten**](#FirewallIssues)**till Outline-servern.**Det händer ofta när man använder offentliga nätverk på till exempel skolor och arbetsplatser, eller kostnadsfria trådlösa nätverk.
- **Enheten har en**[**brandvägg eller ett antivirusprogram**](#SoftwareIssues)**som blockerar åtkomsten till Outline-servern.**
- **Dina**[**telefoninställningar**](#DeviceSettings)**kan behöva ändras.**
- **Tjänstansvarig kan ha**[**förstört servern, eller så kanske din begäran blockeras av internetleverantören**](#ServerIssues).

## Problem med internetanslutningen: {#Internetissues}

### Så här testar du:

Inaktivera Outline och kontrollera om anslutningen till internet återställs.

- Om den gör det hittar du fler felsökningsalternativ nedan.
- Om den inte gör det väntar du en liten stund och kontrollerar om anslutningsinställningarna uppdaterar sig själva.

### Saker att åtgärda:

Få tillbaka enhetens internetanslutning:

1. Använd en annan enhet och kontrollera om den kan ansluta till samma nätverk. Om andra enheter inte heller får någon internetanslutning kanske nätverket är nere och du måste vänta tills det kommer tillbaka eller felsöka det.
2. Om andra enheter kan ansluta till samma nätverk kan du testa ett eller flera av följande alternativ för att återupprätta internetanslutningen:
   1. Starta flygplansläget på enheten (mobil)
   2. Starta om enheten
   3. Stäng av enheten, vänta i två minuter och slå sedan på enheten igen.

## Problem med nätverkets brandvägg: {#FirewallIssues}

### Så här testar du:

1. Koppla från den aktuella wifi-anslutningen eller kabelanslutningen.
2. Anslut till ett annat nätverk, till exempel ett mobilt nätverk.
3. Prova att ansluta till Outline-servern igen.

Om du kan ansluta medan du är i det andra nätverket är det detta som är problemet.

### Saker att åtgärda:

Kontakta tjänsteansvarig och be hen att tillåta åtkomst till Outline-servern eller fortsätt att använda det andra nätverket i stället.

## Problem med brandvägg eller antivirusprogram: {#SoftwareIssues}
### Så här testar du:
 Testa att ansluta till Outline från en annan enhet.

Obs! Tänk på att du behöver en åtkomstnyckel och Outline-appen för att använda Outline på en annan enhet.

### Saker att åtgärda:
Kontrollera inställningarna för brandväggen eller antivirusprogrammet och se till att de låter VPN- och Outline-trafik passera.

## Enhetsinställningar: {#DeviceSettings}

## Saker att kontrollera: {#ServerIssues}
För Android:

1. Öppna Inställningar-appen.
2. Leta reda på **VPN-inställningarna** på enheten (i VPN-inställningarna ser du alla VPN-appar som har åtkomst på din telefon för närvarande).
3. Om du inte ser Outline i VPN-inställningarna avinstallerar du Outline och installerar det igen. Outline ska få åtkomst av enheten automatiskt så fort det installerats.

Se till att du inte har någon app för skärmöverlagring installerad på din Android-enhet, då detta kan skicka fönstret för behörigheter i Outline till bakgrunden och förhindra att det syns i förgrunden.

 På Android går du till Inställningar > Appar > Särskild appåtkomst. Tryck sedan på Visa över andra appar. Du kan ta bort åtkomst till appar som tillåter beteendet.

 För iOS: Läs [den här supportartikeln](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Serverproblem:

### Så här testar du:
Om du har tillgång till mer än en server testar du att ansluta till den andra.

### Saker att åtgärda:

Kontakta tjänsteansvarig för att kontrollera om servern har förstörts. Be i så fall hen om en [åtkomstnyckel](/about/terminology) till en annan server.

Om det är du som konfigurerat servern testar du att ansluta till den via Outline Manager eller en annan metod, t.ex. [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Om det inte fungerar kan du testa att kontrollera molnleverantörskonsolen, om du har en, för att se om servern fortfarande är online.
