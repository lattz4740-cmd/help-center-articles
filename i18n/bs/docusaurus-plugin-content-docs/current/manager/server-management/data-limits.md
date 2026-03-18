---
title: "Kako postaviti ograničenja prenosa podataka za pristupne ključeve?"
sidebar_label: "Kako postaviti ograničenja prenosa podataka za pristupne ključeve?"
---

Možete postaviti ograničenje prenosa podataka koje će se primjenjivati na sve pristupne ključeve. Da postavite ograničenje, otvorite Outline Manager i idite u Postavke. Tu ćete vidjeti prekidač za ograničenja prenosa podataka koji vam dozvoljava da postavite ograničenje kada je omogućen.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Kada postavite ograničenje, možete vidjeti koliko je svaki korisnik blizu ograničenja na stranici pristupnog ključa. Trakasti grafikon na toj stranici prikazuje prenos podataka u posljednjih 30 dana.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Osim što možete postaviti ograničenje za sve pristupne ključeve, možete svakom ključu odobriti i pojedinačno ograničenje prenosa podataka. Ova postavka će nadjačati zadano ograničenje prenosa podataka koje ste postavili. Ako ga niste postavili, i dalje možete postaviti ograničenje prenosa podataka za bilo koji ključ. 

 Da postavite ograničenje prenosa podataka za neki ključ, otvorite Outline Manager, idite na karticu Veze na kojoj se nalazi ključ koji želite postaviti i kliknite na meni koji se nalazi desno od reda ključa. Tu kliknite na Ograničenje prenosa podataka. Da promijenite ograničenje prenosa podataka za "Moj pristupni ključ", kliknite na ikonu ograničenja prenosa podataka ![Ova slika nije dostupna jer nemate prava da je vidite ili je uklonjena iz sistema](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Odaberite opciju Postavi prilagođeno ograničenje prenosa podataka. Kada odaberete ovo polje za potvrdu, pojavit će se polje u kojem možete postaviti prilagođeno ograničenje prenosa podataka za taj ključ. Kliknite na dugme SAČUVAJ kada završite da sačuvate ograničenje prenosa podataka.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Kada sačuvate ograničenje prenosa podataka za odabrani ključ, ono će se pojaviti na glavnom ekranu, zajedno s prenosom podataka (tokom posljednjih 30 dana) za svaki ključ.

Da uklonite ograničenje prenosa podataka s pristupnog ključa, idite u dijaloški okvir Ograničenje prenosa podataka za taj ključ, kao i ranije, poništite potvrdu polja pod nazivom Postavi prilagođeno ograničenje prenosa podataka i kliknite na dugme SAČUVAJ.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Česta pitanja o ograničenju prenosa podataka****

****Šta je ograničenje za praćenje prenosa podataka od 30 dana?****

 Ograničenje za praćenje prenosa podataka od 30 dana će dati zbir korištenja svakog ključa u posljednjih 30 dana i zadržat će korištenje ključa ispod ograničenja u tom periodu. Rezultat je da ključ ne može premašiti ograničenje tokom bilo kojeg perioda od 30 dana, uključujući kalendarske mjesece od 30 dana ili manje. Dakle, to znači da će se dostupni prenos podataka svakog korisnika povećavati svakoga dana za količinu koju je iskoristio prije 31 dan.

**Zašto Outline koristi ograničenja za praćenje?**

 Ograničenja za praćenje pružaju garancije za svaki period od 30 dana, što znači da su jednostavnija za konfiguraciju od ponavljajućeg ograničenja (kao što je prilagodljivi dan u mjesecu), a pružaju slične garancije. Osim toga, odgovaraju postojećem prikazu prenosa podataka za Outline, kao i čestim alatima poput usluga analitike i statistike servera.

**Koji podaci su obuhvaćeni ograničenjem prenosa podataka?**

 Svaki izlaz ključa sa servera je uključen u evidenciju. Zapravo, to označava podatke poslane u ime ključa sa servera, kao i nazad klijentu. U praksi, ovo bi trebalo biti blisko usklađeno sa saobraćajem poslanim s ključa na server i nazad, tako da se nadamo da će se podudarati s evidencijama korisnika. Odabrali smo izlaz jer je to ono što naplaćuju pružaoci usluge oblaka koje smo anketirali.

**Hoće li korisnici biti obaviješteni ako potroše ograničenje?**

 Trenutno ne. Mnogi pružaoci usluge oblaka imaju ograničenje poput 1 TB za cijeli mjesec, što podržava 10 korisnika s 100 GB ili 100 korisnika s 10 GB. To su prilično veliki brojevi i ne očekujemo da će ih mnogo korisnika dosegnuti. Nadamo da se će se korisnici obratiti upraviteljima servera kada dosegnu ograničenje. Međutim, značio bi nam uvid o načinu na koji bi obavještenja mogla pomoći u vašem slučaju upotrebe. Možete nas kontaktirati [ovdje](/about/feedback).

**Hoće li korisnici biti obaviješteni ako se približe ograničenju prenosa podataka?**

 Količina novog prenosa podataka koju dobija korisnik koji se približava ograničenju razlikovat će se iz dana u dan, jer zavisi od njegovog prenosa podataka prije 30 dana. Smatramo da bi upozorenje prije zbunilo krajnje korisnike nego što bi im pomoglo. Značile bi nam povratne informacije o ovom ponašanju. Možete nam pisati [ovdje](/about/feedback).

**Mogu li poništiti prenos podataka nekog korisnika?**

 Ne, ograničenja korisnika uvijek obuhvataju posljednjih 30 dana prenosa podataka. Međutim, možete povećati ograničenje prenosa podataka njegovog ključa ili mu kreirati novi ključ.

**Zašto su neki moji korisnici izgubili pristup čim su omogućena ograničenja prenosa podataka?**

 Ograničenja prenosa podataka se temelje na prenosu podataka korisnika prije 30 dana, što se bilježi bez obzira na to jesu li omogućena ograničenja prenosa podataka. Moguće je da su dotični korisnici premašili ograničenje prije nego što je ono i postavljeno. Imajte na umu i da se sva ograničenja prenosa podataka uvijek primjenjuju, čak i kada promijenite ograničenje prenosa podataka za pojedinačni ključ.

**Mogu li postaviti ograničenje za čitav server, naprimjer "1 TB za 30 dana"?**

 Trenutno ne. Želimo čuti više o vašem slučaju upotrebe. Možete nam pisati [ovdje](/about/feedback).

**Ako postoji zadano ograničenje prenosa podataka i ograničenje prenosa podataka za pojedinačni ključ, koje će se primjenjivati?**

 Ograničenje prenosa podataka pojedinačnog ključa će nadjačati svako zadano ograničenje prenosa podataka (ako postoji) koje ste postavili.

**Mogu li postaviti ograničenje prenosa podataka za pojedinačni ključ bez postavljanja zadanog ograničenja prenosa podataka?**

 Da. Ne morate imati definirana zadana ograničenja da postavite ograničenje prenosa podataka na jednom ključu. Naprimjer, možete postaviti ograničenje na jednom ključu za koji mislite da se može široko dijeliti kako biste se zaštitili od prekomjernog prenosa podataka kroz njega.
