---
title: „Outline“ kliento programos diegimas sistemoje „Linux“
sidebar_label: „Outline“ kliento programos diegimas sistemoje „Linux“
---

Nuo 1.15 versijos visos būsimos „Outline“ kliento programos versijos bus išleistos kaip „Debian“ paketai, skirti „Linux“ operacinėms sistemoms. Jei reikia daugiau informacijos apie tai, kurias operacines sistemas palaikome, peržiūrėkite [minimalius sistemos reikalavimus](/client/getting-started/system-requirements).

## „Outline“ kliento programos diegimas „Debian“ pagrindu sukurtuose „Linux“ platinamuosiuose paketuose (rekomenduojama)

Vykdykite toliau nurodytas komandas.

1. Įdiekite „Outline“ saugyklos raktą ir pridėkite saugyklą.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Atnaujinkite „apt“ paketų sąrašą ir įdiekite naujausios versijos „Outline“ kliento programą.

```
sudo apt update
sudo apt install outline-client
```

Jei norite patikrinti, ar yra būsimų naujinių, arba juos įdiegti, dar kartą vykdykite antrame veiksme nurodytas komandas. Atminkite, kad automatinis atnaujinimas programoje išjungtas „Outline“ kliento programai sistemoje „Linux“ nuo 1.15 versijos.

Jei norite pašalinti „Outline“ kliento programą, vykdykite toliau nurodytą komandą.

```
sudo apt purge outline-client
```

## Alternatyvi parinktis

1. Atsisiųskite naujausią „Outline“ kliento programos „Debian“ paketą iš [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Vykdykite toliau nurodytas komandas komandų eilutėje, kad įdiegtumėte paketą.

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Neautomatiškai patikrinkite, ar yra naujinių, nes automatinis atnaujinimas programoje išjungtas „Outline“ kliento programai sistemoje „Linux“ nuo 1.15 versijos.

4. Jei norite pašalinti „Outline“ kliento programą, komandų eilutėje vykdykite toliau nurodytą komandą.

```
sudo apt purge outline-client
```
