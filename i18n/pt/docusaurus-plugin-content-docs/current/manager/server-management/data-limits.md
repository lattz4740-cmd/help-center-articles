---
title: "Como é que defino limites de dados em chaves de acesso?"
sidebar_label: "Como é que defino limites de dados em chaves de acesso?"
---

Pode definir um limite de dados aplicável a todas as chaves de acesso. Para definir o limite, abra o Gestor Outline e navegue para Definições. Nesta página, encontra o botão Limites de dados. Quando é ativado, este botão permite-lhe definir um limite.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Depois de definir o limite, pode ver a proximidade de cada utilizador em relação ao limite na página da chave de acesso, onde um gráfico de barras mostra a utilização de dados nos últimos 30 dias.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Além de poder definir um limite para todas as suas chaves de acesso, também pode conceder a cada chave o seu próprio limite de dados. Esta definição substitui qualquer limite de dados que tenha predefinido. No entanto, se não tiver predefinido nenhum limite de dados, continua a poder definir um limite de dados para qualquer chave. 

 Para definir o limite de transferência de dados de uma chave, abra o Gestor Outline, navegue para o separador Ligações que contém a chave que quer definir e clique no menu no lado direito da linha da chave. A seguir, clique em Limite de dados. Para alterar o limite de dados em "A minha chave de acesso", clique no ícone Limite de dados ![Ícone de limites de dados](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Selecione a opção Defina um limite de dados personalizado. Após selecionar esta caixa de verificação, aparece um campo onde pode definir o limite de dados personalizado da chave em questão. Clique no botão GUARDAR quando terminar para guardar o limite de dados.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Após guardar o limite de transferência de dados da chave selecionada, o limite aparece no ecrã principal, juntamente com a utilização de dados de cada chave (ao longo dos últimos 30 dias).

Para remover o limite de dados de uma chave de acesso, navegue para a caixa de diálogo Limite de dados da chave, conforme fez anteriormente. Desmarque a caixa com a indicação Defina um limite de dados personalizado e clique no botão GUARDAR.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Perguntas frequentes sobre o limite de dados
## O que é um limite de dados adaptável de 30 dias?
 Um limite de dados adaptável de 30 dias soma a utilização de cada chave ao longo dos últimos 30 dias e mantém a utilização da chave abaixo do limite durante o período em questão. Como efeito, a chave não pode ultrapassar o limite durante qualquer período de 30 dias, incluindo os meses de calendário de 30 dias ou menos. Na prática, isto significa que os dados disponíveis de cada utilizador aumentam a cada dia, conforme a quantidade usada 31 dias antes.

## Porque é que o Outline usa limites adaptáveis?
 Os limites adaptáveis dão garantias para cada período de 30 dias, o que significa que são mais simples de configurar do que um limite recorrente (como um dia personalizável do mês) e oferecem garantias semelhantes. Também correspondem à visualização atual da utilização de dados do Outline, bem como a ferramentas comuns, como serviços de análise e estatísticas de servidores.

## Quais são os dados contabilizados num limite de dados?
 ~

 O cálculo inclui a saída de cada chave de acesso do servidor. Em rigor, isto corresponde aos dados enviados em nome da chave para fora do servidor e também de volta ao cliente. Na prática, este valor deve estar estritamente alinhado com o tráfego enviado da chave para o servidor e vice-versa, pelo que esperamos que corresponda aos registos dos seus utilizadores. Escolhemos a saída porque é o valor faturado pelos fornecedores de nuvem que analisámos.

## Os utilizadores são notificados se esgotarem o limite?
 De momento, não. Muitos fornecedores de nuvem incluem um limite, como 1 TB, para todo o mês, o que pode permitir ter 10 utilizadores a 100 GB ou 100 utilizadores a 10 GB. Estes números são bastante elevados e não esperamos que muitos utilizadores os atinjam. Esperamos que os utilizadores contactem os gestores dos servidores quando atingirem o limite. No entanto, agradecemos que partilhe informações sobre a forma como as notificações podem ajudar no seu exemplo de utilização. Pode contactar-nos [aqui](/about/feedback).

## Os utilizadores são notificados caso se aproximem do respetivo limite de dados?
 A quantidade de novos dados recebida por um utilizador que se aproxima do limite varia de dia para dia, uma vez que é baseada na utilização que fez 30 dias antes. Parece-nos que um aviso iria provavelmente confundir os utilizadores finais em vez de os ajudar. Agradecemos que nos envie o seu feedback sobre este comportamento [aqui](/about/feedback).

## Posso repor a utilização de dados de um utilizador?
 Não, o limite de um utilizador inclui sempre os últimos 30 dias de utilização de dados. No entanto, pode aumentar o limite de dados da respetiva chave ou criar uma nova chave.

## Porque é que alguns dos meus utilizadores perderam o acesso assim que ativei os limites de dados?
 Os limites de dados baseiam-se nos 30 dias anteriores de transferência de dados dos utilizadores, que são registados quer os limites de dados tenham ou não sido ativados. É possível que os utilizadores em questão já tivessem ultrapassado o limite antes de este ter sido implementado. Tenha também em atenção que todos os limites de dados são aplicados mesmo quando altera o limite de dados de uma única chave.

## Posso definir um limite para todo o servidor, como "1 TB por cada 30 dias"?
 De momento, não é possível. Gostaríamos de saber mais sobre o seu exemplo de utilização [aqui](/about/feedback).

## Se existir um limite de dados predefinido e um limite de dados para uma chave específica, qual é aplicado?
 O limite de dados da chave específica substitui qualquer limite de dados que tenha predefinido.

## Posso definir um limite de dados para uma chave específica sem ter um limite de dados predefinido?
 Sim. Não é preciso ter um limite predefinido de modo a definir um limite de dados para uma chave. Por exemplo, pode definir um limite para uma chave que, na sua opinião, pode ser amplamente partilhada, de modo a proteger-se da transferência de dados excessiva através da chave em questão.
