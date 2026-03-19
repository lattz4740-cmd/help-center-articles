---
title: "Hvorfor kan jeg ikke få forbindelse til Outline-tjenesten?"
sidebar_label: "Hvorfor kan jeg ikke få forbindelse til Outline-tjenesten?"
---

Der kan være nogle årsager til, at du muligvis ikke kan få forbindelse til Outline-tjenesten:

- **Din enhed har**/client/troubleshooting/connection-issues#One[**ikke forbindelse til internettet**](#Internetissues)[#Internetissues](#Internetissues)**.**Nogle gange kan der forekomme afbrydelser af din enheds netværksforbindelse, og det kan tage et øjeblik, før netværksikonerne opdateres. Det er også muligt, at din enhed har forbindelse til det lokale netværk, men at internettet er nede.
- **Din**/client/troubleshooting/connection-issues#Two[**netværksfirewall blokerer adgang**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[t](#FirewallIssues)il din Outline-server.**Det er normalt, hvis du bruger et offentligt netværk, f.eks. en skole, en arbejdsplads eller et gratis trådløst netværk.
- **Din enhed har en**/client/troubleshooting/connection-issues#Three[**firewall eller antivirussoftware**](#SoftwareIssues),[#SoftwareIssues](#SoftwareIssues)**der blokerer adgangen til din Outline-server.**
- **Dine**[**indstillinger for telefonenhed**](#DeviceSettings)**skal muligvis ændres.**
- **Administratoren af din tjeneste har muligvis**[**ødelagt serveren, eller din internetudbyder blokerer din anmodning**](#ServerIssues).

## Problemer med internetforbindelsen: {#Internetissues}

### Sådan tester du:

Slå Outline fra, og se om forbindelsen til internettet genoprettes.

- Hvis forbindelsen genoprettes, kan du se flere muligheder for fejlfinding nedenfor.
- Hvis forbindelsen ikke genoprettes, skal du vente et øjeblik for at se, om dine forbindelsesindstillinger opdateres af sig selv.

### Ting, der skal ordnes:

Få din enhed på nettet igen:

1. Tjek en anden enhed for at se, om den kan oprette forbindelse til det samme netværk. Hvis andre enheder ikke kan komme online, er netværket muligvis nede, og du bliver nødt til at vente, til det er oppe at køre igen, eller foretage fejlfinding af det.
2. Hvis andre enheder kan komme på det samme netværk, kan du prøve at komme online igen på en af følgende måder:
   1. Aktivér flytilstand på enheden (mobil)
   2. Genstart enheden
   3. Sluk enheden, vent 2 minutter, og tænd enheden igen

## Problemer med netværksfirewall: {#FirewallIssues}

### Sådan tester du:

1. Afbryd forbindelsen til dit nuværende Wi-Fi-netværk eller kabelnetværk.
2. Opret forbindelse til et andet netværk, f.eks. et mobilnetværk.
3. Prøv at oprette forbindelse til Outline-serveren igen.

Hvis du kan oprette forbindelse, mens du er på det andet netværk, kan det være årsagen til problemet.

### Ting, der skal ordnes:

Kontakt administratoren af tjenesten, og bed vedkommende om at tillade adgang til din Outline-server, eller fortsæt med at bruge det andet netværk i stedet.

## Problemer med firewall eller antivirussoftware: {#SoftwareIssues}
### Sådan tester du:
 Prøv at oprette forbindelse til Outline fra en anden enhed.

Bemærk! Husk, at du skal have en adgangsnøgle og Outline-appen for at bruge Outline på en anden enhed.

### Ting, der skal ordnes:
Tjek indstillingerne for din firewall eller antivirussoftware for at sikre, at VPN- og Outline-trafik er tilladt.

## Enhedsindstillinger: {#DeviceSettings}

## Ting, som du bør tjekke: {#ServerIssues}
På Android:

1. Åbn appen Indstillinger.
2. Find **VPN-indstillingerne** på din enhed (VPN-indstillinger viser dig alle de VPN-apps, der i øjeblikket har adgang til din telefon).
3. Hvis du ikke kan se Outline i VPN-indstillingerne, skal du afinstallere Outline og derefter geninstallere det. Outline burde automatisk få adgang af enheden, når det er installeret.

Sørg for, at du ikke har installeret en skærmoverlejret app på din Android-enhed, da det kan sende Outline-tilladelsesvinduet i baggrunden, så du ikke ser det i forgrunden.

 På din Android-enhed skal du gå til > Apps > Særlig appadgang. Tryk derefter på "Vis oven på andre apps". Du kan fjerne adgang til eventuelle apps, som tillader skærmoverlejring.

 Til iOS: Læs[denne supportartikel](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Serverproblemer:

### Sådan tester du:
Hvis du har adgang til mere end én server, kan du prøve at oprette forbindelse til den anden.

### Ting, der skal ordnes:

Kontakt din tjenesteadministrator for at se, om serveren er ødelagt. I så fald kan du bede vedkommende om en[adgangsnøgle](/about/terminology) til en anden server.

Hvis du selv har konfigureret serveren, kan du prøve at oprette forbindelse til den via Outline Manager eller en anden metode, f.eks.[SSH](https://en.wikipedia.org/wiki/Secure_Shell). Hvis det stadig ikke virker, kan du prøve at tjekke skyudbyderens konsol, hvis en sådan findes, for at se, om serveren stadig er online.
