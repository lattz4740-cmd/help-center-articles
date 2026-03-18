---
title: Installer le client Outline sur Linux
sidebar_label: Installer le client Outline sur Linux
---

À partir de la version 1.15 du client Outline, toutes les prochaines versions seront publiées sous forme de paquets Debian pour les systèmes d'exploitation Linux. Consultez les [configurations système requises](/client/getting-started/system-requirements) pour en savoir plus sur les systèmes d'exploitation compatibles.

## Installer le client Outline pour les distributions Linux basées sur Debian (recommandé)

Exécutez les commandes suivantes :

1. Installez la clé de dépôt d'Outline et ajoutez le dépôt.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Mettez à jour la liste des paquets APT et installez la dernière version du client Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Pour vérifier à l'avenir si des mises à jour sont disponibles et les installer, exécutez à nouveau les commandes de l'étape 2. Notez que la mise à jour automatique dans l'application est désactivée pour le client Outline sur Linux à partir de la version 1.15.

Pour désinstaller le client Outline, exécutez la commande suivante :

```
sudo apt purge outline-client
```

## Autre option

1. Téléchargez le dernier paquet Debian du client Outline sur [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Exécutez les commandes suivantes dans la ligne de commande pour installer le paquet.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Vérifiez manuellement les mises à jour, car la mise à jour automatique dans l'application est désactivée pour le client Outline sur Linux à partir de la version 1.15.
4. Pour désinstaller le client Outline, exécutez la commande suivante dans la ligne de commande :
   ```
   sudo apt purge outline-client
   ```
