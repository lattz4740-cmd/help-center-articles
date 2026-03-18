---
title: "Sicurezza e privacy durante l'utilizzo di Outline"
sidebar_label: "Sicurezza e privacy durante l'utilizzo di Outline"
---

Sicurezza e privacy durante l'utilizzo di Outline

## In che modo Outline protegge le tue comunicazioni online

Il traffico internet è più vulnerabile alla sorveglianza quando viaggia sulla rete locale o nazionale.

Outline aiuta a mantenere private le tue comunicazioni criptando il traffico internet quando viaggia all'interno della tua rete nazionale e lo mantiene criptato finché non raggiunge il server Outline. Quando il traffico è criptato con Outline, chi osserva la rete non può ispezionare i siti web che visiti o le informazioni che stai trasferendo.

Outline può anche farti recuperare l'accesso a strumenti di comunicazione sicura end-to-end che potrebbero non essere altrimenti accessibili nel tuo paese.

## Standard della crittografia

Outline cripta le comunicazioni tra il tuo dispositivo e il server Outline utilizzando il cifrario di crittografia autenticata con dati associati 256-bit Chacha2020 IETF Poly 1305. I cifrari di crittografia autenticata con dati associati offrono riservatezza, integrità e autenticità, inoltre vantano prestazioni eccellenti sui moderni hardware.

## Audit della sicurezza

Nel 2018 Outline è stato valutato da Radically Open Security e Cure53, due organizzazioni indipendenti di sicurezza digitale che verificano i software a fronte dei più recenti standard di sicurezza. Radically Open Security ha condotto un audit aggiuntivo nel 2022 e Cure53 ha condotto un audit di Outline SDK nel 2024. Puoi leggere i report qui:

- [Radically Open Security Penetration Test Report (marzo 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (dicembre 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (dicembre 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (gennaio 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Metriche anonime e log

Outline traccia la larghezza di banda utilizzata come "byte trasferiti" per ciascuna chiave di accesso. Questa informazione permette agli amministratori del server di regolare secondo necessità i loro abbonamenti alla larghezza di banda con i provider di soluzioni cloud, ma non di vedere le informazioni che sono passate attraverso il server Outline.

Scopri di più sulla [raccolta di dati e informazioni](/about/data-collection) di Outline.

---

## Domande frequenti sulla sicurezza e sulla privacy

## Utilizzare Outline può rendere la mia navigazione anonima?

No, Outline non è uno strumento per l'anonimato. La sua funzione è quella di proteggere la tua privacy da potenziali osservatori sulla rete.

Outline non ti offre un anonimato completo sui siti web che visiti, che possono identificarti quando esegui l'accesso o in qualche caso tramite tecniche come il browser fingerprint. Nelle app per dispositivi mobili, gli smartphone più moderni dispongono di API che permettono alle app installate di recuperare la tua posizione indipendentemente dal tuo proxy, sfruttando il GPS incorporato.

Le VPN in generale offrono importanti servizi di protezione, in particolare dalla sorveglianza su internet, ma lavorare online comporta sempre dei rischi. Anche se utilizzi una VPN, se un ISP conosce già la tua identità e può osservare il tuo traffico di rete può anche determinare l'indirizzo IP del tuo server Outline. Questa informazione può essere utilizzata per impedire l'accesso al server Outline o per conoscerne le abitudini d'uso, come gli orari in cui sei tipicamente online e, quando possibile, la tua posizione approssimativa.

## Qualcuno può accorgersi che sto utilizzando Outline?

È possibile. Molto probabilmente le piattaforme e i servizi a cui accedi sono in grado di stabilire se la tua connessione proviene da un cloud server. In alcuni casi possono dedurre che stai utilizzando una VPN, ma non saranno in grado di vedere i contenuti del tuo traffico internet.

## Outline mi protegge da ogni possibile minaccia informatica?

No, nessuno strumento può farlo. Outline ti dà libero accesso a internet e migliora la tua privacy criptando il tuo traffico, ma ti consigliamo di prendere ulteriori precauzioni per proteggerti da altri tipi di attacco, come malware e phishing.

Per migliorare le tue difese online, considera la possibilità di consultare l'esperto di sicurezza informatica della tua organizzazione. In alternativa, puoi ottenere indicazioni personalizzate contattando gli esperti di sicurezza di [Security Planner](https://securityplanner.org/), un sito web creato per darti istruzioni chiare sulla scelta degli strumenti di sicurezza informatica adatti alle tue esigenze.

Puoi anche controllare gli altri prodotti di sicurezza informatica di [Jigsaw](https://jigsaw.google.com/), come [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) e [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## È legale utilizzare una VPN?

Prima di utilizzare Outline, controlla le norme e le leggi locali, così come i Termini di servizio del provider di soluzioni cloud che intendi utilizzare.
