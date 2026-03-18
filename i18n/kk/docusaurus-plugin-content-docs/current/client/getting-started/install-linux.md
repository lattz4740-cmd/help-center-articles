---
title: Outline клиентін Linux жүйесіне орнату
sidebar_label: Outline клиентін Linux жүйесіне орнату
---

Outline клиенті 1.15 нұсқасынан бастап барлық алдағы нұсқа Linux операциялық жүйелеріне арналған Debian пакеттері ретінде шығарылады. Біз қолдайтын операциялық жүйелер туралы қосымша ақпарат алу үшін [минималды жүйелік талаптарымызды](/client/getting-started/system-requirements) қараңыз.

## Debian-ға арналған Linux дистрибутивтері үшін Outline клиентін орнатыңыз (ұсынылады).

Мына пәрмендерді орындаңыз:

1. Outline-ның қойма кілтін орнатып, қойманы қосыңыз.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. "Жетілдірілген пакет құралы" пакетінің тізімін жаңартыңыз және Outline клиентінің соңғы нұсқасын орнатыңыз.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Алдағы жаңартуларды тексеру немесе орнату үшін 2-қадамдағы пәрмендерді қайта орындаңыз. Linux жүйесіндегі Outline клиенті үшін қолданбадағы автоматты жаңарту 1.15 нұсқасынан бастап өшірілгенін ескеріңіз.

Outline клиентін жою үшін мына пәрменді орындаңыз:

```
sudo apt purge outline-client
```

## Балама опция

1. Debian пакетіне арналған соңғы Outline клиентін жүктеп алыңыз: [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Пакетті орнату үшін пәрмен жолындағы мына пәрмендерді орындаңыз.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Linux жүйесіндегі Outline клиенті үшін қолданбадағы автоматты жаңарту 1.15 нұсқасынан бастап өшірілгендіктен, жаңартуларды қолмен тексеріңіз.
4. Outline клиентін жою үшін пәрмен жолындағы мына пәрменді орындаңыз:
   ```
   sudo apt purge outline-client
   ```
