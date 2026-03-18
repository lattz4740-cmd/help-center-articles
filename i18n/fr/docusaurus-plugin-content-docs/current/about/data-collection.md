---
title: "Collecte de données et d'informations"
sidebar_label: "Collecte de données et d'informations"
---

Outline ne collecte aucune information personnelle, à moins que vous l'autorisiez à le faire. De même, l'application ne récupère aucune information concernant les sites Web que vous visitez, les utilisateurs avec qui vous communiquez ou les données que vous partagez.

Lorsque vous vous connectez à un compte ou que vous en créez un auprès d'un fournisseur tiers de services cloud depuis Outline Manager, nous ne recueillons aucune des données que vous transmettez à celui-ci (adresse e-mail, nom, informations de facturation et détails du mode de paiement, par exemple).

****Informations collectées automatiquement****

Nous collectons deux types d'informations de manière automatique.

1. Adresse IP du serveur

L'adresse IP du serveur Outline est collectée par [Quay.io](https://quay.io/), qui nous la transmet au moment où le serveur se met automatiquement à jour avec les dernières fonctionnalités et améliorations de sécurité. Cette adresse IP est susceptible de permettre l'identification du fournisseur de serveurs cloud et de la ville dans laquelle le serveur Outline a été configuré, sans pour autant fournir d'indications sur les personnes qui exécutent le serveur ou qui y accèdent.

2. Informations techniques ne permettant pas d'identifier personnellement l'utilisateur

Si Outline plante ou qu'une exception irrécupérable se produit, ou si vous envoyez manuellement des commentaires dans l'application Outline, les informations listées ci-dessous nous sont communiquées. Nous les utilisons uniquement pour identifier les problèmes de stabilité ou de performances et les résoudre.

- Pays
- Paramètres régionaux
- Date et heure du plantage/de l'exception, et jusqu'à 100 des derniers événements (accès d'un utilisateur à la section "À propos", par exemple)
- Messages d'exception compilés de manière statique
- Nom et version du système d'exploitation
- Modèle de téléphone (le cas échéant)
- Heure de démarrage de l'application
- Navigateur
- Architecture
- Version et numéro de version d'Outline

Ces informations sont transmises à l'aide du protocole HTTPS à Sentry ([sentry.io](https://sentry.io/)), un fournisseur tiers Open Source de suivi d'erreurs. À l'aide d'un ensemble de technologies et de services standards, Sentry protège vos données contre les accès, la divulgation et les utilisations non autorisés, et évite leur perte. Pour toute question concernant les règles de Sentry, veuillez consulter [https://sentry.io/security/](https://sentry.io/security/) et [https://sentry.io/privacy/](https://sentry.io/privacy/) ou envoyer un message à l'adresse [security@sentry.io](mailto:security@sentry.io). L'accès à toutes les données Outline stockées par Sentry est limité aux seuls membres de l'équipe Outline.

****Informations collectées uniquement sur acceptation****

Outline communique les informations suivantes à l'équipe Outline après acceptation de l'utilisateur.

1. Métriques d'utilisation

Chaque serveur Outline collecte automatiquement, pendant la dernière heure et par clé d'accès, le nombre d'octets transférés, la durée de la connexion au serveur, les pays et les systèmes autonomes d'origine des identifiants utilisés, ainsi que des informations sur l'activation ou la désactivation de fonctionnalités. Le contenu des communications et les métadonnées permettant d'identifier l'utilisateur (par exemple, les identifiants de connexion, les adresses e-mail et les ID des appareils) ne sont pas consignés. Toutes les métriques sont associées à un ID de serveur. Vous trouverez des instructions permettant de modifier l'ID du serveur sur [cette page](/manager/server-management/reset-server-id).

Par défaut, les serveurs Outline ne partagent pas de métriques avec l'équipe Outline. Si l'administrateur du serveur accepte explicitement de partager des métriques d'utilisation, ces informations sont transmises de façon sécurisée à l'équipe Outline toutes les heures. Au bout de 60 jours, les statistiques d'utilisation sont cumulées à l'échelle nationale. Les administrateurs de serveur peuvent à tout moment modifier leurs préférences en matière de partage des métriques d'utilisation dans les paramètres d'Outline Manager.

Les métriques d'utilisation anonymes que vous nous communiquez nous aident à identifier des tendances d'utilisation et à améliorer le produit.

Par exemple, si l'administrateur d'un serveur autorise le partage de métriques d'utilisation, nous pouvons savoir que le serveur portant l'ID 12345 a été utilisé pendant trois heures la veille et qu'un total de 500 Mo de données a été transféré par son intermédiaire depuis trois clés utilisées chacune au Canada et aux États-Unis, avec la fonctionnalité Limites des données activée.

2. Vos commentaires et votre adresse e-mail, si vous nous envoyez des commentaires

Les applications Outline Manager et Outline vous offrent la possibilité de transmettre des commentaires à l'équipe. Bien qu'il soit conseillé de ne pas fournir d'informations permettant de vous identifier personnellement, vous pouvez nous indiquer votre adresse e-mail si vous souhaitez que notre équipe vous réponde. Nous collectons également des informations de base qui nous permettent de mieux comprendre vos commentaires. Reportez-vous au point 2 de la section "Informations collectées automatiquement" ci-dessus pour savoir quelles données nous collectons. Pour en savoir plus sur les pratiques en matière de sécurité et de confidentialité d'Outline, [cliquez ici](/about/security-and-privacy).

Si vous utilisez une version bêta de l'application Outline sur Android, nous pouvons être amenés à utiliser le service [Firebase](https://firebase.google.com/) de Google pour collecter des informations de débogage susceptibles de nous aider à détecter les problèmes et à améliorer Outline. Pour en savoir plus sur les règles de confidentialité et de sécurité de Firebase, consultez le site Web [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Si vous ne souhaitez pas qu'Outline envoie ces informations par le biais de Firebase, veuillez utiliser la version "Production" de l'application.
