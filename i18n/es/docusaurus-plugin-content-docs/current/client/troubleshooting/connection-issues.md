---
title: "¿Por qué no puedo conectarme al servicio de Outline?"
sidebar_label: "¿Por qué no puedo conectarme al servicio de Outline?"
---

Hay varios factores que pueden impedir que te conectes al servicio de Outline:

- **Tu dispositivo**[**no tiene conexión a Internet**](#Internetissues)**.**En ocasiones, es posible que el dispositivo se desconecte momentáneamente de la red y tarde un poco en mostrar los iconos de red de nuevo. También es posible que el dispositivo esté conectado a la red local, pero que Internet esté caído.
- **El**[**cortafuegos de la red está bloqueando el acceso**](#SoftwareIssues)**a tu servidor de Outline.**Esto suele ocurrir cuando se usa una red pública; por ejemplo, si estás en un centro educativo o en el trabajo, o si te conectas a una red inalámbrica gratuita.
- **Tu dispositivo tiene**[**un cortafuegos o un software antivirus**](#SoftwareIssues)**que está bloqueando el acceso al servidor de Outline.**
- **Es posible que tengas que cambiar los**[**ajustes de tu dispositivo**](#DeviceSettings)**.**
- **Puede que el gestor del servicio haya**[**eliminado el servidor o que tu proveedor de Internet esté bloqueando tu solicitud**](#ServerIssues)**.**

Problemas con la conexión a Internet:

## Cómo probarlo: {#Internetissues}
Desactiva Outline y comprueba si se ha restablecido la conexión a Internet.

- En caso afirmativo, consulta otras posibles soluciones al problema que se describen a continuación.
- En caso negativo, espera un poco para ver si los ajustes de conexión se actualizan automáticamente.

## Qué hacer:

Vuelve a conectar el dispositivo a Internet:

1. Comprueba si otros dispositivos pueden conectarse a la misma red. Si no pueden, es posible que la red esté caída y que tengas que esperar a que se restablezca para solucionar el problema.
2. Si otros dispositivos sí pueden conectarse a la misma red, prueba una o varias de las siguientes opciones para restablecer la conexión:
   1. Pon el dispositivo en modo Avión (móviles).
   2. Reinicia el dispositivo.
   3. Apaga el dispositivo, espera dos minutos y vuelve a encenderlo.

Problemas con el cortafuegos de la red:

## Cómo probarlo:

1. Desconecta el dispositivo de la red Wi-Fi o de cable actual.
2. Conéctate a otra red (por ejemplo, a la de un móvil).
3. Intenta volver a conectarte al servidor de Outline.

Si puedes conectarte desde la otra red, este es tu problema.

## Qué hacer: {#FirewallIssues}
Ponte en contacto con el gestor del servicio y pídele que dé acceso a tu servidor de Outline, o sigue usando la otra red.

Problemas con el cortafuegos o el software antivirus:

## Cómo probarlo:

Prueba a conectarte a Outline desde otro dispositivo.

Nota: Necesitarás una clave de acceso y la aplicación Outline para usar el software en ese dispositivo.

## Qué hacer:

Comprueba los ajustes del cortafuegos y del software antivirus y confirma que estén configurados de modo que permitan el tráfico de VPN y Outline.

Ajustes del dispositivo:

## Qué comprobar: {#SoftwareIssues}
Android:

1. Abre la aplicación Ajustes.
2. Busca los **ajustes de VPN** en tu dispositivo (donde podrás ver todas las aplicaciones de tu teléfono que tienen acceso actualmente a la VPN).
3. Si no aparece Outline en los ajustes de VPN, desinstala y reinstala el software. El dispositivo debería dar acceso a Outline automáticamente una vez que se instale.

Asegúrate de que no tengas ninguna aplicación de superposición en pantalla instalada en tu dispositivo Android, ya que podría estar enviando la ventana de permisos de Outline a segundo plano (y, por eso, no se ve en primer plano).

En tu dispositivo Android, ve a Ajustes > Aplicaciones > Aplicaciones con accesos especiales. Después, toca "Mostrar sobre otras aplicaciones". Puedes quitar el acceso a cualquier aplicación que permita este comportamiento.

iOS: lee [este artículo de asistencia](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

Problemas con el servidor:

## Cómo probarlo:

## Si tienes acceso a más de un servidor, prueba a conectarte a otro. {#ServerIssues}

## Qué hacer: {#DeviceSettings}
Ponte en contacto con el gestor del servicio para ver si lo ha eliminado. En caso afirmativo, pídele una [clave de acceso](/about/terminology) para otro servidor.

Si configuras el servidor por tu cuenta, prueba a conectarte a él mediante el Administrador de Outline u otro método, como [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Si esta alternativa no funciona, consulta la consola del proveedor de servicios en la nube, si la hubiera, para ver si el servidor sigue conectado.
