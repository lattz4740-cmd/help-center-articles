---
title: Configurare automatizată pentru Google Cloud
sidebar_label: Configurare automatizată pentru Google Cloud
---

## Prezentare generală

Outline Manager include o funcție prin care puteți configura automat serverul Outline pe un server care rulează în Google Cloud. Dacă alegeți să folosiți această funcție, Outline Manager vă va solicita să vă conectați cu Contul Google. Astfel, se vor acorda anumite permisiuni[OAuth](https://developers.google.com/identity/protocols/oauth2) pentru instalarea locală a aplicației Outline Manager în scopul configurării Contului Google Cloud.

 Dacă nu doriți să acordați aceste permisiuni, puteți urma instrucțiunile avansate de configurare din Outline Manager pentru a rula Outline pe Google Cloud Platform.

## Permisiuni acordate

Pentru o configurare automatizată, Outline Manager necesită următoarele permisiuni de la Contul dvs. Google.

## Google Cloud Platform

- Să vadă și să gestioneze resursele Google Compute Engine.
- Să vă vadă datele din serviciile Google Cloud și adresa de e-mail asociată Contului dvs. Google.

## Informații de bază despre cont

- Să vadă adresa de e-mail principală din Contul Google.
- Să vă asocieze cu informațiile cu caracter personal de pe Google.

## Acces suplimentar

- Să vă gestioneze proiectele Cloud Platform.
- Să vadă și să vă gestioneze conturile de facturare Google Cloud Platform.
- Să gestioneze configurarea serviciului API Google.

Având aceste permisiuni putem să oferim funcții avansate pentru gestionarea serverelor Outline, inclusiv:

- posibilitatea de selectare a contului de facturare corect;
- crearea unui proiect nou pentru organizarea serverelor Outline;
- înregistrarea centrelor de date disponibile;
- crearea de mașini virtuale noi pentru rularea aplicației Outline;
- configurarea noii mașini virtuale cu Outline.

## Revocarea permisiunilor

Puteți revoca accesul la Google Cloud Platform pentru Outline Manager accesând [Contul meu](https://myaccount.google.com/permissions). Dacă revocați accesul, serverele pe care le-ați creat folosind configurarea automată vor rămâne active, dar nu vor mai apărea în Outline Manager. Pentru a restabili accesul la acestea, trebuie doar să vă reconectați la Google Cloud Platform și să inițiați fluxul de configurare automatizată.

## Organizarea proiectului Outline

Configurarea automatizată a serviciului Google Cloud folosește un singur[proiect Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) pentru organizarea serverelor Outline. Proiectul este creat în timpul primei utilizări a configurării automatizate, având un ID de proiect sugerat care începe cu „Outline-”, urmat de un șir de caractere aleatorii. Dacă doriți, puteți alege alt ID de proiect la momentul creării. Proiectul se va numi „Servere Outline”.

## Cont de facturare

Proiectele Google Cloud necesită un „cont de facturare” conectat care să definească informațiile de plată. Când folosiți configurarea automatizată Google Cloud, vi se va solicita să adăugați un cont de facturare pentru asocierea cu serverele dvs. Outline. Uneori, serverul nu va mai funcționa deoarece există o problemă legată de contul de facturare. În acest caz, trebuie să vă conectați la[Google Cloud Console](https://console.cloud.google.com/getting-started), să găsiți proiectul Google Cloud asociat cu Outline (numit „Servere Outline”) și să actualizați setările de facturare.

## Distrugerea serverelor

Dacă doriți să distrugeți serverele create folosind configurarea automatizată, cea mai simplă modalitate este din Outline Manager. Dacă doriți să distrugeți serverele pe cont propriu, puteți să vă conectați la [Google Cloud Console](https://console.cloud.google.com/getting-started), să găsiți proiectul creat în timpul configurării inițiale (denumit „Servere Outline”) și să ștergeți resursele de acolo sau să închideți proiectul.
