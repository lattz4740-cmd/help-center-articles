---
title: Terminologie
sidebar_label: Terminologie
---

## Was ist ein VPN?

Ein virtuelles privates Netzwerk (VPN) ist eine private Verbindung zwischen Ihrem Gerät und einem Hostserver. Dadurch hat Ihr Internetanbieter keinerlei Einblick in den Traffic über Ihr Gerät.

Der Einsatz eines VPN ist in verschiedenen Szenarien sinnvoll, z. B.:

- zum Schutz Ihrer Daten im öffentlichen WLAN
- zum Schutz der Browserdaten vor dem Zugriff durch den Internetanbieter oder Behörden
- für den unzensierten Zugriff auf Inhalte verschiedener Quellen weltweit

## Wie unterscheidet sich Outline von herkömmlichen VPNs?

Internetanbieter können herkömmliche VPNs anhand von gängigen Sicherheitsprotokollen und/oder Mustern beim Traffic-Volumen einfach identifizieren. Outline ist resilienter als herkömmliche VPNs, da es auf einem Protokoll basiert, das schwerer zu erkennen ist und sich deshalb auch nicht so leicht blockieren lässt. So schützt Outline sehr gut gegen strikte Formen der Zensur wie Netz- oder IP-Sperren.

## Was ist ein Outline-Server?

Auf dem Outline-Server wird das VPN ausgeführt, mit dem sich autorisierte Nutzer verbinden.

Wenn Sie ein neues Netzwerk erstellen, können Sie als Outline-Server einen eigenen sicheren Server oder einen Cloud-Serviceanbieter nutzen, z. B.:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Sie richten den Server in Outline-Manager ein.

## Was ist ein Dienstmanager? {#servicemanager}

Der Dienstmanager ist die zuständige Person, die den Outline-Server einrichtet und den Nutzern die Zugriffsschlüssel zuteilt. Im Allgemeinen ist der Dienstmanager auch verantwortlich für die Kosten der Servernutzung.

## Was ist ein Zugriffsschlüssel? {#accesskey}

Mit einem Zugriffsschlüssel können Nutzer auf einen Outline-Server zugreifen und sich mit dem VPN verbinden. Sie erhalten den Schlüssel von einem [Dienstmanager](#servicemanager). Sie haben aber auch die Möglichkeit, selbst [einen Outline-Server einzurichten](/manager/server-setup/setup-server).

So sieht ein Zugriffsschlüssel aus (Beispiel):

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Was ist Outline-Manager?

Outline-Manager ist eine Desktopanwendung, in der ein Dienstmanager einen Outline-Server einrichten und [Zugriffsschlüssel](#accesskey) generieren kann. Außerdem besteht die Möglichkeit, für jeden Schlüssel ein Datenlimit festzulegen. Sie können die neueste Version von Outline-Manager [hier](https://getoutline.org/get-started/#step-3) und [hier](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) herunterladen.

## Was ist Outline-Client?

Outline-Client ist die Anwendung, über die Sie mit Ihrem Zugriffsschlüssel eine Verbindung zu einem Outline-Server herstellen und auf das VPN zugreifen können. Sie ist sowohl für Computer als auch für Mobilgeräte verfügbar. Sie können die neueste Version von Outline-Client [hier](https://getoutline.org/get-started/#step-3) und [hier](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) herunterladen.

## Was sind Datenlimits?

In Outline-Manager können Dienstmanager für Zugriffsschlüssel ein abhängiges Datenlimit konfigurieren, bei dem jeweils die letzten 30 Tage zugrunde gelegt werden. So lassen sich Nutzung und Kosten besser in Grenzen halten. Ein Dienstmanager kann ein Standardlimit festlegen, das für alle Schlüssel gilt, sowie ein individuelles Limit für einzelne Schlüssel, das dann Vorrang vor dem Standardwert hat. Konfigurierte Limits treten sofort in Kraft und werden stundengenau durchgesetzt.

Wenn Dienstmanager der Weitergabe von Messwerten an Jigsaw zustimmen, lesen sie am besten in unseren [Richtlinien zur Datenerhebung](https://getoutline.org/policies/data-collection) nach, welche Informationen zur Nutzung von Datenlimits in den Berichten enthalten sind.
