---
title: Insamling av data och uppgifter
sidebar_label: Insamling av data och uppgifter
---

Outline samlar inte in personliga uppgifter såvida du inte tillhandahåller dem. Outline samlar inte heller in information om webbplatser du besöker eller med vem eller om vad du kommunicerar.

 Om du skapar eller loggar in på ett konto hos en tredje parts molnleverantör via Outline Manager har vi inte åtkomst till uppgifterna du anger hos tredjepartsleverantören. Det gäller t.ex. e-postadress, namn, faktureringsuppgifter och betalningsuppgifter.

****Uppgifter som vi får automatiskt****

 Vi samlar in två typer av uppgifter automatiskt.

 1. Server-IP

 Outline-serverns IP-adress samlas in av [Quay.io](http://quay.io/) och blir tillgänglig för oss när servern uppdateras automatiskt med de senaste säkerhets- och funktionsförbättringarna. Med hjälp av serverns IP-adress kan det gå att identifiera leverantören av molnservern och i vilken stad Outline-servern har konfigurerats, men det visas ingen information om vem som kör servern eller vem som har åtkomst till den.

 2. Tekniska uppgifter som inte kan kopplas till en specifik individ

 Om Outline kraschar eller ett allvarligt undantag uppstår, eller om du skickar feedback manuellt via Outline-appen, rapporteras de uppgifter som anges nedan. Uppgifterna används endast för att hjälpa oss att identifiera och lösa problem med stabilitet eller prestanda.

- Land
- Språkkod
- Datum och tid för kraschen/systemfelet och upp till 100 tidigare händelser, exempelvis om en användare öppnat avsnittet About (om)
- Statiskt sammanställda undantagsmeddelanden
- Opertivsystemets namn och version
- Mobilens modell (om tillämpligt)
- Tid då appen startades
- Webbläsare
- Arkitektur
- Version och versionsnummer för Outline

Uppgifterna överförs via HTTPS till Sentry ([sentry.io](http://sentry.io/)) som är en tredjepartsleverantör av felspårning i öppen källkod. Sentry använder en rad olika tekniker och tjänster som uppfyller branschstandarden för att skydda din data mot obehörig åtkomst och användning, otillåtet yppande och förlust. Om du har frågor om Sentrys policyer besöker du [https://sentry.io/security/](https://sentry.io/security/) och [https://sentry.io/privacy/](https://sentry.io/privacy/), eller kontaktar företaget direkt på [security@sentry.io](mailto:security@sentry.io). All Outline-data som lagras av Sentry begränsas så att endast medlemmar i Outline-teamet får åtkomst till den.

****Uppgifter vi samlar in på frivillig basis****

 Outline rapporterar följande uppgifter till Outline-teamet på frivillig basis.

 1. Användningsmått

 Varje Outline-server samlar automatiskt in antal byte som har överförts, hur länge en användare var ansluten till servern, ursprungsländerna och ursprung för de autonoma system för användaruppgifter som används samt om funktioner har aktiverats eller inaktiverats under den sista timmen och per åtkomstnyckel. Varken innehållet i kommunikationen eller metadata som kan kopplas till en specifik individ (t.ex. inloggningar, e-post, enhets-id o.s.v.) loggas. Alla mätvärden kopplas till ett server-id. Du hittar anvisningar om att ändra server-id:t [här](/manager/server-management/reset-server-id).

 Som standard delar inte Outlines servrar dessa mätvärden med Outline-teamet. Om serveradministratören uttryckligen väljer att dela mätvärden om användning skickas uppgifterna på ett säkert sätt till Outline-teamet varje timme. Efter 60 dagar sammanställs mätvärden om användning på landsnivå. Serveradministratörer kan när som helst ändra inställningarna för delning av mätvärden om användning via inställningsmenyn i Outline Manager.

 Vi uppskattar att du delar anonyma mätvärden om serveranvändningen med oss, eftersom vi använder dem för att mäta användningstrender och förbättra produkten.

 Om en serveradministratör exempelvis väljer att dela mätvärden om användning med oss kan vi få information som indikerar att en server med id 12345 användes i tre timmar i går och överförde totalt 500 megabyte data via tre åtkomstnycklar i USA och Kanada, och att funktionen för databegränsning var aktiverad.

 2. Dina kommentarer och din e-postadress om du skickar feedback

 Du kan skicka feedback till teamet via apparna Outline Manager och Outline. Vi rekommenderar inte att du anger uppgifter som kan kopplas till dig specifikt, men det finns ett e-postfält som du kan använda om du vill få ett svar från teamet. Vi samlar även automatiskt in grundläggande uppgifter, så att vi kan tolka feedbacken. I punkt 2 ovan under Uppgifter vi får automatiskt kan du läsa om vilken data vi samlar in. Läs mer om Outlines säkerhets- och sekretesspraxis [här](/about/security-and-privacy).

 Om du använder betaversionen av Outline-appen på Android kan Googles [Firebase-tjänst](https://firebase.google.com/) användas till att samla in felsökninginformation i syfte att upptäcka problem och förbättra Outline. Du kan läsa mer om Firebases integritetspolicy och säkerhetspolicy på webbplatsen: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Om du inte vill att Outline skickar denna information via Firebase ska du använda produktionsverionen av appen.
