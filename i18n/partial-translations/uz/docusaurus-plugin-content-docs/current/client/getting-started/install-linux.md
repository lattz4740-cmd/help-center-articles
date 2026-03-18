---
title: Linux tizimida Outline Client oʻrnatish
sidebar_label: Linux tizimida Outline Client oʻrnatish
---

Outline Client 1.15 versiyasidan boshlab, barcha kelajakdagi versiyalar Linux operatsion tizimlari uchun Debian paketlari sifatida chiqariladi. Qaysi operatsion tizimlarni dastaklashimiz haqida batafsil axborot olish uchun [minimal tizim talablarimiz](/client/getting-started/system-requirements) bilan tanishib chiqing.

## Debian asosidagi Linux distributivlari uchun Outline Client oʻrnatish (tavsiya etiladi)

Quyidagi buyruqlarni bajaring:

1. Outline ombor kalitini oʻrnating va omborni qoʻshing.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Apt paketlar roʻyxatini yangilang va Outline Client ilovasining eng oxirgi versiyasini oʻrnating.

```
sudo apt update
sudo apt install outline-client
```

Kelgusi yangilanishlarni tekshirish yoki oʻrnatish uchun 2-bosqichdagi buyruqlarni qayta ishga tushiring. Yodda tuting, ilova ichidagi avtomatik yangilash 1.15 versiyasidan boshlab Linux tizimidagi Outline Client uchun faolsizlantirilgan.

Outline Client ilovasini oʻchirib tashlash uchun quyidagi buyruqni bajaring:

```
sudo apt purge outline-client
```

## Muqobil variant

1. Eng yangi Outline Client Debian paketini [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) orqali yuklab oling
2. Paketni oʻrnatish uchun buyruqlar qatorida quyidagi buyruqlarni bajaring

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Yangilanishlarni oddiy usulda tekshiring, chunki ilova ichidagi avtomatik yangilash 1.15 versiyasidan boshlab Linux tizimidagi Outline Client uchun faolsizlantirilgan.

4. Outline Client ilovasini oʻchirib tashlash uchun buyruqlar satrida quyidagi buyruqni bajaring:

```
sudo apt purge outline-client
```
