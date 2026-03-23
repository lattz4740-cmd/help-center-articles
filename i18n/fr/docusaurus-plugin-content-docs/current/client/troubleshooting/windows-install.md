---
title: "Pourquoi ne puis-je pas installer le client Outline sur Windows ?"
sidebar_label: "Pourquoi ne puis-je pas installer le client Outline sur Windows ?"
---

Ce message d'erreur apparaît parfois : "Désolé, il semble qu'Outline ne soit pas correctement installé. Veuillez relancer l'installation. Si le problème persiste, [transmettez vos commentaires](/about/feedback) par le biais de l'application."

Si vous utilisez Outline sous Windows, vous risquez de rencontrer de temps à autre une erreur inattendue. Le plus souvent, il suffit de supprimer l'adaptateur (pilote) Outline TAP et de réinstaller Outline.

La procédure peut varier selon la version de votre système d'exploitation Windows, mais vous trouverez ci-dessous des instructions générales pour désinstaller l'adaptateur TAP et Outline, puis réinstaller Outline.

1. Désinstaller l'adaptateur TAP pour le client Outline
   1. Ouvrez le **Gestionnaire de périphériques**, puis développez la liste des **Cartes réseau**.
   2. Recherchez **TAP-Windows Adapter V9** ou l'adaptateur TAP associé à Outline.
   3. Désinstallez ou supprimez cet adaptateur. Notez que cette opération peut affecter les autres applications VPN que vous avez installées.
2. Désinstaller le client Outline
   1. Accédez à **Programmes et fonctionnalités**, puis cliquez sur **Désinstaller un programme**.
   2. Recherchez l'application du client Outline et supprimez-la.
   3. [Téléchargez la dernière version du client Outline](https://getoutline.org/get-started/#step-3) et installez-la sur votre appareil Windows. Cela devrait installer automatiquement un nouvel adaptateur TAP.

Si le problème persiste, [contactez l'assistance](/about/feedback).
