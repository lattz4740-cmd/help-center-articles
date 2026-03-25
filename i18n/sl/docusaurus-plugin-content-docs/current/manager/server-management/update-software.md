---
title: "Kako posodobim strežniško programsko opremo Outline?"
sidebar_label: "Kako posodobim strežniško programsko opremo Outline?"
---

Strežniki Outline se samodejno posodabljajo z najnovejšimi varnostnimi izboljšavami, tako da vedno uporabljate najnovejšo tehnologijo Outline. Proces samodejnega posodabljanja omogoča [Watchtower](https://github.com/containrrr/watchtower), odprtokodna knjižnica, ki redno preverja in posodablja sliko docker, ki vsebuje programsko opremo.

Poleg tega bomo ob namestitvi strežnika Outline prek Upravitelja za Outline nastavili časovno opravilo za samodejno nadgradnjo programske opreme na strežniku z možnostjo [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Nenadzorovane nadgradnje) (Ubuntu) in vnovično zaganjanje po potrebi. Upoštevajte, da se to ne zgodi v naprednem načinu, da se ohrani obstoječa konfiguracija, ob predpostavki, da se gostitelj poleg izvajanja strežnika Outline uporablja tudi za druge namene.
