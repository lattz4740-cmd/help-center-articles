---
title: Errores del firewall
sidebar_label: Errores del firewall
---

Existen tres tipos de problemas del firewall con los que puedes encontrarte:

## Es probable que el firewall de una red te haya bloqueado.

Si intentas instalar Outline mientras usas una red protegida con firewall (por ejemplo, en tu institución educativa o lugar de trabajo), realiza la instalación desde otra red.

Si esta opción no funciona, comunícate con el administrador de la red y pídele que permita las conexiones entre el servidor de Outline y la red protegida con firewall. Deberás conocer la dirección IP de tu servidor de Outline y los puertos en los que se ejecuta el servicio (aparecen al final de la secuencia de comandos de instalación).

## Es posible que el firewall de un dispositivo te haya bloqueado.

Si tienes software en tu dispositivo que bloquea las conexiones salientes en los puertos que no son estándar o software no reconocido (por ejemplo, ZoneAlarm de CheckPoint), consulta la documentación del dispositivo o del software para descubrir cómo crear una excepción para Outline.

## Es posible que el firewall de un servidor te haya bloqueado.

Es posible que el proveedor de servicios en la nube que hayas elegido te exija que crees manualmente excepciones al firewall de tu servidor para abrir los puertos en los que se ejecuta Outline. Una vez que hayas ejecutado la secuencia de comandos de instalación, se te proporcionarán los dos puertos aleatorios en los que se ejecuta Outline en tu servidor. Debería bastar con abrir ambos.

 Para crear excepciones en el firewall de tu servidor, te recomendamos que consultes la documentación de iptables y la de UFW:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
