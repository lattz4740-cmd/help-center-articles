---
title: Terminologie
sidebar_label: Terminologie
---

## Qu'est-ce qu'un VPN ?

Un réseau privé virtuel (VPN, Virtual Private Network) désigne une connexion privée entre votre ou vos appareils et un serveur hôte. Lorsque vous utilisez un VPN, votre trafic est masqué aux yeux de votre fournisseur d'accès à Internet.

L'utilisation d'un VPN est pertinente pour :

- protéger vos données sur les réseaux Wi-Fi publics ;
- préserver la confidentialité de vos données de navigation face à votre fournisseur d'accès à Internet ainsi qu'aux autorités administratives ;
- accéder aux contenus non censurés de diverses sources dans le monde entier.

## Quelle est la différence entre Outline et un VPN traditionnel ?

Les fournisseurs d'accès à Internet peuvent facilement détecter et bloquer les VPN traditionnels en identifiant les protocoles de sécurité et/ou les schémas de volume de trafic courants. Outline est plus résilient que les VPN traditionnels, car il est basé sur un protocole conçu pour rendre la détection, et donc le blocage, plus difficiles. Outline résiste aux formes sophistiquées de censure, y compris le blocage en fonction du réseau ou de l'adresse IP.

## Qu'est-ce qu'un serveur Outline ?

Un serveur Outline exécute le VPN auquel se connecteront les utilisateurs autorisés.

Si vous créez un réseau, vous pouvez utiliser votre propre serveur sécurisé comme serveur Outline si vous en avez un ou faire appel à un fournisseur de services cloud, par exemple :

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Vous configurerez votre serveur dans Outline Manager.

## Qu'est-ce qu'un gestionnaire de service ? {#servicemanager}

Le gestionnaire de service est la personne habilitée à configurer le serveur Outline et à fournir les clés d'accès aux utilisateurs. C'est généralement lui qui supervise les coûts d'utilisation du serveur.

## Qu'est-ce qu'une clé d'accès ? {#accesskey}

Une clé d'accès sert à accéder à un serveur Outline existant et à se connecter au VPN. Le [gestionnaire de service](#servicemanager) vous fournira une clé d'accès, ou vous pouvez [configurer un serveur Outline](/manager/server-setup/setup-server) vous-même.

Voici un exemple de clé d'accès (non fonctionnelle, donnée à titre d'exemple uniquement) :

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Qu'est-ce qu'Outline Manager ?

Outline Manager est une application de bureau qui permet au gestionnaire de service de configurer un serveur Outline, de générer des [clés d'accès](#accesskey) et de définir des limites de données par clé. Vous pouvez télécharger la dernière version d'Outline Manager sur [cette page](https://getoutline.org/get-started/#step-3) ou sur [celle-ci](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Qu'est-ce que le client Outline ?

Le client Outline est une application disponible sur ordinateur et mobile qui permet de se connecter à un serveur Outline et d'accéder au VPN à l'aide d'une clé d'accès. Vous pouvez télécharger la dernière version du client Outline sur [cette page](https://getoutline.org/get-started/#step-3) ou sur [celle-ci](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Que sont les limites de données ?

Outline Manager permet aux gestionnaires de service de définir une limite de données sur 30 jours glissants pour les clés d'accès afin d'éviter toute utilisation abusive et tout imprévu au niveau du budget. Les gestionnaires de service peuvent définir une limite par défaut s'appliquant à chaque clé ou une limite spécifique à chaque clé qui remplace la limite par défaut. Une fois la limite définie, elle entre en vigueur immédiatement et elle est appliquée à l'heure.

Si les gestionnaires de service acceptent de partager les métriques avec Jigsaw, nous leur recommandons de consulter les [Règles relatives à la collecte des données](/about/data-collection) pour savoir comment les limites de données seront journalisées.
