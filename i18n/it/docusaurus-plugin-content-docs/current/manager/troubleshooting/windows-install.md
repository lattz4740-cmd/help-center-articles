---
title: "Perché non riesco a installare Outline Manager su Windows?"
sidebar_label: "Perché non riesco a installare Outline Manager su Windows?"
---

Potresti visualizzare questo messaggio di errore: "Sembra che Outline non sia installato correttamente. Prova a eseguire nuovamente l'installazione. Se non funziona, [inviaci un feedback](/about/feedback)."

Se utilizzi Outline su Windows, potresti occasionalmente riscontrare un errore imprevisto. Nella maggior parte dei casi è necessario eliminare l'adattatore TAP Outline (driver) e reinstallare Outline.

I passaggi potrebbero variare in base alla versione del sistema operativo Windows, ma puoi trovare di seguito una procedura generale per disinstallare l'adattatore TAP e Outline Manager e poi reinstallare Outline Manager.

1. Disinstalla l'adattatore TAP per Outline Manager
   1. Vai a **Gestione dispositivi**, quindi **Schede di rete**
   2. Trova il file "**TAP-Windows Adapter V9**" o l'adattatore TAP associato a Outline
   3. Disinstalla o elimina questo adattatore. Tieni presente che questa operazione potrebbe interessare altre app VPN installate.
2. Disinstalla Outline Manager
   1. Vai a **Programmi e funzionalità**, quindi seleziona **Disinstalla programma**
   2. Individua l'app Outline Manager e disinstallala
   3. [Scarica la versione più recente di Outline Manager](https://getoutline.org/get-started/#step-1) e reinstallala sul tuo dispositivo Windows. In questo modo dovresti installare automaticamente un nuovo adattatore TAP.

Se i problemi persistono, [contatta l'assistenza](/about/feedback).
