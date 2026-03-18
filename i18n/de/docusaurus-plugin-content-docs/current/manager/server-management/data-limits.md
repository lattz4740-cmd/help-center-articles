---
title: "Wie richte ich Datenlimits für Zugriffsschlüssel ein?"
sidebar_label: "Wie richte ich Datenlimits für Zugriffsschlüssel ein?"
---

Sie können ein Datenlimit konfigurieren, das für alle Zugriffsschlüssel gilt. Öffnen Sie dazu Outline-Manager und gehen Sie zu den Einstellungen. Hier sehen Sie die Ein/Aus-Schaltfläche „Datenlimits“, mit der Sie ein Limit festlegen können.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Anschließend können Sie auf der Übersichtsseite zu den Zugriffsschlüsseln an den zugehörigen Balken sehen, wie nah jeder Nutzer am Limit ist. Je mehr vom zugewiesenen Datenkontingent bereits aufgebraucht ist, desto weiter sind die Balken gefüllt.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Sie können aber nicht nur ein für alle Zugriffsschlüssel geltendes Limit festlegen, sondern auch spezielle Datenlimits für einzelne Schlüssel. Das über diese Einstellung konfigurierte Limit überschreibt das von Ihnen festgesetzte Standardlimit. Selbst wenn Sie kein allgemeines Limit festgelegt haben, können Sie für einzelne Schlüssel jeweils eine eigene Beschränkung angeben. 

 Wenn Sie für einen Schlüssel ein Datenlimit festlegen möchten, öffnen Sie Outline-Manager, gehen Sie zum Tab „Verbindungen“ und klicken Sie rechts neben dem entsprechenden Schlüssel auf das Menü. Klicken Sie auf „Datenlimit“. Um das Datenlimit für „Mein Zugriffsschlüssel“ zu ändern, klicken Sie auf das Symbol „Datenlimits“ ![Data limits icon](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Wählen Sie „Benutzerdefiniertes Datenlimit festlegen“ aus. Sobald Sie das Häkchen gesetzt haben, wird Ihnen ein Feld angezeigt, in dem Sie das gewünschte Datenlimit angeben können. Zum Abschließen der Aktion klicken Sie auf SPEICHERN.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Wenn Sie die Datenlimits für die ausgewählten Schlüssel gespeichert haben, werden die festgelegten Beschränkungen auf der Hauptseite zusammen mit der Datennutzung in den letzten 30 Tagen für die einzelnen Schlüssel angezeigt.

Wenn Sie ein festgelegtes Datenlimit für einen Zugriffsschlüssel wieder löschen möchten, gehen Sie bei dem entsprechenden Schlüssel zum Fenster „Datenlimit“, entfernen Sie das Häkchen bei „Benutzerdefiniertes Datenlimit festlegen“ und klicken Sie auf SPEICHERN.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****FAQs zu Datenlimits****

****Was ist ein abhängiges Datenlimit auf Grundlage der letzten 30 Tage?****

 Das Datenlimit für die einzelnen Zugriffsschlüssel wird auf Grundlage der Datennutzung in den letzten 30 Tagen berechnet. Das Limit eines Schlüssels gilt also für den gesamten Zeitraum von 30 Tagen, auch bei Kalendermonaten mit 30 oder weniger Tagen. Das heißt, dass zu den für einen Nutzer verfügbaren Daten jeden Tag die Menge hinzugezählt wird, die er vor 31 Tagen genutzt hat.

**Welchen Vorteil haben abhängige Datenlimits?**

 Bei diesen Limits wird die Datennutzung immer für einen Zeitraum von 30 Tagen berechnet. Sie sind deshalb einfacher zu konfigurieren als wiederkehrende Limits (z. B. ein bestimmter Tag im Monat), bieten aber die gleiche Zuverlässigkeit. Außerdem stimmen die Werte so mit der Anzeige der Outline-Datennutzung sowie mit gängigen Tools wie Analysediensten und Serverstatistiken überein.

**Welche Daten werden auf das Kontingent des Datenlimits angerechnet?**

 Es wird der gesamte vom Server ausgehende Traffic gezählt. Genau genommen umfasst das alle Daten, die auf Anforderung des Schlüssels vom Server und zurück zum Client gesendet werden. In der Praxis sollte dies weitestgehend mit dem Traffic vom Schlüssel zum Server und zurück übereinstimmen – also mit der Menge der genutzten Daten Ihrer Nutzer. Wir haben uns für den ausgehenden Traffic als Messwert entschieden, da dieser von den Cloud-Anbietern in Rechnung gestellt wird, die an unserer Umfrage teilgenommen haben.

**Werden Nutzer benachrichtigt, wenn ihr Datenlimit erreicht ist?**

 Momentan nicht. Viele Cloud-Anbieter arbeiten mit Limits von beispielsweise 1 TB pro Monat. Das ermöglicht Konfigurationen wie etwa 10 Nutzer mit je 100 GB oder 100 Nutzer mit je 10 GB. Dies sind ziemlich hohe Limits und wir gehen davon aus, dass die Datenmenge in den meisten Fällen ausreichend ist. Nutzer, die ihr Datenlimit erreicht haben, sollten sich an den Serveradministrator wenden. Wir freuen uns aber über Ihr Feedback, wie nützlich solche Benachrichtigungen für Sie wären. Sie können uns [hier kontaktieren](/about/feedback).

**Werden Nutzer benachrichtigt, wenn ihr Datenlimit fast erreicht ist?**

 Die Menge an neuen Daten, die dem Nutzer zur Verfügung stehen, wird anhand der in den letzten 30 Tagen genutzten Daten berechnet und variiert deshalb von Tag zu Tag. Eine Benachrichtigung würde Nutzer daher wahrscheinlich eher verwirren und wäre nicht besonders hilfreich. [Hier können Sie uns dazu Feedback geben.](/about/feedback) Wir freuen uns über Ihren Beitrag.

**Kann ich die Datennutzung bei einzelnen Nutzern zurücksetzen?**

 Nein, die Datennutzung wird immer anhand der in den letzten 30 Tagen genutzten Daten berechnet. Sie können aber das Datenlimit für die Zugriffsschlüssel einzelner Nutzer verändern oder ihnen einen neuen Zugriffsschlüssel zuweisen.

**Wieso hatten einige Nutzer umgehend keinen Zugriff mehr, als ich Datenlimits aktiviert habe?**

 Das Kontingent für Datenlimits wird anhand der in den letzten 30 Tagen genutzten Daten berechnet. Auch wenn Sie keine Datenlimits festgelegt haben, wird die Datennutzung aufgezeichnet. Unter Umständen hatten die Nutzer das von Ihnen festgelegte Datenlimit bereits erreicht, bevor Sie die Funktion eingerichtet haben. Hinweis: Alle Datenlimits werden erzwungen, auch wenn Sie nur das Datenlimit bei einem einzigen Schlüssel ändern.

**Kann ich ein serverweites Limit festlegen, z. B. „1 TB für 30 Tage“?**

 Derzeit nicht. Wir freuen uns aber über Ihr Feedback. Wenn Sie uns einen Anwendungsfall schildern möchten, können Sie uns [hier kontaktieren](/about/feedback).

**Falls sowohl ein Standardlimit als auch für einzelne Schlüssel geltende Datenlimits festgelegt wurden, welches Limit wird dann erzwungen?**

 Das für einzelne Schlüssel konfigurierte Limit überschreibt das von Ihnen festgesetzte Standardlimit.

**Kann ich für einzelne Schlüssel ein Limit festlegen, obwohl ich kein Standardlimit konfiguriert habe?**

 Ja. Selbst wenn Sie kein Standardlimit festgelegt haben, können Sie für einzelne Schlüssel jeweils ein eigenes Datenlimit angeben. Wenn Sie beispielsweise einen Schlüssel haben, der von mehreren Nutzern verwendet und möglicherweise weitergegeben wird, können Sie ein Datenlimit für ihn festlegen und so übermäßigen Datentraffic über diesen Schlüssel verhindern.
