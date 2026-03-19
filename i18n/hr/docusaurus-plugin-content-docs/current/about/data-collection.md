---
title: Prikupljanje podataka i informacija
sidebar_label: Prikupljanje podataka i informacija
---

Outline ne prikuplja osobne podatke, osim u slučaju kada uključite tu opciju. Outline ne prikuplja podatke o vašim komunikacijama ili o web-lokacijama koje posjećujete.

 Ako izrađujete račun ili se prijavljujete na račun pomoću davatelja usluga u oblaku treće strane putem Upravitelja Outlinea, ne prikupljamo podatke koje šaljete davatelju usluga u oblaku treće strane, kao što su vaša e-adresa, ime te podaci za naplatu i plaćanje.

## Podaci koje automatski prikupljamo
 Automatski prikupljamo dvije vrste podataka.

 1. IP poslužitelja

[Quay.io](https://quay.io/) prikuplja podatke o IP-u Outline poslužitelja i prosljeđuje nam ih kad se na poslužitelju automatski primijene ažuriranja sigurnosti i poboljšanja značajki. IP poslužitelja može identificirati davatelja usluga u oblaku i grad u kojem je Outline poslužitelj postavljen, ali nisu dostupni podaci o tome tko pokreće poslužitelj ili tko mu pristupa.

 2. Tehnički podaci koji ne otkrivaju osobni identitet

 Ako se Outline sruši ili dođe do fatalne iznimke odnosno ako ručno šaljete povratne informacije putem aplikacije Outline, poslat će se izvješće s podacima navedenim u nastavku. Ti se podaci upotrebljavaju samo za utvrđivanje i rješavanje problema sa stabilnošću ili izvedbom.

- Država
- Jezik
- Datum i vrijeme rušenja / iznimke i do 100 prethodnih događaja, na primjer kada korisnik otvori odjeljak “Više o”
- Statistički sastavljene poruke o iznimci
- Naziv i verzija OS-a
- Model telefona (ako se primjenjuje)
- Vrijeme početka aplikacije
- Preglednik
- Arhitektura
- Verzija i broj međuverzije aplikacije Outline

Ti se podaci pomoću HTTPS-a prenose u Sentry ([sentry.io](https://sentry.io/)), davatelj treće strane za usluge praćenja pogrešaka otvorenog izvornog koda. Sentry upotrebljava razne usluge i tehnologije koje su standard djelatnosti da bi zaštitio vaše podatke od neovlaštenog pristupa, otkrivanja, upotrebe i gubitka. Ako imate pitanja o pravilima Sentryja, posjetite [https://sentry.io/security/](https://sentry.io/security/) i [https://sentry.io/privacy/](https://sentry.io/privacy/) ili pošaljite e-poruku na adresu [security@sentry.io](mailto:security@sentry.io). Pristup svim podacima aplikacije Outline koje Sentry pohranjuje ograničen je, što znači da im mogu pristupiti samo članovi tima za Outline.

## Podaci koje dobivamo samo nakon uključivanja određenih značajki
 Outline šalje izvješća sa sljedećim informacijama timu za Outline nakon uključivanja.

 1. Mjerni podaci o upotrebi

 Svaki Outline poslužitelj automatski prikuplja broj prenesenih bajtova, vrijeme tijekom kojeg je korisnik bio povezan s poslužiteljem, države i autonomne sustave porijekla upotrijebljenih vjerodajnica te jesu li značajke omogućene ili onemogućene. Ti se podaci prikupljaju za posljednji sat i za svaki pristupni ključ. Ne bilježi se sadržaj komunikacije ni metapodaci koji mogu otkriti osobni identitet (npr. prijave, e-poruke, ID-jevi uređaja itd.). Svi mjerni podaci povezani su s ID-jem poslužitelja. Upute za promjenu ID-a poslužitelja mogu se pronaći [ovdje](/manager/server-management/reset-server-id).

 Prema zadanim postavkama Outline poslužitelji ne dijele te mjerne podatke s timom za Outline. Ako administrator poslužitelja izričito uključi dijeljenje mjernih podataka o upotrebi, ti se podaci na siguran način šalju timu za Outline svakih sat vremena. Nakon 60 dana zbrojit će se mjerni podaci o upotrebi na razini zemlje. Administratori poslužitelja mogu promijeniti postavku za dijeljenje mjernih podataka o upotrebi na izborniku Postavke u Upravitelju Outlinea.

 Bit ćemo vam zahvalni ako s nama podijelite anonimne podatke o upotrebi poslužitelja jer ćemo pomoću njih izmjeriti trendove upotrebe i poboljšati proizvod.

 Na primjer, ako administrator poslužitelja uključi dijeljenje mjernih podataka o upotrebi, mogli bismo primiti podatke koji označavaju da je poslužitelj s ID-jem 12345 jučer upotrebljavan tri sata i da je prenio ukupno 500 MB podataka putem tri ključa od kojih je svaki upotrijebljen u SAD-u i Kanadi s omogućenom značajkom ograničenja podatkovnog prometa.

 2. Vaši komentari i e-pošta ako pošaljete povratne informacije

 Upravitelj Outlinea i Outline aplikacije omogućuju vam da pošaljete povratne informacije timu. Preporučujemo da ne navodite podatke koji otkrivaju identitet, ali za slučaj da želite primiti odgovor tima, dostupno vam je polje za e-adresu. Automatski prikupljamo i neke osnovne podatke da bismo bolje razumjeli vaše povratne informacije. Da biste saznali koje podatke prikupljamo, pročitajte 2. odjeljak, Podaci koje automatski prikupljamo. Više o praksama Outlinea u vezi sa sigurnošću i privatnošću možete saznati [ovdje](/about/security-and-privacy).

 Ako upotrebljavate beta verziju aplikacije Outline na Androidu, možemo pomoću Googleove usluge [Firebase](https://firebase.google.com/) prikupiti informacije za otklanjanje pogrešaka koje će nam pomoći da prepoznamo probleme i poboljšamo Outline. Više o pravilima o privatnosti i sigurnosti Firebasea možete saznati na web-lokaciji [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Ako ne želite da Outline te podatke šalje putem Firebasea, upotrijebite produkcijsku verziju aplikacije.
