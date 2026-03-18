---
title: Configuration automatisée de Google Cloud
sidebar_label: Configuration automatisée de Google Cloud
---

## Aperçu

Outline Manager inclut une fonctionnalité qui vous permet de configurer automatiquement le serveur Outline sur un serveur Google Cloud. Si vous décidez d'utiliser cette fonctionnalité, Outline Manager vous invite à vous connecter avec votre compte Google afin d'accorder certaines autorisations [OAuth](https://developers.google.com/identity/protocols/oauth2) à l'installation locale d'Outline Manager pour la configuration de votre compte Google Cloud.

Si vous ne souhaitez pas accorder ces autorisations, vous pouvez suivre les instructions de configuration avancées dans Outline Manager pour exécuter Outline sur Google Cloud Platform.

Autorisations accordées

Pour automatiser la configuration, Outline Manager requiert les autorisations suivantes dans votre compte Google.

## Google Cloud Platform

- Consulter et gérer vos ressources Google Compute Engine
- Consulter vos données dans les services Google Cloud et voir l'adresse e-mail de votre compte Google

## Informations générales sur le compte

- Afficher l'adresse e-mail principale associée à votre compte Google
- Créer une relation entre vous et vos informations personnelles sur Google

## Accès supplémentaire

- Gérer vos projets Cloud Platform
- Consulter et gérer vos comptes de facturation Google Cloud Platform
- Gérer la configuration de vos services Google API

Ces autorisations nous permettent d'utiliser les fonctionnalités avancées avec lesquelles gérer vos serveurs Outline, y compris :

- vous autoriser à sélectionner le compte de facturation approprié ;
- créer un projet pour organiser vos serveurs Outline ;
- répertorier les centres de données disponibles ;
- créer des machines virtuelles pour exécuter Outline ;
- configurer la nouvelle machine virtuelle avec Outline.

## Révoquer les autorisations

Vous pouvez révoquer l'accès à Google Cloud Platform pour Outline Manager en accédant à [Mon compte](https://myaccount.google.com/permissions). Dans ce cas, les serveurs que vous avez créés avec la configuration automatisée continueront de s'exécuter, mais n'apparaîtront plus dans Outline Manager. Pour rétablir leur accès, il vous suffit de vous reconnecter à Google Cloud Platform en lançant le processus de configuration automatisée.

## Organisation du projet Outline

La configuration automatisée de Google Cloud s'appuie sur un seul [projet Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) pour organiser vos serveurs Outline. Le projet est créé lors de la première utilisation de la configuration automatisée, avec une suggestion d'ID de projet qui commence par "Outline" suivi d'une chaîne de caractères aléatoires. Si vous le souhaitez, vous pouvez choisir un autre ID de projet lors de la création. Le projet sera nommé "Serveurs Outline".

## Compte de facturation

Les projets Google Cloud nécessitent un "compte de facturation" associé pour définir les informations de paiement. Lorsque vous utilisez la configuration automatisée de Google Cloud pour la première fois, vous devez fournir un compte de facturation à associer à vos serveurs Outline. Parfois, un serveur s'arrête de fonctionner en raison d'un problème lié au compte de facturation. Dans ce cas, vous devez vous connecter à [Google Cloud Console](https://console.cloud.google.com/), rechercher le projet Google Cloud associé à Outline (nommé "Serveurs Outline") et mettre à jour les paramètres de facturation.

## Détruire des serveurs

Si vous souhaitez détruire les serveurs créés à l'aide de la configuration automatisée, la méthode la plus simple consiste à utiliser Outline Manager. Toutefois, si vous souhaitez les détruire vous-même, vous pouvez vous connecter à [Google Cloud Console](https://console.cloud.google.com/), rechercher le projet créé lors de la configuration initiale (nommé "Serveurs Outline") et y supprimer les ressources ou arrêter le projet.
