---
title: "Pourquoi ne puis-je pas me connecter au service Outline?"
sidebar_label: "Pourquoi ne puis-je pas me connecter au service Outline?"
---

## Plusieurs raisons peuvent expliquer ce problème : {#Internetissues}

- **Votre appareil n'est**[**plus connecté à Internet**](#Internetissues)**.**L'appareil peut parfois perdre sa connexion, et il peut lui falloir un moment pour mettre à jour les icônes réseau. Il se peut aussi que votre appareil soit connecté au réseau local, mais qu'Internet soit en panne.
- **Votre**[**pare-feu réseau bloque l'accès**](#FirewallIssues)**à votre serveur Outline.**Ce problème est courant sur les réseaux publics, comme celui d'un établissement scolaire ou d'une entreprise, ou un réseau sans fil gratuit.
- **Votre appareil est doté d'un**[**pare-feu ou d'un antivirus**](#SoftwareIssues)**qui bloque l'accès à votre serveur Outline.**
- **Vous devez peut-être modifier les**[**paramètres de votre téléphone**](#DeviceSettings)**.**
- **Votre gestionnaire de service a peut-être**[**supprimé le serveur ou votre FAI bloque peut-être votre demande**](#ServerIssues)**.**

Problèmes de connexion Internet :

### À tester :
Désactivez le serveur Outline et vérifiez si votre connexion Internet est rétablie.

- Si oui, consultez les autres options de dépannage ci-dessous.
- Si ce n'est pas le cas, attendez quelques instants pour voir si vos paramètres de connexion se mettent à jour.

### À corriger :

## Reconnectez votre appareil à Internet : {#FirewallIssues}

1. Vérifiez si d'autres appareils peuvent se connecter au même réseau. Si ce n'est pas le cas, il est possible que le réseau soit en panne. Vous devrez alors patienter jusqu'à ce que la connexion soit rétablie ou bien résoudre le problème.
2. Si d'autres appareils peuvent se connecter au même réseau, vous pouvez essayer une ou plusieurs des opérations suivantes pour rétablir la connexion :
   1. Mettre l'appareil en mode Avion (mobile)
   2. Redémarrer l'appareil
   3. Éteindre l'appareil, patienter deux minutes, puis le rallumer

Problèmes liés au pare-feu réseau :

### À tester :

1. Déconnectez-vous de votre réseau Wi-Fi ou filaire actuel.
:::note
2. Connectez-vous à un autre réseau, par exemple un réseau cellulaire.
:::
3. Essayez de vous reconnecter au serveur Outline.

Si vous parvenez à vous connecter au serveur à partir d'un autre réseau, vous avez trouvé l'origine du problème.

### À corriger :
Demandez à votre gestionnaire de service d'autoriser l'accès à votre serveur Outline ou bien continuez d'utiliser l'autre réseau.

Problèmes liés à un pare-feu ou un antivirus :

### À tester :

Essayez de vous connecter à Outline à partir d'un autre appareil.

Remarque : Vous aurez besoin d'une clé d'accès et de l'application Outline pour utiliser Outline sur un autre appareil.

### À corriger :

Vérifiez que les paramètres de votre pare-feu ou de votre antivirus sont configurés pour autoriser le trafic VPN et Outline.

Paramètres de l'appareil :

## À vérifier : {#SoftwareIssues}
## Sur Android : {#DeviceSettings}

1. Ouvrez l'application Paramètres.
2. Recherchez les **paramètres VPN** sur votre appareil. Vous y verrez toutes les applications VPN actuellement autorisées sur votre téléphone.
3. Si Outline n'apparaît pas dans les paramètres VPN, désinstallez et réinstallez l'application. Une fois l'application Outline installée, l'appareil devrait lui accorder automatiquement les accès nécessaires.

Vérifiez qu'aucune application en mode superposition d'écran n'est installée sur votre appareil Android : elle pourrait masquer la fenêtre des autorisations d'Outline au premier plan en l'affichant en arrière-plan.

Sur votre appareil Android, accédez à Paramètres > Applications > Accès spéciaux des applis. Appuyez ensuite sur "Superposition sur d'autres applis". Vous pouvez alors supprimer l'accès à toute application autorisant ce comportement.

Sur iOS : consultez [cet article d'aide](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Problèmes liés au serveur : {#ServerIssues}

### À tester:

### Si vous avez accès à plusieurs serveurs, essayez-en un autre.

### À corriger :
Contactez votre gestionnaire de service pour savoir si le serveur a été supprimé. Si c'est le cas, demandez-lui de vous fournir une [clé d'accès](/about/terminology) à un autre serveur.

Si vous avez configuré le serveur, essayez de vous y connecter depuis Outline Manager ou via une autre méthode, par exemple [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Si cela ne fonctionne pas, vous pouvez essayer d'accéder à la console du fournisseur de services cloud, le cas échéant, pour vérifier si le serveur est toujours en ligne.
