---
title: Säkerhet och integritet när du använder Outline
sidebar_label: Säkerhet och integritet när du använder Outline
---

Säkerhet och integritet när du använder Outline

## Så här skyddas kommunikation online av Outline

Internettrafik är som mest sårbar för övervakning när den färdas inom ett lokalt eller nationellt nätverk.

Med Outline krypteras internettrafiken medan den färdas inom ett nationell nätverk tills den når Outline-servern. På så sätt är kommunikationen privat. När trafik krypteras med Outline kan ingen obehörig i nätverket se vilka webbplatser du besöker eller vilken information som överförs.

Med hjälp av Outline kan du även komma åt säkra verktyg för ändpunktskommunikation som kanske inte är tillgängliga i ditt land.

## Krypteringsstandard

Outline krypterar kommunikation mellan enheten och Outline-servern med hjälp av IETF Poly 1305-chiffret AEAD 256-bit Chacha2020. AEAD-chiffer erbjuder konfidentialitet, integritet och autenticitet och fungerar utmärkt på modern hårdvara.

## Säkerhetsgranskningar

Under 2018 granskades Outline av Radically Open Security och Cure53, två oberoende organisationer inom digital säkerhet som granskar mjukvara mot den senaste säkerhetsstandarden. Radically Open Security gjorde ytterligare en granskning 2022 och Cure53 gjorde en granskning av Outline SDK 2024. Rapporterna finns att läsa här:

- [Radically Open Security Penetration Test Report (March 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (December 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (december 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (januari 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonyma mätvärden och loggar

Outline registrerar vilken bandbredd som används i form av antalet överförda byte för varje åtkomstnyckel. Med hjälp av dessa uppgifter kan serveradministratörerna justera prenumerationerna på bandbredd när det behövs, men de kan inte se den faktiska informationen som överfördes via Outline-servern.

Läs mer om [insamling av data och information](/about/data-collection) i Outline.

---

## Vanliga frågor om säkerhet och integritet

## Kan Outline göra mig anonym på internet?

Nej, Outline är inte ett verktyg för anonymitet. Outline skyddar din integritet från personer med insyn i nätverket.

Outline ger dig inte fullständig anonymitet på webbplatser du besöker, eftersom webbplatserna fortfarande kan identifiera dig när du loggar in eller genom att använda tekniker som webbläsarsignaturer. För mobilappar har de flesta moderna smartphones API:er som ger installerade appar möjlighet att ta emot platsdata oberoende av proxyservern, eftersom de kan förlita sig på den inbyggda GPS:en

I allmänhet ger VPN viktiga former av skydd, i synnerhet från övervakning på internet, men det finns alltid risker med att använda internet. Om en internetleverantör känner till din identitet och kan iaktta nätverkstrafiken är det även möjligt att det går att fastställa Outline-serverns IP-adress, även om du har ett VPN. Informationen kan användas för att blockera åtkomst till Outline-servern och identifiera användningsmönster, som när du oftast är online och kanske även din ungefärliga plats.

## Kan någon se om jag använder Outline?

Det är möjligt. Plattformarna och tjänsterna du använder kan troligtvis se att anslutningen kommer från en molnserver. Ibland kan de dra slutsatsen att du använder ett VPN, men de kan inte se internettrafikens innehåll.

## Skyddar Outline mig från alla typer av hot på internet?

Nej. Inget enskilt verktyg kan skydda dig mot alla faror på internet. Med Outline får du åtkomst till ett öppet internet samtidigt som din integritet skyddas genom kryptering av trafiken, men vi rekommenderar att du vidtar ytterligare försiktighetsåtgärder så att du skyddas mot olika typer av angrepp, t.ex. skadlig kod och nätfiske.

Vi rekommenderar att du samarbetar med organisationens expert på cybersäkerhet för att öka skyddet online. Du kan även få personlig rådgivning från ledande säkerhetsexperter hos [Security Planner](https://securityplanner.org/), en webbplats som har skapats för att tillhandahålla tydliga anvisningar om hur du väljer de verktyg för cybersäkerhet som passar dig.

Du kan även kolla in andra produkter för cybersäkerhet från [Jigsaw](https://jigsaw.google.com/), till exempel [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) och [Lösenordsskydd](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Är det lagligt att använda ett VPN?

Kontrollera lokala lagar och föreskrifter, samt användarvillkoren för den molnleverantör du tänkt använda innan du kör Outline eller använder appen.
