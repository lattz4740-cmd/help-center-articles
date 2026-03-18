---
title: نصب «کارخواه Outline» در Linux
sidebar_label: نصب «کارخواه Outline» در Linux
---

شروع با «کارخواه Outline» نسخه ۱.۱۵، همه نسخه‌های آتی به‌عنوان بسته‌های Debian برای سیستم‌عامل‌های Linux منتشر خواهد شد. برای اطلاعات بیشتر درباره سیستم‌عامل‌هایی که پشتیبانی می‌کنیم، [حداقل الزامات سیستم](/client/getting-started/system-requirements) ما را بررسی کنید.

## نصب کردن «کارخواه Outline» برای توزیع‌های Linux برپایه Debian (توصیه‌شده)

فرمان‌های زیر را اجرا کنید:

1. کلید مخزن Outline را نصب کنید و مخزن را اضافه کنید.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

‫۲. فهرست بسته apt را به‌روز کنید و جدیدترین نسخه «کارخواه Outline» را نصب کنید.

```
sudo apt update
sudo apt install outline-client
```

برای بررسی یا نصب به‌روزرسانی‌های آینده، فرمان‌های «مرحله ۲» را دوباره اجرا کنید. توجه کنید که به‌روزرسانی خودکار درون‌برنامه‌ای برای «کارخواه Outline» در Linux غیرفعال است و در نسخه ۱.۱۵ شروع می‌شود.

برای نصب «کارخواه Outline»، فرمان‌های زیر را اجرا کنید:

```
sudo apt purge outline-client
```

## گزینه جایگزین

1. جدیدترین بسته Debian را برای «کارخواه Outline» از [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) بارگیری کنید.
2. فرمان‌های زیر را در خط فرمان اجرا کنید تا بسته را نصب کنید

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

‫۳. به‌روزرسانی‌ها را به‌صورت دستی بررسی کنید زیرا به‌روزرسانی خودکار درون‌برنامه‌ای برای «کارخواه Outline» در Linux غیرفعال است و در نسخه ۱.۱۵ شروع می‌شود.

‫۴. برای حذف نصب کردن «کارخواه Outline»، فرمان‌های زیر را در خط فرمان اجرا کنید:

```
sudo apt purge outline-client
```
