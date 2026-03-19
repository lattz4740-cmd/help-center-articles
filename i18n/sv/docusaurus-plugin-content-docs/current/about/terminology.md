---
title: Terminologi
sidebar_label: Terminologi
---

## Vad är VPN?
 Ett virtuellt privat nätverk (VPN) är en privat anslutning mellan dina enheter och en värdserver. När du använder VPN döljs din trafik från internetleverantören. VPN kan användas för att

- skydda din data när du använder ett offentligt wifi-nätverk
- dölja din webbinformation från din internetleverantör och myndigheter
- komma åt ocensurerat innehåll från världen över.

## Hur skiljer sig Outline från traditionella VPN?
 Internetleverantörer kan enkelt upptäcka och blockera traditionella VPN genom att identifiera vanliga säkerhetsprotokoll och/eller mönster för trafikvolym. Outline är mer motståndskraftigt än traditionella VPN eftersom det är byggt med ett protokoll som har utformats för att vara svårt att upptäcka och därmed svårare att blockera. Outline motstår sofistikerade former av censur som nätverksbaserad blockering eller IP-blockering.

## Vad är en Outline-server?
 En Outline-server kör ett VPN som tillåtna användare ansluter till. Om du skapar ett nytt nätverk kan du använda din egen säkra server som Outline-server om du har en, eller så kan du använda en leverantör av molntjänster, till exempel

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Du konfigurerar servern i Outline Manager.

## Vad är en tjänsteansvarig? {#servicemanager}
 En tjänsteansvarig är personen som är ansvarig för att konfigurera Outline-servern och dela åtkomstnycklarna med användare. Den tjänsteansvariga är vanligtvis ansvarig för kostnaden för användningen av servern. 

## Vad är en åtkomstnyckel? {#accesskey}
 En åtkomstnyckel används för att komma åt en befintlig Outline-server och ansluta till VPN. En [tjänsteansvarig](#servicemanager) ger dig en åtkomstnyckel, eller så kan du [konfigurera en Outline-server](/manager/server-setup/setup-server) själv. Här är ett exempel på hur en åtkomstnyckel ser ut (endast exempel, fungerar inte): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Vad är Outline Manager?
 Outline Manager är ett datorprogram som en tjänsteansvarig kan använda för att konfigurera en Outline-server, generera [åtkomstnycklar](#accesskey) och ange datagränser för användningen per nyckel. Du kan ladda ned den senaste versionen av Outline Manager [här](https://getoutline.org/get-started/#step-3) eller [här](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Vad är Outline Client?
 Outline Client är ett program, tillgängligt för dator och mobil, som gör att du kan ansluta till en Outline-server och få åtkomst till VPN med hjälp av en åtkomstnyckel. Du kan ladda ned den senaste versionen av Outline Client [här](https://getoutline.org/get-started/#step-3) eller [här](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Vad är datagränser?
 Med Outline Manager kan tjänsteansvariga ställa in en löpande datagräns på 30 dagar för åtkomstnycklar för att förhindra överanvändning och hålla koll på kostnaderna. Tjänsteansvariga kan ställa in en standardgräns som gäller för alla nycklar samt andra gränser för enskilda nycklar som åsidosätter standardgränsen. När en gräns har ställts in börjar den gälla omedelbart och tillämpas varje timme.

Om tjänsteansvariga väljer att dela mätvärden med Jigsaw kan de läsa om hur användningen av datagränser rapporteras i [policyn för datainsamling](/about/data-collection).
