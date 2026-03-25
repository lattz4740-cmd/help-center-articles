---
title: "Hvernig uppfæri ég Outline-netþjónahugbúnaðinn?"
sidebar_label: "Hvernig uppfæri ég Outline-netþjónahugbúnaðinn?"
---

Outline-þjónar uppfærast sjálfkrafa með nýjustu öryggisúrbótunum svo þú keyrir alltaf nýjustu tækni Outline. Sjálfvirka uppfærsluferlið er virkjað með [Watchtower](https://github.com/containrrr/watchtower) sem er safn með opinn kóða sem athugar og uppfærir docker-myndina sem inniheldur Outline-hugbúnaðinn reglulega.

Þegar þú setur upp Outline með Outline Manager setjum við auk þess upp cron-verk til að uppfæra hugbúnaðinn sjálfkrafa á þjóninum með [eftirlitslausum uppfærslum](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) og endurræsa hann þegar þess þarf. Athugaðu að þetta gerist ekki í ítarlegri stillingu til að varðveita núverandi stillingu að því gefnu að hýsillinn sé einnig notaður í öðrum tilgangi en að keyra Outline.
