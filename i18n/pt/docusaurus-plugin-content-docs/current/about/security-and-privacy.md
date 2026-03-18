---
title: Segurança e privacidade enquanto usa o Outline
sidebar_label: Segurança e privacidade enquanto usa o Outline
---

Segurança e privacidade enquanto usa o Outline

## Como o Outline protege as suas comunicações online

O tráfego da Internet é mais vulnerável à vigilância enquanto passa pela sua rede local ou nacional.

O Outline ajuda a manter a privacidade das suas comunicações, encriptando o tráfego da Internet enquanto passa pela sua rede nacional e mantendo-o encriptado até chegar ao servidor do Outline. Quando o tráfego é encriptado com o Outline, os observadores da rede não podem inspecionar os Websites que visita nem as informações que está a transferir.

O Outline também pode ajudar a recuperar o acesso a ferramentas seguras de comunicação ponto a ponto que podem não estar acessíveis no seu país.

## Normas de encriptação

O Outline encripta as comunicações entre o seu dispositivo e o servidor do Outline através da cifra AEAD de 256 bits Chacha2020 IETF Poly 1305. As cifras AEAD oferecem confidencialidade, integridade e autenticidade, e apresentam um excelente desempenho no hardware moderno.

## Auditorias de segurança

Em 2018, o Outline foi auditado pela Radically Open Security e a Cure53, duas organizações independentes de segurança digital que fazem revisão ao software de acordo com as mais recentes normas de segurança. A Radically Open Security fez uma auditoria adicional em 2022, e a Cure53 fez uma auditoria ao Outline SDK em 2024. Pode ler os relatórios aqui:

- [Relatório de teste de intrusão da Radically Open Security (março de 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Relatório de auditoria e teste de intrusão da Cure53 sobre o Jigsaw Outline (dezembro de 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Relatório de teste de intrusão da Radically Open Security (dezembro de 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Relatório de teste de intrusão da Cure53 sobre o Jigsaw Outline VPN SDK (janeiro de 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Métricas e registos anónimos

O Outline monitoriza a largura de banda usada, avaliando-a em "bytes transferidos" para cada chave de acesso. Estas informações permitem aos administradores do servidor ajustar as respetivas subscrições de largura de banda junto dos fornecedores de servidores na nuvem, conforme necessário, mas não lhes permitem ver as informações reais que passaram pelo servidor do Outline.

Saiba mais sobre a [recolha de dados e informações](/about/data-collection) do Outline.

---

## Perguntas frequentes sobre segurança e privacidade

## O Outline pode tornar a minha identidade anónima online?

Não, o Outline não é uma ferramenta de anonimato. O Outline protege a sua privacidade contra potenciais observadores da rede.

O Outline não lhe oferece anonimato total nos Websites que visita, uma vez que estes continuam a conseguir determinar a sua identificação quando inicia sessão e, por vezes, através de técnicas como o fingerprinting do navegador. Em apps para dispositivos móveis, a maioria dos smartphones modernos inclui APIs que permitem que as apps instaladas obtenham a sua localização de forma independente do proxy, uma vez que podem usar o GPS incorporado.

A generalidade das VPNs oferece proteção significativa, particularmente contra a vigilância na Internet, mas existem sempre riscos durante as operações online. Mesmo com uma VPN, se um ISP já souber a sua identidade e conseguir observar o seu tráfego de rede, pode conseguir determinar o endereço IP do seu servidor do Outline. Estas informações podem ser usadas para bloquear o acesso ao servidor do Outline ou aprender padrões de utilização (por exemplo, quando está normalmente online) e, possivelmente, a sua localização aproximada.

## É possível perceber se estou a usar o Outline?

Talvez. É muito provável que as plataformas e os serviços a que acede consigam verificar que a sua ligação é proveniente de um servidor na nuvem. Ocasionalmente, podem deduzir que está a usar uma VPN, mas não conseguem ver o conteúdo do seu tráfego da Internet.

## O Outline protege-me de todas as possíveis ameaças cibernéticas?

Não. Nenhuma ferramenta protege contra todas as possíveis ameaças cibernéticas. O Outline dá-lhe acesso à Internet aberta e aumenta a sua privacidade, encriptando o seu tráfego, mas recomendamos que tome precauções adicionais para se proteger contra outros tipos de ataques, como software malicioso e phishing.

Para reforçar as suas defesas online, pondere trabalhar com o especialista em cibersegurança da sua organização. Em alternativa, pode receber orientação personalizada de especialistas de segurança de renome no [Security Planner](https://securityplanner.org/), um Website criado para lhe explicar claramente como escolher as ferramentas de cibersegurança certas para as suas preocupações.

Também pode consultar os outros produtos de cibersegurança da [Jigsaw](https://jigsaw.google.com/), como o [Intra](https://getintra.org/), o [Project Shield](https://g.co/shield) e o [Alerta de palavra-passe](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## É legal usar uma VPN?

Verifique as leis e os regulamentos locais, bem como os Termos de Utilização do fornecedor de nuvem que tenciona usar antes de operar o Outline ou usar a app.
