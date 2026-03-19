---
title: Linux पर Outline Client को इंस्टॉल करना
sidebar_label: Linux पर Outline Client को इंस्टॉल करना
---

Linux ऑपरेटिंग सिस्टम के लिए Outline Client के 1.15 और इसके बाद के सभी वर्शन, Debian पैकेज के तौर पर रिलीज़ किए जाएंगे. हम किन ऑपरेटिंग सिस्टम के साथ मिलकर काम करते हैं, इस बारे में ज़्यादा जानकारी के लिए, [सिस्टम से जुड़ी ज़रूरी शर्तें](/client/getting-started/system-requirements) देखें.

## Debian आधारित Linux डिस्ट्रिब्यूशन के लिए Outline Client इंस्टॉल करना (सुझाया गया)

ये कमांड दें:

1. Outline की रिपॉज़िटरी कुंजी इंस्टॉल करें और रिपॉज़िटरी जोड़ें.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. एपीटी पैकेज की सूची अपडेट करें और Outline Client का नया वर्शन इंस्टॉल करें.

```
sudo apt update
sudo apt install outline-client
```

आने वाले समय में अपडेट देखने या इंस्टॉल करने के लिए, दूसरे चरण में दिए गए कमांड फिर से दें. ध्यान दें कि Linux के लिए Outline Client के 1.15 और इसके बाद के वर्शन पर, ऐप्लिकेशन के अपने-आप अपडेट होने की सुविधा बंद कर दी गई है.

Outline Client को अनइंस्टॉल करने के लिए, यह कमांड दें:

```
sudo apt purge outline-client
```

## अन्य विकल्प

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) से, Outline Client का नया Debian पैकेज डाउनलोड करें
2. पैकेज इंस्टॉल करने के लिए, कमांड लाइन में ये कमांड दें

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. मैन्युअल तौर पर अपडेट देखें, क्योंकि Linux के लिए Outline Client के 1.15 और इसके बाद के वर्शन पर, ऐप्लिकेशन के अपने-आप अपडेट होने की सुविधा बंद कर दी गई है.

4. Outline Client को अनइंस्टॉल करने के लिए, कमांड लाइन में यह कमांड दें:

```
sudo apt purge outline-client
```
