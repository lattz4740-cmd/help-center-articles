---
title: Cómo funciona Outline
sidebar_label: Cómo funciona Outline
---

### Instalación del servidor

Si bien la instalación de Outline puede parecer sencilla, en realidad se llevan a cabo varios procesos complejos en segundo plano para que tu servidor quede instalado.

Cada vez que se instala Outline, se ejecuta una secuencia de comandos de instalación que sigue estos pasos:

- La versión estable de la imagen de Shadowbox se recupera y se importa por medio de Docker. La imagen se aloja en [Quay.io](https://support.getoutline.org/s/article/how-outline-works?language=es), en [https://quay.io/repository/outline/shadowbox?tab=tags](https://support.getoutline.org/s/article/how-outline-works?language=es). Esta imagen contiene el servidor de Outline y la API de Administración que más adelante la app de Outline Server Management utiliza para crear y quitar claves de acceso, habilitar o inhabilitar el informe de métricas anónimas, etcétera.
- Se instala [Watchtower](https://support.getoutline.org/s/article/how-outline-works?language=es) y se lo configura para que busque actualizaciones de imágenes cada hora, lo que ayuda a garantizar que todos los servidores de Outline estén siempre actualizados con las funciones y las mejoras de seguridad más recientes.
- Se inicia un servidor web en un puerto aleatorio en una ruta de acceso secreta y aleatoria. Este servidor web se utiliza para acceder a la API de Administración.
- Se crea un [certificado de SSL autofirmado](https://support.getoutline.org/s/article/how-outline-works?language=es) para que la administración del servidor de Outline se pueda encriptar con TLS a pesar de no tener un nombre de dominio. También se genera una huella digital única de este certificado y se la almacena en la app de Outline Manager, lo que ayuda a prevenir los ataques de MITM.

La instalación de Outline no necesita ninguna configuración posterior.

### Seguridad del servidor

Outline es un software de código abierto, lo que significa que cualquiera puede ver el código y mejorarlo si se detectan vulnerabilidades. Nuestro código se aloja en

.

Además, todos los servidores instalados de Outline se actualizan automáticamente cada vez que se lanza una nueva versión, lo que garantiza que no haya ningún servidor de Outline que ejecute versiones anteriores del software.

Para administrar las claves de acceso en el servidor, la app de Outline Manager interactúa con un servicio de administrador del servidor de Outline. Este servicio de administración se ejecuta en un puerto aleatorio y en una ruta de acceso única y secreta. El servicio de administración resulta ser resistente, ya que no responde consultas a menos que se especifique la ruta de acceso secreta adecuada. Por último, todas las comunicaciones que se mantienen con el servicio de administración se encriptan con un

.

Asimismo, el servidor de Outline no almacena ningún registro, por lo que no se divulga ningún dato del usuario incluso aunque el servidor se vea vulnerado. Obtén más información

.

En 2018, Outline se sometió a las auditorías de

y

. Consulta los informes

.

### Cómo manejar el tráfico de UDP

Outline puede operar como una VPN en todo el sistema, lo que significa que todo el tráfico de UDP se canaliza por medio del servidor de Outline.

### Tráfico de DNS

Outline realiza todas las peticiones de DNS a través de su servidor, y las protege con el mismo cifrado que se utiliza en el resto de la actividad de red. Tus consultas de DNS se dirigirán a través del servidor de Outline a la guía de Internet de Dyn o a OpenDNS.

Outline no registra nunca las peticiones de DNS.
