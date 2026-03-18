---
title: "Erreurs de pare-feu"
sidebar_label: "Erreurs de pare-feu"
---

Vous pouvez rencontrer trois types d'erreurs liées aux pare-feu :

## Blocage lié à un pare-feu réseau

L'installation d'Outline peut poser problème si vous êtes connecté à un réseau protégé par un pare-feu, sur votre lieu de travail ou dans votre établissement scolaire, par exemple. Dans ce cas, essayez de l'installer sur un autre réseau.

 Si cela ne fonctionne pas, demandez à votre administrateur réseau qu'il autorise les connexions entre votre réseau protégé par un pare-feu et votre serveur Outline. Vous devrez lui fournir l'adresse IP de votre serveur Outline et les ports sur lesquels Outline s'exécute (ceux-ci sont indiqués à la fin du script d'installation).

## Blocage lié à un pare-feu matériel

Si un logiciel installé sur votre appareil bloque les connexions sortantes sur les ports non standards ou les logiciels non reconnus (par exemple, ZoneAlarm de CheckPoint), consultez la documentation de l'appareil ou du logiciel en question en vue de créer une exception pour Outline.

## Blocage lié à un pare-feu de serveur

Le fournisseur de services cloud que vous avez choisi peut vous imposer de créer manuellement des exceptions sur le pare-feu de votre serveur, de manière à ouvrir les ports sur lesquels Outline s'exécute. Ces deux ports sélectionnés aléatoirement ont dû vous être indiqués à la fin du script d'installation. Il suffit généralement d'ouvrir ces deux ports.

 Pour créer des exceptions sur le pare-feu de votre serveur, nous vous recommandons de rechercher les termes "ufw" et "iptables" dans la documentation de ce dernier :

- UFW : [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables : [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
