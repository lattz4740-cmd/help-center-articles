---
title: Как установить клиент Outline на компьютерах с ОС Linux
sidebar_label: Как установить клиент Outline на компьютерах с ОС Linux
---

Начиная с Outline 1.15, все будущие версии будут выпускаться как пакеты Debian для ОС Linux. Чтобы узнать, какие операционные системы поддерживаются, изучите наши [минимальные системные требования](/client/getting-started/system-requirements).

## Установка клиента Outline для дистрибутивов Linux на базе Debian (рекомендуется)

Выполните следующие команды:

1. Установите ключ репозитория Outline и добавьте репозиторий.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Обновите список пакетов apt и установите последнюю версию клиента Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Чтобы в будущем проверять наличие обновлений или устанавливать их, выполняйте команды, указанные в шаге 2. Обратите внимание, что автоматическое обновление для клиента Outline отключено в Linux, начиная с версии 1.15.

Чтобы удалить клиент Outline, выполните следующую команду:

```
sudo apt purge outline-client
```

## Альтернативный вариант

1. Скачайте последний пакет Debian клиента Outline по ссылке [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Чтобы установить пакет, выполните в командной строке указанные ниже команды.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Проверьте наличие обновлений вручную, поскольку автоматическое обновление для клиента Outline отключено в Linux, начиная с версии 1.15.
4. Чтобы удалить клиент Outline, выполните следующую команду:
   ```
   sudo apt purge outline-client
   ```
