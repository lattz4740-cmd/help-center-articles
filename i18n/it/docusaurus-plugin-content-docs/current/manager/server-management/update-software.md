---
title: "Come faccio ad aggiornare il software server Outline?"
sidebar_label: "Come faccio ad aggiornare il software server Outline?"
---

I server Outline vengono aggiornati automaticamente apportando gli ultimi miglioramenti in termini di sicurezza in modo da farti utilizzare sempre la tecnologia Outline più recente. Il processo di aggiornamento automatico è attivato da [Watchtower](https://github.com/v2tec/watchtower), una raccolta open source che controlla e aggiorna regolarmente l'immagine Docker che contiene il software Outline.

Inoltre, quando installi Outline utilizzando Outline Manager, configureremo un cron job che esegue automaticamente l'upgrade del software sul server utilizzando gli

(Ubuntu) ed eseguendo il riavvio quando necessario. Tieni presente che questo non avviene nella modalità avanzata per preservare la configurazione esistente, partendo dal presupposto che l'host viene utilizzato per altri scopi oltre all'esecuzione di Outline.
