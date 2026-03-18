---
title: "¿Por qué no puedo instalar el cliente de Outline en Windows?"
sidebar_label: "¿Por qué no puedo instalar el cliente de Outline en Windows?"
---

Es posible que veas este mensaje de error: "Lamentablemente, parece que Outline no está instalado de forma adecuada. Vuelve a instalarlo. Si el problema persiste, [envía tus comentarios](/about/feedback)".

Si utilizas Outline en Windows, es posible que ocasionalmente te encuentres con un error inesperado. En la mayoría de los casos, se debe borrar el adaptador (controlador) TAP de Outline y reinstalar el servicio.

Si bien los pasos pueden variar según la versión de tu sistema operativo Windows, aquí tienes pasos generales para desinstalar Outline y el adaptador TAP, y, luego, reinstalar Outline.

1. Desinstala el adaptador TAP para el cliente de Outline.
   - Ve al **Administrador de dispositivos** y, luego, a **Adaptadores de red**.
   - Busca el elemento **TAP-Windows Adapter V9** o el adaptador TAP que esté asociado a Outline.
   - Desinstala o borra el adaptador. Recuerda que esta acción podría afectar a otras apps de VPN que hayas instalado.
2. Desinstala el cliente de Outline.
   - Ve a **Programas y características** y, luego, a **Desinstalar programa**.
   - Busca la app del cliente de Outline y desinstálala.
   - [Descarga la versión más reciente del cliente de Outline](https://getoutline.org/get-started/#step-3) y reinstálalo en tu dispositivo Windows. Con la instalación nueva, debería instalarse automáticamente un nuevo adaptador TAP.

Si los problemas persisten, [comunícate con el equipo de asistencia](/about/feedback).
