---
title: Errors del tallafoc
sidebar_label: Errors del tallafoc
---

Et pots trobar amb tres tipus de problemes relacionats amb el tallafoc:

## Et pot bloquejar un tallafoc de xarxa.

Si estàs provant d'instal·lar Outline i la xarxa a què et connectes, com ara la de la feina o del centre educatiu, té un tallafoc, prova de fer la instal·lació connectant-te a una altra xarxa.

Si això no funciona, contacta amb l'administrador de la teva xarxa perquè permeti les connexions entre la xarxa amb tallafoc i el teu servidor d'Outline. Hauràs de saber l'adreça IP del teu servidor d'Outline i els ports en què Outline s'executa. Trobaràs aquestes dades al final de l'script d'instal·lació.

**Et pot bloquejar el tallafoc d'un dispositiu**.

Si el dispositiu conté programari que bloqueja les connexions de sortida en ports no estàndard o programari desconegut (per exemple, ZoneAlarm de CheckPoint), consulta la documentació del dispositiu o del programari per obtenir informació sobre com pots crear una excepció per a Outline.

## Et pot bloquejar el tallafoc d'un servidor.

Pot ser que el proveïdor de serveis en núvol que has triat requereixi la creació manual d'excepcions al tallafoc del servidor perquè s'obrin els ports en què Outline s'executa. Després d'executar l'script d'instal·lació, se t'han d'haver mostrat els dos ports seleccionats aleatòriament en què Outline s'executa al servidor. N'hi hauria d'haver prou amb obrir aquests dos ports.

 Per poder crear excepcions al tallafoc del servidor, et recomanem que cerquis "ufw" i "iptables" a la documentació:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
