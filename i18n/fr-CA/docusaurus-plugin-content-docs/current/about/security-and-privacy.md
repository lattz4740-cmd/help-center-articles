---
title: "Sécurité et confidentialité lors de l'utilisation d'Outline"
sidebar_label: "Sécurité et confidentialité lors de l'utilisation d'Outline"
---

Sécurité et confidentialité lors de l'utilisation d'Outline

## Comment Outline protège vos communications en ligne

Le trafic Internet est le plus vulnérable à la surveillance lorsqu'il transite par votre réseau local ou national.

Outline protège la confidentialité de vos communications en chiffrant votre trafic Internet lorsqu'il transite à l'intérieur de votre réseau national, et le maintient chiffré jusqu'à son arrivée sur le serveur Outline. Lorsque votre trafic est chiffré avec Outline, les observateurs réseau ne peuvent pas voir les sites que vous consultez ni accéder aux informations que vous échangez.

Outline peut également vous aider à retrouver l'accès à des outils de communication sécurisés de bout en bout qui pourraient autrement être inaccessibles dans votre pays.

## Normes de chiffrement

Outline chiffre les communications entre vos appareils et le serveur Outline à l'aide des algorithmes de chiffrement AEAD 256 bits Chacha2020 IETF Poly 1305. Ces algorithmes AEAD offrent confidentialité, intégrité et authenticité, et sont aussi particulièrement performants sur les équipements informatiques récents.

## Audits de sécurité

En 2018, Outline a été audité par Radically Open Security et Cure53, deux organisations indépendantes spécialisées en sécurité numérique, qui ont évalué le logiciel selon les normes de sécurité les plus récentes. Radically Open Security a réalisé un audit additionnel en 2022, et Cure53 a mené un audit de la trousse SDK Outline en 2024. Vous pouvez lire les rapports ici :

- [Rapport de test d'intrusion de Radically Open Security (mars 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Rapport de test d'intrusion et d'audit de Cure53 sur Jigsaw Outline (décembre 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Rapport de test d'intrusion de Radically Open Security (décembre 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Rapport de test d'intrusion de Cure53 sur la trousse SDK du RPV Jigsaw Outline (janvier 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Mesures anonymes et journaux

Outline suit la quantité de bande passante utilisée en enregistrant les « octets transférés » pour chaque clé d'accès. Ces informations permettent aux administrateurs de serveur d'ajuster leur abonnement de bande passante auprès de leur fournisseur de nuage si nécessaire, sans toutefois leur donner accès aux données transitant par le serveur Outline.

Apprenez-en plus sur la [collecte des données et des informations](/about/data-collection) de Outline.

---

## FAQ sur la sécurité et la confidentialité

## Outline peut-il me rendre anonyme en ligne?

Non, Outline n'est pas un outil d'anonymat. Outline protège votre confidentialité contre d'éventuels observateurs réseau.

Outline ne garantit pas un anonymat complet sur les sites que vous visitez, car ceux-ci peuvent toujours vous identifier lorsque vous vous connectez ou au moyen de certaines techniques, comme le pistage par empreinte numérique unique du navigateur. Quant aux applis mobiles, la plupart des téléphones intelligents disposent d'API permettant aux applis installées d'accéder à votre position indépendamment du mandataire, en s'appuyant sur le GPS intégré.

De manière générale, les RPV offrent une protection essentielle, notamment contre la surveillance en ligne, mais opérer sur Internet comporte toujours des risques. Même avec un RPV, si un FAI connaît déjà votre identité et peut observer votre trafic réseau, il pourrait identifier l'adresse IP de votre serveur Outline. Ces informations peuvent être utilisées pour bloquer l'accès au serveur Outline ou analyser vos habitudes d'utilisation, comme vos heures de connexion habituelles et, potentiellement, votre position approximative.

## Peut-on savoir si j'utilise Outline?

Possiblement. Les plateformes et services que vous consultez pourront probablement détecter que votre connexion provient d'un fournisseur de nuage. Dans certains cas, ils pourront en déduire que vous utilisez un RPV, mais ils ne pourront pas voir le contenu de votre trafic Internet.

## Outline me protège-t-il de toutes les cybermenaces?

Non. Aucun outil ne peut vous protéger contre toutes les cybermenaces. Outline vous permet d'accéder à un Internet ouvert et renforce votre confidentialité en chiffrant votre trafic. Toutefois, nous vous recommandons de prendre des précautions additionnelles pour vous protéger contre d'autres types d'attaques, comme les logiciels malveillants et l'hameçonnage.

Pour renforcer votre protection en ligne, nous vous recommandons de consulter l'expert en cybersécurité de votre organisation. Vous pouvez également obtenir des conseils personnalisés auprès des spécialistes en sécurité de [Security Planner](https://securityplanner.org/), un site Web conçu pour vous offrir des recommandations claires et adaptées afin de choisir les meilleurs outils de cybersécurité en fonction de vos besoins.

Vous pouvez également découvrir les autres produits de cybersécurité de [Jigsaw](https://jigsaw.google.com/), comme [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) et [Alerte mot de passe](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Est-ce légal d'utiliser un RPV?

Avant d'utiliser Outline ou l'appli, veuillez vérifier la législation et les règlements locaux en vigueur dans votre pays, ainsi que les conditions d'utilisation du fournisseur de nuage que vous envisagez d'utiliser.
