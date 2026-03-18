---
title: Як установити Клієнт Outline для ОС Linux
sidebar_label: Як установити Клієнт Outline для ОС Linux
---

Починаючи з версії 1.15, усі версії Клієнта Outline випускатимуться як пакети Debian для операційних систем Linux. Щоб дізнатися більше про підтримувані операційні системи, перегляньте [мінімальні системні вимоги](/client/getting-started/system-requirements).

## Як установити Клієнт Outline для дистрибутивів Linux на базі Debian (рекомендовано)

Виконайте наведені нижче команди.

1. Установіть ключ сховища Outline і додайте це сховище.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Оновіть список пакетів apt й установіть останню версію Клієнта Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Щоб перевірити наявність оновлень або встановити їх, знову виконайте команди з кроку 2. Зверніть увагу: починаючи з версії 1.15, для Клієнта Outline у Linux вимкнено автоматичне оновлення в додатку.

Щоб видалити Клієнт Outline, виконайте наведену нижче команду.

```
sudo apt purge outline-client
```

## Альтернативний варіант

1. Завантажте останній пакет Debian для Клієнта Outline на сторінці [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Щоб установити пакет, виконайте в командному рядку наведені нижче команди.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Перевіряйте наявність оновлень вручну, оскільки, починаючи з версії 1.15, для Клієнта Outline у Linux вимкнено автоматичне оновлення в додатку.
4. Щоб видалити Клієнт Outline, виконайте в командному рядку наведену нижче команду.
   ```
   sudo apt purge outline-client
   ```
