---
title: "Fonctionnement d'Outline"
sidebar_label: "Fonctionnement d'Outline"
---

### Installation du serveur

Même si l'installation d'un server Outline semble simple, elle consiste en une série d'étapes complexes réalisées en coulisses.

Lors de l'installation d'Outline, le script effectue les opérations suivantes :

- L'image correspondant à la version stable de Shadowbox est récupérée et importée via Docker. Cette image est hébergée sur Quay.io, à l'adresse https://quay.io/repository/outline/shadowbox?tab=tags. Elle contient le serveur Outline, ainsi que l'API Management qui permettra ensuite à l'application Outline Server Management de créer et de supprimer des clés d'accès, d'accepter/de refuser l'envoi de statistiques anonymes, etc.
- Watchtower est installé et configuré de manière à rechercher des mises à jour de l'image toutes les heures et à garantir que tous les serveurs Outline disposent en permanence des dernières fonctionnalités et améliorations en matière de sécurité.
- Un serveur Web permettant d'accéder à l'API Management est démarré sur un port aléatoire avec un chemin d'accès aléatoire et secret.
- Un certificat SSL autosigné est créé de manière à chiffrer la gestion du serveur Outline avec le protocole TLS, malgré l'absence de nom de domaine. Une empreinte unique de ce certificat est également générée et stockée dans l'application Outline Manager, afin de protéger le serveur des attaques de type MITM (man-in-the-middle, attaque de l'homme du milieu).

Une fois Outline installé, aucune autre configuration n'est requise.

### Sécurité du serveur

Outline est un logiciel Open Source. En d'autres termes, tout le monde peut accéder à son code et l'améliorer si des failles sont découvertes. Notre code est hébergé sur

.

De plus, tous les serveurs Outline installés étant automatiquement mis à jour dès qu'une nouvelle version est disponible, aucun serveur ne peut exécuter une version obsolète du logiciel.

L'application Outline Manager gère les clés d'accès par le biais d'un service de gestion sur le serveur Outline. Ce service s'exécute sur un port aléatoire et avec un chemin d'accès unique tenu secret. Il est lui-même considéré comme fiable, car il ne répond qu'aux requêtes qui spécifient le chemin d'accès secret approprié. Enfin, toutes les communications adressées au service de gestion sont chiffrées avec un

.

Il convient de noter que le serveur Outline ne stocke aucun fichier journal. Cela signifie qu'en cas de piratage, aucune donnée utilisateur ne pourra être divulguée.

pour en savoir plus.

En 2018, Outline a été audité par

et

.

pour consulter les rapports.

### Gestion du trafic UDP

Outline peut fonctionner en tant que VPN à l'échelle du système. En d'autres termes, le trafic UDP transite intégralement via le serveur Outline.

### Trafic DNS

Outline effectue toutes les résolutions DNS via le serveur Outline et les protège avec les mêmes algorithmes de chiffrement que ceux mis en œuvre pour les autres activités du réseau. Vos requêtes DNS passent par le serveur Outline avant d'être adressées à Dyn Internet Guide ou OpenDNS.

Outline ne journalise jamais vos résolutions DNS.
