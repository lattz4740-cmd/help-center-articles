---
title: Configurazione automatica di Google Cloud
sidebar_label: Configurazione automatica di Google Cloud
---

## Panoramica
Outline Manager include una funzionalità che consente di configurare automaticamente il server Outline su un server in esecuzione su Google Cloud. Se decidi di utilizzare questa funzionalità, Outline Manager ti chiederà di accedere con il tuo Account Google, concedendo determinate autorizzazioni[OAuth](https://developers.google.com/identity/protocols/oauth2) alla tua installazione locale di Outline Manager per la configurazione del tuo account Google Cloud.
Se non vuoi fornire queste autorizzazioni, puoi seguire le istruzioni di configurazione avanzate in Outline Manager per eseguire Outline su Google Cloud Platform.
## Autorizzazioni concesse
Per offrire la configurazione automatica, Outline Manager richiede le seguenti autorizzazioni da parte del tuo Account Google.
## Google Cloud Platform
Visualizzare e gestire le risorse Google Compute Engine


Visualizzare i tuoi dati in tutti i servizi Google Cloud e vedere l'indirizzo email del tuo Account Google


## Informazioni di base sull'account
Visualizzare l'indirizzo email principale del tuo Account Google


Associarti alle tue informazioni personali su Google


## Accesso aggiuntivo
Gestire i progetti Cloud Platform


Visualizzare e gestire account di fatturazione Google Cloud Platform


Gestire la configurazione del servizio Google API


Queste autorizzazioni ci consentono di supportare funzionalità avanzate per la gestione dei server Outline, tra cui:


Possibilità di selezionare l'account di fatturazione corretto


Creazione di un nuovo progetto per organizzare i server Outline


Elenco dei data center disponibili


Creazione di nuove macchine virtuali per eseguire Outline


Configurazione della nuova macchina virtuale con Outline


## Revoca delle autorizzazioni
Puoi revocare l'accesso a Google Cloud Platform per Outline Manager dalla pagina[Account personale](https://myaccount.google.com/permissions). Se revochi l'accesso, i server che hai creato con la configurazione automatica rimarranno in esecuzione, ma non verranno più visualizzati in Outline Manager. Per ripristinare l'accesso, riconnettiti a Google Cloud Platform avviando il flusso di configurazione automatica.
## Organizzazione di un progetto Outline
La configurazione automatica di Google Cloud utilizza un singolo[progetto Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) per organizzare i server Outline. Il progetto viene creato durante il primo utilizzo della configurazione automatica, con un ID progetto suggerito che inizia con "Outline-", seguito da una stringa di caratteri casuali. Se preferisci, puoi scegliere un ID progetto diverso in fase di creazione. Il nome del progetto sarà "Server Outline".
## Account di fatturazione
I progetti Google Cloud richiedono un "account di fatturazione" collegato che definisce i dati di pagamento. Quando utilizzi per la prima volta la configurazione automatica di Google Cloud, ti viene chiesto di specificare un account di fatturazione da associare ai tuoi server Outline. A volte l'esecuzione di un server si interrompe perché si è verificato un problema con l'account di fatturazione. In questo caso, devi accedere a[Google Cloud Console](https://console.cloud.google.com/getting-started), individuare il progetto Google Cloud associato ad Outline (denominato "Server Outline") e aggiornare le impostazioni di fatturazione.
## Eliminazione dei server
Se vuoi eliminare i server creati con la configurazione automatica, il modo più semplice per farlo è utilizzare Outline Manager. Tuttavia, se vuoi eliminare i server autonomamente, puoi accedere a[Google Cloud Console](https://console.cloud.google.com/getting-started), trovare il progetto creato durante la configurazione iniziale (denominato "Server Outline") ed eliminare le risorse in quella posizione o cancellare il progetto.
