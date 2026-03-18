---
title: Configuración automatizada de Google Cloud
sidebar_label: Configuración automatizada de Google Cloud
---

## Descripción general

Outline Manager incluye una función que te permite configurar Outline Server automáticamente en un servidor que se ejecute en Google Cloud. Si eliges usar esta función, Outline Manager te pedirá que accedas a tu Cuenta de Google, lo que le otorgará ciertos permisos de [OAuth](https://developers.google.com/identity/protocols/oauth2) a la instalación local de Outline Manager para configurar tu cuenta de Google Cloud.

 Si no quieres otorgar los permisos, puedes seguir las instrucciones de configuración avanzada que figuran en Outline Manager para ejecutar Outline en Google Cloud.

## Permisos otorgados

Para poder ofrecer una configuración automatizada, Outline Manager requiere los siguientes permisos de tu Cuenta de Google.

## Google Cloud

- Ver y administrar tus recursos de Google Compute Engine
- Ver tus datos en todos los servicios de Google Cloud y ver la dirección de correo electrónico de tu Cuenta de Google

## Información básica de la cuenta

- Ver la dirección de correo electrónico principal de tu Cuenta de Google
- Asociarte con tu información personal en Google

## Acceso adicional

- Administrar tus proyectos de Cloud
- Ver y administrar tus cuentas de facturación de Google Cloud
- Administrar la configuración de los servicios de las API de Google

Estos permisos nos permiten admitir funciones avanzadas para administrar tus servidores de Outline, incluidas las siguientes:

- Permitirte seleccionar la cuenta de facturación correcta
- Crear un proyecto nuevo para organizar tus servidores de Outline
- Generar una lista de los centros de datos disponibles
- Crear máquinas virtuales nuevas para ejecutar Outline
- Configurar la nueva máquina virtual con Outline

## Cómo revocar los permisos

Para revocar el acceso de Outline Manager a Google Cloud Platform, puedes visitar [Mi cuenta](https://myaccount.google.com/permissions). Si revocas el acceso, todos los servidores que hayas creado con la configuración automatizada seguirán ejecutándose, pero ya no aparecerán en Outline Manager. Para restablecer el acceso a esos servidores, simplemente inicia el flujo de configuración automatizada para volver a conectarte a Google Cloud Platform.

## Organización de los proyectos de Outline

La configuración automatizada de Google Cloud usa un único [proyecto de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) para organizar los servidores de Outline. El proyecto se crea la primera vez que se utiliza la configuración automatizada, con un ID de proyecto sugerido que comienza con "Outline-" seguido de una cadena de caracteres aleatorios. Si lo prefieres, puedes elegir otro ID de proyecto durante el proceso de creación. El proyecto se llamará "Servidores de Outline".

## Cuenta de facturación

Los proyectos de Google Cloud requieren una "cuenta de facturación" vinculada que defina la información de pago. La primera vez que uses la configuración automatizada de Google Cloud, se te pedirá que proporciones una cuenta de facturación para asociarla con los servidores de Outline. A veces, un servidor puede dejar de ejecutarse si hay un problema con la cuenta de facturación. En ese caso, debes acceder a [Google Cloud Console](https://console.cloud.google.com/getting-started), buscar el proyecto de Google Cloud que esté asociado con Outline (llamado "Servidores de Outline") y actualizar la configuración de facturación.

## Cómo destruir los servidores

Si quieres destruir los servidores que se crean con la configuración automatizada, la forma más sencilla de hacerlo es desde Outline Manager. Sin embargo, si quieres hacerlo manualmente, puedes acceder a la [consola de Google Cloud](https://console.cloud.google.com/getting-started), buscar el proyecto que se creó durante la configuración inicial (llamado "Servidores de Outline") y borrar los recursos que se encuentren allí o dar de baja el proyecto.
