---
title: Linux वर Outline क्लायंट इंस्टॉल करणे
sidebar_label: Linux वर Outline क्लायंट इंस्टॉल करणे
---

Outline क्लायंट च्या 1.15 या आवृत्तीपासून, भविष्यातील सर्व आवृत्त्या Linux ऑपरेटिंग सिस्टीमसाठी Debian पॅकेज म्हणून रिलीझ केल्या जातील. आम्ही कोणत्या ऑपरेटिंग सिस्टीमना सपोर्ट करतो याबद्दल अधिक माहितीसाठी आमच्या [किमान सिस्टीम आवश्यकता](/client/getting-started/system-requirements) यांचे पुनरावलोकन करा.

## Debian वर आधारित Linux डिस्ट्रिब्यूशनसाठी Outline क्लायंट इंस्टॉल करणे (शिफारस केलेले)

पुढील कमांड फॉलो करा:

1. Outline ची रीपॉझिटरी की इंस्टॉल करा आणि रीपॉझिटरी जोडा.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

२. apt पॅकेजची सूची अपडेट करा आणि Outline क्लायंट ची नवीनतम आवृत्ती इंस्टॉल करा.

```
sudo apt update
sudo apt install outline-client
```

भविष्यात अपडेट तपासण्यासाठी किंवा इंस्टॉल करण्यासाठी, पायरी २ मधील कमांड पुन्हा रन करा. लक्षात ठेवा, की Linux वर Outline क्लायंट च्या 1.15 या आवृत्तीपासून पुढील आवृत्तींसाठी ॲपमधील ऑटो-अपडेट बंद केले आहे.

Outline क्लायंट अनइंस्टॉल करण्यासाठी, खालील कमांड रन करा:

```
sudo apt purge outline-client
```

## दुसरा पर्याय

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) वरून नवीनतम Outline क्लायंट Debian पॅकेज डाउनलोड करा
2. पॅकेज इंस्टॉल करण्यासाठी कमांड लाइनमध्ये पुढील कमांड रन करा

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

३. अपडेट आहेत का हे मॅन्युअली तपासा, कारण Linux वर Outline क्लायंट च्या 1.15 या आवृत्तीपासून पुढील आवृत्तींसाठी ॲपमधील ऑटो-अपडेट बंद केले आहे.

४. Outline क्लायंट अनइंस्टॉल करण्यासाठी, कमांड लाइनमध्ये पुढील कमांड रन करा:

```
sudo apt purge outline-client
```
