---
title: "Linux-en Outline Client instalatzea"
sidebar_label: "Linux-en Outline Client instalatzea"
---

Outline Client-en 1.15 bertsiotik aurrera, aurrerantzeko bertsio guztiak Debian-eko pakete gisa kaleratuko dira Linux sistema eragileetarako. Sistema eragile bateragarriei buruzko informazio gehiago lortzeko, berrikusi [sistemaren gutxieneko eskakizunak](/client/getting-started/system-requirements).

## Outline Client instalatu Debian-en oinarritutako Linux-en banaketetarako (gomendatua)

Exekutatu agindu hauek:

1. Instalatu Outline-ren biltegi-gakoa eta gehitu biltegia.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Eguneratu apt paketeko zerrenda eta instalatu Outline Client-en azken bertsioa.

```
sudo apt update
sudo apt install outline-client
```

Aurrerantzeko eguneratzeak bilatzeko edo instalatzeko, exekutatu 2. urratseko aginduak berriro. Kontuan izan 1.15 bertsiotik aurrera aplikazioko eguneratze automatikoak desgaituta daudela Linux-eko Outline Client-en.

Outline Client desinstalatzeko, exekutatu agindu hau:

```
sudo apt purge outline-client
```

## Ordezko aukera

1. Deskargatu Outline Client-en Debian-eko azken paketea hemendik: [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Paketea instalatzeko, exekutatu agindu hauek agindu-lerroan:

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Bilatu eguneratzeak eskuz; izan ere, 1.15 bertsiotik aurrera aplikazioko eguneratze automatikoak desgaituta daude Linux-eko Outline Client-en.

4. Outline Client desinstalatzeko, exekutatu agindu hau agindu-lerroan:

```
sudo apt purge outline-client
```
