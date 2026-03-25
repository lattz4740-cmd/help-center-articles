---
title: "Jak zaktualizować oprogramowanie serwera Outline?"
sidebar_label: "Jak zaktualizować oprogramowanie serwera Outline?"
---

Serwery Outline automatycznie instalują najnowsze poprawki zabezpieczeń, więc zawsze korzystasz z aktualnych rozwiązań. Automatyczne aktualizacje są możliwe dzięki usłudze [Watchtower](https://github.com/containrrr/watchtower) – bibliotece typu open source, która regularnie sprawdza i aktualizuje znajdujące się w rejestrze Docker obrazy obejmujące oprogramowanie Outline.

Co więcej, jeśli zainstalujesz Outline za pomocą Menedżera Outline, utworzymy zadanie cron, aby automatycznie aktualizować oprogramowanie na serwerze przy użyciu funkcji [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) i uruchamiać go ponownie w razie potrzeby. Pamiętaj, że nie następuje to w trybie zaawansowanym, aby zachować istniejącą konfigurację, ponieważ zakłada się, że host jest używany do innych celów poza uruchamianiem Outline.
