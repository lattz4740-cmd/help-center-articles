---
title: "¿Cómo puedo establecer límites de datos para las claves de acceso?"
sidebar_label: "¿Cómo puedo establecer límites de datos para las claves de acceso?"
---

Puedes establecer un límite de datos que se aplique a todas las claves de acceso. Para establecer el límite, abre Outline Manager y navega a Configuración. Allí verás un botón para activar o desactivar la función Límites de datos. Cuando esté habilitada, podrás establecer un límite.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Una vez que lo hagas, podrás ver qué tan cerca está cada usuario de alcanzar el límite en la página de claves de acceso, donde se muestra un gráfico de barras con el uso de datos durante los últimos 30 días.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Además de poder establecer un límite para todas tus claves de acceso, puedes asignarle un límite de datos diferente a cada una. Este parámetro de configuración anulará los límites de datos predeterminados que estableciste. Si aún no lo has hecho, podrás establecer un límite de datos para cualquier clave de cualquier manera. 

 Para establecer un límite de transferencia de datos para una clave, abre Outline Manager, navega a la pestaña Conexiones que contiene la clave que quieres establecer. Luego, haz clic en el menú del lado derecho de la fila de claves. Allí, haz clic en Límites de datos (Data Limit). Para cambiar el límite de datos de "Mi clave de acceso", haz clic en el ícono Límites de datos (Data Limit) ![Ícono de límites de datos](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Selecciona Establecer un límite de datos personalizado (Set a custom data limit). Cuando hayas seleccionado la casilla de verificación, aparecerá un campo en donde podrás establecer el límite de datos personalizado para esa clave. Haz clic en el botón GUARDAR (SAVE) cuando quieras guardarlo.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Cuando hayas guardado el límite de transferencia de datos para la clave que elegiste, este aparecerá en la pantalla principal junto con el uso de datos (de los últimos 30 días) para cada clave.

Si quieres quitar el límite de datos de una clave de acceso, navega hacia el diálogo Límite de datos de esta, desmarca la casilla Establecer un límite de datos personalizado (Set a custom data limit) y, luego, haz clic en el botón GUARDAR (SAVE).

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## **Preguntas frecuentes sobre los límites de datos**
## **¿Qué es un límite de datos retrospectivo de 30 días?**
 Un límite de datos retrospectivo de 30 días suma el uso de cada clave durante los últimos 30 días y mantiene debajo del límite el uso de la clave durante ese período. De esta manera, la clave no puede superar el límite durante ningún período de 30 días, incluidos los meses calendario de 30 días o menos. Así, los datos disponibles de cada usuario aumentarán cada día según la cantidad que usó hace 31 días.

## ¿Por qué Outline usa límites retrospectivos?
 Los límites retrospectivos brindan garantías durante cada período de 30 días, lo que significa que son más fáciles de configurar que los límites recurrentes (como un día personalizable del mes), además de ofrecer garantías similares. También coinciden con la visualización existente sobre el uso de datos de Outline, así como con herramientas comunes, como estadísticas de servidores y servicios de datos.

## ¿Qué datos se registran en los límites?
 El registro incluye la salida del servidor de cada clave de acceso. En sentido estricto, son los datos que salen del servidor de parte de cada clave, así como la información que vuelve al cliente. En la práctica, esto debería alinearse estrechamente con el tráfico enviado desde la clave al servidor y viceversa, por lo que esperamos que coincida con los conteos de tus usuarios. Elegimos la salida porque es lo que facturan los proveedores de servicios en la nube que encuestamos.

## ¿Los usuarios recibirán una notificación si exceden su límite de datos?
 No por el momento. Muchos proveedores de servicios en la nube incluyen un límite, por ejemplo, 1 TB para todo el mes, que puede admitir 10 usuarios con 100 GB o 100 usuarios con 10 GB. Estas cantidades son bastante significativas, por lo que no esperamos que muchos usuarios alcancen los límites. Esperamos que los usuarios se comuniquen con los administradores del servidor cuando alcancen el límite correspondiente. Sin embargo, nos gustaría que nos envíes comentarios sobre cómo las notificaciones podrían ser útiles en tu caso de uso específico. Puedes comunicarte con nosotros[aquí](/about/feedback).

## ¿Los usuarios recibirán una notificación si se acercan al límite de datos?
 La cantidad de datos nuevos que recibirá un usuario que se acerque al límite variará de un día a otro, ya que se basa en su uso de hace 30 días. Creemos que, lejos de ayudarlos, es más probable que una advertencia confunda a los usuarios finales. Agradeceríamos que nos envíes tus comentarios sobre este comportamiento[aquí](/about/feedback).

## ¿Puedo restablecer el uso de datos de un usuario?
 No. El límite de un usuario siempre incluye los últimos 30 días de uso de datos. Sin embargo, puedes aumentar el límite de datos de su clave o crearle una nueva.

## ¿Por qué algunos de mis usuarios perdieron acceso cuando habilité los límites de datos?
 Los límites de datos se basan en los 30 días anteriores a la transferencia de datos de los usuarios, lo cual se registra sin importar si los límites de datos están habilitados o no. Es posible que los usuarios en cuestión ya hayan excedido el límite antes de que se haya establecido. Ten en cuenta que se aplicarán todos los límites de datos, incluso cuando se cambie el de una sola clave.

## ¿Puedo establecer un límite para todo el servidor, como “1 TB por 30 días”?
 Por el momento, no. Nos gustaría que nos brindes más detalles sobre tu caso de uso[aquí](/about/feedback).

## Si hay un límite de datos predeterminado y otro para una clave específica, ¿cuál se aplicará?
 El límite de datos de la clave específica anulará cualquier límite de datos predeterminado que hayas establecido (si corresponde).

## ¿Puedo establecer un límite de datos para una clave específica si no he establecido uno predeterminado?
 Sí. No necesitas tener un límite predeterminado para establecer un límite de datos en una clave. Por ejemplo, puedes establecer un límite en una clave que creas que se podría compartir de forma amplia para protegerte de transferencias de datos excesivas a través de ella.
