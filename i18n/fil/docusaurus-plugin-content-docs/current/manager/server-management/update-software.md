---
title: "Paano ko ia-update ang Outline server software ko?"
sidebar_label: "Paano ko ia-update ang Outline server software ko?"
---

Awtomatikong ina-update ang mga Outline server sa mga pinakabagong pagpapahusay ng seguridad para palagi kang nagpapatakbo ng pinakabagong teknolohiya ng Outline. Ang naka-automate na proseso ng pag-update ay ine-enable ng [Watchtower](https://github.com/containrrr/watchtower), isang open-source library na regular na tumitingin at nag-a-update sa docker image na naglalaman ng Outline software.

Bukod pa rito, kapag na-install mo ang Outline gamit ang Outline Manager, magse-set up kami ng trabaho sa cron para awtomatikong i-upgrade ang software sa server gamit ang [Mga Unattended na Upgrade](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) at i-reboot ito kapag kinakailangan. Tandaang hindi ito nangyayari sa Advanced Mode para mapanatili ang kasalukuyang configuration, sa pagpapalagay na ginagamit ang host para sa iba pang layunin bukod pa sa pagpapagana ng Outline.
