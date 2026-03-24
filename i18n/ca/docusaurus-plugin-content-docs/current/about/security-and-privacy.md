---
title: Seguretat i privadesa en utilitzar Outline
sidebar_label: Seguretat i privadesa en utilitzar Outline
---

Seguretat i privadesa en utilitzar Outline

## De quina manera Outline protegeix les teves comunicacions en línia

El trànsit d'Internet és més vulnerable a la vigilància quan passa per la xarxa local o nacional.

Outline ajuda a mantenir les comunicacions privades encriptant el trànsit d'Internet quan viatja per la xarxa nacional i el manté encriptat fins que no arriba al servidor d'Outline. Quan el trànsit s'encripta amb Outline, els vigilants de la xarxa no poden inspeccionar els llocs web que visites ni la informació que transfereixes.

Outline també et pot ajudar a recuperar l'accés a eines de comunicació segures d'extrem a extrem a les quals al teu país no podries accedir de cap altra manera.

## Estàndards d'encriptació

Outline encripta les comunicacions entre el dispositiu i el servidor d'Outline mitjançant l'encriptació Chacha2020 IETF Poly 1305 d'AEAD, de 256 bits. L'encriptació d'AEAD ofereix confidencialitat, integritat i autenticitat, i té un rendiment excel·lent en maquinari modern.

## Auditories de seguretat

El 2018, Outline es va sotmetre a l'auditoria de Radically Open Security i Cure53, dues organitzacions de seguretat digital independents que comproven que el programari compleixi els estàndards de seguretat més recents. Radically Open Security va dur a terme una auditoria addicional el 2022, i Cure53 va fer una auditoria de l'SDK d'Outline el 2024. Pots llegir els informes aquí:

- [Informe de la prova de penetració de Radically Open Security (març de 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Informe d'auditoria i prova de penetració de Jigsaw Outline per Cure53 (desembre de 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Informe de la prova de penetració de Radically Open Security (desembre de 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Prova de penetració i informe de Cure53 sobre l'SDK d'Outline VPN de Jigsaw (gener de 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Mètriques i registres anònims

Outline fa el seguiment de l'amplada de banda que s'utilitza, com a "bytes transferits" per cada clau d'accés. Aquesta informació permet als administradors del servidor ajustar les subscripcions de l'amplada de banda als seus proveïdors de servidor en núvol en funció de les necessitats, però no els permet veure la informació real que passa pel servidor d'Outline.

Obtén més informació sobre la [recollida de dades i d'informació](/about/data-collection) d'Outline.

---

## Preguntes freqüents sobre seguretat i privadesa

## Outline em permet navegar de manera anònima?

No. Outline no és una eina d'anonimització, sinó que protegeix la teva privadesa davant de possibles vigilants de la xarxa.

Outline no t'ofereix l'anonimat complet als llocs web que visites, perquè se t'hi pot continuar identificant en iniciar-hi la sessió i, de vegades, mitjançant tècniques com l'ús de l'empremta digital al navegador. Pel que fa a les aplicacions mòbils, la majoria de telèfons intel·ligents moderns tenen diverses API que permeten a les aplicacions instal·lades obtenir la teva ubicació independentment del servidor intermediari, ja que poden basar-se en el GPS inserit.

En general, les VPN ofereixen opcions de protecció importants, particularment davant de la vigilància a Internet, però en treballar en línia sempre es corren riscos. Fins i tot amb una VPN, si un proveïdor d'Internet ja coneix la teva identitat i pot observar el teu trànsit de xarxa, podria arribar a determinar l'adreça IP del teu servidor d'Outline. Aquesta informació es pot utilitzar per bloquejar l'accés al servidor d'Outline o per revelar patrons d'ús, com ara quan acostumes a connectar-te i, possiblement, la teva ubicació aproximada.

## Es pot saber que utilitzo Outline?

Possiblement. És molt probable que les plataformes i els serveis a què accedeixis puguin saber si la connexió procedeix d'un servidor en núvol. De vegades, encara que puguin deduir que estàs fent servir una VPN, no podran veure el contingut del teu trànsit d'Internet.

## Outline em protegeix davant de totes les possibles ciberamenaces?

No. Cap eina no et pot protegir contra totes les possibles ciberamenaces. Outline et dona accés a la Internet oberta i augmenta la teva privadesa encriptant el trànsit, però et recomanem que prenguis mesures addicionals per protegir-te contra altres tipus d'atacs, com ara el programari maliciós i la pesca de credencials.

Per poder reforçar les teves defenses en línia, et recomanem que contactis amb un expert en ciberseguretat de la teva organització. També pots obtenir orientació personalitzada d'experts capdavanters en seguretat a [Security Planner](https://securityplanner.org/), un lloc web creat per proporcionar-te instruccions clares per triar les eines de ciberseguretat adequades a les teves necessitats.

També pots consultar altres productes de ciberseguretat de [Jigsaw](https://jigsaw.google.com/), com ara [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) i [Alerta de protecció de contrasenya](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## És legal fer servir una VPN?

Consulta les lleis i les regulacions locals, així com les condicions del servei del proveïdor de serveis en núvol que vulguis fer servir abans d'utilitzar Outline o l'aplicació.
