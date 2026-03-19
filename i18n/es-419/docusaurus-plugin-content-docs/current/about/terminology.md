---
title: Terminología
sidebar_label: Terminología
---

## ¿Qué es una VPN?

Una red privada virtual (VPN) es una conexión privada entre tus dispositivos y un servidor host. Cuando usas una VPN, tu tráfico se oculta del proveedor de Internet.

Se recomienda que uses una VPN en los siguientes casos:

- Para proteger tus datos mientras usas una red Wi-Fi pública
- Para mantener la privacidad de tus datos de navegación ante tu proveedor de Internet y las agencias gubernamentales
- Para acceder a contenido no censurado de varias fuentes en todo el mundo

## ¿Cómo se diferencia Outline de las VPNs tradicionales?

Los proveedores de Internet pueden detectar y bloquear VPNs tradicionales con facilidad, ya que reconocen los protocolos de seguridad comunes o los patrones de volumen de tráfico. Outline es más resistente que las VPNs tradicionales porque se desarrolló con un protocolo diseñado para ser difícil de detectar y, por lo tanto, más difícil de bloquear. Además, es resistente a las formas de censura sofisticadas, incluido el bloqueo basado en redes y el bloqueo de IPs.

## ¿Qué son los servidores de Outline?

Los servidores de Outline ejecutan las VPN a las que se conectarán los usuarios permitidos.

Si creas una nueva red, puedes usar tu propio servidor seguro como servidor de Outline, si tienes uno, o bien puedes usar un proveedor de servicios en la nube, como los que se indican a continuación:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Debes configurar tu servidor en Outline Manager.

## ¿Qué son los administradores de servicios? {#servicemanager}

Los administradores de servicios son las personas encargadas de configurar el servidor de Outline y compartir claves de acceso con los usuarios. Generalmente, son responsables del costo de uso del servidor.

## ¿Qué son las claves de acceso? {#accesskey}

Las claves de acceso se usan para acceder a un servidor de Outline existente y conectarse a la VPN. Un [administrador de servicios](#servicemanager) te dará una clave de acceso, o bien puedes [configurar un servidor de Outline](/manager/server-setup/setup-server) por tu cuenta.

Esta es una clave de acceso de ejemplo (es solo una muestra y no funcionará):

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## ¿Qué es Outline Manager?

Outline Manager es una aplicación para computadoras con la que un administrador de servicios puede configurar un servidor de Outline, generar [claves de acceso](#accesskey) y establecer límites de datos respecto al uso de cada clave. Puedes descargar la versión más reciente de Outline Manager [aquí](https://getoutline.org/get-started/#step-3) o [aquí](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## ¿Qué es el cliente de Outline?

El cliente de Outline es una aplicación para computadoras y dispositivos móviles que te permite conectarte a un servidor de Outline y acceder a la VPN con una clave de acceso. Puedes descargar la versión más reciente del cliente de Outline [aquí](https://getoutline.org/get-started/#step-3) o [aquí](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## ¿Qué son los límites de datos?

Con Outline Manager, los administradores de servicios pueden establecer un límite de datos retrospectivo de 30 días que se aplicará a las claves de acceso para evitar el uso excesivo y predecir los costos. Los administradores de servicios pueden establecer un límite predeterminado que se aplique a todas las claves y un límite diferente en cualquiera de ellas para anular el predeterminado. Una vez que establezcas el límite, entrará en vigencia inmediatamente y se aplicará por hora.

Si los administradores de servicios aceptan compartir métricas con Jigsaw, deberían consultar la [política de recopilación de datos](/about/data-collection) para saber cómo se informará el uso de los límites de datos.
