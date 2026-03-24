---
title: Seguridad y privacidad mientras se utiliza Outline
sidebar_label: Seguridad y privacidad mientras se utiliza Outline
---

Seguridad y privacidad mientras se utiliza Outline

## Cómo Outline protege tus comunicaciones en línea

El tráfico de Internet es muy vulnerable a la vigilancia mientras se traslada a través de tu red local o nacional.

Outline ayuda a mantener la privacidad de tus comunicaciones, ya que encripta tu tráfico de Internet a medida que este se traslada dentro de tu red nacional y lo mantiene encriptado hasta que llega al servidor de Outline. Si el tráfico está encriptado con Outline, los usuarios que observan la actividad de la red no pueden examinar los sitios web que visitas ni la información que transfieres.

Outline también puede ayudarte a recuperar el acceso a herramientas de comunicación integrales y seguras a las que no se pueda acceder de otro modo en tu país.

## Estándares de encriptación

Outline encripta las comunicaciones entre tu dispositivo y el servidor de Outline por medio del algoritmo de cifrado Chacha2020 IETF Poly 1305 de 256 bits de AEAD. Los algoritmos de cifrado de AEAD ofrecen confidencialidad, integridad y autenticidad, y demuestran un rendimiento excelente en los hardware modernos.

## Auditorías de seguridad

En el 2018, Outline se sometió a las auditorías de Radically Open Security y Cure53, dos organizaciones de seguridad digital independientes que revisan software teniendo en cuenta los más recientes estándares de seguridad. Radically Open Security realizó una auditoría adicional en el 2022, y Cure53 realizó una auditoría del SDK de Outline en el 2024. Puedes leer los informes aquí:

- [Informe de prueba de penetración de Radically Open Security (marzo de 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Informe de auditoría y prueba de penetración de Cure53 para Outline de Jigsaw (diciembre de 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Informe de prueba de penetración de Radically Open Security (diciembre de 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Informe de prueba de penetración de Cure53 para el SDK de la VPN de Outline de Jigsaw (enero de 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Métricas y registros anónimos

Outline solo hace un seguimiento del ancho de banda utilizado como "bytes transferidos" para cada clave de acceso. Esta información permite que los administradores del servidor ajusten sus suscripciones de ancho de banda con los proveedores de su servidor en la nube según sea necesario, pero no les permite ver la información real que se trasladó por el servidor de Outline.

Obtén más información sobre la [recopilación de información y datos](/about/data-collection) de Outline.

---

## Preguntas frecuentes sobre la seguridad y la privacidad

## ¿Outline puede hacer que me vea como anónimo en línea?

No, Outline no es una herramienta de anonimato, sino que protege tu privacidad para que los usuarios que observan la actividad de la red no puedan examinar tu tráfico.

Outline no te ofrece un anonimato total en los sitios web que visitas, ya que estos aún pueden identificarte cuando accedes y, en ocasiones, lo hacen por medio de técnicas como la detección de la huella digital del navegador. Con respecto a las apps para dispositivos móviles, la mayoría de los smartphones modernos tienen API que permiten que las apps instaladas recuperen tu ubicación independientemente de tu proxy, ya que pueden utilizar el GPS incorporado.

En general, las VPN ofrecen protecciones importantes, particularmente contra la vigilancia en Internet, pero siempre existen riesgos al trabajar en línea. Aunque tengas una VPN, si un ISP ya conoce tu identidad y puede examinar tu tráfico de red, tal vez pueda determinar la dirección IP de tu servidor de Outline. Esta información se puede utilizar para bloquear el acceso al servidor de Outline o aprender patrones de uso (como cuándo sueles estar en línea) y, posiblemente, obtener tu ubicación aproximada.

## ¿Alguien puede notar que estoy usando Outline?

Posiblemente. Las plataformas y los servicios a los que accedas probablemente puedan notar que tu conexión proviene de un servidor en la nube. En ocasiones, es posible que se infiera que estás usando una VPN, pero no se podrá ver el contenido de tu tráfico de Internet.

## ¿Outline me protege de todas las posibles amenazas cibernéticas?

No. Ninguna herramienta te protegerá de todas las posibles amenazas cibernéticas. Si bien Outline te brinda acceso a un Internet abierto y aumenta tu privacidad mediante la encriptación de tu tráfico, te recomendamos que tomes precauciones adicionales para protegerte de otros tipos de ataques, como el software malicioso y el phishing.

Para fortalecer tus defensas en línea, evalúa trabajar con el experto en seguridad cibernética de tu organización. Como alternativa, puedes obtener instrucciones personalizadas de expertos de seguridad líderes de la industria en [Security Planner](https://securityplanner.org/), un sitio web creado con el fin de brindar instrucciones claras para elegir las herramientas de seguridad cibernética adecuadas según tus necesidades.

También puedes consultar los otros productos de seguridad cibernética de [Jigsaw](https://jigsaw.google.com/), como [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) y [Alerta de contraseña](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## ¿Es legal usar una VPN?

Antes de operar con Outline o de usar la app, consulta las leyes o reglamentaciones locales, y revisa las Condiciones del Servicio del proveedor de nube que planeas usar.
