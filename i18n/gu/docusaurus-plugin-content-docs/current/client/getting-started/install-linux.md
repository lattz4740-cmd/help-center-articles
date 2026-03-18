---
title: Linux પર Outline ક્લાયન્ટ ઇન્સ્ટૉલ કરવા વિશે
sidebar_label: Linux પર Outline ક્લાયન્ટ ઇન્સ્ટૉલ કરવા વિશે
---

Linux ઑપરેટિંગ સિસ્ટમ માટે, Outline ક્લાયન્ટના વર્ઝન 1.15થી લઈને ભવિષ્યના બધા વર્ઝન Debian પૅકેજ તરીકે રિલીઝ કરવામાં આવશે. અમે કઈ ઑપરેટિંગ સિસ્ટમને સપોર્ટ કરીએ છીએ તે વિશે વધુ માહિતી માટે, અમારી [સિસ્ટમની ન્યૂનતમ જરૂરિયાતો](/client/getting-started/system-requirements)નો રિવ્યૂ કરો.

## Debian-આધારિત Linuxના ડિસ્ટ્રિબ્યૂશન માટે Outline ક્લાયન્ટ ઇન્સ્ટૉલ કરવી (સુઝાવ આપવામાં આવે છે)

નીચે આપેલા આદેશો ચલાવો:

1. Outlineની રિપૉઝિટરી કી ઇન્સ્ટૉલ કરો અને રિપૉઝિટરી ઉમેરો.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. apt પૅકેજની સૂચિ અપડેટ કરો અને Outline ક્લાયન્ટનું નવીનતમ વર્ઝન ઇન્સ્ટૉલ કરો.

```
sudo apt update
sudo apt install outline-client
```

ભવિષ્યની અપડેટ ચેક કરવા કે ઇન્સ્ટૉલ કરવા માટે, પગલાં 2માં આપેલા આદેશો ફરીથી ચલાવો. નોંધો કે Linux પર Outline ક્લાયન્ટના 1.15થી લઈને તે પછીના વર્ઝન પર ઍપમાં ઑટો-અપડેટની સુવિધા બંધ કરવામાં આવી છે.

Outline ક્લાયન્ટને અનઇન્સ્ટૉલ કરવા માટે, નીચે આપેલા આદેશ ચલાવો:

```
sudo apt purge outline-client
```

## વૈકલ્પિક વિકલ્પ

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) પરથી Outline ક્લાયન્ટનું નવીનતમ Debian પૅકેજ ડાઉનલોડ કરો
2. પૅકેજ ઇન્સ્ટૉલ કરવા માટે, આદેશની લાઇનમાં નીચે આપેલા આદેશો ચલાવો

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Linux પર Outline ક્લાયન્ટના 1.15થી લઈને તે પછીના વર્ઝન પર ઍપમાં ઑટો-અપડેટની સુવિધા બંધ કરવામાં આવી હોવાથી, અપડેટ માટે મેન્યુઅલી ચેક કરો.

4. Outline ક્લાયન્ટને અનઇન્સ્ટૉલ કરવા માટે, આદેશની લાઇનમાં નીચે આપેલો આદેશ ચલાવો:

```
sudo apt purge outline-client
```
