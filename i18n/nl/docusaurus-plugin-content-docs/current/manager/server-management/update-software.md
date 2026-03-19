---
title: "Hoe update ik de software van mijn Outline-server?"
sidebar_label: "Hoe update ik de software van mijn Outline-server?"
---

Outline-servers worden automatisch geüpdatet met de nieuwste beveiligingsfuncties, zodat je altijd de nieuwste Outline-technologie gebruikt. Dit automatische updateproces wordt mogelijk gemaakt door [Watchtower](https://github.com/v2tec/watchtower), een opensource-bibliotheek die regelmatig de docker-image met de Outline-software checkt en updatet.

Als je daarnaast Outline instelt met Outline Manager, stellen we een cron job in waarmee de software op de server automatisch wordt geüpgraded met [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Upgrades op de achtergrond, Ubuntu) en wanneer nodig opnieuw wordt opgestart. Dit gebeurt niet in de Advanced Mode (Geavanceerde modus) om de bestaande configuratie te beschermen. Hierbij gaan we ervan uit dat de host wordt gebruikt voor meer doeleinden dan alleen het uitvoeren van Outline.
