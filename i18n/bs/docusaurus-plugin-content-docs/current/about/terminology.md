---
title: Terminologija
sidebar_label: Terminologija
---

## Šta je VPN?
 Virtuelna privatna mreža (VPN) privatna je veza između vaših uređaja i servera na host računaru. Kada koristite VPN, saobraćaj se sakriva od pružaoca internetske usluge. Preporučuje se da koristite VPN kada želite:

- zaštititi svoje podatke prilikom korištenja javne WiFi mreže
- sakriti podatke o pregledanju od pružaoca internetske usluge i državnih agencija
- pristupiti necenzuriranom sadržaju iz raznih izvora širom svijeta

## Po čemu se Outline razlikuje od tradicionalnih VPN-ova?
 Pružaoci internetske usluge mogu jednostavno otkrivati i blokirati tradicionalne VPN-ove jer prepoznaju uobičajene sigurnosne protokole i/ili uzorke količine saobraćaja. Outline je otporniji od tradicionalnih VPN-ova jer je izrađen pomoću protokola koji je osmišljen da se teško otkriva, što znači da se teže i blokira. Outline je otporan na sofisticirane oblike cenzure uključujući blokiranje na osnovu mreže i blokiranje IP-ja.

## Šta je Outline server?
 Outline server izvodi VPN s kojim će se povezati korisnici s odobrenjem. Ako kreirate novu mrežu, možete koristiti vlastiti siguran server kao Outline server ako ga imate ili možete koristiti pružaoca usluge oblaka kao što su:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Postavit ćete svoj server u Outline Manageru.

## Šta je upravitelj usluge? {#servicemanager}
 Upravitelj usluge je osoba odgovorna za postavljanje Outline servera i dijeljenje pristupnih ključeva s korisnicima. Upravitelj usluge je općenito odgovoran za troškove korištenja servera. 

## Šta je pristupni ključ? {#accesskey}
 Pristupni ključ se koristi za pristup postojećem Outline serveru i povezivanje s VPN-om. [Upravitelj usluge](#servicemanager) će vam dati pristupni ključ ili možete sami[postaviti Outline server](/manager/server-setup/setup-server). Evo primjera kako pristupni ključ izgleda (to je samo primjer; neće funkcionirati): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Šta je Outline Manager?
 Outline Manager je aplikacija za računare koja omogućava upravitelju usluge da postavi Outline server, generira [pristupne ključeve](#accesskey) i postavi ograničenja prenosa podataka na korištenje po ključu. Najnoviju verziju Outline Managera možete preuzeti[ovdje](https://getoutline.org/get-started/#step-3) ili[ovdje](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Šta je klijent za Outline?
 Klijent za Outline je aplikacija dostupna za računare i mobilne uređaje koja vam omogućava da se povežete s Outline serverom i pristupite VPN-u pomoću pristupnog ključa. Najnoviju verziju klijenta za Outline možete preuzeti[ovdje](https://getoutline.org/get-started/#step-3) ili[ovdje](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Šta su ograničenja prenosa podataka?
 Outline Manager omogućava upraviteljima usluge da na pristupne ključeve postave 30-dnevno ograničenje prenosa podataka radi sprečavanja prekomjernog korištenja i osiguranja predvidivosti troškova. Upravitelji usluge mogu postaviti zadano ograničenje koje će se primjenjivati na sve ključeve, a mogu i postaviti različito ograničenje za svaki ključ kako bi se nadjačalo zadano ograničenje. Kada se ograničenje postavi, odmah stupa na snagu i sprovodi se svaki sat.

Ako upravitelji usluge pristanu da dijele pokazatelje s Jigsawom, trebaju pregledati[pravila za prikupljanje podataka](/about/data-collection) da saznaju detalje o tome kako će se prijavljivati korištenje ograničenja prenosa podataka.
