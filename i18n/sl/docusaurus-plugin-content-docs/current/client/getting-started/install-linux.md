---
title: Nameščanje odjemalske aplikacije Outline v operacijskem sistemu Linux
sidebar_label: Nameščanje odjemalske aplikacije Outline v operacijskem sistemu Linux
---

Od različice 1.15 dalje bodo vse prihodnje različice odjemalske aplikacije Outline izdane kot paketi Debian za operacijske sisteme Linux. Za več informacij o tem, katere operacijske sisteme podpiramo, preglejte [minimalne sistemske zahteve](/client/getting-started/system-requirements).

## Namestitev odjemalske aplikacije Outline za distribucije Linuxa, ki temeljijo na sistemu Debian (priporočeno)

Zaženite naslednje ukaze:

1. Namestite ključ repozitorija odjemalca Outline in dodajte repozitorij.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Posodobite seznam paketov apt in namestite najnovejšo različico odjemalske aplikacije Outline.

```
sudo apt update
sudo apt install outline-client
```

Če želite preveriti, ali so na voljo posodobitve, ali namestiti prihodnje posodobitve, znova zaženite ukaza iz 2. koraka. Upoštevajte, da je samodejno posodabljanje v aplikaciji za odjemalca Outline v sistemu Linux od različice 1.15 onemogočeno.

Če želite odmestiti odjemalca Outline, zaženite naslednji ukaz:

```
sudo apt purge outline-client
```

## Nadomestna možnost

1. Prenesite najnovejši paket odjemalca Outline za Debian z naslova [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Če želite namestiti paket, v ukazni vrstici zaženite naslednje ukaze

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Ročno preverite, ali so na voljo posodobitve, saj je samodejno posodabljanje v aplikaciji za odjemalca Outline v sistemu Linux od različice 1.15 onemogočeno.

4. Če želite odmestiti odjemalca Outline, v ukazni vrstici zaženite naslednji ukaz:

```
sudo apt purge outline-client
```
