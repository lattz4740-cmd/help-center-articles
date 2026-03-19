---
title: "Come faccio a impostare limiti dati sulle chiavi di accesso?"
sidebar_label: "Come faccio a impostare limiti dati sulle chiavi di accesso?"
---

Puoi impostare un limite dati che verrà applicato a tutte le chiavi di accesso. Per impostare il limite, apri Outline Manager e vai alle Impostazioni. Vedrai un pulsante di attivazione/disattivazione dei Limiti dati che, se abilitato, consente di impostare un limite.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Una volta impostato un limite, puoi vedere quanto ogni utente ci si avvicina nella pagina delle chiavi di accesso, dove un grafico a barre mostra l'utilizzo dei dati negli ultimi 30 giorni.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Oltre a poter impostare un limite per tutte le chiavi di accesso, puoi assegnare a ogni chiave il proprio limite dati. Questa impostazione sovrascriverà qualsiasi limite dati predefinito che hai impostato. Se non l'hai fatto, puoi comunque impostare un limite dati per qualsiasi chiave. 

 Per impostare un limite di trasferimento di dati di una chiave, apri Outline Manager, vai alla scheda Connessioni che contiene la chiave che vuoi impostare e fai clic sul menu sul lato destro della riga della chiave. Da qui, fai clic su Limite dati. Per modificare il limite dati su "La mia chiave di accesso", fai clic sull'icona Limiti dati ![Questa immagine non è disponibile perché non disponi dei privilegi per visualizzarla oppure perché è stata rimossa dal sistema](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Seleziona Imposta un limite dati personalizzato. Una volta selezionata questa casella di controllo, verrà visualizzato un campo dove puoi impostare un limite dati personalizzato per quella determinata chiave. Fai clic sul pulsante SALVA quando hai terminato per salvare il limite dati.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Dopo aver salvato il limite di trasferimento di dati per la chiave scelta, il limite verrà visualizzato sulla schermata principale insieme all'utilizzo dei dati (negli ultimi 30 giorni) per ogni chiave.

Per rimuovere il limite dati da una chiave di accesso, vai alla finestra di dialogo Limite dati della chiave come fatto in precedenza, deseleziona la casella denominata Imposta un limite dati personalizzato e fai clic sul pulsante SALVA.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## **Domande frequenti sui limiti dati**
## **Cosa si intende per limite dati cumulativo per 30 giorni?**
 Un limite dati cumulativo per 30 giorni conteggia l'utilizzo di ciascuna chiave negli ultimi 30 giorni e lo mantiene al di sotto del limite impostato per questo periodo. Di conseguenza, la chiave non può superare il limite durante qualsiasi periodo di 30 giorni, inclusi i mesi di calendario di 30 giorni o meno. In pratica, ciò significa che i dati disponibili di ogni utente aumenteranno ogni giorno della quantità utilizzata il 31° giorno precedente.

## Perché Outline utilizza i limiti cumulativi?
 I limiti cumulativi offrono delle garanzie ogni 30 giorni, il che significa che sono più semplici da configurare rispetto a un limite ricorrente (come un giorno del mese personalizzabile), fornendo comunque garanzie simili. Corrispondono anche alla visualizzazione esistente dell'utilizzo dei dati di Outline, nonché a strumenti comuni come i servizi di analisi e le statistiche dei server.

## Quali dati vengono conteggiati in un limite dati?
 Viene incluso nel conteggio il traffico in uscita dal server di ciascuna chiave di accesso. Per la precisione, si intendono i dati inviati per conto della chiave all'esterno del server e che ritornano al client. In pratica, questo processo dovrebbe essere strettamente allineato al traffico inviato dalla chiave al server e viceversa e dovrebbe corrispondere pertanto ai conteggi dati dei tuoi utenti. Abbiamo scelto il traffico in uscita perché è quello fatturato dai provider cloud intervistati.

## Gli utenti ricevono una notifica al superamento del limite dati?
 Al momento no. Molti provider cloud prevedono un limite, ad esempio 1 TB per l'intero mese, che può supportare 10 utenti a 100 GB o 100 utenti a 10 GB. Si tratta di quantità piuttosto elevate e pensiamo sia difficile raggiungerle per molti utenti, ma se ciò accadesse ci auguriamo che contattino i gestori del server. In ogni caso saremmo lieti di sapere come le notifiche potrebbero aiutarti per il tuo caso d'uso; puoi contattarci [qui](/about/feedback).

## Gli utenti ricevono una notifica se si avvicinano al limite dati?
 La quantità di nuovi dati ricevuti da un utente che sta per raggiungere il limite varia da un giorno all'altro perché si basa sull'utilizzo al 30° giorno precedente. Riteniamo che sia più probabile che un avviso possa confondere gli utenti finali piuttosto che aiutarli. Saremmo lieti di ricevere il tuo feedback in merito a questo approccio [qui](/about/feedback).

## Posso reimpostare l'utilizzo dei dati di un utente?
 No, il limite di un utente include sempre l'utilizzo dei dati degli ultimi 30 giorni. Tuttavia, puoi aumentare il limite dati della chiave o creare una nuova chiave per l'utente in questione.

## Perché alcuni dei miei utenti hanno perso l'accesso nel momento in cui ho abilitato i limiti dati?
 I limiti dati si basano sul trasferimento di dati degli utenti nei 30 giorni precedenti, che viene registrato indipendentemente dal fatto che i limiti dati siano stati abilitati o meno. È possibile che gli utenti in questione avessero già superato il limite prima che fosse attivato. Inoltre, tieni presente che vengono applicati tutti i limiti dati, anche quando si modifica il limite dati di una singola chiave.

## Posso impostare un limite a livello di server, ad esempio "1 TB per 30 giorni"?
 Al momento no. Siamo lieti di ricevere ulteriori informazioni sul tuo caso d'uso [qui](/about/feedback).

## Se esiste un limite dati predefinito e un limite dati su una chiave specifica, quale verrà applicato?
 Il limite dati della chiave specifica sovrascriverà qualsiasi limite dati predefinito (se presente) che hai impostato.

## Posso impostare un limite dati per una chiave specifica senza impostare un limite dati predefinito?
 Sì. Non è necessario definire un limite predefinito per impostare un limite dati su una chiave. Ad esempio, potresti impostare un limite su una chiave che ritieni possa essere condivisa ampiamente per proteggerti da un trasferimento di dati eccessivo attraverso quella chiave.
