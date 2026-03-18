---
title: "دليلك لتثبيت \"عميل Outline\" على نظام التشغيل Linux"
sidebar_label: "دليلك لتثبيت \"عميل Outline\" على نظام التشغيل Linux"
---

اعتبارًا من الإصدار 1.15 من "عميل Outline"، سيتم إطلاق جميع الإصدارات المستقبلية كحِزم Debian لأنظمة تشغيل Linux. يمكنك مراجعة [الحدّ الأدنى لمتطلبات النظام](/client/getting-started/system-requirements) للحصول على مزيد من المعلومات حول أنظمة التشغيل المتوافقة.

## خطوات تثبيت "عميل Outline" لتوزيعات Linux المستندة إلى Debian (يُنصح به)

يرجى تنفيذ الأوامر التالية:

1. لتثبيت مفتاح مستودع Outline وإضافة المستودع:
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

‫2. لتحديث قائمة حِزم apt وتثبيت أحدث إصدار من "عميل Outline":

```
sudo apt update
sudo apt install outline-client
```

للبحث عن تحديثات مستقبلية أو تثبيتها، عليك تنفيذ الأوامر الواردة في الخطوة 2 مرة أخرى، علمًا بأنّه تمّ إيقاف ميزة التحديث التلقائي لتطبيق "عميل Outline" على Linux بدءًا من الإصدار 1.15.

لإلغاء تثبيت "عميل Outline"، عليك تنفيذ الأمر التالي:

```
sudo apt purge outline-client
```

## خيار بديل

1. يمكنك تنزيل أحدث حزمة Debian لتطبيق"عميل Outline" من خلال هذا الرابط: [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. يُرجى تنفيذ الأوامر التالية في سطر الأوامر لتثبيت الحزمة:

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

‫3. عليك البحث عن التحديثات يدويًا، بما أنّ ميزة التحديث التلقائي لتطبيق "عميل Outline" غير مفعّلة على Linux بدءًا من الإصدار 1.15.

‫4. لإلغاء تثبيت "عميل Outline"، عليك تنفيذ الأمر التالي في سطر الأوامر:

```
sudo apt purge outline-client
```
