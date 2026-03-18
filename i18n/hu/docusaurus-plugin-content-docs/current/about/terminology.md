---
title: Terminológia
sidebar_label: Terminológia
---

**Mi az a VPN?**

 A virtuális magánhálózat (VPN) az Ön eszköze(i) és egy gazdaszerver között létrejött privát kapcsolat. VPN használatakor az adatforgalom rejtve marad az internetszolgáltató előtt. VPN-t az alábbi esetekben lehet érdemes használni:

- Az adatok védelmére nyilvános Wi-Fi-hálózat használata esetén
- A böngészési adatoknak az internetszolgáltató és a kormányzati szervek előli elrejtésére
- A világ különböző forrásaiból származó, cenzorálatlan tartalmakhoz való hozzáférésre

**Miben különbözik az Outline a hagyományos VPN-ektől?**

 Az internetszolgáltatók könnyen észlelni és blokkolni tudják a hagyományos VPN-eket a gyakori biztonsági protokollok, illetve a forgalom mértékében megmutatkozó egyes szabályszerűségek alapján. Az Outline kevésbé észlelhető, mint a hagyományos VPN-ek, mert egy olyan protokollra épül, amelynek kialakításakor az észlelés megnehezítése volt a fő szempont, ezért nehezebb blokkolni. Az Outline-on nem fognak ki a cenzúra rafinált formái sem, így például a hálózatalapú blokkolás és az IP-címek blokkolása sem.

**Mit nevezünk Outline-szervernek?**

 Az Outline-szerveren fut a VPN, amelyhez az erre jogosult felhasználók csatlakoznak. Ha új hálózatot hoz létre, és van saját biztonságos szervere, használhatja azt Outline-szerverként, de valamelyik felhőszolgáltató rendszerét is választhatja, például:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

A szervert az Outline Manager segítségével telepítheti.

**Ki az a szolgáltatáskezelő?**

 A szolgáltatáskezelő az, aki felel az Outline-szerver telepítéséért, és ő ad hozzáférési kulcsot a felhasználóknak. Általában a szolgáltatáskezelő felel a szerverhasználat költségéért is. 

**Mit nevezünk hozzáférési kulcsnak?**

 A hozzáférési kulcs segítségével lehet hozzáférni a meglévő Outline-szerverekhez, illetve csatlakozni a VPN-hez. A [szolgáltatáskezelő](#servicemanager) ad Önnek hozzáférési kulcsot, vagy Ön saját maga is [telepíthet Outline-szervert](/manager/server-setup/setup-server). A hozzáférési kulcs a következőre hasonlít (ez csak minta, nem működik): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Mi az az Outline Manager?**

 Az Outline Manager asztali alkalmazás, amely lehetővé teszi a szolgáltatáskezelő számára az Outline-szerver telepítését, a [hozzáférési kulcsok](#accesskey) generálását, illetve a kulcsokra vonatkozó adatforgalmi korlátozások beállítását. Az Outline Manager legújabb verziója [innen](https://getoutline.org/get-started/#step-3) és [innen](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) tölthető le.

**Mi az az Outline-ügyfél?**

 Az Outline-ügyfél asztali és mobilverzióban is rendelkezésre álló alkalmazás, amellyel hozzáférési kulcs birtokában kapcsolatot lehet létesíteni az Outline-szerverrel, és hozzá lehet férni a VPN-hez. Az Outline-ügyfél legújabb verziója [innen](https://getoutline.org/get-started/#step-3) és [innen](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) tölthető le.

**Mik azok az adatforgalmi korlátozások?**

 Az Outline Manager segítségével a szolgáltatáskezelők az elmúlt 30 napra összesítve mért adatforgalmi korlátot állíthatnak be, megakadályozva ezzel a túlzott mértékű használatot, és kiszámítható keretek között tartva a költségeket. A szolgáltatáskezelők beállíthatják az alapértelmezett korlátozást, amely minden kulcsra érvényes, de az alapértelmezett korlátozást felülbírálva bármelyik kulcsra eltérő korlátozást is beállíthatnak. A korlátozás a beállításakor azonnal életbe lép, és óránként vizsgálja a rendszer a túllépését.

Ha a szolgáltatáskezelő azt választja, hogy megosztja a mutatókat a Jigsaw-val, akkor az [adatgyűjtési irányelvekből](/about/data-collection) részletesen tájékozódhat az adatforgalmi korlátozásról beküldött jelentésekről.
