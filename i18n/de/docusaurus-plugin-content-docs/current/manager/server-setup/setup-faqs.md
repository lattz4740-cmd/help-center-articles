---
title: "Häufig gestellte Fragen zur Einrichtung des Outline-Servers"
sidebar_label: "Häufig gestellte Fragen zur Einrichtung des Outline-Servers"
---

**Kann ich Outline auch ohne Server nutzen?**

 Nein. Für Outline benötigen Sie Zugriff auf einen Server, der von Ihnen, von Ihrer Organisation oder von einem vertrauenswürdigen Drittanbieter verwaltet wird.

## Wie lange dauert es, einen Outline-Server einzurichten?

In den meisten Fällen weniger als 5 Minuten. Sie können Outline auf jedem Cloudserver installieren. Wir empfehlen jedoch DigitalOcean, da wir zusammen mit diesem Anbieter eine nutzerfreundliche Anleitung für die Installation entworfen haben, die in wenigen Klicks abgeschlossen ist und ganz ohne Skripts auskommt.

Für AWS, die GCP und die erweiterte Einrichtung haben wir die Serverinstallation mithilfe eines Skripts vereinfacht, das für die meisten Umgebungen verwendet werden kann.

## Wo kann ich einen Outline-Server einrichten?

Einen Outline-Server können Sie bei den meisten Cloudanbietern einrichten, ganz egal wo diese ihren Sitz haben.

Wir empfehlen die Einrichtung bei DigitalOcean, da dieser Anbieter Server an mehreren Standorten hat, z. B. in Amsterdam, Toronto, San Francisco und Singapur. Für die Installation bei einem anderen Cloud-Anbieter oder auf einem eigenen Server bietet der Outline-Manager den „Erweiterten Modus“ und ein Einrichtungsskript.

## Welchen Standort sollte ich für meinen Outline-Server wählen?

1. Beim Auswählen des Standorts des Outline-Servers sollten Sie Folgendes beachten:
2. Der Standort des Outline-Servers hat Auswirkungen auf den Internetzugriff der Nutzer. Befindet sich der Server z. B. in Amsterdam, wird den Nutzer das Internet so angezeigt wie in den Niederlanden. Manche Websites sind also auf Niederländisch. In den meisten Fällen können Sie das jedoch ändern, indem Sie eine andere Sprache auswählen.
3. Die Entfernung zwischen den Nutzern und dem Outline-Server beeinflusst die Internetgeschwindigkeit: Ganz allgemein kann sich die räumliche Entfernung zwischen Outline-Nutzern und dem Server auf die Geschwindigkeit des Internets auswirken. In den meisten Fällen können Sie einen Serverstandort auswählen, der sich in der Nähe Ihrer erwarteten Nutzer befindet. Ansonsten können Sie auch [auf dieser Karte](https://www.submarinecablemap.com/) nachsehen, welche Untersee-Internetkabel mit Ihrem Land oder Ihrer Region verbunden sind.
4. Der Standort des VPN-Servers kann Einfluss auf die rechtlichen Rahmenbedingungen haben. In Outline wird Ihr Traffic nicht protokolliert. [Weitere Informationen zu Sicherheit und Datenschutz beim Verwenden von Outline](/about/security-and-privacy)
