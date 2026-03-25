---
title: Terminologie
sidebar_label: Terminologie
---

## Ce este un VPN?
 O rețea privată virtuală (VPN) este o conexiune privată între dispozitivele dvs. și un server gazdă. Când folosiți un VPN, furnizorul de internet nu vă poate vedea traficul. Ați putea dori să folosiți un VPN în următoarele situații:

- să vă protejați datele când folosiți o rețea Wi-Fi publică;
- să mențineți datele de navigare private, pentru a nu fi accesate de furnizorul de internet și agențiile guvernamentale;
- să accesați conținut necenzurat de la diferite surse din jurul lumii.

## Cum diferă Outline de VPN-urile tradiționale?
 Furnizorii de internet pot să detecteze cu ușurință și să blocheze VPN-urile tradiționale recunoscând protocoale de securitate uzuale și/sau tipare de volum de trafic. Outline este mai rezilient decât VPN-urile tradiționale deoarece este construit folosind un protocol conceput pentru a fi dificil de detectat și, prin urmare, mai greu de blocat. Outline este rezistent la forme sofisticate de cenzură, inclusiv blocarea în funcție de rețea și blocarea IP-ului.

## Ce este un server Outline?
 Un server Outline rulează VPN-ul la care se vor conecta utilizatorii cu permisiune. În cazul în care creați o rețea nouă, puteți folosi propriul server securizat ca server Outline, dacă aveți unul, sau puteți folosi un furnizor de servicii cloud, precum:

- DigitalOcean,
- Google Cloud Platform (GCP),
- Amazon Web Services (AWS).

Vă veți configura serverul în Outline Manager.

## Ce este un manager de servicii? {#servicemanager}
 Un manager de servicii este persoana responsabilă pentru configurarea serverului Outline și trimiterea cheilor de acces către utilizatori. Managerul de servicii este responsabil în general de costul folosirii serverului. 

## Ce este o cheie de acces? {#accesskey}
 O cheie de acces este folosită pentru a accesa un server Outline existent și conectarea la VPN. Un [manager de servicii](#servicemanager) vă va oferi o cheie de acces sau puteți [să configurați chiar dvs. un server Outline](/manager/server-setup/setup-server). Iată un exemplu de cheie de acces (doar exemplu, nu va funcționa): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Ce este Outline Manager?
 Outline Manager este o aplicație pentru computer care îi permite unui manager de servicii să configureze un server Outline, să genereze [chei de acces](#accesskey) și să configureze limite de date pentru folosirea fiecărei chei. Puteți descărca cea mai recentă versiune Outline Manager [aici](https://getoutline.org/get-started/#step-3) sau [aici](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Ce este Outline Client?
 Outline Client este o aplicație disponibilă pentru computer și mobil care vă permite să vă conectați la un server Outline și să accesați VPN-ul folosind o cheie de acces. Puteți descărca cea mai recentă versiune Outline Client [aici](https://getoutline.org/get-started/#step-3) sau [aici](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Ce sunt limitele de date?
 Outline Manager le permite managerilor de servicii să seteze o limită de transfer de date timp de 30 de zile pentru cheile de acces, pentru a preveni folosirea excesivă și a menține costurile în limite previzibile. Managerii de servicii pot seta o limită prestabilită pentru fiecare cheie și pot să seteze o limită diferită pentru orice cheie pentru a modifica limita prestabilită. După ce este setată o limită, aceasta devine aplicabilă imediat și este implementată la fiecare oră.

Dacă managerii de servicii optează să trimită valorile către Jigsaw, trebuie să consulte [politica privind colectarea datelor](https://getoutline.org/policies/data-collection) pentru detalii despre raportarea folosirii limitelor de date.
