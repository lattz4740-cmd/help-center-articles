---
title: Gosod Outline Client ar Linux
sidebar_label: Gosod Outline Client ar Linux
---

Gan ddechrau gydag Outline Client fersiwn 1.15, bydd pob fersiwn yn y dyfodol yn cael ei rhyddhau fel pecyn Debian ar gyfer systemau gweithredu Linux. Adolygwch ein [gofynion system sylfaenol](/client/getting-started/system-requirements) i gael rhagor o wybodaeth am ba systemau gweithredu rydym yn eu cefnogi.

## Gosod Outline Client ar gyfer dosbarthwyr Linux seiliedig ar Debian (Argymhellir)

Rhedwch y gorchmynion canlynol:

1. Gosodwch allwedd storfa Outline ac ychwanegwch y storfa.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Diweddarwch y rhestr pecyn apt a gosodwch fersiwn ddiweddaraf Outline Client.

```
sudo apt update
sudo apt install outline-client
```

I wirio am neu osod diweddariadau yn y dyfodol, rhedwch y gorchmynion yng Ngham 2 eto. Sylwch fod diweddaru awtomatig yn yr ap wedi'i analluogi ar gyfer Outline Client ar Linux, gan ddechrau yn fersiwn 1.15.

I ddadosod Outline Client, rhedwch y gorchymyn canlynol:

```
sudo apt purge outline-client
```

## Dewis Amgen

1. Lawrlwythwch y pecyn Debian Outline Client diweddaraf o [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Rhedwch y gorchmynion canlynol yn y llinell orchymyn i osod y pecyn

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Gwiriwch am ddiweddariadau yn bwrpasol, gan fod diweddaru awtomatig yn yr ap wedi'i analluogi ar gyfer Outline Client ar Linux, gan ddechrau yn fersiwn 1.15.

4. I ddadosod Outline Client, rhedwch y gorchymyn canlynol yn y llinell orchymyn:

```
sudo apt purge outline-client
```
