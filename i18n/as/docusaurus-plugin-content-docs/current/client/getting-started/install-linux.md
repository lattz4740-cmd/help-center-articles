---
title: Linuxত Outline Client ইনষ্টল কৰা
sidebar_label: Linuxত Outline Client ইনষ্টল কৰা
---

Outline Clientৰ সংস্কৰণ 1.15ৰ সৈতে আৰম্ভ কৰি, Linux অ’পাৰেটিং ছিষ্টেমৰ বাবে আটাইবোৰ ভৱিষ্যত সংস্কৰণ Debian পেকেজ হিচাপে মুকলি কৰা হ’ব। আমি কোনবোৰ অ’পাৰেটিং ছিষ্টেম সমৰ্থন কৰোঁ সেই বিষয়ে অধিক তথ্যৰ বাবে আমাৰ [ন্যূনতম ছিষ্টেমৰ প্ৰয়োজনীয়তা](/client/getting-started/system-requirements) পৰ্যালোচনা কৰক।

## Debian-আধাৰিত Linux বিতৰণৰ বাবে Outline Client ইনষ্টল কৰক (চুপাৰিছ কৰা হৈছে)

নিম্নলিখিত কামাণ্ডসমূহ চলাওক:

1. ১) Outlineৰ ৰিপ’জিটৰী কী ইনষ্টল কৰি সেয়া যোগ দিয়ক।
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

২) উপযুক্ত পেকেজৰ সূচী আপডে’ট কৰক আৰু Outline Clientৰ শেহতীয়া সংস্কৰণটো ইনষ্টল কৰক।

```
sudo apt update
sudo apt install outline-client
```

ভৱিষ্যতৰ আপডে’টসমূহ পৰীক্ষা বা ইনষ্টল কৰিবলৈ, পদক্ষেপ ২ত কামাণ্ডসমূহ পুনৰ চলাওক। মন কৰিব যে Outline Clientৰ সংস্কৰণ 1.15ত আৰম্ভ কৰি এপৰ ভিতৰৰ স্বয়ংক্ৰিয়-আপডে’ট Linuxত Outline Clientৰ বাবে অক্ষম কৰা হৈছে।

Outline Client আনইনষ্টল কৰিবলৈ, নিম্নলিখিত কামাণ্ডটো চলাওক:

```
sudo apt purge outline-client
```

## বৈকল্পিক বিকল্প

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)ৰ পৰা শেহতীয়া Outline Client Debian পেকেজ ডাউনল’ড কৰক
2. পেকেজ ইনষ্টল কৰিবলৈ নিম্নলিখিত কামান্ড শাৰীৰ কামাণ্ডসমূহ চলাওক

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

৩) যিহেতু Outline Clientৰ সংস্কৰণ 1.15ত আৰম্ভ কৰি এপৰ ভিতৰৰ স্বয়ংক্ৰিয়-আপডে’ট Linuxত Outline Clientৰ বাবে অক্ষম কৰা হৈছে, আপডে’টৰ বাবে মেনুৱেলী পৰীক্ষা কৰক।

৪) Outline Client আনইনষ্টল কৰিবলৈ, নিম্নলিখিত কামান্ড শাৰীৰ কামাণ্ডটো চলাওক:

```
sudo apt purge outline-client
```
