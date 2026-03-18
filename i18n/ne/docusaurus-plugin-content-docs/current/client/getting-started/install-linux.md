---
title: Linux मा Outline क्लाइन्ट इन्स्टल गर्ने तरिका
sidebar_label: Linux मा Outline क्लाइन्ट इन्स्टल गर्ने तरिका
---

Linux अपरेटिङ सिस्टमका लागि Outline Client को संस्करण १.१५ र यसपछिका सबै संस्करण Debian प्याकेजहरूका रूपमा रिलिज गरिने छन्। यो एपले कुन कुन अपरेटिङ सिस्टममा काम गर्छ भन्ने बारेमा थप जानकारी प्राप्त गर्न [सिस्टमसम्बन्धी हाम्रा न्यूनतम मापदण्डहरू](/client/getting-started/system-requirements) हेर्नुहोस्।

## Debian मा आधारित Linux डिस्ट्रिब्युसनहरूका लागि बनाइएको Outline Client इन्स्टल गर्नुहोस् (सिफारिस गरिएको)

निम्न कमान्डहरू रन गर्नुहोस्:

1. Outline को रिपोजिटरी की इन्स्टल गर्नुहोस् र उक्त रिपोजिटरी हाल्नुहोस्।
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

२. APT प्याकेजको सूची अपडेट गर्नुहोस् र Outline Client को नवीनतम संस्करण इन्स्टल गर्नुहोस्।

```
sudo apt update
sudo apt install outline-client
```

भविष्यमा अपडेटहरूको उपलब्धता जाँच्न तथा उपलब्ध अपडेटहरू इन्स्टल गर्न चरण २ मा दिइएका कमान्डहरू फेरि रन गर्नुहोस्। Linux मा Outline Client को संस्करण १.१५ देखि लागू हुने गरी यो एप स्वतः अपडेट हुने सुविधा अफ गरिएको छ भन्ने कुरा ख्याल गर्नुहोस्।

Outline Client अनइन्स्टल गर्न निम्न कमान्ड रन गर्नुहोस्:

```
sudo apt purge outline-client
```

## वैकल्पिक

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) मा गई Outline Client को नवीनतम Debian प्याकेज डाउनलोड गर्नुहोस्।
2. उक्त प्याकेज इन्स्टल गर्न कमान्ड लाइनमा निम्न कमान्डहरू रन गर्नुहोस्

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

३. Linux मा Outline Client को संस्करण १.१५ देखि लागू हुने गरी यो एप स्वतः अपडेट हुने सुविधा अफ गरिएको हुनाले म्यानुअल तरिकाले अपडेटहरूको उपलब्धता जाँच्नुहोस्।

४. Outline Client अनइन्स्टल गर्न कमान्ड लाइनमा निम्न कमान्ड रन गर्नुहोस्:

```
sudo apt purge outline-client
```
