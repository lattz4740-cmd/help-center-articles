---
title: Funktionsweise von Outline
sidebar_label: Funktionsweise von Outline
---

### Server installieren

Die Installation von Outline mag einfach aussehen, aber im Hintergrund laufen dabei eine ganze Reihe komplexer Prozesse ab.

Bei der Installation von Outline wird immer ein Installationsskript mit folgenden Schritten ausgeführt:

- Die stabile Version des Shadowbox-Images wird mit Docker abgerufen und importiert. Das Image wird auf Quay.io unter https://quay.io/repository/outline/shadowbox?tab=tagsgehostet. Es enthält den Outline-Server und die Management API. Letztere wird später von der Anwendung "Outline Server Management" verwendet, um Zugriffsschlüssel zu erstellen und zu entfernen sowie die Meldung anonymer Messwerte zu aktivieren oder zu deaktivieren usw.
- Watchtower wird installiert und so konfiguriert, dass stündlich nach Image-Updates gesucht wird. Das trägt dazu bei, dass jeder Outline-Server ständig die neuesten Funktionen und Sicherheitsverbesserungen erhält und auf dem neuesten Stand ist.
- Ein Webserver für den Zugriff auf die Management API wird auf einem zufälligen Port unter einem geheimen und zufälligen Pfad gestartet.
- Ein selbst signiertes SSL-Zertifikat wird erstellt, sodass die Verwaltung des Outline-Servers mit TLS verschlüsselt werden kann, obwohl der Server keinen Domainnamen hat. Zusätzlich wird ein eindeutiger Fingerabdruck dieses Zertifikats erzeugt und im Outline-Manager gespeichert. So lassen sich MITM-Angriffe verhindern.

Die Outline-Installation muss nach der Installation nicht konfiguriert werden.

### Sicherheit des Servers

Outline ist eine Open-Source-Software, das heißt, jeder kann sich den Quellcode bei GitHub ansehen und ihn verbessern, um eventuelle Schwachstellen zu beheben. Der Quellcode ist bei

gehostet.

Alle installierten Outline-Server werden automatisch aktualisiert, sobald eine neue Version verfügbar ist, damit keiner mit einer veralteten Version der Software betrieben wird.

Die Verwaltung der Zugriffsschlüssel erfolgt durch das Zusammenspiel des Outline-Managers mit einem Verwaltungsdienst auf dem Outline-Server. Letzterer wird von einem geheimen, eindeutigen Pfad aus über einen nach dem Zufallsprinzip ausgewählten Port ausgeführt. Der Dienst kann nicht ausgeforscht werden, weil nur Abfragen beantwortet werden, die den entsprechenden geheimen Pfad enthalten. Zusätzlich ist sämtliche Kommunikation mit dem Verwaltungsdienst mithilfe eines

verschlüsselt.

Selbst durch Manipulationen von Outline-Servern lassen sich keine Nutzerdaten offenlegen, da auf den Servern keine Protokolle gespeichert werden.

Outline wurde im Jahr 2018 von

und

geprüft.

### Handling von UPD-Traffic

Outline kann als systemweites VPN betrieben werden. Das bedeutet, dass der gesamte UDP-Traffic über den Outline-Server geleitet wird.

### DNS-Traffic

In Outline erfolgen alle DNS-Lookups über den Outline-Server. Dabei wird dieselbe Verschlüsselung verwendet wie bei allen anderen Netzwerkaktivitäten. Alle Ihre DNS-Abfragen werden über den Outline-Server an den Dyn Internet Guide oder an OpenDNS weitergeleitet.

Ihre DNS-Lookups werden zu keiner Zeit von Outline protokolliert.
