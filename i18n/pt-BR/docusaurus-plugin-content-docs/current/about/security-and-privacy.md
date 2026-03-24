---
title: Segurança e privacidade ao usar o Outline
sidebar_label: Segurança e privacidade ao usar o Outline
---

Segurança e privacidade ao usar o Outline

## Como o Outline protege as comunicações on-line

O tráfego da Internet fica mais vulnerável à vigilância quando passa pela rede local ou nacional.

Para preservar a privacidade das comunicações, o Outline criptografa o tráfego da Internet enquanto ele transita pela rede nacional e o mantém criptografado até ele chegar ao servidor do Outline. Ao criptografar o tráfego com o Outline, os espectadores da rede não podem inspecionar os sites visitados ou as informações transferidas por você.

O Outline também ajuda a recuperar o acesso a ferramentas seguras de comunicação ponta a ponta que podem não estar disponíveis no seu país.

## Padrões de criptografia

O Outline criptografa as comunicações entre seu dispositivo e o servidor do Outline com a criptografia AEAD de 256 bits Chacha2020 IETF Poly 1305. A criptografia AEAD proporciona confidencialidade, integridade e autenticidade graças ao desempenho excelente em um hardware moderno.

## Auditorias de segurança

Em 2018, o Outline foi auditado pela Radically Open Security e pela Cure53, duas organizações independentes de segurança digital que analisam o software de acordo com as normas de segurança mais recentes. A Radically Open Security realizou outra auditoria em 2022, e a Cure53 realizou uma auditoria do SDK Outline em 2024. Leia os relatórios aqui:

- [Relatório do teste de penetração da Radically Open Security (março de 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Teste de penetração da Cure53 e relatório de auditoria do Outline da Jigsaw (dezembro de 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Relatório do teste de penetração da Radically Open Security (dezembro de 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Relatório do teste de penetração da Cure53 sobre o SDK Outline da VPN do Jigsaw (janeiro de 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Métricas e registros anônimos

O Outline monitora a largura de banda usada, como "bytes transferidos" para cada chave de acesso. Com essas informações, os administradores do servidor podem ajustar as assinaturas de largura de banda com os provedores de servidor de nuvem conforme necessário, mas não veem os dados concretos que passaram pelo servidor do Outline.

Saiba mais sobre a [coleta de dados e informações](/about/data-collection) do Outline.

---

## Perguntas frequentes sobre segurança e privacidade

## Fico anônimo on-line quando uso o Outline?

Não, o Outline não é uma ferramenta de anonimato. Ele protege sua privacidade contra possíveis espectadores da rede.

Com o Outline, você não fica completamente anônimo nos sites que visita, porque eles podem identificá-lo no login e, às vezes, com técnicas como a impressão digital do navegador. Quanto aos apps para dispositivos móveis, a maioria dos smartphones atuais tem APIs que permitem recuperar sua localização independentemente do proxy, porque contam com o GPS incorporado.

Em geral, as VPNs conferem proteção significativa, especialmente contra a vigilância da Internet, mas sempre há riscos no ambiente on-line. Mesmo com uma VPN, se um ISP já souber sua identidade e puder observar o tráfego da rede, ele identificará o endereço IP do servidor do Outline. Essas informações podem ser usadas para bloquear o acesso ao servidor do Outline ou para identificar padrões de uso como, por exemplo, os momentos em que você costuma ficar on-line e sua localização aproximada.

## Alguém sabe quando estou usando o Outline?

É provável que sim. As plataformas e os serviços que você acessa possivelmente identificarão que sua conexão é proveniente de um servidor na nuvem. Às vezes, eles podem deduzir que você está usando uma VPN, mas não veem o conteúdo do tráfego da Internet.

## O Outline protege contra todas as ameaças cibernéticas?

Não, nenhuma ferramenta protege contra todas as ameaças cibernéticas possíveis. O Outline concede acesso à Internet aberta e aumenta sua privacidade criptografando o tráfego, mas recomendamos que você tome precauções para se proteger contra outros tipos de ataques, como malware e phishing.

Para fortalecer suas defesas on-line, consulte o especialista em segurança cibernética da organização. Outra opção é solicitar a orientação personalizada dos maiores especialistas em segurança no [Security Planner](https://securityplanner.org/), um site que ensina como escolher as ferramentas certas de segurança cibernética conforme sua necessidade.

Confira também os outros produtos de segurança cibernética da [Jigsaw](https://jigsaw.google.com/), como o [Intra](https://getintra.org/), o [Project Shield](https://g.co/shield) e o [Alerta de senha](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## É lícito usar uma VPN?

Antes de usar o Outline ou o app, verifique a legislação e os regulamentos do seu país, bem como os Termos de Serviço do provedor de nuvem que você quer contratar.
