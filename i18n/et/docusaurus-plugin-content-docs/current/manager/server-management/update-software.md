---
title: "Kuidas saan oma Outline'i serveritarkvara värskendada?"
sidebar_label: "Kuidas saan oma Outline'i serveritarkvara värskendada?"
---

Outline'i servereid värskendatakse automaatselt uusimate turbetäiustustega, et teil oleks alati uusim Outline'i tehnoloogia. Automaatne värskendusprotsess põhineb teenusel [Watchtower](https://github.com/v2tec/watchtower). See on avatud lähtekoodiga teek, mis kontrollib ja värskendab regulaarselt Dockeri kujutist, mis sisaldab Outline'i tarkvara.

Kui kasutate Outline'i installimiseks Outline Manageri, seadistame lisaks ka käsurea utiliidi cron, et täiendada serveris tarkvara automaatselt, kasutades funktsiooni [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu), ja vajadusel seade taaskäivitada. Võtke arvesse, et seda ei juhtu täpsemas režiimis, kuna soovitakse säilitada olemasolev konfiguratsioon eeldusel, et hosti kasutatakse lisaks Outline'i käitamisele muudel eesmärkidel.
