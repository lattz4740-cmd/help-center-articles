---
title: Securitate și confidențialitate când folosiți Outline
sidebar_label: Securitate și confidențialitate când folosiți Outline
---

Securitate și confidențialitate când folosiți Outline

## Cum vă protejează Outline comunicațiile online

Traficul pe internet este cel mai vulnerabil la supraveghere atunci când trece prin rețeaua locală sau națională.

Outline contribuie la menținerea confidențialității comunicațiilor prin criptarea traficului pe internet în timp ce traversează rețeaua națională și menține traficul criptat până când ajunge la serverul Outline. Când traficul este criptat prin Outline, ceilalți utilizatori din rețea nu pot inspecta site-urile pe care le accesați, nici informațiile pe care le transferați.

Outline poate să fie util și pentru recuperarea accesului la instrumente securizate de comunicații end-to-end, care nu sunt accesibile în alt mod în țara dvs.

## Standarde de criptare

Outline criptează comunicațiile dintre dispozitiv și serverul Outline utilizând cifrul AEAD 256-bit Chacha2020 IETF Poly 1305. Cifrurile AEAD oferă confidențialitate, integritate și autenticitate și dau dovadă de o performanță excelentă pe echipamentele hardware moderne.

## Audituri de securitate

În 2018, Outline a fost auditat de Radically Open Security și Cure53, două organizații pentru securitate digitală independente care examinează programele software în conformitate cu cele mai recente standarde de securitate. Radically Open Security a desfășurat un audit suplimentar în 2022, iar Cure53 a desfășurat un audit al Outline SDK în 2024. Puteți citi rapoartele aici:

- [Raportul testului de penetrare elaborat de Radically Open Security (martie 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Raport de audit și test de penetrare Cure53 privind Jigsaw Outline (decembrie 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Raportul testului de penetrare elaborat de Radically Open Security (decembrie 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Raportul testului de penetrare elaborat de Cure53 privind Jigsaw Outline VPN SDK (ianuarie 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Valori și jurnale anonime

Outline monitorizează lățimea de bandă utilizată, sub formă de „byți transferați” pentru fiecare cheie de acces. Administratorii de servere pot folosi aceste informații pentru a ajusta abonamentele de lățime de bandă la furnizorii de servere cloud după cum este necesar, însă nu le pot folosi pentru a vedea informațiile reale transferate prin serverul Outline.

Aflați mai multe despre [colectarea datelor și a informațiilor](https://getoutline.org/policies/data-collection) în Outline.

---

## Întrebări frecvente privind securitatea și confidențialitatea

## Pot să navighez anonim online prin Outline?

Nu, Outline nu este un instrument pentru anonimitate. Outline vă protejează confidențialitatea față de ceilalți utilizatori potențiali din rețea.

Outline nu vă oferă anonimitate completă pe site-urile web pe care le accesați, deoarece site-urile respective vă pot identifica atunci când vă conectați sau prin tehnici precum amprentare digitală în browser. Pentru aplicațiile mobile, majoritatea smartphone-urilor moderne conțin interfețe API care permit aplicațiilor instalate să vă determine locația independent de serverul proxy, folosind sistemele GPS încorporate.

VPN-urile oferă, în general, niveluri de protecție importante, în special în ceea ce privește supravegherea traficului pe internet, dar există întotdeauna riscuri legate de activitatea online. Chiar și atunci când folosiți VPN, dacă un furnizor de servicii de internet vă cunoaște deja identitatea și poate să vă vadă traficul în rețea, acesta poate să stabilească adresa IP a serverului dvs. Outline. Aceste informații pot fi folosite pentru a bloca accesul la serverul Outline sau pentru a identifica modelele de utilizare, de exemplu, când sunteți de obicei online, eventual chiar și locația aproximativă.

## Poate cineva să-și dea seama că folosesc Outline?

E posibil. Cel mai probabil, platformele și serviciile pe care le accesați pot să determine dacă aveți o conexiune care provine de la un server cloud. Ocazional, pot deduce că utilizați o rețea VPN, dar nu vor putea să vadă conținutul traficului dvs. pe internet.

## Outline mă protejează de toate amenințările cibernetice?

Nu. Niciun instrument nu vă protejează împotriva tuturor amenințărilor cibernetice posibile. Outline vă oferă acces la internetul liber și crește nivelul de confidențialitate prin criptarea traficului, însă vă recomandăm să luați măsuri de precauție suplimentare pentru a vă proteja împotriva altor tipuri de atacuri, cum ar fi programe malware și phishing.

Pentru a vă consolida sistemele de protecție online, este recomandat să vă consultați cu expertul în domeniul securității cibernetice din cadrul organizației dvs. Alternativ, puteți obține îndrumări personalizate de la experți de top în domeniul securității de la [Security Planner](https://securityplanner.org/), un site creat pentru a vă oferi instrucțiuni clare cu privire la alegerea instrumentelor de securitate cibernetică adecvate preocupărilor dvs.

Puteți și să consultați celelalte produse de securitate cibernetică de la [Jigsaw](https://jigsaw.google.com/), cum ar fi [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) și [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Este legală folosirea unei rețele VPN?

Consultați legislația și reglementările locale, precum și Termenii și condițiile furnizorului de servicii cloud pe care intenționați să le folosiți, înainte de a folosi Outline sau înainte de a folosi aplicația.
