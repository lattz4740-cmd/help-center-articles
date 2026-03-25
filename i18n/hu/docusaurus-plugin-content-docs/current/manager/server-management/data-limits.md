---
title: "Hogyan állíthatok be adatforgalmi korlátozásokat a hozzáférési kulcsokhoz?"
sidebar_label: "Hogyan állíthatok be adatforgalmi korlátozásokat a hozzáférési kulcsokhoz?"
---

Beállíthat egy adatforgalmi korlátozást, amely az összes hozzáférési kulcsra vonatkozik. Ha szeretne ilyen korlátozást beállítani, nyissa meg az Outline Managert, és lépjen a Beállításokhoz. Ekkor megjelenik egy Adatforgalmi korlátozások kapcsoló. Ha ezt bekapcsolja, beállíthatja a korlátozást.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

A korlátozás beállítása után a hozzáférési kulcs oldalán láthatja, hogy melyik felhasználó mennyire közelítette már meg a korlátot (sávdiagram mutatja az elmúlt 30 napra vonatkozó adathasználatot).

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Amellett, hogy korlátozást állíthat be az összes hozzáférési kulcshoz, minden kulcsnak megadhatja a saját adatforgalmi korlátozását is. Ez a beállítás felülír minden előzőleg beállított alapértelmezett adatforgalmi korlátozást, de ha nem állított be ilyet, akkor is beállíthat adatforgalmi korlátozást bármely kulcshoz. 

 Egy kulcs adatátviteli korlátozásának beállításához nyissa meg az Outline Managert, lépjen a beállítani kívánt kulcsot tartalmazó Kapcsolatok lapra, majd kattintson a kulcs sorának jobb oldalán található menüre. Itt kattintson az Adatforgalmi korlátozás lehetőségre. A „Saját hozzáférési kulcs” adatforgalmi korlátozásának módosításához kattintson az Adatforgalmi korlátozások ![A kép nem áll rendelkezésre, mert Ön nem rendelkezik a megtekintéséhez szükséges jogosultsággal, vagy a képet eltávolították a rendszerből.](/images/data-limits-icon.png) ikonra.

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Válassza ki az Egyéni adatforgalmi korlátozás beállítása lehetőséget. Miután bejelölte ezt a jelölőnégyzetet, megjelenik egy mező, ahol beállíthatja az adott kulcs egyéni adatforgalmi korlátozását. Ha végzett, kattintson a MENTÉS gombra az adatforgalmi korlátozás mentéséhez.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Miután elmentette a kiválasztott kulcsra vonatkozó adatátviteli korlátozást, a korlátozás megjelenik a főképernyőn az egyes kulcsok (az elmúlt 30 napra vonatkozó) adathasználati információi mellett.

A hozzáférési kulcs adatforgalmi korlátozásának eltávolításához a korábbiakhoz hasonlóan lépjen a kulcs Adatforgalmi korlátozás párbeszédablakába, távolítsa el a jelölést az Egyéni adatforgalmi korlátozás beállítása jelölőnégyzetből, majd kattintson a MENTÉS gombra.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Gyakori kérdések az adatforgalmi korlátozásról
## Mi az a 30 napos visszamenőleges adatforgalmi korlátozás?
 A 30 napos visszamenőleges adatforgalmi korlátozás úgy működik, hogy összeadjuk az egyes kulcsokhoz kapcsolódó használatot az elmúlt 30 napra, és nem engedjük, hogy a kulcs használata meghaladja ezt a korlátozást. Ennek az lesz a hatása, hogy a kulcs egyetlen 30 napos időszakon belül sem lépheti túl a korlátozást, így a 30 napos és a rövidebb naptári hónapokban sem. Ez azt jelenti, hogy az egyes felhasználók rendelkezésére álló adatkeret minden nap megnő azzal a mennyiséggel, amelyet 31 nappal korábban felhasználtak.

## Miért használ az Outline visszamenőleges korlátozásokat?
 A visszamenőleges korlátozások minden 30 napos időszakra garantálják a korlátok betartását, vagyis könnyebb konfigurálni őket, mint az ismétlődő korlátozásokat (például amelyeknek a hónap egy adott napján van a fordulónapjuk), ugyanakkor hasonló garanciákat nyújtanak. Ezenkívül megfelel az Outline-adathasználat most alkalmazott megjelenítésmódjának, valamint az elterjedt – például elemzési szolgáltatásokat és szerverstatisztikákat nyújtó – eszközöknek.

## Milyen adatok számítanak bele az adatforgalmi korlátozásba?
 Az összegbe az egyes hozzáférési kulcsokhoz kapcsolódóan a szerverről kimenő adatok számítanak bele. Ez szigorúan véve a kulcs nevében a szerverről elküldött adatokat jelenti, csakúgy, mint az ügyfélnek visszaküldötteket. Ennek a gyakorlatban nagyon hasonlónak kell lennie a kulcstól a szerver felé és vissza irányuló adatforgalomhoz, így reményünk szerint egyezik a felhasználók számításaival. Azért a kimenő forgalmat választottuk, mert az általunk megkérdezett felhőszolgáltatók ennek alapján állítják ki a számlát.

## Értesítik a felhasználókat, ha túllépik az adatforgalmi korlátot?
 Egyelőre nem. Számos felhőszolgáltató alkalmaz havi korlátot, például 1 TB-osat – ez 10 felhasználónak fejenként 100 GB-ra, vagy 100 felhasználónak 10 GB-ra elég. Ezek meglehetősen nagy számok, és nem számítunk arra, hogy sok felhasználó eléri őket. Reméljük, hogy a felhasználók a szerverük kezelőjéhez fordulnak, amikor a korlátba ütköznek. Hálásak volnánk azonban, ha elmagyaráznák nekünk, hogyan segítenék az értesítések az Önök konkrét céljait. [Itt](/about/feedback) vehetik fel velünk a kapcsolatot.

## Értesítik a felhasználókat, ha megközelítik az adatforgalmi korlátot?
 Változó, hogy a felhasználónak mennyivel nő meg egyik napról a másikra a kerete, hiszen attól függ, hogy mennyit használt fel 30 nappal korábban. Szerintünk egy figyelmeztetés inkább összezavarná a felhasználókat, mint segítene nekik. Hálásak volnánk, ha [itt](/about/feedback) visszajelzéssel szolgálna erről a működésmódról.

## Visszaállíthatom egy felhasználó adathasználatát?
 Nem, a felhasználói korlátozás mindig magában foglalja az elmúlt 30 nap adathasználatát. Megemelheti azonban a kulcsuk adatforgalmi korlátját, vagy új kulcsot hozhat létre számukra.

## Miért veszítették el egyes felhasználóim a hozzáférésüket, amint engedélyeztem az adatforgalmi korlátozásokat?
 Az adatforgalmi korlátozások a felhasználók korábbi 30 napos adatátvitelén alapulnak, amely rögzítésre kerül attól függetlenül, hogy engedélyezték-e az adatforgalmi korlátozásokat. Lehetséges, hogy a szóban forgó felhasználók már a bevezetés előtt túllépték a korlátozást. Vegye figyelembe azt is, hogy minden adatforgalmi korlátozás érvényesül, még akkor is, ha csak egyetlen kulcs adatforgalmi korlátozását módosítja.

## Beállíthatok az egész szerverre vonatkozó korlátozást, például „30 napra 1 TB”?
 Egyelőre nem. Szívesen vennénk, ha [itt](/about/feedback) részletesebben elmondaná, miért volna erre szüksége.

## Ha van egy alapértelmezett adatforgalmi korlátozás és egy adott kulcsra vonatkozó adatforgalmi korlátozás is, melyik lesz érvényes?
 Az adott kulcs adatforgalmi korlátozása felülírja az Ön által beállított alapértelmezett adatforgalmi korlátozást (ha van ilyen).

## Beállíthatok adatforgalmi korlátozást egy adott kulcshoz anélkül, hogy be lenne állítva egy alapértelmezett adatforgalmi korlátozás?
 Igen. Nincs szükség alapértelmezett korlátozásra ahhoz, hogy adatforgalmi korlátozást állítson be egy kulcsra. Például korlátozhat egy kulcsot, amelyről úgy gondolja, hogy széles körben megosztható, hogy így megvédje magát a kulcson keresztüli túlzott adatátviteltől.
