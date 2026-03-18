---
title: Verzamelen van gegevens
sidebar_label: Verzamelen van gegevens
---

Outline verzamelt geen persoonlijke informatie, tenzij je je hier zelf voor aanmeldt. Outline verzamelt ook geen informatie over de websites die je bezoekt of met wie of waarover je communiceert.

 Als je via de Outline Manager een account maakt of erop inlogt bij een externe cloudprovider, krijgen wij niet de gegevens die je naar je externe cloudprovider stuurt, zoals je e-mailadres, naam, en facturerings- en betalingsgegevens.

****Gegevens die we automatisch verzamelen****

 We verzamelen automatisch 2 soorten gegevens.

 1. Server-IP-adres

 Het server-IP-adres van Outline wordt opgehaald door [Quay.io](https://quay.io/) en aan ons doorgestuurd als de server automatisch wordt geüpdatet met de nieuwste beveiligings- en functieverbeteringen. Met het server-IP-adres kunnen de cloudserverprovider en de stad waarin de Outline-server is ingesteld worden geïdentificeerd, maar we krijgen geen gegevens over wie de server beheert of gebruikt.

 2. Technische gegevens die niet persoonlijk identificeerbaar zijn

 Als Outline crasht of er zich een fatale fout voordoet, of als je handmatig feedback verzendt via de Outline-app, worden onderstaande gegevens verzonden. We gebruiken deze gegevens alleen om problemen met de stabiliteit of de prestaties te identificeren en op te lossen.

- Land
- Regio
- Datum en tijd van de crash/exceptie en maximaal honderd eerdere gebeurtenissen, bijvoorbeeld dat een gebruiker het gedeelte Over heeft bekeken.
- Statisch gecompileerde exceptiemeldingen.
- OS-naam en -versie.
- Model telefoon (indien van toepassing).
- Opstarttijd app
- Browser.
- Architectuur.
- Outline-versie en -buildnummer.

Deze informatie wordt overgezet via HTTPS naar Sentry ([sentry.io](https://sentry.io/)), een open source-foutcontroleprovider van derden. Sentry gebruikt verschillende technologieën en services die voldoen aan de branchenorm om je gegevens te beveiligen tegen ongeautoriseerde toegang, vrijgave, gebruik en verlies. Als je vragen hebt over het beleid van Sentry, ga je naar [https://sentry.io/security/](https://sentry.io/security/) en [https://sentry.io/privacy/](https://sentry.io/privacy/) of neem je contact op met [security@sentry.io](mailto:security@sentry.io). Alle Outline-gegevens die door Sentry worden opgeslagen, zijn alleen toegankelijk voor leden van Team Outline.

****Gegevens die we alleen verzamelen als je je hiervoor aanmeldt****

 Outline stuurt de volgende gegevens naar Team Outline als je toestemming hebt gegeven.

 1. Gebruiksstatistieken

 Elke Outline-server verzamelt automatisch het aantal overgebrachte bytes (voor het afgelopen uur en op basis van gebruikte toegangssleutels), de tijd dat een gebruiker verbinding heeft met de server, de landen en autonome systemen van oorsprong van de gebruikte inloggegevens en of er functies zijn aan- of uitgezet. De inhoud van de communicatie en persoonlijk identificeerbare metadata (zoals inlogpogingen, e-mailadressen of apparaat-ID's) worden niet vastgelegd. Alle statistieken zijn gekoppeld aan een server-ID. [Hier](/manager/server-management/reset-server-id) vind je instructies om de server-ID te wijzigen.

 Standaard delen de Outline-servers deze statistieken niet met Team Outline. Als de serverbeheerder zich expliciet aanmeldt voor het delen van deze gebruiksstatistieken, worden deze gegevens elk uur beveiligd verzonden naar Team Outline. Na zestig dagen worden de gebruiksgegevens verzameld per land. Serverbeheerders kunnen zich op elk moment aan- of afmelden voor het delen van gebruiksstatistieken in het menu Instellingen in de Outline Manager.

 We stellen het erg op prijs als je anonieme statistieken over je servergebruik met ons deelt, omdat we hiermee gebruikstrends kunnen meten en het product kunnen verbeteren.

 Als een serverbeheerder zich bijvoorbeeld aanmeldt voor het delen van gebruiksstatistieken, kunnen we de informatie krijgen dat een server met ID 12345 gisteren 3 uur lang is gebruikt, dat er in totaal 500 megabytes aan gegevens zijn overgebracht via 3 sleutels die allemaal zijn gebruikt in de Verenigde Staten en Canada, met de functie voor datalimieten aangezet.

 2. Je opmerkingen en e-mailadres als je feedback verzendt

 In de Outline Manager en de Outline-apps kun je feedback verzenden naar het team. We raden je af persoonlijk identificeerbare informatie toe te voegen. Eventueel kun je wel je e-mailadres toevoegen als je een antwoord wilt krijgen van het team. We verzamelen ook automatisch wat algemene gegevens, zodat we je feedback kunnen begrijpen. Bekijk hierboven item 2 onder 'Gegevens die we automatisch verzamelen' om te zien welke gegevens we verzamelen. [Hier](/about/security-and-privacy) vind je meer informatie over de beveiligings- en privacyprocedures van Outline.

 Als je een bètaversie van de Outline-app op Android gebruikt, kunnen we de [Firebase](https://firebase.google.com/)-service van Google gebruiken om foutopsporingsinformatie te verzamelen waarmee we problemen kunnen opsporen en Outline kunnen verbeteren. Ga voor meer informatie over het privacy- en beveiligingsbeleid van Firebase naar [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Als je niet wilt dat Outline deze informatie verzendt via Firebase, moet je de productieversie van de app gebruiken.
