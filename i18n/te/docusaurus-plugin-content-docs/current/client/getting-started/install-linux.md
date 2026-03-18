---
title: Linuxలో Outline క్లయింట్‌ను ఇన్‌స్టాల్ చేయడం
sidebar_label: Linuxలో Outline క్లయింట్‌ను ఇన్‌స్టాల్ చేయడం
---

Outline క్లయింట్ వెర్షన్ 1.15 నుండి ప్రారంభించి, భవిష్యత్తులో వచ్చే అన్ని వెర్షన్‌లు Linux ఆపరేటింగ్ సిస్టమ్‌ల కోసం Debian ప్యాకేజీలుగా రిలీజ్ చేయబడతాయి. ఏ ఆపరేటింగ్ సిస్టమ్‌లకు మేము సపోర్ట్ చేస్తున్నామో తెలుసుకోవడానికి మా [కనీస సిస్టమ్ ఆవశ్యకతల](/client/getting-started/system-requirements)ను రివ్యూ చేయండి.

## Debian-ఆధారిత Linux డిస్ట్రిబ్యూషన్‌ల కోసం Outline క్లయింట్‌ను ఇన్‌స్టాల్ చేయండి (సిఫార్సు చేయబడింది)

కింది కమాండ్‌లను రన్ చేయండి:

1. Outline రిపోజిటరీ కీని ఇన్‌స్టాల్ చేయండి, రిపోజిటరీని జోడించండి.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. APT ప్యాకేజీ లిస్ట్‌ను అప్‌డేట్ చేసి, Outline క్లయింట్ తాజా వెర్షన్‌ను ఇన్‌స్టాల్ చేయండి.

```
sudo apt update
sudo apt install outline-client
```

భవిష్యత్తు అప్‌డేట్‌ల కోసం చెక్ చేయడానికి లేదా ఇన్‌స్టాల్ చేయడానికి, దశ 2లోని కమాండ్‌లను మళ్లీ రన్ చేయండి. Linuxలోని Outline క్లయింట్ కోసం వెర్షన్ 1.15 నుండి ఇన్-యాప్ 'ఆటో-అప్‌డేట్' డిజేబుల్ చేయబడిందని గమనించండి.

Outline క్లయింట్‌ను అన్‌ఇన్‌స్టాల్ చేయడానికి, ఈ కింది కమాండ్‌ను రన్ చేయండి:

```
sudo apt purge outline-client
```

## ప్రత్యామ్నాయ ఆప్షన్

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) నుండి తాజా Outline క్లయింట్ Debian ప్యాకేజీని డౌన్‌లోడ్ చేయండి
2. ప్యాకేజీని ఇన్‌స్టాల్ చేయడానికి కింది కమాండ్‌లను కమాండ్ లైన్‌లో రన్ చేయండి

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Linuxలోని Outline క్లయింట్ కోసం వెర్షన్ 1.15 నుండి ఇన్-యాప్ ఆటో-అప్‌డేట్ డిజేబుల్ చేయబడింది కాబట్టి,

4. Outline క్లయింట్‌ను అన్‌ఇన్‌స్టాల్ చేయడానికి, కమాండ్ లైన్‌లో ఈ కింది కమాండ్‌ను రన్ చేయండి:

```
sudo apt purge outline-client
```
