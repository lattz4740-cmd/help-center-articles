---
title: "Como faço para definir limites de dados em chaves de acesso?"
sidebar_label: "Como faço para definir limites de dados em chaves de acesso?"
---

É possível definir um limite de dados padrão para todas as chaves de acesso. Para fazer isso, abra o Outline Manager e vá até "Configurações". Lá você verá o botão do recurso Limites de Dados que, quando ativado, permite a definição de um limite.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Após definir um limite, você pode consultar a situação de cada usuário na página "Chaves de acesso". Um gráfico de barras mostra o uso de dados nos últimos 30 dias.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Além de definir um limite de dados padrão para todas as chaves de acesso, é possível configurar um limite próprio para cada chave. Essa configuração substitui qualquer limite padrão definido. Se você não tiver estabelecido um, ainda pode definir limites específicos para chaves individuais. 

 Para definir o limite de transferência de dados de uma chave, abra o Outline Manager, vá até a guia "Conexões" e clique no menu à direita da linha da chave. Em seguida, clique em "Limite de dados". Para alterar o limite de dados em "Minha chave de acesso", clique no ícone Limites de Dados ![Ícone de limites de dados](/images/data-limits-icon.png).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Selecione "Definir um limite de dados personalizado". Depois de marcar essa caixa de seleção, será exibido um campo em que é possível definir o limite de dados personalizado para a chave. Clique no botão SALVAR quando terminar.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Depois disso, o limite de dados para a chave escolhida aparece na tela principal com o uso de dados (nos últimos 30 dias) para cada chave.

Para remover o limite de dados de uma chave de acesso, abra a caixa de diálogo "Limite de dados" da chave, como você já fez, e desmarque a caixa de seleção "Definir um limite de dados personalizado". Depois, clique em SALVAR.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Perguntas frequentes sobre limites de dados
## O que é um limite de uso de dados de 30 dias?
 Esse limite soma o uso de cada chave nos últimos 30 dias e mantém o uso abaixo do limite nesse período. Assim, a chave nunca ultrapassa o limite, mesmo nos meses com mais ou menos de 30 dias. Ou seja, os dados disponíveis para cada usuário aumentam a cada dia de acordo com o valor usado nos 31 dias anteriores.

## Por que o Outline tem limites de uso?

 Esses limites oferecem garantias a cada período de 30 dias. Isso significa que são mais fáceis de configurar do que os limites recorrentes, como no caso de datas personalizadas, mas com garantias semelhantes. Eles também são usados na exibição atual do uso de dados do Outline e em ferramentas comuns, como estatísticas do servidor e serviços de análise de dados.

## Quais dados são contabilizados nos limites?
 Cada saída de chave de acesso é incluída no cálculo. A rigor, isso abrange os dados enviados do servidor em nome da chave e os recebidos pelo cliente. Na prática, como isso se ajusta ao tráfego enviado da chave para o servidor e vice-versa, esperamos que isso corresponda aos cálculos dos seus usuários. Fizemos essa escolha porque os provedores de nuvem que pesquisamos cobram com base na saída.

## Os usuários serão notificados se ultrapassarem o limite?
 No momento, não. Muitos provedores de nuvem adotam um limite de 1 TB para o mês inteiro, que pode ser consumido por até 10 usuários com 100 GB ou 100 usuários com 10 GB. Esses números são bem altos, por isso acreditamos que a maioria dos usuários não os atingirá. Esperamos que os usuários entrem em contato com os gerentes do servidor quando atingirem o limite. No entanto, gostaríamos de saber como as notificações podem ajudar no seu caso de uso. Entre em contato com nossa equipe [aqui](/about/feedback).

## Os usuários serão notificados se chegarem perto do limite de dados?
 A quantidade de novos dados que um usuário perto do limite recebe tende a variar, porque se baseia no uso dos últimos 30 dias. Acreditamos que um alerta pode confundir em vez de ajudar os usuários finais. Gostaríamos de receber seu feedback sobre esse comportamento [aqui](/about/feedback).

## Posso redefinir o uso de dados de um usuário?
 Não. O limite de um usuário sempre inclui os últimos 30 dias do uso de dados. No entanto, é possível aumentar o limite de dados da chave ou criar uma nova chave para a pessoa.

## Por que alguns usuários perderam o acesso assim que ativei os limites de dados?
 Os limites são baseados nos 30 dias anteriores da transferência de dados dos usuários, que são registrados independentemente da ativação desse recurso. É possível que os usuários em questão já tenham excedido o limite antes da implantação. Todos os limites de dados são aplicados, mesmo se você alterar o limite de uma chave.

## Posso definir um limite para o servidor, por exemplo, 1 TB por 30 dias?
 No momento, não. Gostaríamos de saber mais sobre seu caso de uso [aqui](/about/feedback).

## Se houver um limite de dados padrão e outro em uma chave específica, qual deles será aplicado?
 O limite da chave específica substitui qualquer padrão.

## Posso definir o limite de dados de uma chave específica sem ter um padrão definido?
 Sim. Você não precisa ter um limite padrão para definir o de uma chave específica. Por exemplo, é possível definir um limite para uma chave que você acha que será amplamente compartilhada. Assim, você se protege da transferência excessiva de dados nessa chave.
