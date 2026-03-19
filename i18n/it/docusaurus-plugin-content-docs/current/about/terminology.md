---
title: Terminologia
sidebar_label: Terminologia
---

## Che cos'è una VPN?
 Una rete privata virtuale (VPN) è una connessione privata tra i tuoi dispositivi e un server host. Quando usi una VPN, il traffico è nascosto dal provider internet. Puoi utilizzare una VPN nei seguenti scenari:

- Per proteggere i tuoi dati quando utilizzi una rete Wi-Fi pubblica
- Per mantenere privati i tuoi dati di navigazione dal provider internet e dagli enti statali
- Per accedere a contenuti non censurati da diverse origini in tutto il mondo

## Sotto quali aspetti Outline si differenzia dalle reti VPN tradizionali?
 I provider internet possono rilevare e bloccare le VPN tradizionali senza troppe difficoltà, riconoscendo i protocolli di sicurezza comuni e/o gli schemi relativi ai volumi di traffico. Essendo basato su un protocollo appositamente progettato per essere difficilmente rilevabile e di conseguenza più complesso da bloccare, Outline è più resiliente rispetto alle VPN tradizionali. Inoltre, Outline resiste a sofisticate forme di censura, come il blocco basato su rete o il blocco degli IP.

## Che cos'è un server Outline?
 Un server Outline fa funzionare la VPN a cui si collegheranno gli utenti autorizzati. Se intendi creare una nuova rete, puoi utilizzare un server sicuro proprietario come server Outline, se ne hai uno. In caso contrario, puoi servirti di un fornitore di servizi cloud, come ad esempio:

- DigitalOcean
- Piattaforma Google Cloud
- Amazon Web Services (AWS)

Il server dovrà essere configurato in Outline Manager.

## Che cosa si intende per gestore del servizio? {#servicemanager}
 Il gestore del servizio è la persona responsabile della configurazione del server Outline e della condivisione delle chiavi di accesso con gli utenti. In genere il gestore del servizio è la persona che sostiene i costi connessi con l'utilizzo del server. 

## Che cos'è una chiave di accesso? {#accesskey}
 Una chiave di accesso viene utilizzata per accedere a un server Outline esistente e collegarsi alla VPN. La chiave di accesso ti verrà fornita da un [gestore del servizio](#servicemanager). In alternativa, hai la possibilità di [configurare un server Outline](/manager/server-setup/setup-server) autonomamente. Di seguito puoi vedere un esempio tipico di chiave di accesso (solo a scopo di esempio, non funzionante): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Che cos'è Outline Manager?
 Outline Manager è un'applicazione desktop che consente a un gestore del servizio di configurare un server Outline, generare [chiavi di accesso](#accesskey) e impostare limiti dati per l'utilizzo da applicare alle singole chiavi. Puoi scaricare l'ultima versione di Outline Manager [qui](https://getoutline.org/get-started/#step-3) o [qui](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Che cos'è il client Outline?
 Il client Outline è un'applicazione, disponibile sia per computer che per dispositivi mobili, tramite la quale puoi collegarti a un server Outline e accedere alla VPN utilizzando una chiave di accesso. Puoi scaricare l'ultima versione del client Outline [qui](https://getoutline.org/get-started/#step-3) o [qui](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Che cosa sono i limiti dati?
 Outline Manager consente ai gestori del servizio di impostare un limite dati massimo di 30 giorni per le chiavi di accesso, in modo da prevenire casi di utilizzo eccessivo e mantenere i costi prevedibili. I gestori del servizio possono impostare un limite predefinito che verrà applicato a ogni chiave. In aggiunta, possono anche impostare un limite differente su una qualsiasi chiave per sovrascrivere il limite predefinito. Una volta impostato un limite, questo verrà applicato immediatamente e su base oraria.

Nel caso in cui autorizzino la condivisione di metriche con Jigsaw, i gestori del servizio devono consultare le [norme sulla raccolta dei dati](/about/data-collection) per informazioni dettagliate su come verrà riportato l'utilizzo dei limiti dati.
