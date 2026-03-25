---
title: Terminologia
sidebar_label: Terminologia
---

## Què és una VPN?
 Una xarxa privada virtual (VPN) és una connexió privada entre els teus dispositius i un servidor amfitrió. Quan utilitzes una VPN, el teu trànsit s'amaga del proveïdor d'Internet. Et recomanem que utilitzis una VPN en els casos següents:

- Per protegir les teves dades quan facis servir una xarxa Wi‑Fi pública.
- Per mantenir la privadesa de les teves dades de navegació respecte del teu proveïdor d'Internet i d'organismes governamentals.
- Per accedir a contingut no censurat de diverses fonts de tot el món.

## Quina diferència hi ha entre Outline i les VPN tradicionals?
 Els proveïdors d'Internet poden detectar i bloquejar fàcilment les VPN tradicionals en reconèixer els protocols de seguretat comuns o els patrons de volum de trànsit. Outline és més resilient que les VPN tradicionals perquè s'ha creat amb un protocol dissenyat per ser difícil de detectar i, per tant, més complicat de bloquejar. Outline també pot fer front a formes sofisticades de censura, com ara el bloqueig basat en xarxa i el bloqueig d'IP.

## Què és un servidor d'Outline?
 Un servidor d'Outline executa la VPN a la qual es connectaran els usuaris permesos. Si crees una xarxa nova, pots utilitzar el teu servidor segur (si en tens un) com a servidor d'Outline. També pots fer servir un proveïdor de serveis al núvol, com ara:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Configuraràs el servidor al Gestor d'Outline.

## Què és un gestor de serveis? {#servicemanager}
 Un gestor de serveis és la persona responsable de configurar el servidor d'Outline i compartir les claus d'accés amb els usuaris. En general, el gestor de serveis és responsable del cost d'ús del servidor. 

## Què és una clau d'accés? {#accesskey}
 Les claus d'accés s'utilitzen per accedir a un servidor d'Outline existent i connectar-se a la VPN. El [gestor de serveis](#servicemanager) et donarà una clau d'accés, o bé pots [configurar un servidor d'Outline](/manager/server-setup/setup-server) pel teu compte. Aquí tens un exemple de com és una clau d'accés (només és una mostra, així que no funciona): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Què és el Gestor d'Outline?
 El Gestor d'Outline és una aplicació per a ordinadors que permet que un gestor de serveis configuri un servidor d'Outline, generi [claus d'accés](#accesskey) i estableixi límits de dades per a l'ús de cada clau. Et pots baixar la darrera versió del Gestor d'Outline [aquí](https://getoutline.org/get-started/#step-3) o [aquí](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Què és el Client d'Outline?
 El Client d'Outline és una aplicació per a ordinadors i mòbils que et permet connectar-te a un servidor d'Outline i accedir a la VPN mitjançant una clau d'accés. Et pots baixar la darrera versió del Client d'Outline [aquí](https://getoutline.org/get-started/#step-3) o [aquí](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Què són els límits de dades?
 El Gestor d'Outline permet als gestors de serveis establir un límit de dades a les claus d'accés que se cenyeixi als 30 darrers dies per evitar-ne un ús excessiu i fer que els costos siguin previsibles. Els gestors de serveis poden establir un límit predeterminat que s'apliqui a cada clau i un límit diferent de qualsevol clau per anul·lar-ne el predeterminat. Un cop establert, el límit tindrà efecte de manera immediata i s'aplicarà cada hora.

Si els gestors de serveis accepten compartir mètriques amb Jigsaw, és important que consultin la [política de recollida de dades](https://getoutline.org/policies/data-collection) per saber com s'informarà dels límits de dades.
