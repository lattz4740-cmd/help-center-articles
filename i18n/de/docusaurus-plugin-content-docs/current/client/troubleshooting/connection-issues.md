---
title: "Wieso kann ich keine Verbindung zum Outline-Dienst herstellen?"
sidebar_label: "Wieso kann ich keine Verbindung zum Outline-Dienst herstellen?"
---

## Wenn sich die Verbindung zu Outline nicht aufbauen lässt, kann das verschiedene Gründe haben:

- [**Ihr Gerät ist nicht mit dem Internet verbunden**](#Internetissues)**.**Die Netzwerkverbindung Ihres Geräts kann unterbrochen sein. In diesem Fall dauert es möglicherweise einen Moment, bis die Netzwerksymbole aktualisiert werden. Es kann auch sein, dass Ihr Gerät zwar mit dem lokalen Netzwerk verbunden, das Internet aber ausgefallen ist.
- **Die**[**Firewall Ihres Netzwerks blockiert den Zugriff**](#FirewallIssues)**auf den Outline-Server.**Das kommt häufig bei Verbindungen über ein öffentliches Netzwerk vor, z. B. wenn Sie das Netzwerk einer Bildungseinrichtung oder eines Unternehmens bzw. ein kostenloses WLAN nutzen.
- **Die**[**Firewall oder das Antivirenprogramm Ihres Geräts blockiert den Zugriff**](#SoftwareIssues)**auf den Outline-Server.**
- **Die**[**Geräteeinstellungen Ihres Smartphones**](#DeviceSettings)**müssen aktualisiert werden.**
- **Möglicherweise hat der Administrator den**[**Server heruntergefahren oder der Internetanbieter blockiert Ihre Anfrage**](#ServerIssues)**.**

Probleme mit der Internetverbindung:

## So können Sie testen, ob hier die Ursache liegt: {#Internetissues}
Deaktivieren Sie Outline und überprüfen Sie, ob die Internetverbindung wiederhergestellt wird.

- Falls ja, finden Sie unten weitere Optionen zur Fehlerbehebung.
- Falls nein, warten Sie bitte einige Minuten, um zu sehen, ob die Verbindungseinstellungen automatisch aktualisiert werden.

## So beheben Sie dieses Problem:

## Verbinden Sie Ihr Gerät wieder mit dem Internet:

1. Versuchen Sie, ein anderes Gerät mit demselben Netzwerk zu verbinden. Wenn das nicht funktioniert, ist das Netzwerk möglicherweise ausgefallen. In diesem Fall müssen Sie warten, bis es wieder verfügbar ist, oder den Fehler beheben.
2. Falls Sie ein anderes Gerät mit demselben Netzwerk verbinden können, probieren Sie mindestens einen der folgenden Schritte aus:
   1. Versetzen Sie das Gerät in den Flugmodus (nur Mobilgeräte).
   2. Starten Sie das Gerät neu.
   3. Schalten Sie das Gerät aus, warten Sie zwei Minuten und schalten Sie es dann wieder ein.

Probleme mit der Firewall eines Netzwerks:

## So können Sie testen, ob hier die Ursache liegt: {#FirewallIssues}
1. Trennen Sie die aktuelle LAN- oder WLAN-Verbindung.
2. Stellen Sie eine Verbindung zu einem anderen Netzwerk her, z. B. zu einem Mobilfunknetz.
3. Versuchen Sie noch einmal, die Verbindung zum Outline-Server herzustellen.

## Wenn der Versuch erfolgreich ist, liegt das Problem bei der Firewall.

## So beheben Sie dieses Problem:

Wenden Sie sich an den Netzwerkadministrator und bitten Sie ihn, den Zugriff auf den Outline-Server zu erlauben, oder verwenden Sie stattdessen weiterhin das andere Netzwerk.

## Probleme mit der Firewall oder dem Antivirenprogramm: {#SoftwareIssues}

## So können Sie testen, ob hier die Ursache liegt:

Versuchen Sie, über ein anderes Gerät eine Verbindung zu Outline herzustellen.

Hinweis: Dazu benötigen Sie auf dem anderen Gerät den Zugriffsschlüssel und die Outline App.

## So beheben Sie dieses Problem:

Überprüfen Sie in den Einstellungen Ihrer Firewall oder Antivirussoftware, ob VPN- und Outline-Traffic zugelassen wird.

## Geräteeinstellungen: {#DeviceSettings}

## Was Sie prüfen sollten:

Bei Android:

1. Öffnen Sie die App „Einstellungen“.
2. Suchen Sie die **VPN-Einstellungen** Ihres Geräts. Hier sollten alle VPN-Apps mit Zugriff auf Ihr Smartphone angezeigt werden.
3. Wenn Outline nicht in der Liste steht, deinstallieren Sie die Outline App und installieren Sie sie dann neu. Sobald Outline installiert ist, sollte die App über das Gerät automatisch Zugriff erhalten.

Auf Ihrem Android-Gerät darf kein Display-Overlay installiert sein. Durch eine solche App wird das Outline-Berechtigungsfenster unter Umständen in den Hintergrund verschoben und kann nicht im Vordergrund eingeblendet werden.

Rufen Sie auf Ihrem Android-Gerät „Einstellungen“ > „Apps“ > „Spezieller App-Zugriff“ auf. Tippen Sie dann auf „Über anderen Apps einblenden“. Anschließend können Sie diese Zugriffsberechtigung für alle Apps entfernen, die hier aufgelistet sind.

Bei iOS: Lesen Sie die Anleitung [in diesem Hilfeartikel](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Probleme mit dem Server: {#ServerIssues}

## So können Sie testen, ob hier die Ursache liegt:
Wenn Sie auf mehrere Server Zugriff haben, versuchen Sie, eine Verbindung zu einem anderen Server herzustellen.

So beheben Sie dieses Problem:

Erkundigen Sie sich beim Serveradministrator, ob der Server noch läuft. Falls ja, bitten Sie ihn um den [Zugriffsschlüssel](/about/terminology) eines anderen Servers.

Wenn Sie den Server selbst eingerichtet haben, versuchen Sie, über den Outline-Manager oder [eine andere Methode wie SSH](https://en.wikipedia.org/wiki/Secure_Shell) eine Verbindung herzustellen. Falls das nicht funktioniert, können Sie in der Konsole des Cloud-Anbieters, falls vorhanden, prüfen, ob der Server noch online ist.
