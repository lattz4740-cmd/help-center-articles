---
title: Kako postaviti ograničenje podatkovnog prometa za pristupne ključeve
sidebar_label: Kako postaviti ograničenje podatkovnog prometa za pristupne ključeve
---

Možete postaviti ograničenje podatkovnog prometa koje će se primjenjivati na sve pristupne ključeve. Da biste postavili ograničenje, otvorite Upravitelj Outlinea i idite na postavke. U postavkama ćete vidjeti prekidač Ograničenje podatkovnog prometa koji možete omogućiti radi postavljanja ograničenja.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Nakon što postavite ograničenje, na stranici s pristupnim ključem možete vidjeti koliko se svaki korisnik približio ograničenju. Trakasti grafikon prikazuje potrošnju podatkovnog prometa tijekom posljednjih 30 dana.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Osim što možete postaviti ograničenje za sve svoje pristupne ključeve, možete postaviti ograničenje podatkovnog prometa zasebno za svaki ključ. Ta će postavka nadjačati sva zadana ograničenja podatkovnog prometa koja ste postavili, ali ako niste postavili zadano ograničenje podatkovnog prometa, i dalje možete postaviti ograničenje podatkovnog prometa za svaki ključ.

 Da biste postavili ograničenje prijenosa podataka za ključ, otvorite Upravitelj Outlinea, prijeđite na karticu Veze koja sadrži ključ koji želite postaviti i kliknite izbornik desno od retka ključa. Zatim kliknite Ograničenje podatkovnog prometa. Da biste promijenili ograničenje podatkovnog prometa u odjeljku Moj pristupni ključ, kliknite ikonu ograničenja podatkovnog prometa ![Ta slika nije dostupna iz sljedećih razloga: nemate ovlasti za njezin pregled ili je uklonjena iz sustava](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Odaberite Postavi prilagođeno ograničenje podatkovnog prometa. Nakon što potvrdite taj potvrdni okvir, prikazat će se polje u kojem možete postaviti prilagođeno ograničenje podatkovnog prometa za taj ključ. Kliknite gumb SPREMI kada završite da biste spremili ograničenje podatkovnog prometa.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Nakon što spremite ograničenje prijenosa podataka za odabrani ključ, ograničenje će se prikazivati na glavnom zaslonu uz potrošnju podatkovnog prometa (tijekom prethodnih 30 dana) za svaki ključ.

Da biste uklonili ograničenje podatkovnog prometa s pristupnog ključa, otvorite dijaloški okvir ograničenja podatkovnog prometa za ključ kao i prije, uklonite kvačicu iz okvira s oznakom Postavi prilagođeno ograničenje podatkovnog prometa i kliknite gumb SPREMI.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Česta pitanja o ograničenju podatkovnog prometa****

****Što je 30-dnevno promjenjivo ograničenje podatkovnog prometa?****

 Promjenjivo ograničenje podatkovnog prometa za 30 dana zbrojit će upotrebu svakog ključa u proteklih 30 dana i zadržati je ispod ograničenja tijekom tog razdoblja. To znači da ključ ne može prekoračiti ograničenje tijekom bilo kojeg 30-dnevnog razdoblja, uključujući kalendarske mjesece koji imaju 30 dana ili manje. To zapravo znači da će se dostupan podatkovni promet svakog korisnika povećavati svaki dan na temelju količine podataka koju je potrošio prije 31 dan.

**Zašto Outline upotrebljava promjenjiva ograničenja?**

 Promjenjiva ograničenja pružaju jamstvo za svako 30-dnevno razdoblje. To znači da ih je jednostavnije konfigurirati od ponavljajućih ograničenja (kao što je prilagodba dana u mjesecu), iako pružaju slična jamstva. Također su prikladna za postojeći prikaz upotrebe podataka Outlinea te za standardne alate, kao što su analitičke usluge i statistika poslužitelja.

**Koji se podaci ubrajaju u ograničenje podatkovnog prometa?**

 U izračun je uključen svaki izlazak pristupnog ključa iz poslužitelja. Strogo uzevši, to se odnosi na podatke koji su poslani iz poslužitelja u ime ključa, kao i na podatke koji su poslani natrag klijentu. To bi praktički trebalo biti usko usklađeno s prometom koji se šalje s ključa na poslužitelj i natrag. Stoga se nadamo da će biti u skladu s izračunom vaših klijenata. Odabrali smo izlaz jer ga naplaćuju davatelji usluga u oblaku koje smo anketirali.

**Hoće li se korisnici obavijestiti ako prijeđu ograničenje podatkovnog prometa?**

 Trenutačno ne. Mnogi davatelji usluga u oblaku nude ograničenje od 1 TB za cijeli mjesec koje se odnosi na 10 korisnika i potrošnju od 100 GB po korisniku ili 100 korisnika i potrošnju od 10 GB po korisniku. To su prilično velike brojke i ne očekujemo da će ih mnogi korisnici dosegnuti. Nadamo se da će se korisnici javiti upraviteljima poslužitelja kada dosegnu ograničenje. No željeli bismo čuti vaše mišljenje o tome kako bi obavijesti mogle pomoći u vašoj upotrebi. Možete nam se javiti [ovdje](/about/feedback).

**Hoće li se korisnici obavijestiti ako se približe ograničenju podatkovnog prometa?**

 Količina novih podataka koje će korisnik koji se približava ograničenju primiti razlikuje se ovisno o danu jer se temelji na upotrebi od prije 30 dana. Smatramo da će upozorenje vjerojatno zbuniti krajnje korisnike, umjesto da im pomogne. Rado bismo čuli vaše povratne informacije o tom ponašanju [ovdje](/about/feedback).

**Mogu li ponovno postaviti potrošnju podatkovnog prometa za korisnika?**

 Ne, ograničenje korisnika uvijek uključuje prethodnih 30 dana potrošnje podataka. Međutim, možete povećati ograničenje podatkovnog prometa za ključ ili izraditi novi ključ za korisnika.

**Zašto su neki od mojih korisnika izgubili pristup odmah nakon omogućavanja ograničenja podatkovnog prometa?**

 Ograničenja podatkovnog prometa temelje se na prethodnih 30 dana prijenosa podataka korisnika koji se bilježe bez obzira na to jesu li ograničenja podatkovnog prometa omogućena. Moguće je da su ti korisnici već prekoračili ograničenje prije nego što je postavljeno. Osim toga, sva su ograničenja podatkovnog prometa implementirana, čak i pri promjeni ograničenja podatkovnog prometa za jedan ključ.

**Mogu li postaviti ograničenje za cijeli poslužitelj, na primjer 1 TB u 30 dana?**

 Trenutačno ne. Htjeli bismo čuti više o vašoj upotrebi [ovdje](/about/feedback).

**Ako postoji zadano ograničenje podatkovnog prometa i ograničenje podatkovnog prometa za određeni ključ, koje će se ograničenje implementirati?**

 Ograničenje podatkovnog prometa za određeni ključ nadjačat će sva zadana ograničenja podatkovnog prometa koja (i ako) ste postavili.

**Mogu li postaviti ograničenje podatkovnog prometa za određeni ključ bez postavljanja zadanog ograničenja podatkovnog prometa?**

 Da. Ne trebate definirati zadano ograničenje da biste postavili ograničenje podatkovnog prometa za jedan ključ. Mogli biste primjerice postaviti ograničenje za jedan ključ za koji smatrate da bi se mogao uvelike dijeliti da biste se zaštitili od prekomjernog prijenosa podataka za taj ključ.
