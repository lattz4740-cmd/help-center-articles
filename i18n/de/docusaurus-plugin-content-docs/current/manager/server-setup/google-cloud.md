---
title: Google Cloud – automatisierte Einrichtung
sidebar_label: Google Cloud – automatisierte Einrichtung
---

## Übersicht

Mit Outline-Manager können Sie automatisch einen Outline-Server auf einem Server in Google Cloud konfigurieren. Wenn Sie diese Funktion verwenden möchten, werden Sie aufgefordert, sich mit Ihrem Google-Konto anzumelden. Dabei werden Ihrer lokalen Installation von Outline-Manager bestimmte [OAuth-Berechtigungen](https://developers.google.com/identity/protocols/oauth2) für die Konfiguration Ihres Google Cloud-Kontos zugewiesen.

 Wenn Sie diese Berechtigungen nicht gewähren möchten, können Sie der Einrichtungsanleitung in Outline-Manager folgen, um Outline auf der Google Cloud Platform auszuführen.

## Gewährte Berechtigungen

Für die automatisierte Einrichtung sind in Outline-Manager die unten genannten Berechtigungen erforderlich.

## Google Cloud Platform

- Google Compute Engine-Ressourcen abrufen und verwalten
- Ihre Daten aus allen Google Cloud-Diensten aufrufen und die E-Mail-Adresse Ihres Google-Kontos sehen

## Grundlegende Kontoinformationen

- Primäre E‑Mail-Adresse für das Google-Konto abrufen
- Ihr Profil Ihren persönlichen Daten auf Google zuordnen

## Weitere Zugriffsberechtigungen

- Cloud Platform-Projekte verwalten
- Google Cloud Platform-Rechnungskonten abrufen und verwalten
- Servicekonfiguration der Google API verwalten

Damit werden diese erweiterten Funktionen zur Verwaltung der Outline-Server unterstützt:

- Auswahl des richtigen Rechnungskontos
- Neues Projekt zum Organisieren der Outline-Server erstellen
- Verfügbare Rechenzentren auflisten
- Neue virtuelle Maschinen erstellen, um Outline auszuführen
- Neue virtuelle Maschinen mit Outline konfigurieren

## Berechtigungen aufheben

Sie können den Zugriff auf die Google Cloud Platform für Outline-Manager über [Mein Konto](https://myaccount.google.com/permissions) widerrufen. In diesem Fall werden alle Server, die Sie mit der automatisierten Einrichtung erstellt haben, weiterhin ausgeführt, sind aber nicht mehr in Outline-Manager zu sehen. Wenn Sie den Zugriff darauf wiederherstellen möchten, verbinden Sie sich einfach wieder mit der Google Cloud Platform. Starten Sie dazu den automatisierten Einrichtungsvorgang.

## Outline – Projektorganisation

Bei der automatisierten Google Cloud-Einrichtung wird ein einzelnes [Google Cloud-Projekt](https://cloud.google.com/resource-manager/docs/creating-managing-projects) verwendet, um Ihre Outline-Server zu organisieren. Das Projekt wird beim ersten Verwenden der automatisierten Einrichtung mit einer vorgeschlagenen Projekt-ID erstellt, die mit „Outline-“ beginnt, gefolgt von einer Reihe zufälliger Zeichen. Sie können jedoch auch eine andere Projekt-ID angeben. Das Projekt erhält den Namen „Outline-Server“.

## Rechnungskonto

Für Google Cloud-Projekte ist ein verknüpftes Rechnungskonto erforderlich, in dem die Zahlungsinformationen definiert sind. Wenn Sie die automatisierte Einrichtung von Google Cloud erstmals verwenden, werden Sie aufgefordert, ein Rechnungskonto anzugeben, das mit Ihren Outline-Servern verknüpft wird. Manchmal wird ein Server aufgrund eines Problems mit dem Rechnungskonto nicht weiter ausgeführt. Melden Sie sich in diesem Fall in der [Google Cloud Console](https://console.cloud.google.com/getting-started) an und suchen Sie das mit Outline verknüpfte Google Cloud-Projekt (mit dem Namen „Outline-Server“). Aktualisieren Sie dann die Abrechnungseinstellungen.

## Server löschen

Wenn Sie Ihre Server löschen möchten, die mit der automatisierten Einrichtung erstellt wurden, verwenden Sie dafür am einfachsten Outline-Manager. Möchten Sie die Server lieber selbst löschen, melden Sie sich in der [Google Cloud Console](https://console.cloud.google.com/getting-started) an und rufen Sie das Projekt auf, das bei der Ersteinrichtung erstellt wurde (mit dem Namen „Outline-Server“). Anschließend können Sie entweder die Ressourcen löschen oder das Projekt schließen.
