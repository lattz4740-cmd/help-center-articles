---
title: "Comment définir des limites de données sur les clés d'accès?"
sidebar_label: "Comment définir des limites de données sur les clés d'accès?"
---

Vous pouvez définir une limite de données qui s'appliquera à toutes les clés d'accès. Pour définir la limite, ouvrez Outline Manager et accédez aux paramètres. Vous verrez alors un commutateur de limite de données qui, lorsqu'il est activé, vous permet de définir une limite.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Une fois la limite définie, vous pouvez voir à quel point chaque utilisateur est proche de la limite sur la page de la clé d'accès, où un graphique à barres indique l'utilisation de données au cours des 30 derniers jours.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

En plus de pouvoir définir une limite pour toutes vos clés d'accès, vous pouvez accorder à chaque clé sa propre limite de données. Ce paramètre remplacera toute limite de données par défaut que vous avez définie, mais si vous n'en avez pas défini, vous pouvez toujours en définir une pour n'importe quelle clé. 

 Pour définir la limite de transfert de données d'une clé, ouvrez Outline Manager, accédez à l'onglet Connexions dans lequel se trouve la clé que vous souhaitez définir, puis cliquez sur le menu situé à droite de la ligne de la clé. De là, cliquez sur Limite de données. Pour modifier la limite de données dans « Ma clé d'accès », cliquez sur l'icône Limite de données ![Icône de limites de données](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Cochez Définir une limite de données personnalisées. Une fois que vous aurez coché cette case, un champ s'affichera dans lequel vous pourrez définir la limite de données personnalisée pour cette clé. Cliquez sur le bouton ENREGISTRER lorsque vous avez terminé pour enregistrer la limite de données.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Une fois que vous aurez enregistré votre limite de transfert de données pour la clé choisie, la limite s'affichera sur l'écran principal, à côté de l'utilisation de données (au cours des 30 derniers jours) pour chaque clé.

Pour retirer la limite de données d'une clé d'accès, accédez à la boîte de dialogue Limite de donnée de la clé comme auparavant, décochez la case intitulée Définir une limite de données personnalisées et cliquez sur le bouton ENREGISTRER.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****FAQ sur les limites de données****

****Qu'est-ce qu'une limite de données glissantes de 30 jours?****

 Une limite de données glissantes de 30 jours additionnera l'utilisation de chaque clé au cours des 30 derniers jours et maintiendra l'utilisation de la clé pendant cette période en dessous de la limite. Par conséquent, la clé ne peut pas dépasser la limite pendant une période de 30 jours, y compris les mois civils de 30 jours ou moins. Cela signifie donc que les données disponibles de chaque utilisateur augmenteront chaque jour de la quantité utilisée par celui-ci il y a 31 jours.

**Pourquoi Outline utilise-t-il des limites glissantes?**

 Les limites glissantes offrent des garanties sur une période de 30 jours, ce qui signifie qu'elles sont plus faciles à configurer qu'une limite récurrente (comme un jour du mois personnalisable) tout en offrant des garanties semblables. Elles correspondent également à l'affichage existant pour l'utilisation des données Outline, ainsi qu'aux outils courants, tels que les services d'analyse et les statistiques du serveur.

**Quelles données sont prises en compte dans une limite de données?**

 La sortie de chaque clé d'accès du serveur est incluse dans le décompte. Proprement dit, cela signifie les données envoyées au nom de la clé à partir du serveur, ainsi que vers le client. En pratique, cela devrait correspondre étroitement au trafic envoyé de la clé au serveur et vice versa. Nous espérons donc que cela correspondra aux décomptes de vos utilisateurs. Nous avons choisi la sortie parce que c'est ce que facturent les fournisseurs de service infonuagique que nous avons interrogés.

**Les utilisateurs seront-ils avertis s'ils dépassent leur limite de données?**

 Pas pour le moment. De nombreux fournisseurs de service infonuagique incluent une limite telle que 1 To pour tout le mois, qui peut prendre en charge 10 utilisateurs avec 100 Go ou 100 utilisateurs avec 10 Go. Ce sont des quantités assez importantes, et nous ne nous attendons pas à ce que de nombreux utilisateurs les atteignent. Nous espérons que les utilisateurs communiqueront avec les gestionnaires de serveurs lorsqu'ils atteindront leur limite. Cependant, nous aimerions avoir votre avis sur la façon dont les notifications pourraient vous aider dans votre cas d'utilisation, et vous pouvez communiquer avec nous [ici](/about/feedback).

**Les utilisateurs seront-ils avertis s'ils s'approchent de leur limite de données?**

 La quantité de nouvelles données qu'un utilisateur s'approchant de sa limite recevra variera de jour en jour, car elle est basée sur son utilisation d'il y a 30 jours. Nous croyons qu'un avertissement est plus susceptible de dérouter les utilisateurs finaux que de les aider. Vous pouvez nous envoyer vos commentaires sur ce comportement [ici](/about/feedback).

**Puis-je réinitialiser l'utilisation de données d'un utilisateur?**

 Non, la limite d'un utilisateur inclut toujours les 30 derniers jours d'utilisation des données. Cependant, vous pouvez augmenter la limite de données de sa clé ou créer une nouvelle clé pour lui.

**Pourquoi certains de mes utilisateurs ont-ils perdu l'accès dès que j'ai activé les limites de données?**

 Les limites de données sont basées sur les 30 derniers jours de transfert de données des utilisateurs, ce qui est enregistré, que les limites de données aient été activées ou non. Il est possible que les utilisateurs concernés aient déjà dépassé la limite avant sa mise en place. Notez également que toutes les limites de données sont appliquées, même lors de la modification de la limite de données d'une seule clé.

**Puis-je définir une limite à l'échelle du serveur, telle que « 1 To tous les 30 jours »?**

 Pas pour le moment. Nous aimerions en savoir plus sur votre cas d'utilisation. Vous pouvez communiquer avec nous [ici](/about/feedback).

**S'il existe une limite de données par défaut et une limite de données sur une clé en particulier, laquelle sera appliquée?**

 La limite de données de la clé en particulier remplacera la limite de données par défaut (le cas échéant) que vous avez définie.

**Puis-je définir une limite de données pour une clé en particulier sans définir de limite de données par défaut?**

 Oui. Vous n'avez pas besoin de définir de limite par défaut pour définir une limite de données sur une clé. Par exemple, vous pouvez définir une limite pour une clé qui, selon vous, peut être largement partagée afin de vous protéger contre un transfert excessif de données au moyen de cette clé.
