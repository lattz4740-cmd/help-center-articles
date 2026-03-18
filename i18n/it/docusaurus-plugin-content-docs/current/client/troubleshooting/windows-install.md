---
title: "Perché non riesco a installare il client Outline su Windows?"
sidebar_label: "Perché non riesco a installare il client Outline su Windows?"
---

Potresti visualizzare questo messaggio di errore: "Sembra che Outline non sia installato correttamente. Prova a eseguire nuovamente l'installazione. Se non funziona, [inviaci un feedback](https://support.getoutline.org/s/contactsupport)".

Se utilizzi Outline su Windows, potresti occasionalmente riscontrare un errore imprevisto. Nella maggior parte dei casi è necessario eliminare l'adattatore TAP Outline (driver) e reinstallare Outline.

I passaggi potrebbero variare in base alla versione del sistema operativo Windows, ma puoi trovare di seguito una procedura generale per disinstallare l'adattatore TAP e Outline e poi reinstallare Outline.

1. Disinstalla l'adattatore TAP per il client Outline
   1. Vai a **Gestione dispositivi**, quindi **Schede di rete**.
   2. Trova il file **TAP-Windows Adapter V9** o l'adattatore TAP associato a Outline.
   3. Disinstalla o elimina questo adattatore. Tieni presente che questa operazione potrebbe interessare altre app VPN installate.
2. Disinstalla il client Outline
   1. Vai a **Programmi e funzionalità**, quindi seleziona **Disinstalla programma**.
   2. Individua l'app del client Outline e disinstalla il client Outline.
   3. [Scarica la versione più recente del client Outline](https://getoutline.org/get-started/#step-3) e reinstallala sul tuo dispositivo Windows. In questo modo dovresti installare automaticamente un nuovo adattatore TAP.

Se i problemi persistono, [contatta l'assistenza](https://support.getoutline.org/s/contactsupport).
