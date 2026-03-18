---
title: Terminologija
sidebar_label: Terminologija
---

**Što je VPN?**

 Virtualna privatna mreža (VPN) privatna je veza između vaših uređaja i poslužitelja koji hosta sadržaj. Dok upotrebljavate VPN, vaš je promet skriven od davatelja internetskih usluga. Upotreba VPN-a preporučuje se u sljedećim situacijama:

- radi zaštite podataka tijekom upotrebe javnog Wi-Fija
- radi sprječavanja otkrivanja podataka o pregledavanju davatelju internetskih usluga i državnim tijelima
- radi pristupa necenzuriranom sadržaju iz raznih izvora širom svijeta.

**Što Outline razlikuje od tradicionalnih VPN-ova?**

 Davatelji internetskih usluga mogu jednostavno otkriti i blokirati tradicionalne VPN-ove putem prepoznavanja uobičajenih sigurnosnih protokola i/ili obrazaca količine prometa. Outline je robusniji od tradicionalnih VPN-ova jer je razvijen pomoću protokola koji je osmišljen tako da se teško otkriva, što znači da se teže i blokira. Outline je otporan na sofisticirane oblike cenzure, uključujući blokiranje na temelju mreže i blokiranje IP adresa.

**Što je Outline poslužitelj?**

 Na Outline poslužitelju nalazi se VPN s kojim se mogu povezati odobreni korisnici. Ako izrađujete novu mrežu, kao Outline poslužitelj možete upotrijebiti vlastiti poslužitelj ako ga imate, a možete upotrijebiti i davatelja usluga u oblaku poput sljedećih:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS).

Poslužitelj možete postaviti u Upravitelju Outlinea.

**Što je upravitelj usluga?**

 Upravitelj usluga osoba je odgovorna za postavljanje Outline poslužitelja i dodjelu pristupnih ključeva korisnicima. Upravitelj usluga u načelu je odgovoran za troškove upotrebe poslužitelja. 

**Što je pristupni ključ?**

 Pristupni ključ služi za pristup postojećem Outline poslužitelju i povezivanje s VPN-om. [Upravitelj usluga](#servicemanager) dat će vam pristupni ključ, a možete i sami [postaviti Outline poslužitelj](/manager/server-setup/setup-server). U nastavku se nalazi primjer pristupnog ključa (to je ogledni ključ koji ne funkcionira):

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Što je Upravitelj Outlinea?**

 Upravitelj Outlinea aplikacija je za računalo koja upravitelju usluga omogućuje postavljanje Outline poslužitelja, generiranje [pristupnih ključeva](#accesskey) i postavljanje podatkovnih ograničenja upotrebe za svaki ključ. Najnoviju verziju Upravitelja Outlinea možete preuzeti [ovdje](https://getoutline.org/get-started/#step-3) ili [ovdje](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Što je Outline Klijent?**

 Outline Klijent aplikacija je za računala i mobilne uređaje koja omogućuje povezivanje s Outline poslužiteljem i pristupanje VPN-u pomoću pristupnog ključa. Najnoviju verziju Outline Klijenta možete preuzeti [ovdje](https://getoutline.org/get-started/#step-3) ili [ovdje](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Što su ograničenja podatkovnog prometa?**

 Upravitelj Outlinea omogućuje upraviteljima usluga da postave promjenjivo 30-dnevno ograničenje podatkovnog prometa za pristupne ključeve kako bi spriječili prekomjernu upotrebu i povećali predvidljivost troškova. Upravitelji usluga mogu postaviti zadano ograničenje koje se primjenjuje na svaki ključ ili drukčije ograničenje za pojedine ključeve koje nadjačava zadano ograničenje. Postavljeno ograničenje stupa na snagu odmah i primjenjuje se svakih sat vremena.

Ako upravitelji usluga uključe dijeljenje mjernih podataka s Jigsawom, trebaju u [pravilima o prikupljanju podataka](/about/data-collection) potražiti pojedinosti o tome kako se prijavljuje upotreba ograničenja podatkovnog prometa.
