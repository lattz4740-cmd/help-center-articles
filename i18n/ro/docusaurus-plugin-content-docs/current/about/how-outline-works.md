---
title: Cum funcționează Outline
sidebar_label: Cum funcționează Outline
---

**Instalarea serverului**

 ​Deși instalarea Outline poate părea simplă, există, însă, un set complex de pași care au loc în fundal pentru a vă instala serverul. La instalarea Outline se rulează un script care execută următorii pași.

- Se preia și se importă versiunea stabilă a imaginii Shadowbox, prin Docker. Imaginea este găzduită pe [Quay.io](https://quay.io/), la [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Această imagine conține serverul Outline și API-ul Management, care este folosit ulterior de aplicația Outline Server Management pentru a crea și a elimina chei de acces, a activa / dezactiva raportarea valorilor anonime etc.
- [Watchtower](https://github.com/v2tec/watchtower) este instalat și configurat pentru a verifica dacă există actualizări de imagini în fiecare oră, ajutând să vă asigurați că fiecare server Outline este actualizat în mod constant cu cele mai recente funcții și îmbunătățiri de securitate.
- Este pornit un server web, folosit pentru accesarea API-ului Management, pe un port aleatoriu pe o cale aleatorie și secretă.
- Se creează un [certificat SSL autosemnat](https://en.wikipedia.org/wiki/Self-signed_certificate), astfel încât gestionarea serverului Outline să poată fi criptată folosindu-se TLS chiar dacă nu există un nume de domeniu. Se generează și o amprentă digitală unică a certificatului, care este generată și stocată în aplicația Outline Manager, contribuind astfel la prevenirea atacurilor MITM.

Aplicația Outline nu necesită o configurare după instalare.

**Securitatea serverului**

 Software-ul Outline este open source, ceea ce înseamnă că oricine poate vedea codul și îl poate îmbunătăți dacă sunt descoperite vulnerabilități. Codul nostru este găzduit pe [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 În plus, toate serverele Outline instalate sunt actualizate automat când este lansată o versiune nouă, astfel încât niciun server Outline nu mai rulează versiunile vechi de software.

 Pentru gestionarea cheilor de acces la server, aplicația Outline Manager interacționează cu un serviciu de gestionare pe serverul Outline. Serviciul de gestionare rulează pe un port aleatoriu și pe o cale unică și secretă. Serviciul de gestionare nu poate fi scanat deoarece nu răspunde la interogări decât dacă este specificată calea secretă corespunzătoare. Toată comunicarea cu serviciul de gestionare este criptată cu un [certificat SSL autosemnat](https://en.wikipedia.org/wiki/Self-signed_certificate).

 În plus, serverul Outline nu stochează niciun jurnal, prin urmare, chiar dacă este compromis, nu sunt dezvăluite datele utilizatorilor. Aflați mai multe [aici](https://support.getoutline.org/s/article/Security-and-privacy). Outline a fost auditat de [Radically Open Security](https://radicallyopensecurity.com/) și [Cure53](https://cure53.de/) în 2018. Consultați rapoartele [aici](https://support.getoutline.org/s/article/Security-and-privacy).

**Gestionarea traficului UDP**

 Outline poate funcționa ca o rețea VPN pentru tot sistemul, ceea ce poate însemna că tot traficul UDP este direcționat prin serverul Outline.

**Trafic DNS**

Outline efectuează toate căutările DNS prin intermediul serverului Outline și le protejează folosind aceeași criptare utilizată pentru restul activităților din rețea. Interogările DNS vor trece prin serverul Outline către Dyn Internet Guide, OpenDNS, Cloudflare DNS sau Quad9 DNS. Outline nu înregistrează niciodată căutările DNS.
