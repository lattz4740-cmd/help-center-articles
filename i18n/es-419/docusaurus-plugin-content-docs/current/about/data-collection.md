---
title: Recopilación de información y datos
sidebar_label: Recopilación de información y datos
---

Outline no recopila información personal, a menos que aceptes proporcionarla. Además, este servicio no recopila información sobre los sitios web que visitas, las personas con las que te comunicas ni el contenido de tus comunicaciones.

 Cuando creas una cuenta con un proveedor externo de servicios en la nube a través de Outline Manager o accedes a ella, no obtenemos la información que le proporcionas a ese proveedor, como tu nombre, dirección de correo electrónico, los datos de facturación y detalles del pago.

****Información que obtenemos automáticamente****

 Existen dos tipos de información que recopilamos automáticamente.

 1. IP del servidor

[Quay.io](http://quay.io/) recopila la IP del servidor de Outline y la pone a nuestra disposición cuando el servidor se actualiza automáticamente con las mejoras de funciones y de seguridad más recientes. La IP del servidor puede identificar a su proveedor en la nube y la ciudad en la que se configuró el servidor de Outline, pero no brinda información sobre quién ejecuta el servidor ni quiénes acceden a él.

 2. Información técnica que no permite la identificación personal

 Si Outline falla, si ocurre una excepción irrecuperable o si envías comentarios de forma manual a través de la app de Outline, se enviará la información que aparece a continuación. Esta información solo se utilizará para identificar y solucionar problemas de estabilidad o rendimiento.

- País
- Configuración regional
- Fecha y hora de la falla/excepción y un máximo de 100 eventos previos, como el acceso de un usuario a la sección "Acerca de"
- Mensajes de excepción compilados de forma estática
- Nombre y versión del SO
- Modelo del teléfono (si resulta aplicable)
- Hora de inicio de la app
- Navegador
- Arquitectura
- Versión y número de compilación de Outline

Esta información se transfiere a través de HTTPS a Sentry ([sentry.io](http://sentry.io/)), un proveedor externo de código abierto para el seguimiento de errores. Sentry utiliza una variedad de tecnologías y servicios estándares de la industria para proteger tus datos del acceso no autorizado, la divulgación, la utilización y la pérdida. Si tienes preguntas sobre las políticas de Sentry, visita [https://sentry.io/security/](https://sentry.io/security/) y [https://sentry.io/privacy/](https://sentry.io/privacy/), o envía un correo electrónico a [security@sentry.io](mailto:security@sentry.io). Todos los datos de Outline que almacena Sentry están restringidos, de manera que solo los miembros del equipo de Outline pueden acceder a ellos.

****Información que obtenemos solo si el usuario acepta compartirla****

 Outline le envía la siguiente información al equipo del servicio cuando aceptas compartirla.

 1. Métricas de uso

 Todos los servidores de Outline recopilan automáticamente, durante la última hora y en función de cada clave de acceso, la cantidad de bytes transferidos, el tiempo que un usuario estuvo conectado al servidor, los países y los sistemas autónomos de origen de las credenciales utilizadas, y si se habilitó o inhabilitó alguna función. No se registra el contenido de la comunicación ni los metadatos de identificación personal (p. ej., accesos, correos electrónicos, ID de dispositivo, etc.). Todas las métricas están vinculadas a un ID de servidor. Para cambiar el ID del servidor, sigue [estas instrucciones](/manager/server-management/reset-server-id).

 De forma predeterminada, los servidores de Outline no comparten estas métricas con el equipo de la app. Si el administrador del servidor acepta de forma explícita compartir las métricas de uso, esta información se enviará de forma segura al equipo de Outline cada hora. Luego de 60 días, las métricas de uso se agregarán a nivel del país. Los administradores del servidor pueden cambiar sus preferencias de uso compartido de métricas de uso cuando quieran desde el menú "Configuración" de Outline Manager.

 Agradecemos que compartas con nosotros métricas anónimas sobre el uso que haces del servidor, ya que las ocupamos para medir las tendencias de uso y mejorar el producto.

 Por ejemplo, si un administrador del servidor acepta compartir métricas de uso con nosotros, podríamos recibir información que indique que se usó un servidor con el ID 12345 durante 3 horas el día anterior, con una transferencia total de 500 megabytes de datos desde tres claves utilizadas en Estados Unidos y Canadá, con la función de límites de datos habilitada.

 2. Tus opiniones y tu correo electrónico si envías comentarios

 Las apps de Outline y Outline Manager te permiten enviarle comentarios al equipo. Si bien te recomendamos que no incluyas información de identificación personal, cuentas con un campo de correo electrónico que está disponible de forma opcional si deseas obtener una respuesta del equipo. También recopilamos automáticamente algunos datos básicos para poder comprender tus comentarios. Para ver qué datos recopilamos, consulta el punto 2 que se detalló en "Información que obtenemos automáticamente". Obtén más información sobre las prácticas de seguridad y privacidad de Outline [aquí](/about/security-and-privacy).

 Si usas una versión beta de la app de Outline para Android, podremos utilizar el servicio [Firebase](https://firebase.google.com/) de Google para recopilar información de depuración que pueda ayudarnos a detectar problemas y a mejorar Outline. Puedes obtener más información sobre las políticas de privacidad y seguridad de Firebase en su sitio web: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Si no quieres que Outline envíe esta información a través de Firebase, usa la versión de producción de la app.
