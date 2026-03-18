---
title: Slik fungerer Outline
sidebar_label: Slik fungerer Outline
---

**Installering av tjeneren**

 ​Selv om det ser lett ut å installere Outline, skjer det en rekke teknisk kompliserte trinn bak kulissene for å installere tjeneren. Når Outline installeres, kjøres et installeringsskript som utfører følgende trinn:

- Den stabile versjonen av Shadowbox-bildet blir hentet og importert ved hjelp av Docker. Avbildningen ligger på [Quay.io](https://quay.io/): [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Denne avbildningen inneholder Outline-tjeneren og Management API, som senere brukes av Outline Server Management-programmet til å opprette og fjerne tilgangsnøkler, velge eller velge bort rapportering av anonyme verdier osv.
- [Watchtower](https://github.com/v2tec/watchtower) blir installert og konfigurert til å se etter avbildningsoppdateringer hver time, noe som bidrar til å sikre at hver eneste Outline-tjener til enhver tid er oppdatert med de nyeste funksjonene og sikkerhetsforbedringene.
- En nettjener som brukes til å få tilgang til Management API, startes på en tilfeldig port i en hemmelig og tilfeldig bane.
- Det opprettes et [selvsignert SSL-sertifikat](https://en.wikipedia.org/wiki/Self-signed_certificate), slik at administreringen av Outline-tjeneren kan krypteres med TLS selv om den ikke har noe domenenavn. Et unikt fingeravtrykk for dette sertifikatet blir også generert og lagret i appen Outline-administrator, noe som bidrar til å forhindre MITM-angrep.

Outline-installasjonen krever ingen konfigurering når den er installert.

**Tjenersikkerhet**

 Outline-programvaren har åpen kildekode, noe som betyr at alle kan se koden og forbedre den hvis eventuelle sårbarheter blir oppdaget. [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline) er vert for koden vår.

 I tillegg blir alle installerte Outline-tjenere automatisk oppdatert når en ny versjon blir utgitt, slik at ingen Outline-tjenere kjører gamle versjoner av programvaren.

 For å kunne administrere tilgangsnøklene på tjeneren samhandler appen Outline-administrator med en administrasjonstjeneste på Outline-tjeneren. Administrasjonstjenesten kjører på en tilfeldig port og i en hemmelig og unik bane. Selve administrasjonstjenesten er beskyttet mot innsyn, da den ikke responderer på søk med mindre den riktige hemmelige banen oppgis. All kommunikasjon til administrasjonstjenesten blir dessuten kryptert med et [selvsignert SSL-sertifikat](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Vær oppmerksom på at Outline-tjeneren ikke lagrer noen logger, så selv om den skulle bli utsatt for sikkerhetsbrudd, blir ingen brukerdata avslørt. Finn ut mer [her](/about/security-and-privacy). Outline ble revidert av [Radically Open Security](https://radicallyopensecurity.com/) og [Cure53](https://cure53.de/) i 2018. Du kan lese rapportene [her](/about/security-and-privacy).

**Håndtering av UDP-trafikk**

 Outline kan fungere som systemomfattende VPN, noe som betyr at all UDP-trafikk rutes gjennom Outline-tjeneren.

**DNS-trafikk**

Outline utfører alle DNS-oppslag via Outline-tjeneren og beskytter dem med den samme krypteringen som brukes for all annen nettverksaktivitet. DNS-søkene dine går via Outline-tjeneren til Dyn Internet Guide, OpenDNS, Cloudflare DNS eller Quad9 DNS. Outline loggfører aldri DNS-oppslagene dine.
