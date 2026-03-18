---
title: "Miért nem tudok csatlakozni az Outline szolgáltatáshoz?"
sidebar_label: "Miért nem tudok csatlakozni az Outline szolgáltatáshoz?"
---

Több oka is lehet annak, hogy nem tud csatlakozni az Outline szolgáltatáshoz:

- **Az eszköz**/client/troubleshooting/connection-issues#One[**nem kapcsolódik az internethez**](#Internetissues)[#Internetissues](#Internetissues)**.**Előfordulhat, hogy megszakad az eszköz hálózati kapcsolata, és eltart egy pár másodpercig, amíg a hálózati ikonok frissülnek. Az is lehet, hogy az eszköz csatlakozik a helyi hálózathoz, de az internetkapcsolat nem működik.
- **A**/client/troubleshooting/connection-issues#Two[**hálózati tűzfal korlátozza**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[#FirewallIssues](#FirewallIssues)az Outline-szerverhez való hozzáférést.**Ez nyilvános hálózat, például iskolai, munkahelyi vagy díjmentes vezeték nélküli hálózat használata esetén gyakori.
- **Az eszközön lévő**/client/troubleshooting/connection-issues#Three[**tűzfal vagy vírusirtó szoftver**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**letiltja az Outline-szerverhez való hozzáférést.**
- **Az Ön**[**telefonján lévő eszközbeállításokat**](#DeviceSettings)**esetleg módosítania kell.**
- **Lehet, hogy a szolgáltatáskezelője**[**megsemmisítette a szervert, vagy az internetszolgáltató letiltotta a kérelmét**](#ServerIssues).

## Internetkapcsolattal kapcsolatos problémák: {#Internetissues}

## A tesztelés módja:

Kapcsolja ki az Outline-t, és nézze meg, hogy helyreáll-e az internetkapcsolat.

- Ha igen, hajtsa végre az alábbi hibaelhárítási lépéseket.
- Ha nem, várjon néhány másodpercet, és ellenőrizze, hogy frissülnek-e a hálózati beállítások.

## Javítási lehetőségek:

Kapcsolódjon újra az internethez:

1. Ellenőrizze, hogy más eszközök tudnak-e csatlakozni ugyanehhez a hálózathoz. Ha más eszközök sem tudnak csatlakozni, lehet, hogy a hálózat nem működik megfelelően, és meg kell várnia, amíg helyreáll, vagy Önnek kell megoldania a hálózati problémát.
2. Ha más eszközök képesek csatlakozni a hálózathoz, próbálkozzon az alábbi lépésekkel a kapcsolat helyreállításához:
   1. Állítsa Repülős üzemmódba az eszközt (mobiltelefonon).
   2. Indítsa újra az eszközt.
   3. Kapcsolja ki az eszközt, várjon 2 percet, majd kapcsolja be újra.

## Hálózati tűzfallal kapcsolatos problémák: {#FirewallIssues}

## A tesztelés módja:

1. Csatlakozzon le a jelenlegi Wi-Fi- vagy vezetékes hálózatról.
2. Csatlakozzon másik hálózathoz (például mobilhálózathoz).
3. Próbáljon újracsatlakozni az Outline-szerverhez.

Ha másik hálózatról sikerül csatlakozni, ez a probléma lépett fel.

## Javítási lehetőségek:

Kérje meg a hálózati adminisztrátort, hogy engedélyezze az Outline-szerverhez való hozzáférést, vagy használjon másik hálózatot.

**Tűzfallal vagy vírusirtó szoftverrel kapcsolatos problémák:**

**A tesztelés módja:**

 Csatlakozzon az Outline-hoz egy másik eszközről.

Megjegyzés: Ne feledje, hogy ha az Outline szolgáltatást egy másik eszközön szeretné használni, szüksége lesz egy hozzáférési kulcsra és az Outline alkalmazásra.

## Javítási lehetőségek: {#SoftwareIssues}
Ellenőrizze a tűzfal vagy a vírusirtó szoftver beállításait, és győződjön meg róla, hogy azok lehetővé teszik a VPN- és az Outline-forgalom áthaladását.

## Eszközbeállítások: {#DeviceSettings}

## Amit érdemes ellenőrizni: {#DeviceSettings}
Android esetén:

1. Nyissa meg a Beállítások alkalmazást.
2. Keresse meg a **VPN-beállításokat** az eszközén. (A VPN-beállítások között az összes olyan VPN-alkalmazás megjelenik, amely jelenleg hozzáféréssel rendelkezik a telefonjához.)
3. Ha nem látja az Outline szolgáltatást a VPN-beállítások között, távolítsa el, majd telepítse újra az Outline-t. Az Outline a telepítést követően automatikusan megkapja a hozzáférést az eszköztől.

Győződjön meg arról, hogy nincsenek képernyőfedvényt előidéző alkalmazások telepítve az Android-eszközén, mert ezek az Outline engedélyeket megjelenítő ablakát a háttérbe küldhetik, így az nem lesz látható az előtérben.

 Az Android-eszközön válassza a Beállítások > Alkalmazások > Különleges alkalmazás-hozzáférés lehetőséget. Ezután koppintson A többi alkalmazás felett elemre. Bármely, ezt a viselkedést engedélyező alkalmazás esetén eltávolíthatja a hozzáférést.

 iOS esetén: Olvassa el [ezt a súgócikket](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Szerverrel kapcsolatos problémák: {#ServerIssues}

## A tesztelés módja: {#ServerIssues}
Ha egynél több szerverhez fér hozzá, csatlakozzon egy másikhoz.

## Javítási lehetőségek:

Kérdezze meg a szolgáltatáskezelőjét, hogy nem semmisítette-e meg a szervert. Ha igen, kérjen tőle [hozzáférési kulcsot](/about/terminology) egy másik szerverhez.

Ha Ön állította be a szervert, csatlakozzon hozzá az Outline Manageren keresztül vagy más módon, például [SSH](https://hu.wikipedia.org/wiki/Secure_Shell) segítségével. Ha így sem jön létre a kapcsolat, ellenőrizze a felhőszolgáltató konzolján, hogy a szerver online-e még.
