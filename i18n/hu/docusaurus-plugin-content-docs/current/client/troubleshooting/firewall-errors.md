---
title: A tűzfallal kapcsolatos problémák
sidebar_label: A tűzfallal kapcsolatos problémák
---

A tűzfallal kapcsolatban előforduló hibák három típusba sorolhatók:

## Lehet, hogy hálózati tűzfal gátolja a telepítést.

Ha egy tűzfallal rendelkező hálózathoz csatlakozva próbálja meg telepíteni az Outline alkalmazást (például iskolában vagy a munkahelyén), azt javasoljuk, hogy csatlakozzon egy másik hálózathoz.

Ha így sem sikerül, kérje meg a hálózatkezelő rendszergazdát, hogy tegye lehetővé a tűzfalat használó hálózat és az Outline-szervere közötti kapcsolat létrehozását. Ehhez szüksége lesz az Outline-t futtató Outline-szerver IP-címére és portjaira, melyeket a telepítési szkript végén talál.

**Lehet, hogy az eszközön beállított tűzfal gátolja a telepítést**.

Ha egy, az eszközön lévő szoftver (például a CheckPoint ZoneAlarm alkalmazása) gátolja a nem szabványos portokon vagy nem ismert szoftvereken keresztüli kimenő kapcsolatokat, olvassa el az eszköz vagy a szoftver leírását, melyből megtudhatja, hogy hogyan állíthatja be az Outline alkalmazást kivételként.

## Lehet, hogy a szerveren beállított tűzfal gátolja a telepítést.

Előfordulhat, hogy felhőszolgáltatója megköveteli, hogy az Outline-t futtató portok megnyitásához manuálisan állítson be kivételeket a szerver tűzfalához. A telepítési szkript futtatása után a rendszer megjelenítette azt a két véletlenszerűen kiválasztott portot, amelyen az Outline a szerverét futtatja. Ha ezt a két portot kinyitja, a rendszernek működnie kell.

 Ha kivételt szeretne adni a szerver tűzfalához, olvassa el az UFW és az Iptables programok dokumentációját:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
