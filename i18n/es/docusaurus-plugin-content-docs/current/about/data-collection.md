---
title: Recogida de datos e información
sidebar_label: Recogida de datos e información
---

Outline no recoge información personal, a menos que aceptes proporcionarla. Tampoco recoge información sobre los sitios web que visitas, con quién te comunicas ni qué transmites.

 Cuando creas una cuenta de un proveedor de servicios en la nube, o inicias sesión en ella, desde Administrador de Outline no recogemos ninguno de los datos que facilitas a tu proveedor externo de servicios en la nube, como tu dirección de correo electrónico, nombre, datos de facturación y detalles de pagos.

## Información que obtenemos automáticamente
 Recogemos dos tipos de información de forma automática.

 1. IP del servidor

[Quay.io](https://quay.io/) obtiene la IP del servidor de Outline y nos la facilita cuando el servidor instala automáticamente las mejoras de seguridad y funciones más recientes. Puede que mediante la IP del servidor se pueda identificar al proveedor del servidor basado en la nube y la ciudad donde se ha configurado el servidor de Outline, pero no se podrá saber quién utiliza el servidor ni quién accede a él.

 2. Información técnica que no permite identificar personalmente al usuario

 Si Outline falla o se produce una excepción grave, o si envías comentarios manualmente a través de la aplicación de Outline, recibiremos la información que se indica más abajo. Esta información solo se utilizará para detectar y corregir problemas de estabilidad o rendimiento.

- País
- Configuración regional
- Fecha y hora del fallo o excepción y un máximo de 100 eventos anteriores (por ejemplo, si el usuario ha abierto la sección Información)
- Mensajes de excepción compilados de forma estática
- Nombre y versión del SO
- Modelo del teléfono (si procede)
- Hora de inicio de la aplicación
- Navegador
- Arquitectura
- Versión y número de compilación de Outline

Esta información se transfiere mediante HTTPS A Sentry ([sentry.io](https://sentry.io/)), un proveedor externo de código abierto para monitorizar errores. Sentry utiliza diferentes tecnologías y servicios estándares del sector para proteger tus datos contra el acceso, uso o divulgación no autorizados y para evitar su filtración. Si tienes alguna duda sobre las políticas de Sentry, visita [https://sentry.io/security/](https://sentry.io/security/) y [https://sentry.io/privacy/](https://sentry.io/privacy/), o escribe un correo a [security@sentry.io](mailto:security@sentry.io). Los datos de Outline que guarda Sentry están restringidos, de modo que solo los miembros del equipo de Outline pueden acceder a ellos.

## Información que obtenemos solo tras la aceptación
 Una vez que aceptas la cesión de información, Outline envía los siguientes datos a su equipo.

 1. Métricas de usos

 Todos los servidores de Outline recogen automáticamente el número de bytes transferidos, el tiempo que el usuario ha estado conectado al servidor, los países y los sistemas autónomos de origen de las credenciales usadas y si se ha habilitado o inhabilitado alguna función, durante la última hora y por clave de acceso. No se registran ni el contenido de las comunicaciones ni los metadatos de identificación personal (por ejemplo, datos de inicio de sesión, correos electrónicos, IDs de dispositivo, etc.). Todas las métricas están vinculadas al ID del servidor. Consulta las instrucciones sobre [cómo cambiar el ID del servidor](/manager/server-management/reset-server-id).

 De forma predeterminada, los servidores de Outline no comparten estas métricas con el equipo de Outline. Si el administrador del servidor acepta explícitamente que se compartan las métricas de uso, esta información se enviará de forma segura al equipo de Outline cada hora. Al cabo de 60 días, las métricas de uso se agregan a nivel nacional. Los administradores del servidor pueden cambiar sus preferencias para compartir métricas de uso en el momento que quieran en los ajustes del Administrador de Outline.

 Las métricas anónimas que compartes con nosotros sobre el uso que haces del servidor nos permiten evaluar las tendencias de uso y mejorar el producto.

 Por ejemplo, si un administrador del servidor acepta compartir métricas de uso con nosotros, podríamos recibir información que indicara que un servidor con el ID 12345 se utilizó durante tres horas el día anterior y transfirió un total de 500 megabytes de datos desde tres claves en Estados Unidos y Canadá, con la función de límites de datos habilitada.

 2. Tus comentarios y tu dirección de correo electrónico, si nos envías tu opinión

 El Administrador de Outline y las aplicaciones de Outline te permiten enviar tus opiniones al equipo. Te recomendamos que no incluyas información personal identificable, pero hay un campo opcional para que incluyas tu correo electrónico si quieres que el equipo te responda. También recogemos automáticamente algunos datos básicos para entender tus comentarios. Consulta el punto 2 del apartado anterior "Información que obtenemos automáticamente” para ver qué datos recogemos. Consulta más información sobre las [prácticas de seguridad y privacidad de Outline](/about/security-and-privacy).

 Si utilizas una beta de la aplicación de Outline en Android, podríamos usar el servicio [Firebase](https://firebase.google.com/) de Google para recoger información de depuración que nos ayude a detectar problemas y a mejorar Outline. Para obtener más información sobre las políticas de seguridad y privacidad de Firebase, visita el sitio web [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Si no quieres que Outline envíe esta información a través de Firebase, utiliza la versión de producción de la aplicación.
