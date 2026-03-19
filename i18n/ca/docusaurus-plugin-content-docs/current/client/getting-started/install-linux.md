---
title: "Instal·lar el client d'Outline a Linux"
sidebar_label: "Instal·lar el client d'Outline a Linux"
---

A partir de la versió 1.15 del client d'Outline, totes les versions futures es llançaran com a paquets per a Debian per a sistemes operatius Linux. Revisa els nostres [requisits mínims del sistema](/client/getting-started/system-requirements) per obtenir més informació sobre quins sistemes operatius admetem.

## Instal·lar el client d'Outline per a distribucions de Linux basades en Debian (opció recomanada)

Executa les ordres següents:

1. Instal·la la clau del repositori d'Outline i afegeix el repositori.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Actualitza la llista de paquets d'apt i instal·la la darrera versió del client d'Outline.

```
sudo apt update
sudo apt install outline-client
```

Per cercar o instal·lar futures actualitzacions, torna a executar les ordres del pas 2. Tingues en compte que l'actualització automàtica des de l'aplicació està desactivada per al client d'Outline a Linux a partir de la versió 1.15.

Per desinstal·lar el client d'Outline, executa l'ordre següent:

```
sudo apt purge outline-client
```

## Opció alternativa

1. Baixa el paquet per a Debian del client d'Outline més recent des de [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Executa les ordres següents a la línia d'ordres per instal·lar el paquet.

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Comprova manualment si hi ha actualitzacions, ja que l'actualització automàtica des de l'aplicació està desactivada per al client d'Outline a Linux a partir de la versió 1.15.

4. Per desinstal·lar el client d'Outline, executa l'ordre següent a la línia d'ordres:

```
sudo apt purge outline-client
```
