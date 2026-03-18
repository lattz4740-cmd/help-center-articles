---
title: Outline Client a Shuiteáil ar Linux
sidebar_label: Outline Client a Shuiteáil ar Linux
---

Ag tosú le leagan 1.15 de Outline Client, eiseofar na leaganacha amach anseo ar fad mar phacáistí Debian le haghaidh córais oibriúcháin Linux. Féach ar ár [gceanglais chórais íosta](/client/getting-started/system-requirements) chun tuilleadh faisnéise a fháil maidir leis na córais oibriúcháin a dtacaímid leo.

## Outline Client a shuiteáil le haghaidh dáiltí atá bunaithe ar Debian Linux (Molta)

Rith na horduithe seo a leanas:

1. Suiteáil eochair stórlainne Outline agus cuir an stórlann leis.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Nuashonraigh liosta an phacáiste apt agus suiteáil an leagan is déanaí de Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Chun seiceáil le haghaidh nuashonruithe amach anseo nó chun iad a shuiteáil, rith na horduithe atá i gCéim 2 arís. Tabhair faoi deara go bhfuil uathnuashonrú ionaipe díchumasaithe do Outline Client ar Linux, ag tosú i leagan 1.15.

Chun Outline Client a dhíshuiteáil, rith an t-ordú seo a leanas:

```
sudo apt purge outline-client
```

## Rogha Mhalartach

1. Íoslódáil an pacáiste Outline Client Debian is déanaí ó [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Rith na horduithe seo a leanas sa líne orduithe chun an pacáiste a shuiteáil:

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Seiceáil le haghaidh nuashonruithe de láimh, toisc go bhfuil uathnuashonrú ionaipe díchumasaithe do Outline Client ar Linux, ag tosú i leagan 1.15.

4. Chun Outline Client a dhíshuiteáil, rith an t-ordú seo a leanas sa líne orduithe:

```
sudo apt purge outline-client
```
