---
title: Sicherheit und Datenschutz bei der Nutzung von Outline
sidebar_label: Sicherheit und Datenschutz bei der Nutzung von Outline
---

Sicherheit und Datenschutz bei der Nutzung von Outline

## So schützt Outline Ihre Online-Kommunikation

Der Internettraffic ist am anfälligsten für Überwachung, wenn er über Ihr lokales oder nationales Netzwerk läuft.

Outline trägt dazu bei, Ihre Kommunikation privat zu halten, indem es Ihren Internetverkehr während der Übertragung innerhalb Ihres nationalen Netzwerks verschlüsselt und die Verschlüsselung aufrechterhält, bis er den Outline-Server erreicht. Wenn der Traffic mit Outline verschlüsselt ist, können Netzwerkbeobachter weder die von Ihnen besuchten Websites noch die von Ihnen übertragenen Informationen überprüfen.

Outline kann Ihnen auch dabei helfen, den Zugriff auf sichere End-to-End-Kommunikationstools wiederherzustellen, die in Ihrem Land möglicherweise sonst nicht zugänglich sind.

## Verschlüsselungsstandards

Outline verschlüsselt die Kommunikation zwischen Ihrem Gerät und dem Outline-Server mit der 256-Bit-Chiffre Chacha2020 IETF Poly 1305 von AEAD. AEAD-Chiffren bieten Vertraulichkeit, Integrität und Authentizität und weisen eine hervorragende Leistung auf moderner Hardware auf.

## Sicherheitsüberprüfungen

Im Jahr 2018 wurde Outline von Radically Open Security und Cure53 geprüft, zwei unabhängigen Organisationen für digitale Sicherheit, die Software anhand der neuesten Sicherheitsstandards überprüfen. Radically Open Security führte 2022 ein zusätzliches Audit durch und Cure53 führte 2024 ein Audit des Outline SDK durch. Die Berichte können Sie hier nachlesen:

- [Radically Open Security Penetrationstestbericht (März 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Cure53 Pentest- und Auditbericht Jigsaw-Gliederung (Dezember 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Bericht zum Penetrationstest von Radically Open Security (Dezember 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Cure53-Pentestbericht Jigsaw Outline VPN SDK (Januar 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonyme Messwerte und Protokolle

Outline verfolgt die genutzte Bandbreite als «übertragene Bytes» für jeden Zugriffsschlüssel. Mithilfe dieser Informationen können Serveradministratoren ihre Bandbreitenabonnements bei ihren Cloud-Server-Anbietern nach Bedarf anpassen, können jedoch nicht die tatsächlichen Informationen sehen, die über den Outline-Server gelaufen sind.

Erfahren Sie mehr über die [Daten- und Informationssammlung](/about/data-collection) von Outline.

---

## Häufig gestellte Fragen zu Sicherheit und Datenschutz

## Kann Outline mich online anonym machen?

Nein, Outline ist kein Anonymitätstool. Outline schützt Ihre Privatsphäre vor potenziellen Netzwerk-Zuschauern.

Outline bietet Ihnen auf den von Ihnen besuchten Websites keine vollständige Anonymität, da Sie beim Anmelden und manchmal auch durch Techniken wie Browser-Fingerprinting dennoch identifiziert werden können. Für mobile Apps verfügen die meisten modernen Smartphones über APIs, die es installierten Apps ermöglichen, Ihren Standort unabhängig von Ihrem Proxy abzurufen, da sie auf das eingebettete GPS zurückgreifen können.

VPNs bieten im Allgemeinen einen wichtigen Schutz, insbesondere vor Internetüberwachung, doch der Online-Betrieb ist immer mit Risiken verbunden. Selbst bei Verwendung eines VPN kann ein ISP, wenn er Ihre Identität bereits kennt und Ihren Netzwerkverkehr beobachten kann, möglicherweise die IP-Adresse Ihres Outline-Servers ermitteln. Diese Informationen können verwendet werden, um den Zugriff auf den Outline-Server zu blockieren oder Nutzungsmuster zu ermitteln, z. B. wann Sie normalerweise online sind und möglicherweise Ihren ungefähren Standort.

## Kann jemand sagen, ob ich Outline verwende?

Möglich. Die Plattformen und Services, auf die Sie zugreifen, erkennen höchstwahrscheinlich, dass Ihre Verbindung von einem Cloud-Server kommt. Gelegentlich können sie daraus schliessen, dass Sie ein VPN verwenden, aber sie können den Inhalt Ihres Internettraffics nicht sehen.

## Schützt mich Outline vor allen möglichen Cyberbedrohungen?

Nein. Kein Tool schützt Sie vor allen möglichen Cyberbedrohungen. Outline ermöglicht Ihnen Zugriff auf das offene Internet und erhöht Ihre Privatsphäre durch die Verschlüsselung Ihres Traffics. Wir empfehlen Ihnen jedoch, zusätzliche Vorsichtsmassnahmen zu ergreifen, um sich vor anderen Arten von Angriffen wie Malware und Phishing zu schützen.

Um Ihre Online-Abwehr zu stärken, sollten Sie eine Zusammenarbeit mit dem Cybersicherheitsexperten Ihres Unternehmens in Betracht ziehen. Alternativ können Sie bei [Security Planner](https://securityplanner.org/) persönliche Beratung von führenden Sicherheitsexperten erhalten. Diese Website bietet Ihnen klare Anweisungen zur Auswahl der richtigen Cybersicherheitstools für Ihre Anforderungen.

Schauen Sie sich auch die anderen Cybersicherheitsprodukte von [Jigsaw](https://jigsaw.google.com/), sowie [Intra](https://getintra.org/), [Project Shield](https://g.co/shield), und [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?) an.

## Ist die Verwendung eines VPN legal?

Bitte überprüfen Sie Ihre lokalen Gesetze, Vorschriften und die Servicebedingungen des Cloud-Anbieters, den Sie nutzen möchten, bevor Sie Outline betreiben oder die App verwenden.
