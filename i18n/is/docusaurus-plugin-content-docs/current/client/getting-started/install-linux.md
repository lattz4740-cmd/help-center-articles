---
title: Uppsetning Outline Client í Linux
sidebar_label: Uppsetning Outline Client í Linux
---

Við byrjum með Outline Client, útgáfu 1.15, en allar framtíðarútgáfur verða gefnar út sem Debian-pakkar fyrir Linux-stýrikerfi. Skoðaðu [lágmarkskerfiskröfur](/client/getting-started/system-requirements) okkar til að fá nánari upplýsingar um hvaða stýrikerfi við styðjum.

## Setja upp Outline Client fyrir Linux-dreifingu sem byggist á Debian (mælt með)

Keyrðu eftirfarandi skipanir:

1. Settu upp geymslulykil Outline og bættu geymslunni við.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Uppfærðu apt-pakkaskráninguna og settu upp nýjustu útgáfuna af Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Til að athuga með eða setja upp seinni tíma uppfærslur skaltu keyra skipanirnar í skrefi 2 aftur. Athugaðu að slökkt er á sjálfvirkri uppfærslu sem fylgir forritinu fyrir Outline Client í Linux frá og með útgáfu 1.15.

Til að fjarlægja Outline Client skaltu keyra eftirfarandi skipun:

```
sudo apt purge outline-client
```

## Annar valkostur

1. Sæktu nýjasta Outline Client Debian-pakkann af [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Keyrðu eftirfarandi skipanir í skipanalínunni til að setja pakkann upp

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Athuga verður handvirkt með uppfærslur þar sem slökkt er á sjálfvirkri uppfærslu sem fylgir forritinu fyrir Outline Client í Linux frá og með útgáfu 1.15.

4. Til að fjarlægja Outline Client skaltu keyra eftirfarandi skipun í skipanalínunni:

```
sudo apt purge outline-client
```
