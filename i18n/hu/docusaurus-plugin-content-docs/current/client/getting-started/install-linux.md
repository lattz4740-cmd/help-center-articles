---
title: Az Outline ügyfélalkalmazás telepítése Linux rendszeren
sidebar_label: Az Outline ügyfélalkalmazás telepítése Linux rendszeren
---

Az Outline-ügyfél 1.15-ös verziójától kezdve az összes jövőbeli verzió Debian-csomagként jelenik meg a Linux operációs rendszerekhez. A támogatott operációs rendszerekről a [minimális rendszerkövetelményekben](/client/getting-started/system-requirements) talál további információt.

## Az Outline-ügyfél telepítése Debian-alapú Linux-kiadások esetén (ajánlott)

Futtassa a következő parancsokat:

1. Telepítse az Outline tárhelykulcsát, és adja hozzá a tárhelyet.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Frissítse az apt-csomaglistát, és telepítse az Outline-ügyfél legújabb verzióját.

```
sudo apt update
sudo apt install outline-client
```

A jövőbeli frissítések kereséséhez és telepítéséhez futtassa újra a 2. lépésben szereplő parancsokat. Felhívjuk figyelmét, hogy az 1.15-ös verziótól kezdve a Linuxon használt Outline-ügyfél alkalmazáson belüli automatikus frissítése ki van kapcsolva.

Az Outline-ügyfél eltávolításához futtassa a következő parancsot:

```
sudo apt purge outline-client
```

## Másik lehetőség

1. Töltse le az Outline-ügyfél legújabb Debian-csomagját innen: [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. A csomag telepítéséhez adja meg a következő parancsokat a parancssorban

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Keresse meg a frissítéseket manuálisan, mivel az 1.15-ös verziótól kezdve a Linuxon használt Outline-ügyfél alkalmazáson belüli automatikus frissítése ki van kapcsolva.

4. Az Outline-ügyfél eltávolításához adja meg a következő parancsot a parancssorban

```
sudo apt purge outline-client
```
