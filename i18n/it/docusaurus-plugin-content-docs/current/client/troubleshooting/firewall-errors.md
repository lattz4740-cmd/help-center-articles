---
title: Errori causati dal firewall
sidebar_label: Errori causati dal firewall
---

Il firewall potrebbe causare tre tipi di errori.

## Il firewall di rete potrebbe bloccare la connessione.

Se stai cercando di installare Outline utilizzando la connessione a una rete protetta da firewall, ad esempio mentre sei a scuola o al lavoro, cerca di installarlo quando utilizzi un'altra rete.

Se il problema persiste, contatta il tuo amministratore di rete per autorizzare le connessioni tra la rete protetta da firewall e il tuo server Outline. Devi conoscere l'indirizzo IP del tuo server Outline e le porte utilizzate da Outline, che sono indicate in fondo allo script di installazione.

## Il firewall del dispositivo potrebbe bloccare la connessione.

Se sul tuo dispositivo hai del software che blocca le connessioni in uscita su porte non standard o del software non riconosciuto (ad esempio ZoneAlarm di CheckPoint), consulta la documentazione del tuo dispositivo o del software per imparare come si crea un'eccezione per Outline.

## Il firewall del server potrebbe bloccare la connessione.

Il tuo provider di soluzioni cloud può richiedere di creare eccezioni al firewall del server manualmente, per aprire le porte sulle quali lavora Outline. Dopo aver eseguito lo script di installazione, dovrebbero esserti note le due porte scelte in modo casuale utilizzate da Outline sul tuo server. Dovrebbe essere sufficiente aprire queste due porte.

Per creare eccezioni al firewall del tuo server, ti consigliamo di consultare la documentazione per "ufw" e "iptables":

- UFW: [https://help.ubuntu.com/community/UFW](https://support.getoutline.org/s/article/Firewall-errors?language=it)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://support.getoutline.org/s/article/Firewall-errors?language=it)
