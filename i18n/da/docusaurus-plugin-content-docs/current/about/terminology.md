---
title: Terminologi
sidebar_label: Terminologi
---

Hvad er et VPN?

 Et virtuelt privat netværk (VPN) er en privat forbindelse mellem dine enheder og en hostserver. Når du bruger et VPN, er din trafik skjult fra internetudbyderen. Du kan eventuelt vælge at bruge et VPN i følgende scenarier:

- For at beskytte dine data, når du bruger et offentligt Wi-Fi-netværk
- For at skjule dine browserdata over for din internetudbyder og offentlige myndigheder
- For at tilgå ucensureret indhold fra diverse kilder rundt omkring i verden

**Hvordan skiller Outline sig ud fra traditionelle VPN'er?**

 Internetudbydere kan nemt registrere og blokere traditionelle VPN'er ved at genkende almindelige sikkerhedsprotokoller og/eller mønstre i mængden af trafik. Outline er mere modstandsdygtigt end traditionelle VPN'er, fordi det er udviklet ved hjælp af en protokol, der er designet til at være vanskelig at registrere og dermed sværere at blokere. Outline er modstandsdygtigt over for sofistikerede former for censur, herunder netværksbaseret blokering og IP-blokering.

**Hvad er en Outline-server?**

 En Outline-server kører det VPN, som tilladte brugere opretter forbindelse til. Hvis du opretter et nyt netværk, kan du bruge din egen sikre server som din Outline-server, hvis du har en, eller du kan bruge en tjenesteudbyder i skyen som f.eks.:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Du konfigurerer din server i Outline Manager.

**Hvad er en tjenesteadministrator?**

 En tjenesteadministrator er den person, der er ansvarlig for at konfigurere Outline-serveren og dele adgangsnøgler med brugere. Tjenesteadministratoren er generelt ansvarlig for omkostningerne for brugen af serveren. 

**Hvad er en adgangsnøgle?**

 En adgangsnøgle bruges til at tilgå en eksisterende Outline-server og oprette forbindelse til det pågældende VPN. En [tjenesteadministrator](#servicemanager) giver dig en adgangsnøgle, eller du kan selv [konfigurere en Outline-server](/manager/server-setup/setup-server). Her er der et eksempel på, hvordan en adgangsnøgle ser ud (kun et eksempel; fungerer ikke): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Hvad er Outline Manager?**

 Outline Manager er et computerprogram, som tillader, at en tjenesteadministrator konfigurerer en Outline-server, genererer [adgangsnøgler](#accesskey) og angiver datagrænser for brug pr. nøgle. Du kan downloade den seneste version af Outline Manager [her](https://getoutline.org/get-started/#step-3) eller [her](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Hvad er Outline Client?**

 Outline Client er et program, der fås til computer og mobil, og som gør det muligt for dig at oprette forbindelse til en Outline-server og få adgang til VPN'et ved hjælp af en adgangsnøgle. Du kan downloade den seneste version af Outline Client[her](https://getoutline.org/get-started/#step-3) eller[her](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Hvad er datagrænser?**

 Outline Manager gør det muligt for tjenesteadministratorer at angive en løbende datagrænse på 30 dage for adgangsnøgler for at forhindre overforbrug og hjælpe med at holde omkostningerne forudsigelige. Tjenesteadministratorer kan angive en standardgrænse, som gælder for enhver nøgle, og de kan også angive en anden grænse for en hvilken som helst nøgle for at overskride standardgrænsen. Når grænsen er angivet, træder den øjeblikkeligt i kraft og håndhæves hver time.

Hvis tjenesteadministratorer tilvælger at dele metrics med Jigsaw, skal de gå til[politikken for dataindsamling](/about/data-collection) for at få flere oplysninger om, hvordan brugen af datagrænser rapporteres.
