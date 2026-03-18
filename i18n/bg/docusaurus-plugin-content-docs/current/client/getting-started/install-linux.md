---
title: Инсталиране на клиента за Outline под Linux
sidebar_label: Инсталиране на клиента за Outline под Linux
---

От версия 1.15 на клиента за Outline всички бъдещи версии ще се публикуват като пакети за Debian за операционните системи Linux. За повече информация относно поддържаните от нас операционни системи прегледайте [минималните системни изисквания](/client/getting-started/system-requirements).

## Инсталиране на клиента за Outline за дистрибуции на Linux, базирани на Debian (препоръчително)

Изпълнете следните команди:

1. Инсталирайте ключа за хранилището на Outline и добавете хранилището.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Актуализирайте списъка с пакети на apt и инсталирайте най-новата версия на клиента за Outline.

```
sudo apt update
sudo apt install outline-client
```

За да проверите за бъдещи актуализации или да ги инсталирате, изпълнете отново командите от стъпка 2. Обърнете внимание, че автоматичното актуализиране в приложението е деактивирано за клиента за Outline под Linux от версия 1.15 нататък.

За да деинсталирате клиента за Outline, изпълнете следната команда:

```
sudo apt purge outline-client
```

## Алтернативна опция

1. Изтеглете най-новия пакет за Debian за клиента за Outline от [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Изпълнете следните команди в командния ред, за да инсталирате пакета

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Проверявайте ръчно за актуализации, тъй като автоматичното актуализиране в приложението е деактивирано за клиента за Outline под Linux от версия 1.15 нататък.

4. За да деинсталирате клиента за Outline, изпълнете следната команда в командния ред:

```
sudo apt purge outline-client
```
