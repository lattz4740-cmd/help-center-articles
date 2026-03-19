---
title: ‫Outline کلائنٹ کو Linux پر انسٹال کرنا
sidebar_label: ‫Outline کلائنٹ کو Linux پر انسٹال کرنا
---

‫Outline کلائنٹ ورژن 1.15 سے، تمام مستقبل کے ورژنز Linux آپریٹنگ سسٹمز کے لیے Debian پیکیجز کے طور پر ریلیز کیے جائیں گے۔ ہم کن آپریٹنگ سسٹمز کو سپورٹ کرتے ہیں ان سے متعلق مزید معلومات کے لیے ہمارے [کم سے کم سسٹم کے تقاضوں](/client/getting-started/system-requirements) کا جائزہ لیں۔

## ‫Debian پر مبنی Linux ڈسٹری بیوشنز کے لیے Outline کلائنٹ انسٹال کریں (تجویز کردہ)

درج ذیل کمانڈز چلائیں:

1. ‫Outline کی ریپازٹری کلید انسٹال کریں اور ریپازٹری شامل کریں۔
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2۔ مناسب پیکیج کی فہرست کو اپ ڈیٹ کریں اور Outline کلائنٹ کا تازہ ترین ورژن انسٹال کریں۔

```
sudo apt update
sudo apt install outline-client
```

مستقبل کی اپ ڈیٹس کو چیک کرنے یا انسٹال کرنے کے لیے، مرحلہ 2 میں کمانڈز کو دوبارہ چلائیں۔ نوٹ کریں کہ ورژن 1.15 سے شروع ہونے والے، Linux پر Outline کلائنٹ کے لیے درون ایپ آٹو اپ ڈیٹ غیر فعال ہے۔

‫Outline کلائنٹ کو ان انسٹال کرنے کے لیے، درج ذیل کمانڈ کو چلائیں:

```
sudo apt purge outline-client
```

## متبادل آپشن

1. ‫[https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) سے تازہ ترین Outline کلائنٹ Debian پیکیج ڈاؤن لوڈ کریں
2. پیکیج کو انسٹال کرنے کے لیے کمانڈ لائن میں درج ذیل کمانڈز کو چلائیں

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3۔ اپ ڈیٹس کو دستی طور پر چیک کریں، کیونکہ ورژن 1.15 سے شروع ہونے والے، Linux پر Outline کلائنٹ کے لیے درون ایپ آٹو اپ ڈیٹ غیر فعال ہے۔

4۔ ‫ Outline کلائنٹ کو ان انسٹال کرنے کے لیے، کمانڈ لائن میں درج ذیل کمانڈ کو چلائیں:

```
sudo apt purge outline-client
```
