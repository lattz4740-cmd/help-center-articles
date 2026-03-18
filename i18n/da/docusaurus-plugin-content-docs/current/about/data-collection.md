---
title: Indsamling af data og oplysninger
sidebar_label: Indsamling af data og oplysninger
---

Outline indsamler ikke personlige oplysninger, medmindre du tilvælger at angive dem. Outline indsamler heller ikke oplysninger om de websites, du besøger, eller med hvem eller hvad du kommunikerer.

 Hvis du opretter eller logger ind på en konto hos en tredjepartscloududbyder via Outline Manager, modtager vi ingen af de oplysninger, du giver til din tredjepartscloududbyder, f.eks. mailadresse, navn, faktureringsoplysninger og betalingsoplysninger.

****Oplysninger, som vi automatisk indhenter****

 Vi indsamler automatisk to typer oplysninger.

 1. Serverens IP-adresse

 Outline-serverens IP-adresse indsamles af [LINKQuay.io](https://quay.io/) og gøres tilgængelig for os, når serveren automatisk opdateres med de nyeste forbedringer af sikkerheden og funktionerne. Serverens IP-adresse kan identificere cloudserverudbyderen og den by, hvor Outline-serveren er oprettet, men den giver ingen oplysninger om, hvem der driver serveren, eller hvem der har adgang til den.

 2. Ikke-personhenførbare tekniske oplysninger

 Hvis Outline går ned, eller der opstår en alvorlig undtagelse, eller hvis du manuelt sender feedback via Outline-appen, rapporteres nedenstående oplysninger. Disse oplysninger bruges kun som en hjælp til at identificere og løse problemer med stabiliteten eller ydeevnen.

- Land
- Landestandard
- Dato og klokkeslæt for nedbrud/undtagelse og op til 100 forudgående hændelser, f.eks. en bruger, der åbner sektionen "Om"
- Statisk kompilerede undtagelsesmeddelelser
- Version og navn på operativsystem
- Telefonmodel (hvis det er relevant)
- Starttidspunkt for app
- Browser
- Arkitektur
- Outline-version og buildnummer

Disse oplysninger overføres via HTTPS til Sentry ([sentry.io](https://sentry.io/)), som er en tredjepartsudbyder af open source-fejlsporing. Sentry benytter en række forskellige teknologier og tjenester, der er standard i branchen, til at beskytte dine data mod uautoriseret adgang, videregivelse, brug og tab. Hvis du har spørgsmål om Sentrys politikker, kan du gå til [https://sentry.io/security/](https://sentry.io/security/) og [https://sentry.io/privacy/](https://sentry.io/privacy/) eller kontakte [security@sentry.io](mailto:security@sentry.io). Alle Outline-data, der lagres af Sentry, er adgangsbegrænsede, så kun medlemmer af Outline-teamet kan få adgang til dem.

****Oplysninger, vi kun indhenter ved tilvalg****

 Outline rapporterer følgende oplysninger til Outline-teamet ved tilvalg.

 1. Brugsmetrics

 For den sidste time og pr. adgangsnøgle indsamler hver Outline-server automatisk oplysninger om antallet af overførte bytes, hvor længe brugeren havde forbindelse til serveren, hvilke lande og hvilke automatiserede systemer de anvendte loginoplysninger stammer fra, og om eventuelle funktioner er blevet aktiveret eller deaktiveret. Hverken indholdet af kommunikationen eller personhenførbare metadata (f.eks. loginoplysninger, mails, enheds-id'er osv.) logføres. Alle metrics er knyttet til et server-id. Du kan finde en vejledning i, hvordan du ændrer server-id'et, [her](/manager/server-management/reset-server-id)

 Outline-servere videregiver som standard ikke disse metrics til Outline-teamet. Hvis serveradministratoren udtrykkeligt tilvælger deling af brugsmetrics, sendes disse oplysninger på sikker vis til Outline-teamet en gang i timen. Efter 60 dage samles brugsmetrics på landeniveau. Serveradministratorer kan til enhver tid ændre deres præferencer for deling af brugsmetrics ved at gå til menuen "Indstillinger" i Outline Manager.

 Vi sætter pris på, at du deler anonyme metrics om din serverbrug med os, da vi bruger dem til at følge brugstendenser og til at forbedre produktet.

 Hvis en serveradministrator vælger at dele brugsmetrics med os, kan vi f.eks. modtage oplysninger, der indikerer, at en server med id'et 12345 blev brugt i tre timer i går til at overføre i alt 500 MB data fra tre nøgler, som hver især blev brugt i USA og Canada, og at datagrænsefunktionen var aktiveret.

 2. Dine kommentarer og din mail, hvis du indsender feedback

 Outline Manager og Outline Apps giver dig mulighed for at indsende feedback til teamet. Vi anbefaler, at du ikke medtager personhenførbare oplysninger, men du kan vælge at udfylde mailfeltet, hvis du gerne vil modtage et svar fra teamet. Vi indsamler også automatisk nogle grundlæggende oplysninger, så vi kan forstå din feedback. Se punkt 2 ovenfor under "Oplysninger, som vi automatisk indhenter" for at se, hvilke data vi indsamler. Få flere oplysninger om Outlines sikkerheds- og privatlivsprocedurer [her](/about/security-and-privacy).

 Hvis du bruger en betaversion af Outline-appen på Android, kan vi bruge Google-tjenesten [Firebase](https://firebase.google.com/) til at indsamle oplysninger om fejlretning, som kan hjælpe os med at registrere problemer og forbedre Outline. Du kan få flere oplysninger om privatlivs- og sikkerhedspolitikker for Firebase på deres website: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Hvis du ikke vil have Outline til at sende disse oplysninger via Firebase, skal du bruge produktionsversionen af appen.
