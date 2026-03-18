---
title: "Kā atjaunināt Outline servera programmatūru?"
sidebar_label: "Kā atjaunināt Outline servera programmatūru?"
---

Outline serveri automātiski tiek atjaunināti ar visjaunākajiem drošības uzlabojumiem, tādējādi jūs vienmēr izmantojat jaunāko Outline tehnoloģiju. Automātisku atjaunināšanu nodrošina [Watchtower](https://github.com/v2tec/watchtower) — atklātā pirmkoda bibliotēka, kas regulāri pārbauda un atjaunina Docker attēlu, kurā ir ietverta Outline programmatūra.

Turklāt, ja instalējat Outline, izmantojot Outline pārvaldnieku, mēs iestatīsim “cron” uzdevumu, lai serverī esošā programmatūra tiktu automātiski atjaunināta, izmantojot funkciju [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu), un tiktu veikta atkārtota palaišana, kad tas ir nepieciešams. Ņemiet vērā, ka šis uzdevums netiek izmantots izvērstajā režīmā. Tas netiek darīts, lai tiktu saglabāta esošā konfigurācija, jo tiek pieņemts, ka saimniekdators tiek izmantots ne tikai Outline palaišanai, bet arī citiem mērķiem.
