---
title: Segurtasuna eta pribatutasuna Outline erabiltzean
sidebar_label: Segurtasuna eta pribatutasuna Outline erabiltzean
---

Segurtasuna eta pribatutasuna Outline erabiltzean

## Nola babesten ditu Outline-k sareko komunikazioak?

Interneteko trafikoa gainbegiratzeko arrisku handiena tokiko sarean edo sare nazionalean zehar bidaiatzen ari denean egon ohi da.

Outline-k komunikazioen pribatutasuna babesten laguntzen dizu, Interneteko trafikoa sare nazionalean zehar bidaiatzen ari denean hura enkriptatuta. Gainera, enkriptatuta mantentzen du Outline-ren zerbitzarira iristen den arte. Trafikoa Outline bidez enkriptatzen denean, sarearen zelatariek ezin dute ikusi zer webgune bisitatzen dituzun edo zer informazio transferitzen duzun.

Halaber, agian zure herrialdean erabilgarri ez dauden muturretik muturrerako komunikazio-tresna seguruak erabiltzeko aukera berreskuratzen lagun diezazuke Outline-k.

## Enkriptatze-arauak

Outline-k AEAD-en 256 biteko Chacha2020 IETF Poly 1305 enkriptatze-katea erabiltzen du zure gailuaren eta Outline-ren zerbitzariaren arteko komunikazioak enkriptatzeko. AEAD-en enkriptatze-kateek isilpekotasuna, osotasuna eta benetakotasuna eskaintzen dute eta errendimendu bikaina daukate hardware modernoan.

## Segurtasun-auditoretzak

2018an, Outline-ri auditoretza bat egin zioten Radically Open Security-k eta Cure53-k. Segurtasun digitaleko bi erakunde independente horiek azken segurtasun-arauen arabera berrikusten dute softwarea. Radically Open Security-k beste auditoretza bat egin zuen 2022an, eta Cure53-k Outline-ren SDKren auditoretza egin zuen 2024an. Hemen irakur ditzakezu txostenak:

- [Radically Open Security Penetration Test Report (2018ko martxoa)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (2018ko abendua)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (2022ko abendua)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (2024ko abendua)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Neurketa eta erregistro anonimoak

Outline-k sarbide-gako bakoitzarekin erabilitako banda-zabalera neurtzen du, "transferitutako byte" gisa. Informazio horri esker, zerbitzariaren administratzaileek beharren arabera doi ditzakete hodeiko zerbitzari-hornitzaileekin dituzten banda-zabaleraren harpidetzak. Hala eta guztiz ere, ezin dute ikusi Outline-ren zerbitzariaren bidez bidalitako informazioa.

Lortu Outline-k [datuak eta informazioa biltzeko duen moduari](https://getoutline.org/policies/data-collection) buruzko informazio gehiago.

---

## Segurtasunari eta pribatutasunari buruz maiz egiten diren galderak

## Outline-k anonimo bihur nazake sarean?

Ez, Outline ez da anonimo izateko tresna bat. Outline-k zure pribatutasuna babesten du sareko zelatarien aurrean.

Outline-k ez dizu erabateko anonimotasuna ematen bisitatzen dituzun webguneetan, zu identifikatzeko gai baitira saioa hasten duzunean edo teknika jakin batzuen bidez, hala nola aztarna digital bidezko jarraipena. Mugikorretarako aplikazioen kasuan, telefono adimendun moderno gehienen APIek zure kokapena eskuratzeko baimena ematen diete instalatutako aplikazioei (proxya edozein dela ere), kapsulatutako GPSa erabil baitezakete.

Orokorrean, VPNek babes garrantzitsuak eskaintzen dituzte, batik bat Interneteko gainbegiratzeari dagokionez, baina sarean ibiltzeak arriskuak dakartza beti. VPN bat erabilita ere, Interneteko zerbitzu-hornitzaile batek jada zure identitatea ezagutzen badu eta zure sareko trafikoari begiratu ahal badio, agian Outline-ren zerbitzariko IP helbidea zehazteko gai izango da. Informazio hori Outline-ren zerbitzarirako sarbidea blokeatzeko edo erabilera-ereduak identifikatzeko erabil daiteke; adibidez, noiz konektatu ohi zaren eta gutxi gorabehera non zauden.

## Jakin al dezakete Outline erabiltzen ari naizela?

Ziurrenik bai. Atzitzen dituzun plataforma eta zerbitzuek hodeiko zerbitzari batetik konektatzen ari zarela ikusi ahalko dute ziurrenik. Agian VPN bat erabiltzen ari zarela ondorioztatuko dute batzuetan, baina ezingo dute ikusi zure Interneteko trafikoaren edukia.

## Outline-k zibereraso guztien aurrean babesten al nau?

Ez, ez dago balizko zibereraso guztien aurrean babestuko zaituen tresnarik. Outline-k Internet irekia erabiltzeko aukera ematen dizu eta trafikoa enkriptatzen du zure pribatutasuna babesteko, baina beste eraso batzuen aurrean (hala nola malwarea edo phishinga) zure burua babesteko beste neurri batzuk hartzea gomendatzen dizugu.

Sareko defentsak indartzeko, jardun elkarlanean zure erakundeko zibersegurtasuneko adituarekin. Bestela, [Security Planner](https://securityplanner.org/) webgunean laguntza pertsonalizatua eskura dezakezu segurtasuneko aditu onenen eskutik. Webgune horren helburua da zure beharretarako zibersegurtasun-tresna egokiak aukeratzeko jarraibide argiak ematea.

Halaber, [Jigsaw-ren](https://jigsaw.google.com/) beste zibersegurtasun-produktuak ikus ditzakezu; esaterako, [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) eta [Pasahitz-babesaren alerta](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Legezkoa al da VPN bat erabiltzea?

Outline edo haren aplikazioa erabili aurretik, irakurri tokiko legeak, erregelamenduak eta erabiliko duzun hodeiko hornitzailearen Zerbitzu-baldintzak.
