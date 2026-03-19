---
title: Firewall errors
sidebar_label: Firewall errors
---

There are three type of firewall issues that you may encounter:

## You might be blocked by a network firewall.

If you're trying to install Outline while connected to a firewalled network, like at school or in your workplace, try installing while on a different network.

If this doesn't work, please contact your network administrator to allow for connections between the firewalled network to your Outline server. You will need to know your Outline server's IP address and the ports where Outline is running, which are indicated at the end of the installation script.

## You might be blocked by a device firewall.

If you have software on your device that blocks outgoing connections on non-standard ports, or non recognized software, (CheckPoint's ZoneAlarm), please consult your device or software documentation to learn how to create an exception for Outline.

## You might be blocked by a server firewall.

The cloud provider you have chosen may require you to manually create exceptions to your server firewall, to open the ports Outline is running on. After you ran the installation script, you should have been presented with the two randomly selected ports where Outline is running in your server. Opening these two ports should suffice.

 In order to create exceptions to your Server firewall, we recommend you look into the documentation for 'ufw' and 'iptables':

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
