---
title: "Sécurité et confidentialité lors de l'utilisation d'Outline"
sidebar_label: "Sécurité et confidentialité lors de l'utilisation d'Outline"
---

Sécurité et confidentialité lors de l'utilisation d'Outline

## Comment Outline protège vos communications en ligne

Le trafic Internet est particulièrement vulnérable à la surveillance lorsqu'il transite sur votre réseau local ou national.

Outline contribue à la confidentialité de vos communications en chiffrant votre trafic Internet lors de son transit sur votre réseau national, jusqu'à son arrivée sur le serveur Outline. Quand Outline chiffre votre trafic, les observateurs du réseau n'ont aucun moyen de savoir quels sites Web vous consultez ou quelles informations vous transférez.

Outline peut également vous redonner accès à des outils de communication sécurisée de bout en bout, qui ne seraient peut-être pas disponibles sans cela dans votre pays.

## Normes de chiffrement

Outline chiffre les communications entre votre appareil et le serveur Outline à l'aide de l'algorithme AEAD 256 bits Chacha2020 IETF Poly 1305. Les algorithmes de chiffrement AEAD offrent confidentialité, intégrité et authenticité, et affichent d'excellentes performances sur le matériel moderne.

## Audits de sécurité

En 2018, Outline a été contrôlé par Radically Open Security et Cure53, deux organisations de sécurité numérique indépendantes qui jugent les logiciels selon les normes de sécurité les plus récentes. Radically Open Security a mené un audit supplémentaire en 2022, et Cure53 a audité le SDK Outline en 2024. Vous pouvez consulter les rapports ici :

- [Rapport sur le test d'intrusion réalisé par Radically Open Security (mars 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Rapport sur le test d'intrusion réalisé par Cure53 et rapport d'audit sur Jigsaw Outline (décembre 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Rapport sur le test d'intrusion réalisé par Radically Open Security (décembre 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Rapport sur le test d'intrusion réalisé par Cure53 sur le SDK Jigsaw Outline VPN (janvier 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Métriques et journaux anonymes

Outline analyse la bande passante utilisée, qu'il évalue en "octets transférés" par clé d'accès. Grâce à cette information, les administrateurs de serveur peuvent ajuster la bande passante souscrite auprès de leur fournisseur de serveurs cloud en fonction de leurs besoins, mais ils n'ont pas accès aux données qui transitent par le serveur Outline.

Découvrez quelles sont les [données et informations collectées](/about/data-collection) par Outline.

---

## Questions fréquentes sur la sécurité et la confidentialité

## Outline peut-il me rendre anonyme en ligne ?

Non. Outline n'est pas un outil d'anonymisation. Outline protège votre vie privée des éventuels observateurs du réseau.

Outline ne vous garantit pas une anonymisation complète sur les sites Web que vous visitez, car ces derniers peuvent toujours vous identifier si vous vous y connectez, ou par d'autres techniques telles que les empreintes numériques de navigateur. Quant aux applications mobiles, sur les tout derniers smartphones, elles ont accès à des API qui leur permettent de vous localiser à l'aide du GPS intégré, sans passer par votre proxy.

De manière générale, les VPN offrent des protections significatives, notamment en ce qui concerne la surveillance sur Internet, mais ils ne peuvent pas prévenir tous les risques liés aux opérations en ligne. Même si vous utilisez un VPN, un FAI connaissant déjà votre identité et pouvant observer votre trafic réseau sera éventuellement en mesure de déterminer l'adresse IP de votre serveur Outline. Muni de cette information, il pourra bloquer votre accès au serveur Outline ou déterminer vos habitudes d'utilisation (les moments où vous êtes en ligne) et votre position approximative.

## Quelqu'un peut-il savoir que j'utilise Outline ?

C'est possible. Les plates-formes et les services auxquels vous accéderez seront certainement en mesure de déterminer que votre connexion provient d'un serveur cloud. Dans certains cas, ils pourront en déduire que vous utilisez un VPN, mais ils ne pourront pas connaître le contenu de votre trafic Internet.

## Outline me protège-t-il de toutes les cybermenaces possibles ?

Non. Aucun outil ne peut vous protéger de toutes les cybermenaces. Outline vous donne accès à l'Internet public et renforce la confidentialité de vos communications en chiffrant votre trafic, mais nous vous recommandons de prendre des précautions supplémentaires pour vous protéger des autres types d'attaques, tels que les logiciels malveillants et l'hameçonnage.

Si vous souhaitez renforcer votre sécurité en ligne, demandez conseil aux spécialistes en cybersécurité de votre organisation. Vous pourrez également profiter de l'assistance personnalisée des experts en sécurité de [Security Planner](https://securityplanner.org/), un site Web conçu pour vous fournir des instructions claires qui vous aideront à choisir des outils de cybersécurité adaptés à vos besoins.

Vous pouvez également vous renseigner sur les autres produits de cybersécurité de [Jigsaw](https://jigsaw.google.com/), tels que [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) et [Alerte mot de passe](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Est-ce légal d'utiliser un VPN ?

Avant d'utiliser Outline ou l'application, veillez à consulter les lois et règlements locaux, ainsi que les conditions d'utilisation du fournisseur de services cloud auquel vous comptez faire appel.
