---
title: Come funziona Outline
sidebar_label: Come funziona Outline
---

## Installazione del server
 ​Sebbene l'installazione di Outline possa sembrare semplice, dietro le quinte si svolge un complesso insieme di passaggi per fare in modo che il tuo server venga installato. Quando viene installato Outline, viene eseguito uno script di installazione attraverso i seguenti passaggi:

- La versione stabile dell'immagine di Shadowbox viene recuperata e importata utilizzando Docker. L'immagine è ospitata su [Quay.io](https://quay.io/), all'indirizzo [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Questa immagine contiene il server Outline e l'API di gestione che in seguito viene utilizzata dall'applicazione di gestione del server Outline per creare e rimuovere le chiavi di accesso, attivare/disattivare la generazione di report sulle metriche anonime e così via.
- [Watchtower](https://github.com/containrrr/watchtower) viene installato e configurato in modo da verificare la presenza di aggiornamenti dell'immagine ogni ora, aiutando a mantenere tutti i server Outline costantemente aggiornati con le funzioni e i miglioramenti in termini di sicurezza più recenti.
- Un server web utilizzato per accedere all'API di gestione viene avviato su una porta scelta in modo casuale e su un percorso segreto e casuale.
- Viene creato un [certificato SSL autofirmato](https://en.wikipedia.org/wiki/Self-signed_certificate) in modo che la gestione del server Outline possa essere criptata utilizzando TLS anche senza disporre di un nome di dominio. Nell'applicazione Outline Manager viene generata e archiviata un'impronta digitale unica di questo certificato, aiutando a prevenire gli attacchi man in the middle.

L'installazione di Outline non richiede nessuna configurazione successiva all'installazione.

## Sicurezza del server
 Il software Outline è open source, il che significa che chiunque può vedere il codice e migliorarlo se vengono scoperte delle vulnerabilità. Il nostro codice è ospitato su [GitHub](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline).

 Inoltre, tutti i server Outline installati vengono aggiornati automaticamente ogni volta che viene rilasciata una nuova versione; in questo modo, nessun server Outline esegue versioni obsolete del software.

 Per gestire le chiavi di accesso del server, l'applicazione Outline Manager interagisce con un servizio di gestione sul server Outline. Questo servizio viene eseguito su una porta scelta in modo casuale e utilizza un percorso segreto e unico. Tale servizio si difende esso stesso dalle esplorazioni poiché non risponde alle query se non viene specificato il percorso segreto corretto. Infine, tutte le comunicazioni al servizio di gestione sono criptate con un [certificato SSL autofirmato](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Inoltre il server Outline non conserva nessun log, per cui anche se venisse compromesso, nessun dato dell'utente potrebbe essere divulgato. Scopri di più [qui](/about/security-and-privacy). Nel 2018 Outline è stato valutato da [Radically Open Security](https://radicallyopensecurity.com/) e [Cure53](https://cure53.de/). Consulta i report [qui](/about/security-and-privacy).

## Gestione del traffico UDP
 Outline può funzionare come una VPN a livello di sistema, ovvero eseguendo il tunneling di tutto il traffico UDP tramite il server Outline.

## Traffico DNS
Outline esegue tutte le ricerche DNS tramite il proprio server e le protegge utilizzando la stessa crittografia applicata alle altre attività di rete. Le query DNS passeranno per il server Outline alla Dyn Internet Guide, OpenDNS, Cloudflare DNS o Quad9 DNS. Outline non registra nessuna ricerca DNS.
