---
title: Terminología
sidebar_label: Terminología
---

## ¿Qué es una VPN?

Una red privada virtual (VPN) es una conexión privada entre tus dispositivos y un servidor host. Cuando usas una VPN, tu proveedor de Internet no puede ver tu tráfico.

Es posible que quieras usar una VPN para lo siguiente:

- Proteger tus datos cuando utilizas una red Wi-Fi pública
- Mantener la privacidad de tus datos de navegación frente a tu proveedor de Internet y los organismos públicos
- Acceder a contenido sin censurar de diversas fuentes de todo el mundo

## ¿En qué se diferencia Outline de las VPNs tradicionales?

Los proveedores de Internet pueden detectar y bloquear fácilmente las VPNs tradicionales, ya que reconocen los protocolos de seguridad comunes o los patrones de volumen de tráfico que las caracterizan. Outline tiene más resiliencia que las VPNs tradicionales porque su diseño se basa en un protocolo desarrollado para ser difícil de detectar y, por tanto, más complicado de bloquear. Outline resiste a formas sofisticadas de censura, como el bloqueo por red y por IP.

## ¿Qué es un servidor de Outline?

Los servidores de Outline ejecutan la VPN a la que se conectan los usuarios autorizados.

Si vas a crear una red, puedes usar tu propio servidor seguro (en caso de que tengas uno) como servidor de Outline, o bien utilizar un proveedor de servicios en la nube como:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

El servidor se configura en Administrador de Outline.

## ¿Qué es un gestor de servicio? {#servicemanager}

El gestor de servicio es la persona responsable de configurar el servidor de Outline y de compartir las claves de acceso con los usuarios. Además, suele encargarse de los costes derivados del uso del servidor.

## ¿Qué es una clave de acceso? {#accesskey}

La clave de acceso se usa para acceder a un servidor de Outline ya configurado y para conectarse a la VPN. El [gestor de servicio](#servicemanager) te dará una clave de acceso, aunque también puedes [configurar un servidor de Outline](/manager/server-setup/setup-server) por tu cuenta.

Aquí tienes una clave de acceso de muestra (es solo un ejemplo; no funciona):

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## ¿Qué es Administrador de Outline?

Administrador de Outline es una aplicación de escritorio que permite a los gestores de servicio configurar servidores de Outline, generar [claves de acceso](#accesskey) y definir límites de datos en función del uso de cada clave. Puedes descargar la versión más reciente de Administrador de Outline [aquí](https://getoutline.org/get-started/#step-3) o [aquí](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## ¿Qué es el cliente de Outline?

El cliente de Outline es una aplicación, disponible para ordenadores y móviles, que te permite conectarte a un servidor de Outline y acceder a la VPN mediante una clave de acceso. Puedes descargar la versión más reciente del cliente de Outline [aquí](https://getoutline.org/get-started/#step-3) o [aquí](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## ¿Qué son los límites de datos?

Administrador de Outline permite a los gestores de servicio establecer un límite de datos para las claves de acceso que se ciña a los últimos 30 días. Así, se evita un uso excesivo y se consigue que los costes sigan siendo predecibles. Los gestores de servicio pueden definir un límite predeterminado que se aplique a todas las claves, o bien establecer límites distintos en cualquier clave para reemplazar el límite predeterminado. Cuando se establece un límite, empieza a aplicarse de inmediato y su cumplimiento se revisa cada hora.

Si los gestores de servicio deciden compartir las métricas con Jigsaw, deben revisar la [política sobre recogida de datos](/about/data-collection) para saber cómo se registrará el uso de límites de datos.
