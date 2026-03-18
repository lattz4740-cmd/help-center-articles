---
title: "Outline'i tööpõhimõte"
sidebar_label: "Outline'i tööpõhimõte"
---

**Serveri installimine**

 ​Kuigi Outline'i installimine võib tunduda lihtne, leiavad kulisside taga aset keerukad protseduurid teie serveri installimiseks. Outline'i installimisel käitab installiskript järgmisi toiminguid.

- Shadowboxi kujutise stabiilne versioon tuuakse ja imporditakse Dockeri abil. Kujutist hostitakse teenuses [Quay.io](https://quay.io/) aadressil [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Kujutis sisaldab Outline'i serverit ja Management API-d, mille abil Outline'i serveri haldusrakendus saab hiljem pääsuvõtmeid luua ja eemaldada, anonüümsete mõõdikute esitamise lubada/keelata jms.
- [Watchtower](https://github.com/v2tec/watchtower) installitakse ja seadistatakse nii, et see kontrolliks kujutise värskendusi kord tunnis. See aitab tagada, et kõik Outline'i serverid oleksid alati asjakohased ning hõlmaksid uusimaid funktsioone ja turbetäiustusi.
- Veebiserver, mida kasutatakse Management API-le juurdepääsemiseks, käivitatakse salajasel ja juhuslikul teel juhuslikus pordis.
- [Iseallkirjastatud SSL-sertifikaat](https://en.wikipedia.org/wiki/Self-signed_certificate), et Outline'i serveri haldust saaks TLS-iga krüpteerida vaatamata sellele, et domeeninimi puudub. Samuti luuakse selle sertifikaadi unikaalne sõrmejälg, mis talletatakse Outline Manageri rakenduses ja mis aitab takistada vahendusründeid.

Installitud Outline'i ei ole vaja pärast installimist seadistada.

**Serveri turvalisus**

 Outline'i tarkvara on avatud lähtekoodiga, mis tähendab, et igaüks saab koodi vaadata ja haavatavuste leidmisel täiustada. Meie koodi hostib [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Lisaks värskendatakse uue versiooni väljalaskmisel kõiki installitud Outline'i servereid automaatselt, et ükski Outline'i server ei käitaks tarkvara vana versiooni.

 Selleks et hallata serveris pääsuvõtmeid, suhtleb Outline Manageri rakendus Outline'i serveris oleva haldusteenusega. Haldusteenus töötab juhuslikus pordis ning salajasel ja unikaalsel teel. Haldusteenus ise on sondeerimiskindel, kuna see reageerib päringutele ainult juhul, kui määratud on sobiv salajane tee. Viimaks krüpteeritakse kogu side haldusteenusega [iseallkirjastatud SSL-sertifikaadi](https://en.wikipedia.org/wiki/Self-signed_certificate) abil.

 Lisaks ei talleta Outline'i server ühtki logi, seega isegi kui selle turvalisust rikutakse, ei avalikustata kasutajaandmeid. Vaadake lisateavet [siit](https://support.getoutline.org/s/article/Security-and-privacy). Outline'i auditeerisid [Radically Open Security](https://radicallyopensecurity.com/) ja [Cure53](https://cure53.de/) aastal 2018. Vaadake aruandeid [siin](https://support.getoutline.org/s/article/Security-and-privacy).

**UDP-liikluse juhtimine**

 Outline suudab toimida süsteemiülese VPN-ina, mis tähendab, et kogu UDP-liiklus suunatakse läbi Outline'i serveri.

**DNS-i liiklus**

Outline teeb kõik DNS-i otsingud Outline'i serveri kaudu ja kaitseb neid sama krüpteerimismeetodiga, mida kasutatakse kõigi muude võrgutegevuste puhul. Teie DNS-päringud suunatakse läbi Outline'i serveri teenusesse Dyn Internet Guide, OpenDNS, Cloudflare DNS või Quad9 DNS. Outline ei logi kunagi teie DNS-i otsinguid.
