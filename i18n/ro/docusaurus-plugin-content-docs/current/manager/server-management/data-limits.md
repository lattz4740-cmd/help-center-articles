---
title: "Cum setez limite de date pentru cheile de acces?"
sidebar_label: "Cum setez limite de date pentru cheile de acces?"
---

Puteți să setați o limită de date care se va aplica pentru toate cheile de acces. Pentru a seta limita, deschideți Outline Manager și navigați la Setări. Veți vedea comutatorul Limite de date, care odată activat vă permite să setați o limită.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

După ce setați o limită, puteți vedea cât de mult s-a apropiat de limită fiecare utilizator pe pagina cheii de acces, unde un grafic cu bare arată utilizarea datelor din ultimele 30 de zile.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Pe lângă opțiunea să setați o limită pentru toate cheile de acces, puteți să acordați fiecărei chei propria limită de date. Această setare va modifica limita de date prestabilită pe care ați ales-o. Dacă nu ați setat o limită de date prestabilită, puteți totuși să o setați pentru fiecare cheie. 

 Pentru a seta limita de transfer de date a unei chei, deschideți Outline Manager, navigați la fila Conexiuni care include cheia pentru care doriți să setați limita și dați clic pe meniul din partea dreaptă a rândului cheii. Apoi, dați clic pe Limită de date. Pentru a modifica limita de date în pagina Cheia mea de acces, dați clic pe pictograma Limite de date ![Această imagine nu este disponibilă deoarece: nu aveți privilegiile necesare pentru a o vedea sau a fost eliminată din sistem.](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Selectați Setați o limită de date personalizată. După ce bifați această casetă, se va afișa un câmp în care puteți să setați limita de date personalizată pentru cheia în cauză. Dați clic pe butonul SALVAȚI, pentru a salva limita de date.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

După ce salvați limita de transfer de date pentru cheia aleasă, limita se va afișa pe ecranul principal, alături de utilizarea datelor (în ultimele 30 de zile) pentru fiecare cheie.

Pentru a elimina limita de date a unei chei de acces, navigați la caseta de dialog Limită de date a cheii, debifați caseta etichetată Setați o limită de date personalizată și dați clic pe butonul SALVAȚI.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Întrebări frecvente privind limitele de date****

****Ce este o limită de date timp de 30 de zile?****

 O limită de date timp de 30 de zile va însuma utilizarea fiecărei chei în ultimele 30 de zile și va păstra utilizarea acesteia în perioada respectivă sub limita stabilită. Efectul este următorul: cheia nu poate depăși limita pe orice perioadă de 30 de zile, inclusiv lunile calendaristice de maximum 30 de zile. În fapt, datele disponibile pentru fiecare utilizator vor crește în fiecare zi cu cantitatea pe care au folosit-o acum 31 de zile.

**De ce folosește Outline astfel de limite?**

 Aceste limite oferă garanții pentru fiecare perioadă de 30 de zile, fiind mai simplu de configurat decât o limită recurentă (cum ar fi o zi din lună care poate fi personalizată) și oferind garanții similare. În plus, limitele se potrivesc cu afișarea existentă a utilizării de date din Outline, precum și cu instrumentele frecvente, cum ar fi serviciile de date statistice și statisticile serverului.

**Ce date sunt contorizate într-o limită de date?**

 Fiecare ieșire a cheii de acces din server este inclusă în contorizare. În sens strict, este vorba de datele trimise în numele cheii în afara serverului și cele trimise înapoi clientului. Practic, acest volum trebuie să se alinieze îndeaproape cu traficul trimis de la cheie către server și înapoi, prin urmare, sperăm că va corespunde contorizărilor utilizatorilor. Am ales traficul de ieșire deoarece este traficul facturat de furnizorii de servicii în cloud pe care i-am analizat.

**Utilizatorii vor primi o notificare dacă depășesc limita de date?**

 Momentan, nu. Mulți furnizori de servicii în cloud includ o limită, cum ar fi 1 TB pe lună, care poate accepta 10 utilizatori la 100 GB sau 100 de utilizatori la 10 GB. Aceste cifre oferă limite destul de ridicate și nu ne așteptăm să fie atinse de mulți utilizatori. Sperăm că utilizatorii vor apela la administratorii de server când ating limita. Totuși, am aprecia dacă ne trimiteți feedback legat de modul în care notificările pot fi utile în situația dvs. de folosire. Ne puteți contacta [aici](https://support.getoutline.org/s/contactsupport).

**Utilizatorii vor primi o notificare dacă se apropie de limita de date?**

 Cantitatea de date noi primite de un utilizator care se apropie de limita de date va varia de la o zi la alta, deoarece se bazează pe utilizarea din perioada anterioară de 30 de zile. Credem că o atenționare va crea mai degrabă confuzie în rândul utilizatorilor finali, în loc să le fie de ajutor. Am aprecia feedbackul dvs. legat de acest comportament [aici](https://support.getoutline.org/s/contactsupport).

**Pot să resetez utilizarea datelor a unui utilizator?**

 Nu, limita unui utilizator include întotdeauna ultimele 30 de zile de utilizare a datelor. Totuși, puteți să creșteți limita de date a cheii utilizatorului sau să creați o cheie nouă pentru acesta.

**De ce unii utilizatori au pierdut accesul imediat ce am activat limitele de date?**

 Limitele de date se bazează pe transferul de date al utilizatorilor în perioada anterioară de 30 de zile, care este înregistrată indiferent dacă sunt activate sau nu limitele de date. Este posibil ca utilizatorii în cauză să fi depășit deja limita înainte să fie activată. Rețineți că toate limitele de date sunt aplicate, chiar și dacă modificați limita de date a unei chei.

**Pot să setez o limită la nivel de server, cum ar fi 1 TB per 30 de zile?**

 Momentan, nu. Ne-am dori să aflăm mai multe despre situația dvs. de folosire [aici](https://support.getoutline.org/s/contactsupport).

**Dacă există o limită de date prestabilită și o limită de date pentru o anumită cheie, care dintre limite va fi aplicată?**

 Limita de date a cheii în cauză va înlocui orice limită de date prestabilită (dacă există) pe care ați setat-o.

**Pot să setez o limită de date pentru o anumită cheie fără să fi setat o limită de date prestabilită?**

 Da. Nu este necesar să definiți o limită prestabilită pentru a seta o limită de date pentru o cheie. De exemplu, puteți să setați o limită pentru o cheie care credeți că va fi distribuită frecvent, pentru a vă proteja de transferurile excesive de date prin acea cheie.
