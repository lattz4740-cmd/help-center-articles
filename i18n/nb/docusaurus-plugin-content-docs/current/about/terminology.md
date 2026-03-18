---
title: Terminologi
sidebar_label: Terminologi
---

**Hva er VPN?**

 Et virtuelt privat nettverk (VPN) er en privat tilkobling mellom én eller flere enheter og en vertstjener. Når du bruker et VPN, skjules aktiviteten din for internettleverandøren. Det kan være lurt å bruke VPN hvis du vil

- beskytte dataene dine når du bruker offentlige wifi-nettverk
- holde nettlesingsdataene dine skjult fra internettleverandøren din og offentlige organer
- se usensurert innhold fra ulike kilder rundt om i verden

**Hvordan skiller Outline seg fra tradisjonelle VPN-nettverk?**

 Internettleverandører kan enkelt oppdage og blokkere tradisjonelle VPN-nettverk ved å gjenkjenne vanlige sikkerhetsprotokoller og/eller trafikkmønstre. Outline er mer robust enn tradisjonelle VPN-nettverk fordi det er laget med en protokoll som er vanskelig å oppdage og dermed også vanskeligere å blokkere. Outline takler avanserte former for sensur, inkludert nettverks- og IP-basert blokkering.

**Hva er en Outline-tjener?**

 VPN-nettverket som brukere med tillatelse kobler seg til, kjøres på en Outline-tjener. Hvis du oppretter et nytt nettverk, kan du bruke din egen sikre tjener som Outline-tjener (hvis du har en) – eller du kan bruke en nettskyleverandør, for eksempel

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Du konfigurerer tjeneren i Outline-administratoren.

**Hva er en tjenesteadministrator?**

 En tjenesteadministrator er en person som har ansvar for å konfigurere Outline-tjeneren og dele tilgangsnøkler med brukerne. Tjenesteadministratoren er vanligvis ansvarlig for kostnadene ved bruken av tjeneren. 

**Hva er en tilgangsnøkkel?**

 En tilgangsnøkkel brukes til å få tilgang til en eksisterende Outline-tjener og koble til VPN. Tilgangsnøkkelen får du av en [tjenesteadministrator](#servicemanager) – eller du kan [konfigurere din egen Outline-tjener](/manager/server-setup/setup-server). Her er et eksempel på hvordan en tilgangsnøkkel kan se ut (dette er bare et eksempel og fungerer ikke i praksis): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Hva er Outline-administratoren?**

 Outline-administratoren er et skrivebordsprogram som en tjenesteadministrator kan bruke til å konfigurere en Outline-tjener, generere [tilgangsnøkler](#accesskey) og angi datagrenser for bruk per nøkkel. Du kan laste ned den nyeste versjonen av Outlook-administratoren [her](https://getoutline.org/get-started/#step-3) eller [her](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Hva er Outline-klienten?**

 Outline-klienten er både et skrivebordsprogram og en mobilapp som gjør at du kan koble til en Outline-tjener og få tilgang til VPN ved bruk av en tilgangsnøkkel. Du kan laste ned den nyeste versjonen av Outlook-klienten [her](https://getoutline.org/get-started/#step-3) eller [her](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Hva er datagrenser?**

 I Outline-administratoren kan tjenesteadministratorer angi en 30-dagers datagrense med sporing for tilgangsnøkler, noe som gjør det enklere å hindre overforbruk og forutse kostnader. Tjenesteadministratorer kan angi en standardgrense som gjelder for alle nøklene. Det er også mulig å angi en annen grense som overstyrer standardgrensen, for enkelte nøkler. Grensen trer i kraft så snart den er angitt, og den gjelder hver time.

Tjenesteadministratorer som velger å dele beregninger med Jigsaw, bør lese [retningslinjene for datainnsamling](/about/data-collection) for å finne ut mer om hvordan bruken av datagrenser rapporteres.
