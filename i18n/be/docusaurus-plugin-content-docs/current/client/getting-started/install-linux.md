---
title: Усталяванне Outline Client для Linux
sidebar_label: Усталяванне Outline Client для Linux
---

Пачынаючы з Outline Client 1.15, усе будучыя версіі будуць выпускацца як пакеты Debian для аперацыйных сістэм Linux. Каб даведацца, якія аперацыйныя сістэмы падтрымліваюцца, азнаёмцеся з нашымі [мінімальнымі сістэмнымі патрабаваннямі](/client/getting-started/system-requirements).

## Усталяванне Outline Client для дыстрыбутываў Linux на базе Debian (рэкамендуецца)

Выканайце наступныя каманды:

1. Усталюйце ключ сховішча Outline і дадайце сховішча.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Абнавіце спіс пакетаў apt і ўсталюйце апошнюю версію Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Каб праверыць наяўнасць абнаўленняў або ўсталяваць іх у будучыні, зноў выканайце каманды, указаныя ў кроку 2. Звярніце ўвагу, што аўтаматычнае абнаўленне ў праграме адключана для Outline Client на Linux, пачынаючы з версіі 1.15.

Каб выдаліць Outline Client, выканайце наступную каманду:

```
sudo apt purge outline-client
```

## Альтэрнатыўны варыянт

1. Спампуйце апошнюю версію пакета Debian для Outline Client з сайта [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Для ўсталявання пакета выканайце наступныя каманды

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Праверце наяўнасць абнаўленняў уручную, бо аўтаматычнае абнаўленне ў праграме Outline Client для Linux адключана, пачынаючы з версіі 1.15.

4. Каб выдаліць Outline Client, выканайце наступную каманду:

```
sudo apt purge outline-client
```
