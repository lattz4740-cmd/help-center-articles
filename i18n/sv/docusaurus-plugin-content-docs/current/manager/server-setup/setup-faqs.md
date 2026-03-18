---
title: "Vanliga frågor om konfiguration av Outline-servrar"
sidebar_label: "Vanliga frågor om konfiguration av Outline-servrar"
---

**Går det att använda Outline utan en server?**

 Tyvärr inte. Outlines mjukvara behöver åtkomst till en server, oavsett om den hanteras av dig, en organisation eller tredje part.

## Hur lång tid tar det att konfigurera en Outline-server?

Oftast tar under fem minuter. Du kan installera Outline på valfri molnserver, men vi samarbetar med DigitalOcean för att erbjuda en mer användarvänlig installation så att du kan konfigurera servern på bara några klick, helt utan skript.

Om du väljer AWS, GCP eller avancerad konfiguration har vi gjort installationen enkel med ett enda skript som hanterar de flesta miljöer.

## Var kan jag konfigurera en Outline-server?

Det går att konfigurera en Outline-server hos de flesta molnleverantörer oavsett var de är baserade.

Det enklaste alternativet är att konfigurera servern hos DigitalOcean eftersom de har servrar på flera olika platser, till exempel Amsterdam, Toronto, San Francisco och Singapore. Om du hellre vill installera den hos en annan molnleverantör eller i din egen infrastruktur kan du välja Advanced Mode (avancerat läge) i Outline Manager-appen och följa installationsanvisningarna med hjälp av ett konfigurationsskript.

## Var ska jag konfigurera Outline-servern?

1. Du ska tänka på några saker när du väljer plats för Outline-servern:
2. Outline-servern plats påverkar vilken upplevelse användarna får på internet. Om servern finns i till exempel Amsterdam visas internet för användarna på servern som om de faktiskt befann sig i Nederländerna. En del webbplatser kanske till och med visas på nederländska. Det går oftast att åsidosätta det lokala språket med hjälp av en språkväljare på webbplatsen.
3. Avståndet mellan användarna och Outline-servern kan påverka hastigheten. Det är vanligt att det fysiska avståndet mellan Outlines användare och servern påverkar användarnas internethastighet. Det går oftast att välja en server i närheten av där användarna troligen befinner sig, men du kan kolla [Submarine Cable Map](https://www.submarinecablemap.com/) för att se vilka internetkablar som är ansluta till ditt land eller din region.
4. VPN-serverns plats kan påverka det juridiska ramverket. Observera att Outlines mjukvara inte loggar din trafik. Läs mer om [säkerhet och integritet när du använder Outline](/about/security-and-privacy).
