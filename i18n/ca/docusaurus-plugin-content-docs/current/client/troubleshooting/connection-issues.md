---
title: "Per què no em puc connectar al servei d'Outline?"
sidebar_label: "Per què no em puc connectar al servei d'Outline?"
---

Hi ha uns quants motius pels quals és possible que no puguis connectar-te al servei d'Outline:

- **El dispositiu està**[/client/troubleshooting/connection-issues#One](/client/troubleshooting/connection-issues#Internetissues)[**desconnectat d'Internet**](#Internetissues)[#Internetissues](#Internetissues)**.**De vegades, el dispositiu experimenta una interrupció a la connexió de xarxa i pot ser que tardi un moment a actualitzar les icones de la xarxa. També pot ser que estigui connectat a la xarxa local, però no a Internet.
- **El teu**[/client/troubleshooting/connection-issues#Two](/client/troubleshooting/connection-issues#FirewallIssues)[**tallafoc de xarxa està bloquejant l'accés**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[al](#FirewallIssues) servidor d'Outline.**Això és habitual si fas servir una xarxa pública, com ara la d'un centre educatiu, la de la feina o una xarxa sense fil gratuïta.
- **El dispositiu té un**[/client/troubleshooting/connection-issues#Three](/client/troubleshooting/connection-issues#SoftwareIssues)[**tallafoc o un programari antivirus**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**que està bloquejant l'accés al servidor d'Outline.**
- **És possible que hagis de canviar la**[**configuració del teu dispositiu de telèfon**](#DeviceSettings)**.**
- **Pot ser que el gestor del servei hagi**[**destruït el servidor o que el proveïdor d'Internet estigui bloquejant la teva sol·licitud**](#ServerIssues).

## Problemes de connexió a Internet: {#Internetissues}

## Com pots fer una prova:
Desactiva Outline i comprova si es restableix la connexió a Internet.

- Si es restableix, consulta més opcions de resolució de problemes a continuació.
- Si no es restableix, espera una mica per veure si la configuració de la connexió s'actualitza.

## Coses que cal corregir:

Torna a connectar el dispositiu:

1. Comprova si un altre dispositiu es pot connectar a la mateixa xarxa. Si tampoc no s'hi pot connectar, és possible que la xarxa no funcioni. Hauràs d'esperar que torni a estar activa o resoldre el problema de xarxa.
2. En cas que l'altre dispositiu es pugui connectar a la mateixa xarxa, pots seguir un o diversos dels passos que hi ha a continuació per tornar a tenir connexió:
   1. Posa el dispositiu en mode d'avió (per a mòbils).
   2. Reinicia el dispositiu.
   3. Apaga el dispositiu, espera dos minuts i torna a engegar-lo.

## Problemes amb el tallafoc de xarxa: {#FirewallIssues}

## Com pots fer una prova:

1. Desconnecta't de la xarxa Wi‑Fi o amb cable actual.
2. Connecta't a una altra xarxa, com ara una xarxa mòbil.
3. Prova de tornar a connectar-te al servidor d'Outline.

Si et pots connectar des de l'altra xarxa, ja saps quin problema hi ha.

## Coses que cal corregir:
Contacta amb el gestor del servei i demana-li que permeti l'accés al servidor d'Outline o bé continua utilitzant l'altra xarxa.

## Problemes amb el tallafoc o el programari antivirus: {#SoftwareIssues}

## Com es pot provar: {#DeviceSettings}

 Prova de connectar-te a Outline des d'un altre dispositiu.

Nota: recorda que necessitaràs una clau d'accés i l'aplicació Outline per fer servir Outline en un altre dispositiu.

## Coses que cal corregir:

Comprova la configuració del tallafoc o del programari antivirus per assegurar-te que permeten la VPN i el trànsit d'Outline.

## Configuració del dispositiu: {#ServerIssues}

## Coses que cal comprovar:

Per a Android:

1. Obre l'aplicació Configuració.
2. Cerca la **configuració de la VPN** al dispositiu (aquesta configuració et mostrarà totes les aplicacions de VPN que actualment tenen accés al telèfon).
3. Si no veus Outline a la configuració de la VPN, desinstal·la Outline i torna a instal·lar-lo. Un cop instal·lat, el dispositiu hauria de donar accés a Outline automàticament.

Assegura't que no tinguis cap aplicació de superposició de pantalla instal·lada al dispositiu Android, ja que això podria estar enviant la finestra de permisos d'Outline a un segon pla i fer que no es mostri en primer pla.

 Al dispositiu Android, ves a Configuració > Aplicacions > Accés especial d'aplicacions. A continuació, toca "Mostra sobre altres aplicacions". Pots suprimir l'accés a qualsevol aplicació que permeti aquest comportament.

 Per a iOS: llegeix [aquest article d'assistència](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

**Problemes amb el servidor**:

## Com pots fer una prova:
Si tens accés a més d'un servidor, prova de connectar-te a un altre.

## Coses que cal corregir:

Contacta amb el gestor del servei per saber si el servidor s'ha destruït. Si és així, demana-li una [clau d'accés](/about/terminology) a un altre servidor.

Si vas configurar el servidor pel teu compte, prova de connectar-t'hi amb el Gestor d'Outline o un altre mètode, com ara [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Si això no funciona, pots provar de consultar la consola del proveïdor de serveis al núvol (si n'hi ha cap) per veure si el servidor continua en línia.
