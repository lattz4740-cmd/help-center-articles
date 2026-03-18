---
title: "¿Por qué no puedo instalar Outline Manager en Windows?"
sidebar_label: "¿Por qué no puedo instalar Outline Manager en Windows?"
---

Es posible que veas este mensaje de error: "Lamentablemente, parece que Outline no está instalado de forma adecuada. Vuelve a instalarlo. Si el problema persiste, [envía tus comentarios](https://support.getoutline.org/s/contactsupport?)".

Si utilizas Outline en Windows, es posible que ocasionalmente te encuentres con un error inesperado. En la mayoría de los casos, se debe borrar el adaptador (controlador) TAP de Outline y reinstalar el servicio.

Si bien los pasos pueden variar según la versión de tu sistema operativo Windows, aquí tienes pasos generales para desinstalar Outline Manager y el adaptador TAP, y, luego, reinstalar Outline Manager.

1. Desinstala el adaptador TAP para Outline Manager.
   1. Ve al Administrador de dispositivos y, luego, a Adaptadores de red.
   2. Busca el elemento "TAP-Windows Adapter V9" o el adaptador TAP que esté asociado a Outline.
   3. Desinstala o borra el adaptador. Recuerda que esta acción podría afectar a otras apps de VPN que hayas instalado.
2. Desinstala Outline Manager.
   1. Ve a Programas y características; luego, a Desinstalar programa.
   2. Busca la app de Outline Manager y desinstálala.
   3. [Descarga la versión más reciente de Outline Manager](https://getoutline.org/get-started/#step-1) y reinstálala en tu dispositivo Windows. Con la instalación nueva, debería instalarse automáticamente un nuevo adaptador TAP.

Si los problemas persisten, [comunícate con el equipo de asistencia](https://support.getoutline.org/s/contactsupport?l).
