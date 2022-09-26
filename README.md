
# ORM-IA

ORM IA é um projeto de desenvolvimento de uma rede neural para classificação de perfis de aprendizado aplicado a um jogo educacional de história

### CONTEXTO
___
O processo de ensino-aprendizagem, mesmo seguindo alguns padrões, é complexo, dinâmico e relativamente personalizado. Em um contexto de gamificação o objetivo é sanar os problemas motivacionais de um aluno, deixando de lado os processo de aprendizado que é o mesmo para todos jogadores. Com base nisso o projeto visa sanar esse problema do processo de gamificação propondo um processo de aprendizado personalizado dentro do contexto do jogo.
___
### FUNCIONALIDADES

User Stories

1. Eu como usuario final gostaria que o jogo se adaptasse a minha forma de aprender, para que possa melhorar meu aprendizado

        Critérios de aceitação:
        * O jogo deve mapear o perfil do aluno com base nas dimensões visual/verbal, ativo/reflexico, sensorial/intuitivo e sequencial/global do modelo de felder e silverman.
        * Devem ser coletados informações de alunos do ensino médio
        * O questionário deve ser preenchido por uma grande quantidade de alunos
        DOD :
        * Questionários com as respostas de cada aluno
        * Arquivo XLSX com os dados preenchidos de todos os alunos
    
 

2. Eu como usuario final gostaria que o jogo descobrisse qual a melhor forma de eu aprender. 

        Criterios de aceitação:
        * A rede neural deve coletar as informações do usuário dentro do jogo
        * As métricas de desemepenho do usuario devem atender os requisistos do modelo de felder e silverman
        * A eficacia da rede neural deve ser superior a 70% em relação a predição de aprendizado
        * 60% dos dados devem usados como conjunto de treinamento e 40% para o conjunto de teste
        DOD:
        * Diagramas com a porcentagem da efetividade da rede neural
        * Relatório de conclusão do código da rede neural e como foi desenvolvido
        * Relatório dos conjuntos de dteste da rede neural

3. Eu como usuario final gostaria que toda vez que retornar ao jogo, minha estratégia de jogo fosse a mesma

        Criterios de aceitação:
        * O banco de dados deve conter informações para identificar cada aluno individualmente
        * Os dados de desempenho dele devem ser persistidos no banco de dados 
        * O progresso dele deve ser persistido no banco de dados
        DOD:
        *Diagrama de desenvolvimento do banco de dados
        *Relatórios dos testes do banco 
        




