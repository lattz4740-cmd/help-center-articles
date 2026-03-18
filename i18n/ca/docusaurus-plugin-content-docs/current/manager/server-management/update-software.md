---
title: "Com puc actualitzar el programari del servidor d'Outline?"
sidebar_label: "Com puc actualitzar el programari del servidor d'Outline?"
---

Els servidors d'Outline s'actualitzen automàticament amb les darreres millores de seguretat perquè sempre utilitzis la tecnologia d'Outline més recent. El procés d'actualització automàtic s'activa amb [Watchtower](https://github.com/v2tec/watchtower), una biblioteca de codi obert que comprova i actualitza regularment la imatge Docker que conté el programari d'Outline.

A més, quan instal·lis Outline utilitzant el Gestor d'Outline, configurarem una tasca cronològica per actualitzar automàticament el programari del servidor mitjançant [actualitzacions sense supervisió](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) i reiniciar-lo quan calgui. Tingues en compte que això no passa en el Mode avançat per preservar la configuració existent, segons la premissa que l'amfitrió es fa servir per a altres finalitats a més d'executar Outline.
