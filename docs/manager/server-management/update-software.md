---
title: "How do I update my Outline server software?"
sidebar_label: Update server software
---

Outline servers automatically update with the latest security improvements so that you are always running the latest Outline technology. The automated update process is enabled by [Watchtower](https://github.com/v2tec/watchtower), an open-source library that regularly checks and updates the docker image containing the Outline software.

Additionally, when you install Outline using the Outline Manager, we will set up a cron job to automatically upgrade the software on the server using [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) and reboot it when necessary. Note that this doesn’t occur in Advanced Mode to preserve the existing configuration, under the assumption that the host is being used for other purposes in addition to running Outline.
