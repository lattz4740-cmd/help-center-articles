---
title: "¿Por qué no puedo conectarme al servicio de Outline?"
sidebar_label: "¿Por qué no puedo conectarme al servicio de Outline?"
---

Existen algunos motivos por los que quizás no puedas conectarte al servicio de Outline. Por ejemplo:

- **Tu dispositivo**/client/troubleshooting/connection-issues#One[**no está conectado a Internet**](#Internetissues)[#Internetissues](#Internetissues)**.**En ocasiones, tu dispositivo puede experimentar problemas de conexión de red y es posible que los íconos de red demoren un poco en actualizarse. También es posible que tu dispositivo esté conectado a la red local, pero que Internet no funcione.
- **El**/client/troubleshooting/connection-issues#Two[**firewall de la red bloquea el acceso**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[a](#FirewallIssues)l servidor de Outline.**Este es un problema común si usas una red pública, como la de una institución educativa, la del trabajo o una red inalámbrica gratuita.
- **El**/client/troubleshooting/connection-issues#Three[**firewall o software antivirus**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**de tu dispositivo bloquea el acceso al servidor de Outline.**
- **Es posible que la**[**configuración de dispositivo de tu teléfono**](#DeviceSettings)**requiera cambios.**
- **El administrador del servicio puede haber**[**destruido el servidor, o tu ISP puede estar bloqueando tu solicitud**](#ServerIssues) .

## Problemas con la conexión a Internet: {#Internetissues}

## Cómo hacer la prueba:

Desactiva Outline y observa si se restablece tu conexión a Internet.

- De ser así, consulta más opciones para solucionar problemas a continuación.
- De no ser así, espera unos minutos para ver si se actualiza tu configuración de conexión.

## Aspectos que se deben corregir:

Logra que tu dispositivo vuelva a estar en línea:

1. Prueba con otro dispositivo para ver si se conecta a esa misma red. Si los otros dispositivos tampoco se pueden conectar, es posible que la red no funcione y que debas esperar a que vuelva o intentar solucionar el problema.
2. Si los otros dispositivos se pueden conectar a la red, puedes probar una o más de las siguientes opciones para que tu dispositivo vuelva a estar en línea:
   1. Pon el dispositivo en modo de avión (dispositivo móvil).
   2. Reinicia el dispositivo.
   3. Apaga el dispositivo, espera 2 minutos y vuelve a encenderlo.

## Problemas con el firewall de la red: {#FirewallIssues}

## Cómo hacer la prueba:

1. Desconéctate de la red con cable o Wi-Fi a la que esté conectado el dispositivo.
2. Conéctate a otra red, por ejemplo, a una red móvil.
3. Vuelve a conectarte al servidor de Outline.

Si puedes conectarte desde la otra red, entonces aquí está el problema.

## Aspectos que se deben corregir:

Comunícate con el administrador del servicio y solicita que te permita acceder al servidor de Outline, o bien sigue usando la otra red.

## Problemas con el firewall o software antivirus:
## Cómo hacer la prueba:
 Intenta conectarte a Outline desde otro dispositivo.

Nota: Recuerda que necesitarás una clave de acceso y la app de Outline para usar este servicio en otro dispositivo.

## Aspectos que se deben corregir: {#SoftwareIssues}
Comprueba la configuración de tu firewall o software antivirus para asegurarte de que esta permita el tráfico entre la VPN y Outline.

## Configuración del dispositivo: {#DeviceSettings}

## Aspectos que debes comprobar: {#DeviceSettings}
Para Android:

1. Abre la app de Configuración.
2. Busca la **configuración de VPN** en tu dispositivo (en esta, se mostrarán todas las apps de VPN que actualmente tienen acceso en tu teléfono).
3. Si no ves Outline en la configuración de VPN, desinstala Outline y reinstálalo. Cuando termine este proceso, el dispositivo otorgará acceso a Outline automáticamente.

Asegúrate de que no haya ninguna aplicación de pantalla superpuesta en tu dispositivo Android, ya que esta podría enviar la ventana de permisos de Outline a segundo plano y causar que no se vea en primer plano.

 En tu dispositivo Android, ve a Configuración > Apps > Acceso especial de apps. Luego, presiona “Mostrar sobre otras apps”. Puedes quitar el acceso a cualquier app que permita este comportamiento.

 Para iOS, consulta[este artículo de ayuda](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Problemas con el servidor: {#ServerIssues}

## Cómo hacer la prueba: {#ServerIssues}
Si tienes acceso a más de un servidor, intenta conectarte a otro.

## Aspectos que se deben corregir:

Comunícate con el administrador del servicio para ver si se destruyó el servidor. Si es así, solicita una[clave de acceso](/about/terminology) para usar otro servidor.

Si configuraste el servidor, intenta conectarte a él por medio de Outline Manager o algún otro método, como[SSH](https://en.wikipedia.org/wiki/Secure_Shell). Si no funciona esa opción, puedes verificar la consola del proveedor de servicios en la nube (si hay una) para saber si el servidor sigue en línea.
