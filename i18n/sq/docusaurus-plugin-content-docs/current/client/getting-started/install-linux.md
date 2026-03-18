---
title: Instalimi i klientit të Outline në Linux
sidebar_label: Instalimi i klientit të Outline në Linux
---

Duke filluar me versionin 1.15 të klientit të Outline, të gjitha versionet e ardhshme do të publikohen si paketa Debian për sistemet operative Linux. Rishiko [kërkesat tona minimale të sistemit](/client/getting-started/system-requirements) për më shumë informacione se cilat sisteme operative mbështesim ne.

## Instalo klientin e Outline për shpërndarjet e Linux bazuar në Debian (rekomandohet)

Ekzekuto komandat e mëposhtme:

1. Instalo çelësin e depos të Outline dhe shto depon.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Përditëso listën e paketës së përparuar dhe instalo versionin më të fundit të klientit të Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Për të kontrolluar ose instaluar përditësimet në të ardhmen, ekzekuto përsëri komandat në hapin 2. Ki parasysh se përditësimi automatik në aplikacion është çaktivizuar për klientin e Outline në Linux, duke filluar nga versioni 1.15.

Për të çinstaluar klientin e Outline, ekzekuto komandën e mëposhtme:

```
sudo apt purge outline-client
```

## Opsioni alternativ

1. Shkarko paketën më të fundit Debian të klientit të Outline nga [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Ekzekuto komandat e mëposhtme në rreshtin e komandës për të instaluar paketën
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Kontrollo manualisht për përditësime pasi përditësimi automatik në aplikacion është çaktivizuar për klientin e Outline në Linux, duke filluar nga versioni 1.15.
4. Për të çinstaluar klientin e Outline, ekzekuto komandën e mëposhtme në rreshtin e komandës:
   ```
   sudo apt purge outline-client
   ```
