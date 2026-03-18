---
title: "Com puc establir límits de dades per a les claus d'accés?"
sidebar_label: "Com puc establir límits de dades per a les claus d'accés?"
---

Pots establir un límit de dades que s'aplicarà a totes les claus d'accés. Per establir-lo, obre el Gestor d'Outline i navega fins a Configuració. Hi veuràs el commutador Límits de dades, que, quan està activat, et permet establir un límit.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Un cop estableixis un límit, podràs veure quant li queda a cada usuari per assolir-lo a la pàgina de claus d'accés, en què un gràfic de barres mostra l'ús de dades durant els 30 darrers dies.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

A més de poder establir un límit per a totes les teves claus d'accés, pots concedir a cada clau el seu propi límit de dades. Aquesta opció de configuració anul·larà qualsevol límit de dades predeterminat que hagis establert, però si no n'has definit cap, podràs configurar un límit de dades per a qualsevol clau. 

 Per establir el límit de transferència de dades d'una clau, obre el Gestor d'Outline, navega fins a la pestanya Connexions que conté la clau en qüestió i fes clic al menú que hi ha a la part dreta de la fila de la clau. Des d'aquí, fes clic a Límit de dades. Per canviar el límit de dades a "La meva clau d'accés", fes clic a la icona Límit de dades ![Aquesta imatge no està disponible perquè o bé no tens els privilegis per veure-la o bé s'ha suprimit del sistema.](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Selecciona Estableix un límit de dades personalitzat. Un cop hagis seleccionat aquesta casella, es mostrarà un camp en què podràs establir el límit de dades personalitzat per a la clau en qüestió. Quan hagis acabat, fes clic al botó DESA per desar el límit de dades.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Un cop hagis desat el límit de transferència de dades per a la clau que has triat, aquest límit es mostrarà a la pantalla principal, juntament amb l'ús de dades (durant els 30 darrers dies) de cada clau.

Per suprimir el límit de dades d'una clau d'accés, igual que abans, navega fins al quadre de diàleg Límit de dades, desmarca la casella Estableix un límit de dades personalitzat i fes clic al botó DESA.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Preguntes més freqüents sobre el límit de dades****

****Què és un límit de dades final de 30 dies?****

 Amb un límit de dades final de 30 dies, se suma l'ús de cada clau durant els 30 darrers dies i se'n manté l'ús per sota del límit durant aquest període. En conseqüència, la clau no pot superar el límit durant cap període de 30 dies, inclosos els mesos naturals de 30 dies o menys. De fet, això vol dir que les dades disponibles de cada usuari augmentaran cada dia d'acord amb la quantitat que hagués utilitzat 31 dies abans.

**Per què Outline utilitza límits finals?**

 Els límits finals proporcionen garanties durant tots els períodes de 30 dies, de manera que són més senzills de configurar que un límit recurrent (com ara un dia del mes que es pugui personalitzar) i ofereixen garanties semblants. També coincideixen amb la visualització existent per a l'ús de dades d'Outline, així com amb les eines habituals, com ara els serveis d'anàlisi i les estadístiques del servidor.

**Quines dades es comptabilitzen en un límit de dades?**

 S'inclou al recompte la sortida del servidor de cada clau d'accés. En un sentit estricte, això significa que s'inclouen les dades que s'envien fora del servidor en nom de la clau i les que es tornen al client. En la pràctica, això hauria d'estar alineat estretament amb el trànsit enviat de la clau al servidor i del servidor a la clau, de manera que esperem que coincideixi amb els recomptes dels teus usuaris. Vam triar la sortida perquè és el que facturen els proveïdors de serveis al núvol que vam enquestar.

**Els usuaris rebran una notificació si superen el límit de dades?**

 De moment, no. Molts proveïdors de serveis al núvol inclouen un límit, com ara 1 TB per a tot el mes, que pot admetre 10 usuaris amb 100 GB o 100 usuaris amb 10 GB. Són xifres força grans i no entra dins de les nostres expectatives que gaires usuaris hi arribin. Esperem que els usuaris contactin amb els gestors de servidor quan arribin al seu límit. Tanmateix, agrairíem que ens donessis la teva opinió sobre com les notificacions poden ser útils en el teu cas d'ús. Pots contactar amb nosaltres [aquí](/about/feedback).

**Els usuaris rebran una notificació si s'apropen al límit de dades?**

 La quantitat de dades noves que rebrà un usuari que s'apropa al seu límit variarà d'un dia a l'altre perquè es basa en el seu ús 30 dies abans. Pensem que, més que ajudar els usuaris finals, un advertiment els confondria. Agrairíem que ens enviessis [aquí](/about/feedback) els teus suggeriments sobre aquest comportament.

**Puc restablir l'ús de dades d'un usuari?**

 No, el límit d'un usuari sempre inclou els 30 darrers dies d'ús de dades. Tanmateix, pots augmentar el límit de dades de la seva clau o crear-li'n una de nova.

**Per què alguns dels meus usuaris han perdut l'accés de seguida que he activat els límits de dades?**

 Els límits de dades es basen en les transferències de dades dels usuaris durant els 30 darrers dies, que es registren independentment de si s'han activat o no els límits de dades. És possible que els usuaris en qüestió ja hagin superat el límit abans que s'hagi establert. A més, tingues en compte que s'apliquen tots els límits de dades, fins i tot quan canvies el d'una clau concreta.

**Puc establir un límit per a tot el servidor, com ara "1 TB cada 30 dies"?**

 De moment, no. Agrairíem que ens fessis arribar [aquí](/about/feedback) més informació sobre el teu cas d’ús.

**Si hi ha un límit de dades predeterminat i un límit de dades per a una clau específica, quin s'aplicarà?**

 El límit de dades de la clau específica anul·larà qualsevol límit de dades predeterminat que hagis establert (en cas que n'hi hagi).

**Puc establir un límit de dades per a una clau específica sense tenir cap límit de dades predeterminat?**

 Sí, no cal que tinguis definit cap límit predeterminat per establir un límit de dades d'una clau. Per exemple, podries establir un límit per a una clau que creguis que es pot compartir amb moltes persones per protegir-te de transferències de dades excessives a través de la clau en qüestió.
