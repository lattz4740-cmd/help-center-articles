---
title: Fífi Outline Client sí orí Linux
sidebar_label: Fífi Outline Client sí orí Linux
---

Bẹ̀rẹ̀ láti Outline Client ẹ̀yà 1.15, gbogbo àwọn ẹ̀yà ọjọ́ iwájú ni a máa gbé jáde gẹ́gẹ́ bíi àwọn àkójọ Debian fún àwọn ètò ìṣiṣẹ́ Linux. Ṣe àgbéyẹ̀wò [àwọn ìbéèrè ẹ̀rọ tí ó kéré jùlọ](/client/getting-started/system-requirements)fún ẹ̀kúnrẹ́rẹ́ àlàyé nípa àwọn ètò ìṣiṣẹ́ tí à ń tì lẹ́yìn.

## Ṣe ìfilọ́ọ́lẹ̀ Outline Client fún àwọn ìpínkiri Linux tó dá lóríi Debian (A dábàá rẹ̀)

Mú àwọn àṣẹ wọ̀nyìí ṣẹ:

1. Ṣe ìfilọ́ọ́lẹ̀ kọ́kọ́rọ́ ibùdó ìpamọ́ Outline, kí o sì fi ibùdó ìpamọ́ náà kún un.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Ṣe ìmúdójúìwọ̀n àtòkọ àkójọ apt, kí o sì fi ẹ̀yà Outline Client tuntun síi.

```
sudo apt update
sudo apt install outline-client
```

Láti wá tàbí gbé àwọn ìmúdójúìwọ̀n ọjọ́ iwájú wọlé, mú àwọn àṣẹ tó wà ní ìgbésẹ̀ 2 ṣẹ lẹ́ẹ̀kan síi. Ṣe àkíyèsí pé a dá'ṣẹ́ ìmúdójúìwọ̀n àìfọwọ́yí inú áàpù dúró fún Outline Client lóríi Linux, bẹ̀rẹ̀ láti ẹ̀yà 1.15.

Láti yọ Outline Client kúrò, mú àṣẹ yìí ṣẹ:

```
sudo apt purge outline-client
```

## Àṣàyàn mìíràn

1. Ṣe ìgbàsílẹ̀ àkójọ Debian tuntun ti Outline Client láti [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Mú àwọn àṣẹ wọ̀nyìí ṣẹ lórí ìlà àṣẹ láti gbé àkójọ náà wọlé

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Wá àwọn ìmúdójúìwọ̀n fún ara rẹ, nítorí a ti dá iṣẹ́ ìmúdójúìwọ̀n àìfọwọ́yí inú áàpù dúró fún Outline Client lóríi Linux, bẹ̀rẹ̀ láti ẹ̀yà 1.15.

4. Láti yọ Outline Client, mú àṣẹ yìí ṣẹ lórí ìlà àṣẹ:

```
sudo apt purge outline-client
```
