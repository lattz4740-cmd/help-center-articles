---
title: "Wie aktualisiere ich die Serversoftware von Outline?"
sidebar_label: "Wie aktualisiere ich die Serversoftware von Outline?"
---

Die Outline-Server erhalten automatisch die neuesten Sicherheitsverbesserungen, damit Sie immer die aktuelle Outline-Technologie verwenden. Die Updates werden über die Open‑Source-Bibliothek [Watchtower](https://github.com/v2tec/watchtower) ausgeführt, mit der regelmäßig das Docker-Image mit der Outline-Software geprüft und automatisch aktualisiert wird.

Zusätzlich wird bei der Installation von Outline über den Outline-Manager ein Cronjob eingerichtet, mit dem die Serversoftware über die Ubuntu-Funktion [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) automatisch aktualisiert und bei Bedarf neu gestartet wird. Hinweis: Im erweiterten Modus werden diese automatischen Updates nicht ausgeführt. Hier wird davon ausgegangen, dass der Host neben Outline auch noch für andere Zwecke verwendet wird und die aktuelle Konfiguration erhalten bleiben soll.
