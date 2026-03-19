---
title: "De ce nu pot să mă conectez la serviciul Outline?"
sidebar_label: "De ce nu pot să mă conectez la serviciul Outline?"
---

Există câteva motive pentru care nu puteți să vă conectați la serviciul Outline.

- **Dispozitivul este**/client/troubleshooting/connection-issues#One[**deconectat de la internet**](#Internetissues)[#Internetissues](#Internetissues)**.**Uneori, conexiunea dispozitivului la rețea se poate întrerupe și actualizarea pictogramelor de rețea poate dura ceva timp. Este posibil și ca dispozitivul să fie conectat la rețeaua locală, dar conexiunea la internet să fie oprită.
- **Firewallul**/client/troubleshooting/connection-issues#Two[**rețelei blochează accesul**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[#FirewallIssues](#FirewallIssues)la serverul Outline.**Se întâmplă frecvent dacă folosiți o rețea publică, cum ar fi rețeaua școlii, a locului de muncă sau o rețea wireless gratuită.
- **Dispozitivul are un**/client/troubleshooting/connection-issues#Three[**firewall sau software antivirus**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**care blochează accesul la serverul Outline.**
- **Poate fi necesar ca**[**setările telefonului**](#DeviceSettings)**să fie modificate.**
- **Este posibil ca administratorul serviciului**[**să fi distrus serverul sau ca ISP-ul să blocheze solicitarea**](#ServerIssues) .

## Probleme privind conexiunea la internet {#Internetissues}

## Cum să testați

Dezactivați Outline și controlați dacă a fost restabilită conexiunea la internet.

- Dacă s-a restabilit, vedeți mai multe opțiuni de remediere a erorilor mai jos.
- Dacă nu, așteptați câteva minute ca să vedeți dacă setările pentru conexiune se actualizează de la sine.

## De remediat

Conectați din nou dispozitivul la internet:

1. verificați alt dispozitiv pentru a vedea dacă se poate conecta la aceeași rețea. Dacă alte dispozitive nu se pot conecta la internet, este posibil ca rețeaua să nu funcționeze și va trebui să așteptați să repornească sau să încercați să rezolvați problema.
2. dacă alte dispozitive se pot conecta la aceeași rețea, puteți încerca unul sau mai mulți dintre următorii pași pentru a vă conecta la internet:
   1. setați dispozitivul în modul avion (mobil);
   2. reporniți dispozitivul;
   3. închideți dispozitivul, așteptați două minute și reporniți-l.

## Probleme privind firewallul de rețea {#FirewallIssues}

## Cum să testați

1. Deconectați-vă de la rețeaua Wi-Fi sau prin cablu la care v-ați conectat.
2. Conectați-vă la altă rețea, de exemplu, o rețea mobilă.
3. Încercați să vă reconectați la serverul Outline.

Dacă vă puteți conecta din altă rețea, înseamnă că aceasta este problema dvs.

## De remediat

Contactați administratorul serviciului și cereți-i să vă permită accesul la serverul Outline sau continuați să folosiți cealaltă rețea.

## Probleme privind firewallul sau software-ul antivirus
## Cum să testați
 Încercați să vă conectați la Outline de pe alt dispozitiv.

Rețineți: aveți nevoie de o cheie de acces și de aplicația Outline pentru a putea folosi Outline pe alt dispozitiv.

## De remediat {#SoftwareIssues}
Verificați firewallul sau software-ul antivirus ca să vă asigurați că sunt setate să permită traficul prin VPN și Outline.

## Setările dispozitivului {#DeviceSettings}

## De verificat {#DeviceSettings}
Pentru Android:

1. deschideți aplicația Setări;
2. căutați **setările VPN** pe dispozitiv (setările VPN vor afișa toate aplicațiile VPN care au momentan acces pe telefon);
3. dacă nu vedeți Outline în setările VPN, dezinstalați Outline și reinstalați. Outline ar trebui să primească automat acces de la dispozitiv după instalare.

Asigurați-vă că nu ați instalat nicio aplicație cu suprapunere pe ecran pe dispozitivul Android, deoarece poate trimite în fundal fereastra de permisiuni Outline, astfel încât nu mai este vizibilă în prim-plan.

 Pe dispozitivul Android, accesați Setări > Aplicații > Acces special la aplicații. Apoi, atingeți Afișați peste alte aplicații. Puteți să eliminați accesul la orice aplicație care permite un astfel de comportament.

 Pentru iOS: citiți [acest articol de ajutor](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Probleme privind serverul {#ServerIssues}

## Cum să testați {#ServerIssues}
Dacă aveți acces la mai multe servere, încercați să vă conectați la alt server.

## De remediat

Contactați administratorul serviciului pentru a vedea dacă serverul a fost distrus. Dacă da, cereți-i o [cheie de acces](/about/terminology) la alt server.

Dacă dvs. ați configurat serverul, încercați să vă conectați la acesta prin Outline Manager sau folosind altă metodă, cum ar fi [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Dacă nu funcționează, verificați consola furnizorului de servicii cloud, dacă există, pentru a vedea dacă serverul este încă online.
