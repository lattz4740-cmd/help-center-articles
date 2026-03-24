---
title: Seguridad y privacidad al usar Outline
sidebar_label: Seguridad y privacidad al usar Outline
---

Seguridad y privacidad al usar Outline

## Cómo protege Outline las comunicaciones online

El tráfico de Internet es más vulnerable a la vigilancia cuando viaja por tu red local o nacional.

Outline te ayuda a mantener la privacidad de tus comunicaciones cifrando tu tráfico de Internet mientras se desplaza por tu red nacional y lo mantiene cifrado hasta que llega al servidor de Outline. Cuando el tráfico está cifrado con Outline, los observadores de la red no pueden inspeccionar los sitios web que visitas ni la información que transfieres.

Outline también puede ayudarte a recuperar el acceso a herramientas de comunicación seguras de extremo a extremo a las que, de otro modo, no podrías acceder en tu país.

## Estándares de cifrado

Outline cifra las comunicaciones entre tu dispositivo y el servidor de Outline mediante el cifrado de Chacha2020 IETF Poly 1305 de 256 bits de AEAD. El cifrado de AEAD ofrece confidencialidad, integridad y autenticidad, y tiene un rendimiento excelente en el hardware moderno.

## Auditorías de seguridad

En el 2018, Outline se sometió a una auditoría de la mano de Radically Open Security y Cure53, dos organizaciones independientes de seguridad digital que analizan software para verificar si cumple los últimos estándares de seguridad. Radically Open Security realizó otra auditoría en el 2022 y Cure53 hizo una auditoría del SDK de Outline en el 2024. Puedes acceder a los informes a continuación:

- [Informe de prueba de penetración de Radically Open Security (marzo del 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Informe de auditoría y prueba de penetración de Cure53 sobre Outline de Jigsaw (diciembre del 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Informe de prueba de penetración de Radically Open Security (diciembre del 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Informe de prueba de penetración de Cure53 sobre el SDK de la VPN de Outline de Jigsaw (enero del 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Métricas y registros anónimos

Outline hace un seguimiento del ancho de banda utilizado, como "bytes transferidos", para cada clave de acceso. Esta información permite a los administradores de servidores ajustar sus suscripciones de ancho de banda con sus proveedores de servidores en la nube según sea necesario, pero no les permite ver la información real que ha pasado por el servidor de Outline.

Consulta más información sobre la [recogida de datos e información](/about/data-collection) de Outline.

---

## Preguntas frecuentes sobre seguridad y privacidad

## ¿Puede Outline anonimizarme en Internet?

No, Outline no es una herramienta de anonimización. Outline protege tu privacidad frente a posibles observadores de la red.

Outline no te ofrece anonimato completo en los sitios web que visitas, ya que pueden identificarte cuando inicias sesión y, a veces, también pueden hacerlo mediante técnicas como la recogida de huellas digitales de navegador. En el caso de las aplicaciones móviles, la mayoría de los smartphones modernos tienen APIs que permiten que las aplicaciones instaladas obtengan tu ubicación independientemente de tu proxy, ya que pueden usar el GPS integrado.

En general, las VPNs ofrecen importantes protecciones, especialmente contra la vigilancia en Internet, pero siempre hay riesgos cuando se opera online. Incluso con una VPN, si un proveedor de Internet ya conoce tu identidad y puede observar tu tráfico de red, puede determinar la dirección IP de tu servidor de Outline. Con esta información, puede bloquear el acceso al servidor de Outline o descubrir patrones de uso, como cuándo sueles estar online y, posiblemente, tu ubicación aproximada.

## ¿Puede alguien saber si estoy usando Outline?

Posiblemente. Es muy probable que las plataformas y los servicios a los que accedas puedan detectar que tu conexión procede de un servidor en la nube. En ocasiones, pueden deducir que estás usando una VPN, pero no podrán ver el contenido de tu tráfico de Internet.

## ¿Outline me protege de todas las ciberamenazas posibles?

No. Ninguna herramienta te protegerá contra todas las ciberamenazas que hay. Outline te da acceso a un Internet abierto y aumenta tu privacidad cifrando tu tráfico. Sin embargo, te recomendamos que tomes precauciones adicionales para protegerte contra otros tipos de ataques, como el malware y el phishing.

Para reforzar tus defensas online, te recomendamos que trabajes con el experto en ciberseguridad de tu organización. También puedes obtener asesoramiento personalizado de expertos en seguridad líderes de [Security Planner](https://securityplanner.org/), un sitio web diseñado para ofrecer instrucciones claras sobre cómo elegir las herramientas de ciberseguridad adecuadas según tus necesidades.

También puedes consultar otros productos de ciberseguridad de [Jigsaw](https://jigsaw.google.com/), como [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) y [Alerta de Protección de Contraseña](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## ¿Es legal usar una VPN?

Consulta las leyes y los reglamentos locales, así como los Términos del Servicio del proveedor de servicios en la nube que tienes previsto utilizar antes de poner en marcha Outline o de usar la aplicación.
