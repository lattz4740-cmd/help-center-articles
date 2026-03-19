---
title: "Comment fixer des limites de données pour les clés d'accès ?"
sidebar_label: "Comment fixer des limites de données pour les clés d'accès ?"
---

Vous pouvez fixer une limite de données pour l'ensemble de vos clés d'accès. Pour ce faire, ouvrez Outline Manager et accédez aux paramètres. Vous y trouverez le bouton "Limites de données", qui vous permet de fixer une limite lorsque vous l'activez.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Une fois la limite fixée, vous pouvez suivre la consommation de chaque utilisateur sur la page de la clé d'accès, où un graphique à barres indique la consommation de données au cours des 30 derniers jours.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Outre la possibilité de fixer une limite pour l'ensemble de vos clés d'accès, vous pouvez doter chaque clé de sa propre limite. Ce paramètre prime sur toute limite de données définie par défaut. Il convient de noter qu'il est possible d'appliquer une limite de données à une clé en particulier même si aucune limite par défaut n'a été définie.

 Pour fixer la limite de transfert de données d'une clé, ouvrez Outline Manager, accédez à l'onglet "Connexions" qui contient la clé que vous souhaitez configurer, puis cliquez sur le menu situé à droite de la ligne correspondant à la clé. Ensuite, cliquez sur "Limite de données". Pour changer la limite de données dans "Ma clé d'accès", cliquez sur l'icône correspondante ![Icône Limites des données](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Sélectionnez "Définir une limite de données personnalisée". Une fois que vous avez coché cette case, un champ s'affiche et vous permet de définir une limite de données personnalisée pour cette clé. Lorsque vous avez terminé, cliquez sur le bouton ENREGISTRER pour sauvegarder la limite de données.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Une fois que vous avez enregistré la limite de transfert de données pour une clé, elle s'affiche sur l'écran principal, à côté de la consommation de données (au cours des 30 derniers jours) pour chaque clé.

Pour supprimer la limite de données d'une clé d'accès, accédez à la boîte de dialogue "Limite de données" de la clé comme précédemment, décochez la case "Définir une limite de données personnalisée" et cliquez sur le bouton ENREGISTRER.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## **Questions fréquentes sur les limites de données**
## **Qu'est-ce qu'une limite de données sur 30 jours glissants ?**
 Une limite de données sur 30 jours glissants additionne l'utilisation de chaque clé au cours des 30 derniers jours et maintient les valeurs en dessous de la limite au cours de cette période. Ainsi, la clé ne peut pas dépasser la limite pendant toute période de 30 jours, y compris les mois calendaires de 30 jours ou moins. Cela signifie que la quantité de données disponible pour chaque utilisateur augmente chaque jour selon la quantité utilisée 31 jours avant.

## Pourquoi Outline fixe-t-il des limites glissantes ?
 Les limites de ce type fournissent des garanties sur des périodes de 30 jours. Elles sont donc plus simples à configurer qu'une limite récurrente (telle qu'un jour du mois personnalisable) tout en offrant des garanties similaires. Elles correspondent également à l'affichage existant pour l'utilisation des données Outline, ainsi qu'aux outils courants tels que les services d'analyse et les statistiques de serveur.

## Quelles sont les données prises en compte dans la limite ?
 Le trafic sortant de chaque clé d'accès du serveur est comptabilisé. À proprement parler, il s'agit des données envoyées au nom de la clé depuis le serveur, ainsi que vers le client. Dans la pratique, elles sont liées au trafic envoyé depuis la clé vers le serveur et inversement. Nous espérons donc que les chiffres correspondront aux résultats de vos utilisateurs. Nous avons choisi le trafic sortant, car c'est ce que facturent les fournisseurs de services cloud que nous avons interrogés.

## Les utilisateurs recevront-ils une notification en cas de dépassement de la limite de données ?
 Pas pour le moment. De nombreux fournisseurs de services cloud incluent une limite de 1 To par mois, pouvant accueillir 10 utilisateurs avec 100 Go ou 100 utilisateurs avec 10 Go. Il s'agit de chiffres assez élevés, et nous ne pensons pas que les utilisateurs les atteindront facilement. Nous espérons que les utilisateurs contacteront les administrateurs des serveurs lorsqu'ils atteindront leur limite. Mais si vous souhaitez nous expliquer en quoi les notifications peuvent vous être utiles, nous vous invitons à [nous contacter.](/about/feedback)

## Les utilisateurs recevront-ils une notification s'ils approchent de leur limite de données ?
 La quantité de nouvelles données que reçoit un utilisateur approchant de sa limite varie d'un jour à l'autre, car elle est calculée en fonction de sa consommation 30 jours auparavant. Nous pensons qu'un avertissement risque de perturber les utilisateurs finaux plutôt que de les aider. Toutefois, vous pouvez [nous contacter](/about/feedback) pour nous faire part de vos commentaires à ce sujet.

## Puis-je réinitialiser la consommation des données d'un utilisateur ?
 Non, la limite d'un utilisateur comprend toujours les données consommées au cours des 30 derniers jours. Cependant, vous pouvez relever la limite de données de sa clé ou lui créer une nouvelle clé.

## Pourquoi certains de mes utilisateurs ont-ils perdu leur accès dès que j'ai activé les limites de données ?
 Les limites sont calculées en fonction des données transférées par les utilisateurs au cours des 30 derniers jours. Ces informations sont automatiquement enregistrées, même si les limites ne sont pas activées. Les utilisateurs en question avaient probablement dépassé la limite avant qu'elle ne soit mise en place. Sachez également que toutes les limites de données sont appliquées, même lorsque vous modifiez une limite individuelle.

## Puis-je définir une limite pour l'ensemble du serveur, par exemple "1 To pour 30 jours" ?
 Pas pour le moment, mais nous aimerions beaucoup en savoir plus sur votre cas d'utilisation. N'hésitez pas à [nous contacter.](/about/feedback)

## S'il existe une limite de données par défaut ainsi qu'une limite individuelle pour une clé donnée, laquelle est appliquée ?
 Les limites individuelles priment sur toute limite de données par défaut.

## Puis-je fixer une limite individuelle en l'absence de limite de données par défaut ?
 Oui, vous n'avez pas besoin d'avoir une limite de données par défaut pour fixer une limite individuelle pour une clé donnée. Par exemple, vous pouvez fixer une limite pour une clé dont vous craignez le partage à grande échelle afin d'empêcher qu'une quantité excessive de données ne soient transférées par son intermédiaire.
