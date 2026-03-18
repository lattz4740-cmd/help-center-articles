---
title: "Outline Client кызматын Linux'та орнотуу"
sidebar_label: "Outline Client кызматын Linux'та орнотуу"
---

Outline Client кызматынын 1.15 версиясынан баштап, келечекте бардык нускалар Linux операциялык тутумга арналган Debian топтому катары жарыкка чыгат. Колдоого алган операциялык тутумдар тууралуу кеңири маалымат алуу үчүн [минималдуу системдик талаптарды](/client/getting-started/system-requirements) карап чыгыңыз.

## Debian операциялык тутумунун негизиндеги Linux дистрибутивдери үчүн Outline Client колдонмосун орнотуңуз (сунушталат)

Төмөнкү буйруктарды аткарыңыз:

1. Outline кызматынын сактоочу жайдын ачкычы орнотуп, сактоочу жайды кошуңуз.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2-кадам Apt топтомдун тизмесин жаңыртып, Outline Client колдонмосунун эң акыркы версиясын орнотуңуз.

```
sudo apt update
sudo apt install outline-client
```

Келечектеги жаңыртууларды орнотуу же текшерүү үчүн, 2-кадамда көрсөтүлгөн буйруктарды кайрадан аткарыңыз. 1.15 версиясынан баштап Linux'та иштеген Outline Client колдонмосунда авто-жаңыртуу өчүрүлгөнүн эске алыңыз.

Outline Client кызматты чыгарып салуу үчүн, төмөнкү буйрукту аткарыңыз:

```
sudo apt purge outline-client
```

## Башка жолу

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) дарегинен Debian үчүн эң акыркы Outline Client топтомун жүктөп алыңыз
2. Топтомду орнотуу үчүн төмөнкү буйруктарды аткарыңыз:

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3-кадам Жаңыртууларды кол менен текшериңиз, анткени 1.15 версиясынан баштап Linux'та иштеген Outline Client колдонмосунда авто-жаңыртуу өчүрүлгөн.

4-кадам Outline Client колдонмосун чыгарып салуу үчүн, төмөнкү буйрукту аткарыңыз:

```
sudo apt purge outline-client
```
