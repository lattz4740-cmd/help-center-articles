---
title: "Waarom kan ik geen verbinding maken met de Outline-service?"
sidebar_label: "Waarom kan ik geen verbinding maken met de Outline-service?"
---

Er zijn verschillende redenen waarom je geen verbinding kunt maken met de Outline-service:

- **Je apparaat heeft [geen verbinding met internet](#Internetissues).** Soms is er een onderbreking in de netwerkverbinding en kan het even duren voordat de netwerkiconen zijn geüpdatet. Of het apparaat heeft verbinding met het lokale netwerk, maar het internet werkt niet.
- **Je [netwerkfirewall blokkeert de toegang](#FirewallIssues) tot de Outline-server.** Dit gebeurt vaak als je een openbaar netwerk gebruikt, zoals dat van je school of werk of een gratis draadloos netwerk.
- **Je apparaat gebruikt [een firewall of antivirussoftware](#SoftwareIssues) die de toegang tot de Outline-server blokkeert.**
- **Je moet misschien de [instellingen van je telefoon](#DeviceSettings) wijzigen.**
- **Je serverbeheerder heeft misschien [de server vernietigd of je internetprovider blokkeert het verzoek](#ServerIssues).**

## Problemen met de internetverbinding: {#Internetissues}

### Hoe je dit test:

Zet Outline uit en check of je weer verbinding krijgt met internet.

- Zo ja, check dan andere opties voor probleemoplossing hieronder.
- Zo nee, wacht dan even of de verbindingsinstellingen vanzelf worden geüpdatet.

### Oplossingen:

Zorgen dat je apparaat weer online komt:

1. Check op een ander apparaat of je verbinding kunt maken met hetzelfde netwerk. Als andere apparaten ook niet online kunnen komen, is het netwerk misschien niet beschikbaar en moet je wachten tot het weer beschikbaar is of probleemoplossing uitvoeren.
2. Als andere apparaten wel verbinding kunnen maken met hetzelfde netwerk, kun je een of meer van de volgende acties uitvoeren om te zorgen dat het apparaat weer online gaat:
   1. Zet het apparaat in de vliegtuigstand (mobiel).
   2. Start het apparaat opnieuw op.
   3. Zet het apparaat uit, wacht 2 minuten en zet het weer aan.

## Problemen veroorzaakt door de netwerkfirewall: {#FirewallIssues}

### Hoe je dit test:

1. Verbreek de verbinding met het huidige wifi- of bedrade netwerk.
2. Maak verbinding met een ander netwerk, zoals een mobiel netwerk.
3. Probeer opnieuw verbinding te maken met de Outline-server.

Als je op het andere netwerk wel verbinding kunt maken, is dit de oorzaak van het probleem.

### Oplossingen:

Vraag de servicemanager je toegang te geven tot de Outline-server of blijf het andere netwerk gebruiken.

## Problemen veroorzaakt door de firewall of antivirussoftware: {#SoftwareIssues}

### Hoe je dit test:

Probeer verbinding te maken met Outline op een ander apparaat.

:::note
Je hebt een toegangssleutel en de Outline-app nodig om Outline te kunnen gebruiken op een ander apparaat.
:::

### Oplossingen:

Zorg dat de firewall of antivirussoftware zo is ingesteld dat VPN- en Outline-verkeer wordt doorgelaten.

## Apparaatinstellingen: {#DeviceSettings}

### Check het volgende:

Voor Android:

1. Open de Instellingen-app.
2. Zoek de **VPN-instellingen** op je apparaat (hier staan alle VPN-apps die momenteel toegang hebben op je telefoon).
3. Als Outline er niet bij staat in de VPN-instellingen, verwijder je de app en installeer je deze opnieuw. Nadat Outline is geïnstalleerd, zou de app automatisch toegang moeten krijgen van het apparaat.

Zorg dat je geen apps voor schermoverlay hebt geïnstalleerd op je Android-apparaat. Hierdoor kan het venster voor Outline-rechten op de achtergrond worden geopend, waardoor het niet zichtbaar is.

Ga op je Android-apparaat naar Instellingen > Apps > Speciale app-toegang. Tik dan op Weergeven vóór andere apps. Je kunt de toegang verwijderen tot apps die dit gedrag toestaan.

Voor iOS: Ga naar [dit supportartikel](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Serverproblemen: {#ServerIssues}

### Hoe je dit test:

Als je toegang hebt tot meer dan één server, probeer je verbinding te maken met de andere server.

### Oplossingen:

Vraag je servicemanager of de server is vernietigd. Als dit het geval is, vraag je de servicemanager om een [toegangssleutel](/about/terminology) tot een andere server.

Als je de server zelf hebt ingesteld, probeer je er verbinding mee te maken via Outline Manager of een andere methode, zoals [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Als dat niet werkt, kun je in de console van de cloudprovider (indien aanwezig) checken of de server nog online is.
