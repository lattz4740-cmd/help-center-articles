---
title: "¿Cómo puedo configurar límites de datos para las claves de acceso?"
sidebar_label: "¿Cómo puedo configurar límites de datos para las claves de acceso?"
---

Puedes fijar un límite de datos que se aplicará a todas las claves de acceso. Para hacerlo, abre Administrador de Outline y ve a Ajustes. Desde ahí, activa la opción Límites de datos. Después, podrás fijar un límite.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Cuando hayas establecido el límite, podrás ver cuánto le queda a cada usuario para alcanzarlo en la página de claves de acceso, donde un gráfico de barras muestra el uso de datos de los últimos 30 días.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

También puedes fijar un límite de datos concreto para cada una de tus claves de acceso, que prevalecerá sobre el límite predeterminado que tengas configurado. Aunque no tengas uno predeterminado, puedes fijar límites de datos para cualquier clave. 

 Para aplicar un límite de transferencia de datos a una clave, abre Administrador de Outline, accede a la pestaña Conexiones y dirígete a la clave en cuestión. Luego, haz clic en el menú que aparece a la derecha de la fila de esa clave y haz clic en Límite de datos. Para cambiar el límite de datos de "Mi clave de acceso", haz clic en el icono de la opción Límite de datos ![Icono de Límites de datos](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Selecciona Establecer límite de datos personalizado. Una vez hecho esto, aparecerá un campo donde podrás fijar el límite de datos personalizado de esa clave. Cuando termines, haz clic en el botón GUARDAR.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Una vez guardado el límite de transferencia de datos de la clave en cuestión, este aparecerá en la pantalla principal junto al uso de datos de los últimos 30 días correspondiente a cada clave.

Para quitar el límite de datos de una clave de acceso, ve al cuadro de diálogo Límite de datos de la clave, tal y como se ha explicado anteriormente. Una vez ahí, desmarca la casilla Establecer límite de datos personalizado y, luego, haz clic en el botón GUARDAR.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Preguntas frecuentes sobre los límites de datos****

****¿Qué es un límite de datos adaptable de 30 días?****

 Con este límite, se suma el uso que se ha hecho de cada clave en los últimos 30 días, de modo que el uso dentro de ese periodo siempre debe estar por debajo del límite. Así, no se podrá superar el límite de las claves en ningún periodo de 30 días, incluidos los meses naturales de 30 días o menos. Esto significa que, cada día, se sumará a los datos disponibles de un usuario la cantidad de datos que usó hace 31 días.

**¿Por qué se usan límites adaptables en Outline?**

 Los límites adaptables ofrecen una garantía en cualquier intervalo de 30 días, por lo que son más fáciles de configurar que los límites periódicos (que se reiniciarían el día del mes que eligieras) y ofrecen garantías similares. Además, es el mismo sistema que se usa para visualizar el uso de datos en Outline y en otras herramientas habituales, como servicios de análisis y estadísticas de servidores.

**¿Qué datos se tienen en cuenta para el límite de datos?**

 Se considera el tráfico de salida del servidor de cada clave de acceso. Para ser exactos, son los datos que se envían en nombre de la clave hacia fuera del servidor y de vuelta al cliente. Los datos deberían coincidir prácticamente con el tráfico enviado de la clave al servidor y viceversa, por lo que esperamos que no haya mucha diferencia con los cálculos de tus usuarios. Hemos elegido el tráfico de salida porque es el elemento por el que facturan los proveedores de servicios en la nube con los que hemos contactado.

**¿Se notificará a los usuarios si han alcanzado el límite de datos?**

 Por el momento, no. Muchos proveedores de servicios en la nube aplican, por ejemplo, un límite de 1 TB para todo el mes, lo que equivale a 10 usuarios con 100 GB o a 100 con 10 GB. Son volúmenes bastante grandes y no creemos que muchos usuarios los alcancen. En el caso de que un usuario alcanzara el límite, debería ponerse en contacto con el administrador de su servidor. Sin embargo, si crees que las notificaciones podrían ser de ayuda en tu caso concreto, te agradeceríamos que [te pusieras en contacto con nosotros](/about/feedback) y nos lo contaras.

**¿Se notificará a los usuarios si falta poco para que alcancen el límite de datos?**

 La cantidad de datos nuevos que recibirá un usuario que se acerque a su límite variará de un día para otro, ya que se basa en su uso de hace 30 días. Si apareciera una advertencia, creemos que esto confundiría a los usuarios finales más que ayudarlos. Agradeceríamos que nos enviaras tus comentarios al respecto a través de [este enlace](/about/feedback).

**¿Puedo restablecer el uso de datos de un usuario?**

 No, el límite de cada usuario siempre abarca su uso de datos durante los últimos 30 días. Sin embargo, puedes aumentar el límite de su clave o crear una nueva.

**¿Por qué algunos de mis usuarios perdieron su acceso en cuanto habilité los límites de datos?**

 Los límites de datos se basan en el volumen de transferencia de datos de los usuarios durante los últimos 30 días, que se registra independientemente de si se han habilitado o no los límites de datos. Es posible que los usuarios afectados ya hayan superado el límite que has establecido. Además, ten en cuenta que todos los límites de datos se aplican incluso cuando cambias el de una clave concreta.

**¿Puedo definir un límite para todo el servidor (por ejemplo, 1 TB por cada 30 días)?**

 Por el momento, no. Nos encantaría que nos dejaras tus comentarios sobre tu caso concreto [aquí](/about/feedback).

**Si hay un límite de datos predeterminado y un límite de datos en una clave concreta, ¿cuál de los dos se aplicará?**

 El límite de datos específico de la clave prevalecerá sobre cualquier límite predeterminado que hayas configurado.

**¿Puedo configurar un límite de datos para una clave específica sin tener ningún límite de datos predeterminado?**

 Sí. No necesitas un límite predeterminado para configurar un límite de datos en una clave. Por ejemplo, puedes configurar un límite para una clave que creas que podría compartirse entre varias personas, para protegerte del exceso de datos que se transferirán con esa clave.
