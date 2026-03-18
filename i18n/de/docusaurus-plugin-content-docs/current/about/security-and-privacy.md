---
title: Sicherheit und Datenschutz beim Verwenden von Outline
sidebar_label: Sicherheit und Datenschutz beim Verwenden von Outline
---

Sicherheit und Datenschutz beim Verwenden von Outline

## Schutz Ihrer Onlinekommunikation mithilfe von Outline

Bei Internettraffic ist das Risiko einer unbefugten Überwachung am größten, während die Daten über lokale oder nationale Netzwerke übertragen werden.

Mit Outline bleiben Ihre Unterhaltungen privat, da Ihr gesamter Internettraffic während der Übertragung verschlüsselt ist und erst am Outline-Server entschlüsselt wird. Die Verschlüsselung verhindert, dass Dritte im Netzwerk sehen können, welche Websites Sie besuchen oder welche Informationen Sie mit anderen austauschen.

Zusätzlich können Sie mit Outline möglicherweise wieder Tools für sichere Ende-zu-Ende-Kommunikation nutzen, die ansonsten in Ihrem Land womöglich nicht zugänglich sind.

## Verschlüsselungsstandards

Die Kommunikation zwischen Ihrem Gerät und dem Outline-Server wird mithilfe von AEAD 256‑bit Chacha2020 IETF Poly 1305 verschlüsselt. Die AEDAD-Verschlüsselungen bieten Vertraulichkeit, Integrität, Authentizität und exzellente Performance auf moderner Hardware.

## Sicherheitsprüfungen

Im Jahr 2018 wurde Outline von Radically Open Security und Cure53 geprüft, zwei unabhängigen Organisationen für digitale Sicherheit, die Software nach den neuesten Sicherheitsstandards prüfen. Radically Open Security führte 2022 eine weitere Prüfung durch und Cure53 führte 2024 eine Prüfung des Outline SDK durch. Die Ergebnisse finden Sie in folgenden Berichten:

- [Radically Open Security Penetration Test Report (März 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (Dezember 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (Dezember 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (Januar 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonyme Messwerte und Logs

In Outline wird für jeden Zugriffsschlüssel nur die verwendete Bandbreite als „Übertragene Bytes“ erfasst. Administratoren können mit diesen Daten das Bandbreitenabo beim Cloudanbieter anpassen, haben aber keinen Einblick in die Informationen, die über den Outline-Server übertragen wurden.

[Weitere Informationen](/about/data-collection)

---

## Häufig gestellte Fragen (FAQ) zu den Themen Sicherheit und Datenschutz

## Bin ich mit Outline im Internet anonym?

Nein, Outline macht Sie nicht anonym. Durch dieses Tool schützen Sie lediglich Ihre Daten vor Überwachung.

Mit Outline können Sie Websites nicht vollständig anonym besuchen, denn Sie sind noch immer identifizierbar, sei es durch Anmeldungen oder mithilfe von Techniken wie Browser-Fingerprinting. Das gilt auch bei mobilen Apps, denn die meisten modernen Smartphones haben APIs, über die installierte Apps Ihren Standort abfragen können. Da hierzu das integrierte GPS verwendet wird, sind Proxys wirkungslos.

Virtuelle private Netzwerke (virtual private networks, VPNs) bieten zwar wichtigen Schutz, besonders vor Überwachung im Internet, aber das Internet zu nutzen bleibt dennoch immer ein Risiko. Wenn ein Internetanbieter bereits Ihre Identität kennt und den Traffic überwachen kann, ist es selbst in einem VPN möglich, die IP-Adresse Ihres Outline-Servers zu ermitteln. Diese Information kann genutzt werden, um den Zugriff auf den Server zu blockieren oder Nutzungsmuster zu ermitteln, die Rückschlüsse auf Ihre typischen Onlinezeiten und sogar Ihren ungefähren Standort erlauben.

## Kann man erkennen, dass ich Outline verwende?

Eventuell. Bei Plattformen und Diensten, auf die Sie zugreifen, wird möglicherweise festgestellt, dass Ihre Verbindung von einem Cloudserver ausgeht. Manchmal ist auch erkennbar, dass Sie ein VPN verwenden. Der Inhalt Ihres Internettraffics ist jedoch nicht sichtbar.

## Schützt mich Outline vor allen Gefahren im Internet?

Nein, denn das kann ein Tool alleine gar nicht leisten. Mit Outline sind Ihre Daten trotz uneingeschränktem Internetzugriff deutlich besser geschützt, da der Traffic verschlüsselt ist. Dennoch empfiehlt es sich, zusätzliche Maßnahmen gegen andere Arten von Angriffen zu treffen, z. B. gegen Malware und Phishing.

Hierbei sollten Sie mit dem Experten für Cybersicherheit in Ihrer Organisation zusammenarbeiten. Sie können sich aber auch über die Website [Security Planner](https://securityplanner.org/) persönlich von führenden Sicherheitsexperten beraten lassen. Dort erhalten Sie klare Hilfestellungen, um die für Sie passenden Cybersecurity-Tools zu finden.

Auch die anderen [Jigsaw-Produkte](https://jigsaw.google.com/) für Cybersicherheit sind einen Blick wert, z. B. [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) und die [Passwort-Warnung](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Ist die Nutzung eines VPNs legal?

Bitte informieren Sie sich über die an Ihrem Standort geltende Gesetze und Bestimmungen sowie die Nutzungsbedingungen des verwendeten Cloudanbieters, bevor Sie Outline und den Outline-Manager verwenden.
