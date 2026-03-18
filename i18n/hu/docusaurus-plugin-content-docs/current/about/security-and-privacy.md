---
title: Biztonság és adatvédelem az Outline használata során
sidebar_label: Biztonság és adatvédelem az Outline használata során
---

Biztonság és adatvédelem az Outline használata során

## Hogyan óvja meg az Outline az online kommunikációt?

Illetéktelenek akkor figyelhetik meg a legegyszerűbben az internetes forgalmat, ha az épp a helyi vagy országos hálózaton zajlik.

Az Outline-nal egyszerűen rejtheti el a forgalmazott adatokat az illetéktelenek elől, hiszen a rendszer titkosítja őket az országos hálózaton, és egészen az Outline-szerverig való eljutásukig titkosítva is tartja őket. Az Outline-nal titkosított forgalom alapján a hálózatról senki sem tudhatja meg, milyen webhelyeket nyitott meg, vagy hogy milyen információkat visz át.

Az Outline emellett abban is segít, hogy azokhoz a biztonságos, végpontok közötti eszközökhöz is hozzáférhessen, amelyek egyébként le vannak tiltva az országában.

## Titkosítási szabványok

Az Outline az AEAD (256 bites) Chacha2020 IETF Poly 1305 rejtjelezéssel titkosítja az eszköze és az Outline-szerver közötti kommunikációt. Az AEAD-rejtjelezés megbízható, integratív és hatékony megoldás, amely kiváló teljesítményt nyújt modern hardvereken.

## Biztonsági auditálások

2018-ban az Outline-t két független, digitális biztonsággal foglalkozó szervezet, a Radically Open Security és a Cure53 is auditálta. A szervezetek a legújabb biztonsági szabványoknak való megfelelőséget vizsgálják. A Radically Open Security még egy további auditálást is elvégzett 2022-ben, a Cure53 pedig 2024-ben végezte el az Outline SDK auditálását. A jelentéseket itt találja:

- [A Radically Open Security behatolási tesztjéről készült jelentés (2018. március)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [A Cure53 behatolási tesztjéről és auditálásáról készült jelentés – Jigsaw Outline (2018. december)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [A Radically Open Security behatolási tesztjéről készült jelentés (2022. december)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [A Cure53 behatolási tesztjéről készült jelentés – Jigsaw Outline VPN SDK (2024. január)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonimizált mérőszámok és naplók

Az Outline az egyes hozzáférési kulcsokhoz tartozó „átvitt bájtokként” követi nyomon a felhasznált sávszélességet. Ezen információ birtokában a szerveradminisztrátorok az igényeknek megfelelően állíthatják be a felhőszerver-szolgáltatóval kötött sávszélesség-előfizetéseiket, de nem férhetnek hozzá az Outline-szerveren ténylegesen áthaladó információkhoz.

További információ az Outline által végzett [adat- és információgyűjtésről](/about/data-collection).

---

## Biztonsági és adatvédelmi GYIK

## Képes az Outline anonimmá tenni az online jelenlétemet?

Nem, az Outline nem az internethasználat anonimizálására szolgáló eszköz, csupán a forgalmához illetéktelenül hozzáférni kívánók elől óvja meg adatait.

Az Outline nem biztosít teljes anonimitást a megnyitott webhelyeken, mert azok továbbra is képesek azonosítani Önt, ha bejelentkezik, illetve más módokon (például böngésző-ujjlenyomatok alapján). Ha mobilalkalmazásokat használ, a legtöbb modern okostelefon rendelkezik olyan API-kkal, melyek lehetővé teszik a telepített appoknak, hogy a proxytól függetlenül (a beépített GPS-nek köszönhetően) lekérjék a helyadatait.

A virtuális magánhálózatok (VPN-ek) hatékony védelmet nyújtanak, különösen az internetes megfigyeléssel szemben, de az internethasználattal járó kockázatok soha nem szüntethetők meg teljesen. Még ha VPN-t is használ, az internetszolgáltató már tisztában van a személyazonosságával, és megfigyelheti a hálózati forgalmát, így megállapíthatja például az Outline-szerver IP-címét. Ezen információ birtokában letilthatja az Outline-szerverhez való hozzáférését, vagy akár megismerheti a használati szokásait, például hogy mikor szokott csatlakozni az internethez, sőt akár a körülbelüli tartózkodási helyét is lekérheti.

## Mások láthatják, hogy az Outline-t használom?

Lehetséges. A használt platformok és szolgáltatások valószínűleg képesek megmondani, hogy a kapcsolatot egy felhőszerverről indította. Ebből aztán kikövetkeztethetik, hogy VPN-t használ, de magához az internetes forgalom tartalmához nem férhetnek hozzá.

## Képes megvédeni az Outline az összes lehetséges számítógépes fenyegetéstől?

Nem, egyetlen eszköz sem képes rá, hogy az összes potenciális kiberfenyegetéssel szemben megóvja Önt. Az Outline hozzáférést biztosít Önnek a nyílt internethez, és a forgalom titkosításával biztonságosabbá teszi az adatforgalmat, de azt javasoljuk, hogy további óvintézkedéseket is tegyen, hogy megóvja magát a különböző támadásokkal – például a rosszindulatú programokkal és az adathalászattal – szemben.

Az online védelmi vonalak megerősítése érdekében érdemes lehet egyeztetni a szervezete kiberbiztonsági munkatársával. Alternatív megoldásként személyre szabott segítséget kaphat a [Security Planner](https://securityplanner.org/) vezető biztonsági szakértőitől. A Security Planner webhely célja, hogy hatékony tippeket nyújtson az Ön számára megfelelő kiberbiztonsági eszközök kiválasztásához.

Érdemes lehet továbbá kipróbálni a [Jigsaw](https://jigsaw.google.com/) más kiberbiztonsági termékeit, például az [Intra](https://getintra.org/), a [Project Shield](https://g.co/shield) és a [Jelszóriasztás](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?) szolgáltatást.

## Törvényesen használhatok VPN-t?

Mielőtt beüzemelné az Outline-t, vagy használatba venné az alkalmazást, olvassa át a helyi törvényeket és jogszabályokat, valamint a tervezett felhőszolgáltató Általános Szerződési Feltételeit.
