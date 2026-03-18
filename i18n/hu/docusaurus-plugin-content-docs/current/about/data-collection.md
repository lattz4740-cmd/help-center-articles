---
title: Az általunk gyűjtött adatok és információk
sidebar_label: Az általunk gyűjtött adatok és információk
---

Az Outline kizárólag akkor gyűjt be személyes adatokat, ha azt Ön engedélyezi. Az Outline a meglátogatott webhelyekről sem gyűjt információkat, ahogy arról sem, hogy kivel vagy mit kommunikál.

 Ha az Outline Manager segítségével hoz létre fiókot egy harmadik fél felhőszolgáltatónál, vagy az Outline Manageren keresztül jelentkezik be egy ilyen fiókba, nem rögzítjük a harmadik fél felhőszolgáltatónak küldött adatait (például az e-mail-címét, a nevét, a számlázási adatait és a fizetési részleteket).

****Az automatikusan gyűjtött információk****

 Két információtípust gyűjtünk automatikusan.

 1. A szerver IP-címe

 Az Outline-szerver IP-címét a [Quay.io](https://quay.io/) szolgáltatás gyűjti be és teszi számunkra hozzáférhetővé, amikor a szerver automatikusan frissül a legújabb biztonsági funkciókkal és más fejlesztésekkel. A szerver IP-címe alapján azonosítható a felhőszolgáltató, illetve az a település, ahol az Outline-szerver üzemel, de az, hogy ki futtatja a szervert, és ki fér hozzá, nem fejthető ki ebből az információból.

 2. Személyazonosításra nem alkalmas, műszaki jellegű információk

 Ha az Outline leáll, vagy végzetes kivétel történik, illetve ha Ön manuálisan küld visszajelzést az Outline alkalmazásból, az alábbi információkat küldi el a rendszer. Ezek birtokában azonosíthatjuk és kijavíthatjuk a stabilitást és a teljesítményt érintő problémákat.

- Ország
- Nyelv- és országkód
- A leállás/végzetes kivétel napja és időpontja, illetve az ezt megelőző legfeljebb 100 esemény (példa eseménye: a felhasználó megnyitotta a „Névjegy” szakaszt)
- Statikusan tömörített kivételüzenetek
- Az operációs rendszer neve és verziója
- A telefon modellje (ha releváns)
- Az alkalmazás elindításának időpontja.
- Böngésző
- Architektúra
- Az Outline verziószáma és buildszáma.

Ezeket az adatokat HTTPS protokollon keresztül küldi el az alkalmazás a Sentry ([sentry.io](https://sentry.io/)) rendszerébe, amely egy nyílt forráskódot használó, harmadik fél hibakövetési szolgáltató. A Sentry többféle, az ipari szabványoknak megfelelő technológiával és szolgáltatással óvja meg adatait a jogosulatlan hozzáféréstől, kiszivárgástól, használattól és elvesztéstől. Ha kérdése van a Sentry irányelveivel kapcsolatban, látogasson el a [https://sentry.io/security/](https://sentry.io/security/) és a [https://sentry.io/privacy/](https://sentry.io/privacy/) webhelyre, vagy írjon a [security@sentry.io](mailto:security@sentry.io) címre. A Sentry által tárolt összes Outline-adat korlátozva van, így csak az Outline-csapat tagjai férhetnek hozzájuk.

****A kizárólag a felhasználók külön engedélyével gyűjtött információk****

 Az Outline akkor jelenti a következő információkat az Outline csapatának, ha erre Ön külön engedélyt ad.

 1. Használati mutatók

 Mindegyik Outline-szervere automatikusan begyűjti az elmúlt órából az egyes hozzáférési kulcsokhoz kapcsolódóan átvitt bájtok számát, a felhasználó szerverhez való csatlakozásainak számát, a használt hitelesítési adatok forrásországát és autonóm rendszereit, valamint azt, hogy engedélyeztek vagy letiltottak-e valamilyen funkciót. Sem a kommunikáció tartalmát, sem a személyazonosításra alkalmas metaadatokat (például bejelentkezési azonosítókat, e-mail-címeket és eszközazonosítókat) nem rögzítjük. Minden mérőszám egy szerverazonosítóhoz kapcsolódik. A szerverazonosító módosítására vonatkozó útmutatást [itt](/manager/server-management/reset-server-id) találja.

 Alapértelmezés szerint az Outline-szerverek nem osztják meg ezeket a mérőszámokat az Outline csapatával. Ha azonban a szerveradminisztrátor kifejezetten engedélyezi a mérőszámok megosztását, a rendszer minden órában biztonságosan elküldi ezeket az információkat az Outline csapatának. 60 nap után ezeket a használati mérőszámokat országos szinten összesítjük. A szerveradminisztrátorok az Outline Manager „Beállítások” menüjében bármikor módosíthatják a mérőszámok megosztási beállításait.

 Nagyra értékeljük, ha úgy dönt, hogy megosztja velünk a szerverhasználatra vonatkozó anonimizált mérőszámokat, mivel ezekkel azonosíthatjuk a használati tendenciákat, illetve fejleszthetjük a terméket.

 Ha például egy szerveradminisztrátor úgy dönt, hogy megosztja velünk a mérőszámokat, többek között olyan információkat kaphatunk, mint hogy az 12345-ös azonosítójú szervert tegnap 3 órán át használták, ez idő során 500 megabájtnyi adat haladt át rajta 3 kulcsról, amelyet az Egyesült Államokban és Kanadában használtak, és közben engedélyezve volt az adatkorlátozási funkció.

 2. Megjegyzések és e-mail-cím visszajelzés küldésekor

 Az Outline Manager és az Outline-alkalmazások lehetővé teszik, hogy közvetlen visszajelzést küldjön csapatunknak. Azt javasoljuk, hogy ebben ne adjon meg személyazonosításra alkalmas adatokat, de ha kíváncsi válaszunkra, megadhatja az e-mail-címét. A visszajelzés pontos értelmezése érdekében néhány alapvető adatot automatikusan begyűjtünk. Erről „Az automatikusan gyűjtött információk” szakasz 2. pontjában tudhat meg többet. Ha részletesebben szeretne tájékozódni az Outline biztonsági és adatvédelmi gyakorlatáról, kattintson [ide](/about/security-and-privacy).

 Ha az Outline alkalmazás bétaverzióját használja Androidon, akkor mi a Google [Firebase](https://firebase.google.com/) szolgáltatásával a problémák felismeréséhez és az Outline fejlesztéséhez szükséges hibaelhárítási adatokat gyűjthetünk. A Firebase adatvédelmi és biztonsági irányelveiről a Firebase webhelyén tájékozódhat részletesebben: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Ha nem szeretné, hogy az Outline elküldje ezeket az információkat a Firebase szolgáltatáson keresztül, térjen át az alkalmazás éles verziójára.
