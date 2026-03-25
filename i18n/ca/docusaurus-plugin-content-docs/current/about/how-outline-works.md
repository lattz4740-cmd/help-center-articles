---
title: Com funciona Outline
sidebar_label: Com funciona Outline
---

## Instal·lació del servidor
 ​Tot i que Outline pot semblar una aplicació senzilla, hi ha un conjunt de passos complexos que es duen a terme en segon pla per poder instal·lar el servidor. Quan s'instal·la Outline, un script d'instal·lació executa els passos següents:

- La versió estable de la imatge de Shadowbox es recupera i s'importa mitjançant Docker. La imatge, que s'allotja a [Quay.io](https://quay.io/) ([https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags)), conté el servidor d'Outline i l'API de gestió que l'aplicació Gestor de servidors d'Outline utilitzarà més endavant per crear i suprimir les claus d'accés, optar per informar o no informar de mètriques de manera anònima, etc.
- [Watchtower](https://github.com/containrrr/watchtower) s'instal·la i es configura per cercar actualitzacions d'imatges cada hora. Així es garanteix que cada servidor d'Outline estigui sempre actualitzat amb les millores de seguretat i funcions més recents.
- Un servidor web, utilitzat per accedir a l'API de gestió, s'inicia en un port aleatori en un camí secret i aleatori.
- Es crea un [certificat SSL amb firma automàtica](https://en.wikipedia.org/wiki/Self-signed_certificate) perquè la gestió del servidor d'Outline es pugui encriptar utilitzant TLS malgrat no tenir cap nom de domini. També es genera una empremta digital única d'aquest certificat i s'emmagatzema a l'aplicació Gestor d'Outline, cosa que permet evitar atacs d'intermediari (MITM).

Per instal·lar Outline, no cal dur a terme cap configuració després de la instal·lació.

## Seguretat del servidor
 El programari d'Outline és de codi obert, la qual cosa significa que tothom pot veure'n el codi i millorar-lo si s'hi troben vulnerabilitats. El nostre codi s'allotja a [GitHub](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline).

 A més, tots els servidors d'Outline instal·lats s'actualitzen automàticament sempre que es publica una versió nova; per tant, es garanteix que cap servidor d'Outline no faci servir versions antigues del programari.

 Per gestionar les claus d'accés al servidor, l'aplicació Gestor d'Outline interacciona amb un servei de gestió del servidor d'Outline. Aquest servei s'executa en un port aleatori i en un camí únic i secret. També s'ha demostrat que és resistent, ja que no respon a consultes si no s'especifica el camí secret adequat. Per últim, totes les comunicacions mantingudes amb el servei de gestió s'encripten amb un [certificat SSL amb firma automàtica](https://en.wikipedia.org/wiki/Self-signed_certificate).

 A més, el servidor d'Outline no emmagatzema cap registre i, per tant, encara que es posi en perill, no es revelarà cap dada de l'usuari. [Obtén més informació](/about/security-and-privacy). El 2018, Outline es va sotmetre a l'auditoria de [Radically Open Security](https://radicallyopensecurity.com/) i [Cure53](https://cure53.de/). En pots consultar els informes [aquí](/about/security-and-privacy).

## Gestionar el trànsit d'UDP
 Outline pot funcionar com una VPN de sistema, amb la qual cosa tot el trànsit d'UDP es canalitzarà a través del servidor d'Outline.

## Trànsit de DNS
Outline executa totes les cerques de DNS a través del servidor i les protegeix utilitzant la mateixa encriptació que es fa servir per a la resta d'activitat de xarxa. Les consultes de DNS passen pel servidor d'Outline fins a Internet Guide de Dyn, OpenDNS, Cloudflare DNS o Quad9 DNS. Outline no registra mai les teves cerques de DNS.
