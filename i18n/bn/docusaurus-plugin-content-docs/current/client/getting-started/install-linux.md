---
title: "Linux-এ Outline ক্লায়েন্ট ইনস্টল করা"
sidebar_label: "Linux-এ Outline ক্লায়েন্ট ইনস্টল করা"
---

Linux অপারেটিং সিস্টেমের জন্য, Outline Client-এর ভার্সন 1.15 থেকে শুরু করে ভবিষ্যতের সব ভার্সন Debian প্যাকেজ হিসেবে রিলিজ করা হবে। আমরা কোন অপারেটিং সিস্টেম সমর্থন করি সে সম্পর্কে আরও জানতে, আমাদের [ন্যূনতম সিস্টেমের প্রয়োজনীয়তা](/client/getting-started/system-requirements) দেখুন।

## Debian-ভিত্তিক Linux ডিস্ট্রিবিউশনের জন্য Outline Client ইনস্টল করুন (সাজেস্ট করা)

এই কমান্ডগুলি রান করুন:

1. Outline-এর রিপোজিটরি কী ইনস্টল করুন এবং রিপোজিটরি যোগ করুন।
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

২. APT প্যাকেজের তালিকা আপডেট করুন এবং Outline Client-এর লেটেস্ট ভার্সন ইনস্টল করুন।

```
sudo apt update
sudo apt install outline-client
```

ভবিষ্য়তের আপডেট চেক এবং ইনস্টল করতে, ধাপ ২-এ আবার কমান্ডগুলি রান করুন। মনে রাখবেন যে Linux-এ Outline Client-এর 1.15 এবং পরবর্তী ভার্সনে অ্যাপে অটো-আপডেট ফিচারটি বন্ধ করা আছে।

Outline Client আনইনস্টল করতে, এই কমান্ড রান করুন:

```
sudo apt purge outline-client
```

## অন্য বিকল্প

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) থেকে লেটেস্ট Outline Client Debian প্যাকেজ ডাউনলোড করুন
2. প্যাকেজ ইনস্টল করতে কমান্ড লাইনে এই কমান্ডগুলি রান করুন

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

৩. ম্যানুয়ালি আপডেট চেক করুন, কারণ Linux-এ Outline Client-এর 1.15 এবং পরবর্তী ভার্সনে ইন-অ্যাপ অটো-আপডেট ফিচারটি বন্ধ করা আছে।

৪. Outline Client আনইনস্টল করতে, কমান্ড লাইনে এই কমান্ড রান করুন::

```
sudo apt purge outline-client
```
