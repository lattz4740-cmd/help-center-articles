---
title: "Comment mettre à jour mon logiciel serveur Outline?"
sidebar_label: "Comment mettre à jour mon logiciel serveur Outline?"
---

Les serveurs Outline sont automatiquement mis à jour avec les dernières améliorations de sécurité. Vous bénéficiez donc en permanence des technologies Outline les plus récentes. Cette procédure automatisée est rendue possible par [Watchtower](https://github.com/containrrr/watchtower), une bibliothèque Open Source qui recherche régulièrement les mises à jour et les applique à l'image Docker contenant le logiciel Outline.

Par ailleurs, lorsque vous installez Outline à l'aide d'Outline Manager, nous configurons un job Cron qui met automatiquement à niveau le logiciel sur le serveur grâce aux [mises à niveau autonomes](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) et le redémarre si besoin. Notez que pour préserver la configuration actuelle, cela ne se produit pas en mode avancé, car il est probable que l'hôte ne serve pas seulement à exécuter Outline.
