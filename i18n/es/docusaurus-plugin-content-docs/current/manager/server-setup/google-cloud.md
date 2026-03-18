---
title: Configuración automatizada de Google Cloud
sidebar_label: Configuración automatizada de Google Cloud
---

## Descripción general

Administrador de Outline incluye una función que te permite configurar automáticamente el servidor de Outline en un servidor que funciona en Google Cloud. Si decides utilizar esta función, Administrador de Outline te pedirá que inicies sesión con tu cuenta de Google, lo que te permitirá dar determinados permisos de [OAuth](https://developers.google.com/identity/protocols/oauth2) a tu instalación local de Administrador de Outline para configurar tu cuenta de Google Cloud.

Si no quieres dar estos permisos, puedes seguir las instrucciones de configuración avanzada de Administrador de Outline para ejecutar Outline en Google Cloud Platform.

## Permisos dados

Para proporcionar una configuración automática, Administrador de Outline necesita los siguientes permisos de tu cuenta de Google.

## Google Cloud Platform

- Ver y gestionar tus recursos de Google Compute Engine
- Consultar tus datos en los servicios de Google Cloud y ver la dirección de correo de tu cuenta de Google

## Información básica de la cuenta

- Ver la dirección de correo principal de tu cuenta de Google
- Asociar tu identidad a tu información personal en Google

## Acceso adicional

- Gestionar tus proyectos de Cloud Platform
- Ver y gestionar tus cuentas de facturación de Google Cloud Platform
- Gestionar tu configuración de servicios de la API de Google

## Con estos permisos podemos ofrecer funciones avanzadas para gestionar tus servidores de Outline como las mencionadas a continuación:

- Permitir que se seleccione la cuenta de facturación correcta
- Crear un proyecto para organizar tus servidores de Outline
- Mostrar los centros de datos disponibles
- Crear máquinas virtuales para ejecutar Outline
- Configurar la nueva máquina virtual con Outline

## Revocar permisos

Puedes revocar el acceso a Google Cloud Platform de Administrador de Outline desde [Mi Cuenta](https://myaccount.google.com/permissions). Si revocas el acceso, los servidores que hayas creado con la configuración automática seguirán funcionando, pero ya no aparecerán en Administrador de Outline. Para restaurar el acceso a ellos, solo tienes que volver a conectarte a Google Cloud Platform iniciando el proceso de configuración automatizado.

## Organización de un proyecto de Outline

La configuración automática de Google Cloud utiliza un único [proyecto de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) para organizar tus servidores de Outline. El proyecto se crea la primera vez que se usa la configuración automatizada y se sugiere un ID de proyecto que empieza por "Outline-" seguido de una cadena de caracteres aleatorios. Si lo prefieres, puedes elegir otro ID de proyecto al crear el proyecto. En este caso, el proyecto tendrá el nombre "Servidores de Outline".

## Cuenta de facturación

Los proyectos de Google Cloud requieren una "cuenta de facturación" vinculada que defina datos de pago. La primera vez que uses la configuración automática de Google Cloud, se te pedirá que proporciones una cuenta de facturación para asociarla a tus servidores de Outline. A veces un servidor deja de funcionar porque hay un problema con la cuenta de facturación. En ese caso, inicia sesión en la [consola de Google Cloud](https://console.cloud.google.com/), busca el proyecto de Google Cloud asociado a Outline (denominado "Servidores de Outline") y actualiza la configuración de facturación.

## Eliminar servidores definitivamente

Si quieres eliminar definitivamente tus servidores que has creado mediante la configuración automática, la forma más sencilla de hacerlo es desde Administrador de Outline. Sin embargo, si quieres eliminar definitivamente los servidores por tu cuenta, inicia sesión en la [consola de Google Cloud](https://console.cloud.google.com/), busca el proyecto creado durante la configuración inicial (denominado "Servidores de Outline") y elimina los recursos allí o cierra el proyecto.
