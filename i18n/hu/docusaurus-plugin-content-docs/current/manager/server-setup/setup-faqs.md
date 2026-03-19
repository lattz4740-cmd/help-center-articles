---
title: "Az Outline-szerver beállítására vonatkozó GYIK"
sidebar_label: "Az Outline-szerver beállítására vonatkozó GYIK"
---

## Használhatom az Outline-t szerver nélkül?
 Sajnos nem. Az Outline szoftvernek hozzá kell férnie egy szerverhez, amelyet kezelhet Ön, a szervezete vagy egy megbízható harmadik fél.

## Mennyi időbe telik beállítani egy Outline-szervert?

Általában kevesebb mint 5 percbe. Az Outline-t bármilyen felhőszerverre telepítheti, de a DigitalOceannel együttműködve egy felhasználóbarát, irányított telepítési folyamatot alkottunk meg, amely során néhány kattintással hozhat létre szervert, mindenféle szkript nélkül.

Ha az AWS-t, a GCP-t vagy speciális beállításokat választ, a legtöbb környezet esetén akkor se lesz szükség egynél több szkriptre a szervertelepítési folyamat során.

## Hol állíthatok be Outline-szervert?

A legtöbb felhőszolgáltatónál az üzemeltetési helyeiken állíthat be Outline-szervert.

A legegyszerűbb, ha a DigitalOceant választja, melynek több helyen is vannak szerverei, így például Amszterdamban, San Franciscóban, Szingapúrban és Torontóban. Ha másik felhőszolgáltatót választana, vagy a saját infrastruktúrájában telepítené a szoftvert, válassza az Outline Manager alkalmazásban az <b>Advanced Mode</b> módot, és hajtsa végre a beállítási szkripttel való beállítás telepítési lépéseit.

## Hol érdemes beállítanom az Outline-szerveremet?

1. Néhány szempontot érdemes figyelembe venni az Outline-szerver helyének kiválasztásakor:
2. Az Outline-szerver helye hatással van a felhasználók internetes élményére. Ha például amszterdami szervert használ, a szerverhez hozzáférő felhasználó számára olyan lesz az internet, mintha fizikailag Hollandiában lenne. Egyes webhelyek például hollandul jelennek meg. A webhelyeken általában található nyelvválasztó opció, amellyel a felhasználók felülírhatják a nyelvi beállításokat.
3. A felhasználók és az Outline-szerver közötti távolság hatással lehet a sebességre. A fizikai távolság a szerver és az Outline-felhasználók között a sebességre is kihathat. Általában olyan szerverhelyet érdemes választani, amely a legközelebb van a felhasználók várt tartózkodási helyéhez. A [tenger alatti kábelek térképén](https://www.submarinecablemap.com/) megtekintheti, hogy mely internetkábelek kötik be a rendszerbe az országát vagy régióját.
4. A VPN-szerver üzemeltetésének helye a vonatkozó jogszabályokat is befolyásolhatja. Ne feledje, hogy az Outline szoftver nem naplózza a forgalmat. További információ: [Biztonság és adatvédelem az Outline használata során](/about/security-and-privacy).
