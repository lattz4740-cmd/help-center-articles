---
title: Εγκατάσταση της εφαρμογής Outline Client σε Linux
sidebar_label: Εγκατάσταση της εφαρμογής Outline Client σε Linux
---

Από την έκδοση 1.15 της εφαρμογής Outline Client, όλες οι μελλοντικές εκδόσεις θα κυκλοφορούν ως πακέτα Debian για λειτουργικά συστήματα Linux. Ανατρέξτε στις [ελάχιστες απαιτήσεις συστήματος](/client/getting-started/system-requirements) για περισσότερες πληροφορίες σχετικά με τα λειτουργικά συστήματα που υποστηρίζουμε.

## Εγκατάσταση της εφαρμογής Outline Client για διανομές Linux που βασίζονται στο Debian (προτείνεται)

Εκτελέστε τις ακόλουθες εντολές:

1. Εγκαταστήστε το κλειδί χώρου φύλαξης του Outline και προσθέστε τον χώρο φύλαξης.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Ενημερώστε τη λίστα πακέτων apt και εγκαταστήστε τη νεότερη έκδοση του Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Για να ελέγξετε ή να εγκαταστήσετε μελλοντικές ενημερώσεις, εκτελέστε ξανά τις εντολές στο Βήμα 2. Λάβετε υπόψη ότι η αυτόματη ενημέρωση εντός εφαρμογής είναι απενεργοποιημένη για το Outline Client σε Linux, από την έκδοση 1.15 και έπειτα.

Για να απεγκαταστήσετε το Outline Client, εκτελέστε την ακόλουθη εντολή:

```
sudo apt purge outline-client
```

## Εναλλακτική επιλογή

1. Κατεβάστε το νεότερο πακέτο Debian του Outline Client από τη διεύθυνση [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Εκτελέστε τις παρακάτω εντολές στη γραμμή εντολών για να εγκαταστήσετε το πακέτο

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Ελέγξτε για ενημερώσεις με μη αυτόματο τρόπο, καθώς η αυτόματη ενημέρωση εντός εφαρμογής είναι απενεργοποιημένη για το Outline Client στο Linux, από την έκδοση 1.15 και έπειτα.

4. Για να απεγκαταστήσετε το Outline Client, εκτελέστε την ακόλουθη εντολή στη γραμμή εντολών:

```
sudo apt purge outline-client
```
