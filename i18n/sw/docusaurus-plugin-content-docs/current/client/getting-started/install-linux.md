---
title: Kuweka Programu ya Outline kwenye Linux
sidebar_label: Kuweka Programu ya Outline kwenye Linux
---

Kuanzia toleo la Programu ya Outline la 1.15, matoleo yote ya siku zijazo yatachapishwa kama vifurushi vya Debian katika mifumo ya uendeshaji ya Linux. Angalia [masharti yetu ya msingi ya mfumo](/client/getting-started/system-requirements) ili upate maelezo zaidi kuhusu mifumo ya uendeshaji tunayoruhusu.

## Weka Programu ya Outline katika mifumo mahuluti ya uendeshaji ya Linux iliyo kwenye Debian (Inapendekezwa)

Tekeleza amri zifuatazo:

1. Weka ufunguo wa hazina wa Programu ya Outline kwenye kifaa kisha uweke hazina.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Sasisha orodha ya zana za kina za kudhibiti kifurushi kisha uweke toleo jipya kabisa la Programu ya Outline kwenye kifaa.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Ili uweke au uangalie masasisho ya siku zijazo, tekeleza tena amri zilizo katika Hatua ya pili. Kumbuka kuwa kipengele cha kusasisha kiotomatiki cha ndani ya programu kimezimwa kuanzia toleo la 1.15 la Programu ya Outline kwenye Linux.

Ili uondoe Programu ya Outline, tekeleza amri ifuatayo:

```
sudo apt purge outline-client
```

## Chaguo Mbadala

1. Pakua kifurushi kipya kabisa cha Debian cha Programu ya Outline katika [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Tekeleza amri zifuatazo katika kiolesura cha kuweka amri ili uweke kifurushi kwenye kifaa
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Angalia masasisho mwenyewe kwa sababu kipengele cha kusasisha kiotomatiki cha ndani ya programu kimezimwa kuanzia toleo la 1.15 la Programu ya Outline kwenye Linux.
4. Ili uondoe Programu ya Outline, tekeleza amri inayofuata katika kiolesura cha kuweka amri:
   ```
   sudo apt purge outline-client
   ```
