---
title: Probleme mit Firewalls
sidebar_label: Probleme mit Firewalls
---

Firewalls können bei der Installation von Outline drei Probleme verursachen:

## Netzwerkfirewall blockiert Verbindung zum Outline-Server

Dieses Problem kann auftreten, wenn Sie versuchen, Outline über ein Netzwerk zu installieren, das mit einer Firewall geschützt wird, z. B. das Netzwerk Ihrer Bildungseinrichtung oder Ihres Unternehmens. Wiederholen Sie den Installationsversuch über ein anderes Netzwerk.

 Lässt sich das Problem so nicht lösen, wenden Sie sich an den Netzwerkadministrator und bitten Sie ihn, Verbindungen zwischen dem firewallgeschützten Netzwerk und Ihrem Outline-Server zuzulassen. Sie benötigen die IP-Adresse Ihres Outline-Servers und müssen die Ports angeben, über die Outline ausgeführt wird. Sie finden sie am Ende des Installationsskripts.

## Gerätefirewall blockiert Verbindung zum Outline-Server

Hierzu kann es kommen, wenn auf Ihrem Gerät eine Software installiert ist, mit der ausgehende Verbindungen über nicht standardmäßige Ports blockiert werden, oder wenn Sie eine Software verwenden, die nicht erkannt wurde, z. B. ZoneAlarm von Check Point. Lesen Sie bitte in der Dokumentation der Software oder des Geräts nach, wie Sie eine Ausnahme für Outline erstellen können.

## Serverfirewall blockiert Verbindung zum Outline-Server

Abhängig vom ausgewählten Cloudanbieter müssen Sie möglicherweise manuell Ausnahmen bei Ihrer Serverfirewall erstellen, um die Ports zu öffnen, über die Outline ausgeführt wird. Nachdem Sie das Installlationsskript ausgeführt haben, sollten für Outline auf Ihrem Server zwei Ports nach dem Zufallsprinzip ausgewählt worden sein. Das Öffnen dieser beiden Ports sollte das Problem beheben.

 Wie Sie Ausnahmen bei Ihrer Serverfirewall erstellen, können Sie in den Dokumentationen zu UFW und Iptables lesen:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
