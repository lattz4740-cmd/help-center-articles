---
title: Az Outline működése
sidebar_label: Az Outline működése
---

## A szerver telepítése
 ​Noha az Outline telepítése egyszerűnek tűnhet, a szerver telepítéséhez a háttérben bonyolult folyamatok zajlanak. Az Outline telepítésekor a telepítési szkript a következő lépéseken halad végig:

- A Docker szolgáltatással lekéri és importálja a Shadowbox kép stabil verzióját. A képet a [Quay.io](https://quay.io/) tárolja a [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags) webhelyen. A kép tartalmazza az Outline-szervert és a Management API-t, mellyel később az Outline Server Management alkalmazás létrehozza és eltávolítja a hozzáférési kulcsokat, engedélyezi és letiltja az anonim mérőszámok elküldését, stb.
- Telepíti és konfigurálja a [Watchtower](https://github.com/containrrr/watchtower) alkalmazást, amely óránként ellenőrzi, hogy rendelkezésre áll-e új képverzió, így biztosítva, hogy az Outline-szerver mindig naprakész legyen, és rendelkezzen a legújabb funkciókkal és biztonsági javításokkal.
- A rendszer elindít egy webszervert egy véletlenszerűen kiválasztott porton, egy titkos és véletlenszerű elérési úton, mely a Management API-hoz való hozzáféréshez szükséges.
- Létrehoz egy [saját aláírású SSL-tanúsítványt](https://en.wikipedia.org/wiki/Self-signed_certificate), hogy domainnév hiányában is lehessen a TLS protokollal titkosítani az Outline-szerver kezelését. Emellett létrejön a tanúsítvány egyedi ujjlenyomata, melyet a rendszer az Outline Manager alkalmazásban tárol, így megakadályozva a közbeékelődéses támadásokat.

A telepítést követően nem kell konfigurálni az Outline szolgáltatást.

## Szerverbiztonság
 Az Outline szoftver nyílt forráskódú, ami azt jelenti, hogy bárki hozzáférhet a programkódhoz, és ha biztonsági rést talál, tovább is fejlesztheti. A programkód a [GitHub](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline) webhelyén található.

 Emellett a telepített Outline-szerverek automatikusan frissülnek minden alkalommal, amikor új verzió jelenik meg, így egy Outline-szerver sem fogja a szoftver régebbi verzióját futtatni.

 A szerveren lévő hozzáférési kulcsok kezeléséhez az Outline Manager alkalmazás az Outline-szerveren lévő felügyeleti szolgáltatással kommunikál. A felügyeleti szolgáltatás egy véletlenszerűen kiválasztott porton és egy titkos és egyedi elérési úton fut. A felügyeleti szolgáltatás ellenáll a lekérdezéses támadásoknak, mivel csak abban az esetben reagál a lekérdezésekre, ha a megfelelő titkos elérési út van megadva. Végül pedig a felügyeleti szolgáltatással folytatott kommunikáció teljes mértékben titkosítva van egy [saját aláírású SSL-tanúsítvánnyal](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Az Outline-szerver nem naplózza a forgalmat, így ha illetéktelenek fel is törnék, nem férhetnének hozzá a felhasználói adatokhoz. További információ [itt](/about/security-and-privacy) található. 2018-ban az Outline-t két szervezet, a [Radically Open Security](https://radicallyopensecurity.com/) és a [Cure53](https://cure53.de/) auditálta. Az erről szóló jelentéseket [itt](/about/security-and-privacy) találja.

## Az UDP-forgalom kezelése
 Az Outline képes rendszerszintű VPN-ként működni, ami azt jelenti, hogy az összes UDP-forgalom az Outline-szerveren halad keresztül.

## DNS-forgalom
Az Outline az összes DNS-keresést az Outline-szerveren keresztül hajtja végre, és a többi hálózati tevékenységhez használt titkosítással védi. A DNS-lekérdezések az Outline szerveren át jutnak el a Dyn Internet Guide, az OpenDNS, a Cloudflare DNS vagy a Quad9 DNS szolgáltatáshoz. Az Outline sohasem naplózza a DNS-kereséseket.
