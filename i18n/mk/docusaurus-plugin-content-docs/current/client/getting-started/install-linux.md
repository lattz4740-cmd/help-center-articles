---
title: Инсталирање на клиентот Outline на Linux
sidebar_label: Инсталирање на клиентот Outline на Linux
---

Почнувајќи од верзијата 1.15 на клиентот Outline, сите идни верзии ќе се објавуваат како пакети на Debian за оперативните системи Linux. Прегледајте ги нашите [минимални спецификации на системот](/client/getting-started/system-requirements) за повеќе информации за оперативните системи што ги поддржуваме.

## Инсталирајте ја клиент Outline за дистрибуции на Linux засновани на Debian (препорачано)

Извршете ги следниве наредби:

1. Инсталирајте го клучот за складиште на Outline и додајте го складиштето.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Ажурирајте го списокот на apt-пакетот и инсталирајте ја најновата верзија на клиентот Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

За да проверите дали има идни ажурирања или да ги инсталирате, извршете ги наредбите во чекор 2 повторно. Имајте предвид дека, почнувајќи од верзијата 1.15, автоматското ажурирање во апликацијата е оневозможено за клиентот Outline на Linux.

За да ја деинсталирате клиент Outline, извршете ја следнава наредба:

```
sudo apt purge outline-client
```

## Алтернативна опција

1. Преземете го најновиот пакет на Debian за клиентот Outline од [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Извршете ги следниве наредби во линијата за наредби за да го инсталирате пакетот
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Проверувајте за ажурирања рачно бидејќи, почнувајќи од верзијата 1.15, автоматското ажурирање во апликацијата е оневозможено за клиентот Outline на Linux.
4. За да ја деинсталирате клиент Outline, извршете ја следнава наредба во линијата за наредби:
   ```
   sudo apt purge outline-client
   ```
