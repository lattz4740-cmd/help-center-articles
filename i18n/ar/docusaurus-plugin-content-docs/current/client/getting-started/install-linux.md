---
title: "كيف أثبت تطبيق \"عميل Outline\" على أجهزة Linux؟"
sidebar_label: "كيف أثبت تطبيق \"عميل Outline\" على أجهزة Linux؟"
---

اعتبارًا من الإصدار 1.15 من تطبيق "عميل Outline"، ستصدُر جميع الإصدارات المستقبلية كحِزم Debian لأنظمة التشغيل Linux. يمكنك مراجعة [الحدّ الأدنى لمتطلبات النظام](/client/getting-started/system-requirements) للحصول على مزيد من المعلومات حول أنظمة التشغيل المتوافقة.

## تثبيت تطبيق "عميل Outline" لتوزيعات Linux المستنِدة إلى Debian (يُنصح به)

يرجى تنفيذ الأوامر التالية:

1. ثبِّت مفتاح مستودع Outline وأضِف المستودع.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. حدِّث قائمة حِزم apt وثبِّت أحدث إصدار من "عميل Outline".
   ```
   sudo apt update
   sudo apt install outline-client
   ```

للبحث عن تحديثات مستقبلية أو تثبيتها، نفِّذ الأوامر الواردة في الخطوة 2 مرة أخرى، علمًا بأنّه تمّ إيقاف ميزة التحديث التلقائي داخل تطبيق "عميل Outline" على نظام التشغيل Linux بدءًا من الإصدار 1.15.

لإلغاء تثبيت تطبيق "عميل Outline"، نفِّذ الأمر التالي:

```
sudo apt purge outline-client
```

## خيار بديل

1. نزِّل أحدث حزمة Debian لتطبيق"عميل Outline" من خلال هذا الرابط: [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. نفِّذ الأوامر التالية في سطر الأوامر لتثبيت الحزمة:
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. ابحث عن التحديثات يدويًا، بما أنّ ميزة التحديث التلقائي داخل تطبيق "عميل Outline" غير مفعّلة على نظام التشغيل Linux بدءًا من الإصدار 1.15.
4. لإلغاء تثبيت تطبيق "عميل Outline"، نفِّذ الأمر التالي في سطر الأوامر:
   ```
   sudo apt purge outline-client
   ```
