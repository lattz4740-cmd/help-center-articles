---
title: "Инсталирање Outline Client-а на Linux-у"
sidebar_label: "Инсталирање Outline Client-а на Linux-у"
---

Почев од верзије 1.15 Outline клијента, све будуће верзије биће објављене као Debian пакети за Linux оперативне системе. Више информација о томе које оперативне системе подржавамо потражите у [минималним системским захтевима](/client/getting-started/system-requirements).

## Инсталирајте Outline клијент за Linux дистрибуције засноване на Debian-у (препоручено)

Покрените следеће команде:

1. Инсталирајте кључ Outline складишта и додајте складиште.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Ажурирајте листу apt пакета и инсталирајте најновију верзију Outline клијента.

```
sudo apt update
sudo apt install outline-client
```

Да бисте потражили или инсталирали будућа ажурирања, поново покрените команде из 2. корака. Имајте на уму да је аутоматско ажурирање у апликацији онемогућено за Outline клијент на Linux-у почев од верзије 1.15.

Да бисте деинсталирали Outline клијент, покрените следећу команду:

```
sudo apt purge outline-client
```

## Алтернативна опција

1. Преузмите најновији Debian пакет за Outline клијент са [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Покрените следеће команде на командној линији да бисте инсталирали пакет

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Ручно проверите да ли постоје ажурирања, јер је аутоматско ажурирање у апликацији онемогућено за Outline клијент на Linux-у од верзије 1.15.

4. Да бисте деинсталирали Outline клијент, покрените следећу команду на командној линији:

```
sudo apt purge outline-client
```
