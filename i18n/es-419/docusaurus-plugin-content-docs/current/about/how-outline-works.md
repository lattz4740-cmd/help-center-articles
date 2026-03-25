---
title: Cómo funciona Outline
sidebar_label: Cómo funciona Outline
---

## Instalación del servidor
 ​Si bien la instalación de Outline puede parecer sencilla, en realidad se llevan a cabo varios procesos complejos en segundo plano para que tu servidor quede instalado. Cada vez que se instala Outline, se ejecuta una secuencia de comandos de instalación que sigue estos pasos:

- Se recupera y se importa la versión estable de la imagen de Shadowbox por medio de Docker. La imagen se aloja en [Quay.io](https://quay.io/), en [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Esta imagen contiene el servidor de Outline y la API de Management que más adelante utilizará la aplicación de administración del servidor de Outline para crear y quitar claves de acceso, habilitar o inhabilitar el informe de métricas anónimas, etcétera.
- Se instalará [Watchtower](https://github.com/containrrr/watchtower) y se configurará para que busque actualizaciones de imágenes cada hora, lo que ayuda a garantizar que todos los servidores de Outline estén siempre actualizados con las funciones y las mejoras de seguridad más recientes.
- Se inicia un servidor web en un puerto aleatorio en una ruta de acceso secreta y aleatoria. Este servidor web se utiliza para acceder a la API de Administración.
- Se crea un [certificado SSL autofirmado](https://en.wikipedia.org/wiki/Self-signed_certificate) para que la administración del servidor de Outline se pueda encriptar con TLS a pesar de no tener un nombre de dominio También se genera una huella digital única de este certificado y se la almacena en la app de Outline Manager, lo que ayuda a prevenir los ataques de MITM.

La instalación de Outline no necesita ninguna configuración posterior.

## Seguridad del servidor
 El software de Outline es de código abierto, lo que significa que cualquiera puede ver el código y mejorarlo si se detectan vulnerabilidades. Nuestro código se aloja en [GitHub](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline).

 Además, todos los servidores instalados de Outline se actualizan automáticamente cada vez que se lanza una nueva versión, lo que garantiza que no haya ningún servidor de Outline que ejecute versiones anteriores del software.

 Para administrar las claves de acceso en el servidor, la aplicación de Outline Manager interactúa con un servicio de administración del servidor de Outline. Este servicio de administración se ejecuta en un puerto aleatorio y en una ruta de acceso única y secreta. El servicio de administración resulta ser resistente, ya que no responde consultas a menos que se especifique la ruta de acceso secreta adecuada. Por último, toda la comunicación dirigida al servicio de administración está encriptada con un [certificado SSL autofirmado](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Asimismo, el servidor de Outline no almacena ningún registro, por lo que no se divulga ningún dato del usuario, incluso si el servidor se ve vulnerado. Obtén más información [aquí](/about/security-and-privacy). En el 2018, Outline se sometió a las auditorías de [Radically Open Security](https://radicallyopensecurity.com/) y [Cure53](https://cure53.de/). Lee sus informes [aquí](/about/security-and-privacy).

## Maneja el tráfico de UDP
 Outline puede operar como una VPN en todo el sistema, lo que significa que todo el tráfico de UDP se canaliza a través del servidor de Outline.

## Tráfico de DNS
Outline realiza todas las búsquedas de DNS a través de su propio servidor y las protege con la misma encriptación que se utiliza para todas las demás actividades de red. Tus consultas de DNS se transferirán a Internet Guide de Dyn, OpenDNS, el DNS de Cloudflare o el DNS de Quad9 a través del servidor de Outline. Outline no registra nunca tus búsquedas de DNS.
