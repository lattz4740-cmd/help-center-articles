---
title: Kako funkcionira Outline
sidebar_label: Kako funkcionira Outline
---

## Instalacija poslužitelja
 Iako se instalacija Outlinea može činiti jednostavnom, za instalaciju poslužitelja zapravo je potrebno slijediti niz složenih uputa. Svaki put kada se Outline instalira, pokreće se skripta za instalaciju i poduzima sljedeće korake:

- Stabilna verzija slike Shadowbox dohvaća se i uvozi putem Dockera. Slika se hosta na web-lokaciji [Quay.io](https://quay.io/), na adresi [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Ta slika sadrži Outline poslužitelj i Management API koji aplikacija Outline Server Management kasnije upotrebljava za izradu i uklanjanje pristupnih ključeva, uključivanje/isključivanje izvješćivanja o anonimnim mjernim podacima itd.
- [Watchtower](https://github.com/containrrr/watchtower) se instalira i konfigurira radi traženja ažuriranja slike svakih sat vremena, čime se osigurava da je svaki Outline poslužitelj kontinuirano ažuran te da ima najnovije značajke i sigurnosna poboljšanja.
- Web-poslužitelj koji se upotrebljava za pristupanje Managament API-ju pokreće se na nasumičnom priključku na tajnoj i nasumičnoj putanji.
- Izrađuje se [samopotpisani SSL certifikat](https://en.wikipedia.org/wiki/Self-signed_certificate) tako da se upravljanje Outline poslužiteljem može šifrirati pomoću TLS-a bez naziva domene. U aplikaciji Upravitelj Outlinea generira se i sprema jedinstveni otisak prsta tog certifikata. To pomaže u sprječavanju MITM napada.

Instalacija aplikacije Outline ne zahtijeva naknadnu instalaciju konfiguracije.

## Sigurnost poslužitelja
 Outline je softver otvorenog izvornog koda. To znači da bilo tko može vidjeti kôd i poboljšati ga ako se otkriju nedostaci. Naš se kôd hostira na [GitHubu](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline).

 Nadalje, svi instalirani Outline poslužitelji automatski se ažuriraju nakon svake objave nove verzije tako da nijedan Outline poslužitelj nema zastarjelu verziju softvera.

 Radi upravljanja pristupnim ključevima na poslužitelju aplikacija Upravitelj Outlinea komunicira s uslugom za upravljanje na Outline poslužitelju. Usluga za upravljanje pokreće se na nasumičnom priključku te na tajnoj i jedinstvenoj putanji. Ta je usluga otporna na utvrđivanje dostupnosti jer ne odgovara na upite ako se ne navede odgovarajuća tajna putanja. Konačno, sva komunikacija s uslugom za upravljanje šifrirana je [samopotpisanim SSL certifikatom](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Također, Outline poslužitelj ne sprema zapisnike, što znači da se korisnički podaci ne otkrivaju čak ni ako je ugrožen. Više možete saznati [ovdje](/about/security-and-privacy). [Radically Open Security](https://radicallyopensecurity.com/) i [Cure53](https://cure53.de/) provele su reviziju Outlinea 2018. Izvješća potražite [ovdje](/about/security-and-privacy).

## Rukovanje UDP prometom
 Outline funkcionira kao VPN za cijeli sustav, što znači da se cijeli UDP promet kanalizira putem Outline poslužitelja.

## DNS promet
Outline sva pretraživanja DNS-a izvršava putem Outline poslužitelja i štiti ih istim šifriranjem koje se upotrebljava za sve druge mrežne aktivnosti. Upiti DNS-a proći će kroz Outline poslužitelj do Dyn Internet Guidea, OpenDNS-a, Cloudflare DNS-a ili Quad9 DNS-a. Outline nikada ne bilježi vaša mapiranja alfa-numeričkih naziva u IP adresu.
