---
title: Configuració automàtica de Google Cloud
sidebar_label: Configuració automàtica de Google Cloud
---

## Informació general

El Gestor d'Outline inclou una funció que et permet configurar automàticament el servidor d'Outline en un servidor que s'executi a Google Cloud. Si tries utilitzar aquesta funció, el Gestor d'Outline et demanarà que iniciïs la sessió amb el teu Compte de Google, que concedirà determinats permisos d'[OAuth](https://developers.google.com/identity/protocols/oauth2) a la instal·lació local del Gestor d'Outline per poder configurar el compte de Google Cloud.

 Si no vols concedir aquests permisos, pots seguir les instruccions de configuració avançada del Gestor d'Outline per executar-lo a Google Cloud Platform.

## Permisos que cal concedir

Per tal de fer la configuració automàtica, el Gestor d'Outline necessita els permisos següents del teu Compte de Google.

## Google Cloud Platform

- Consultar i gestionar els recursos de Google Compute Engine
- Visualitzar les teves dades als serveis de Google Cloud i veure l'adreça electrònica del teu Compte de Google

## Informació bàsica del compte

- Veure l'adreça electrònica principal del teu Compte de Google
- Associar-te a la teva informació personal a Google

## Accés addicional

- Gestionar els projectes de Cloud Platform
- Visualitzar i gestionar els comptes de facturació de Google Cloud Platform
- Gestionar la configuració del servei de l'API de Google

Aquests permisos ens permeten oferir funcions avançades per gestionar els servidors d'Outline, com ara els següents:

- Poder seleccionar el compte de facturació correcte
- Crear un projecte nou per organitzar els servidors d'Outline
- Llistar els centres de dades disponibles
- Crear màquines virtuals noves per executar Outline
- Configurar la màquina virtual nova amb Outline

## Revocar els permisos

Pots revocar l'accés del Gestor d'Outline a Google Cloud Platform des d'[El meu compte](https://myaccount.google.com/permissions). Si ho fas, qualsevol servidor que hagis creat amb la configuració automàtica continuarà funcionant, però ja no es mostrarà al Gestor d'Outline. Per restaurar-ne l'accés, només cal que tornis a connectar-te a Google Cloud Platform iniciant el flux de configuració automàtic.

## Organització d'un projecte d'Outline

La configuració automàtica de Google Cloud utilitza un únic [projecte de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) per organitzar els servidors d'Outline. El projecte es crea el primer cop que s'utilitza la configuració automàtica, amb el suggeriment d'un identificador de projecte que comença per "Outline-" seguit d'una cadena de caràcters aleatoris. Si ho prefereixes, pots triar un altre identificador de projecte en el moment de crear-lo. El projecte s'anomenarà "Servidors d'Outline".

## Compte de facturació

En els projectes de Google Cloud cal que hi hagi un compte de facturació enllaçat que defineixi la informació de pagament. La primera vegada que utilitzis la configuració automàtica de Google Cloud, se't demanarà que proporcionis un compte de facturació per associar-lo als teus servidors d'Outline. De vegades, un servidor pot deixar d'executar-se perquè hi ha un problema amb el compte de facturació. En aquest cas, has d'iniciar la sessió a la [consola de Google Cloud](https://console.cloud.google.com/getting-started), localitzar el projecte de Google Cloud associat a Outline (anomenat "Servidors d'Outline") i actualitzar la configuració de facturació.

## Destruir els servidors

Si vols destruir els servidors que s'han creat amb la configuració automàtica, la manera més fàcil de fer-ho és des del Gestor d'Outline. No obstant això, si vols destruir els servidors, pots iniciar la sessió a la [consola de Google Cloud](https://console.cloud.google.com/getting-started), cercar el projecte que es va crear durant la configuració inicial (anomenat "Servidors d'Outline") i suprimir allà els recursos o bé tancar el projecte.
