
# ORM-IA

ORM IA é um projeto de desenvolvimento de uma rede neural para classificação de perfis de jogador aplicado a um jogo educacional de história

### CONTEXTO
___
O processo de ensino-aprendizagem, mesmo seguindo alguns padrões, é complexo, dinâmico e relativamente personalizado. Em um contexto de gamificação o objetivo é sanar os problemas motivacionais de um aluno, deixando de lado os processo de aprendizado que é o mesmo para todos jogadores. Com base nisso o projeto visa sanar esse problema do processo de gamificação propondo um processo de aprendizado personalizado dentro do contexto do jogo.
___
### FUNCIONALIDADES

User Stories

1. Eu como usuario final gostaria que o jogo se adaptasse a minha forma de jogar, para que possa melhorar meu jogo

        Critérios de aceitação:
        * O jogo deve mapear o perfil do aluno com base nos tipos de jogadores de Richard Bartle.
        * Devem ser coletados informações de desempenho no jogo de alunos do ensino médio
        * O jogo deve ser jogado por uma grande quantidade de alunos, para que a IA possua uma grande base de dados.
        * Questionário para mapear o tipo de jogado do aluno, a ser comparado no final do jogo
        DOD :
        * Questionários e respostas em arquivo XLSX com os dados preenchidos de todos os alunos
        * Código de implementação da IA dentro do jogo complilada e sem erros.
        * Testes de unidade
        * Relatório de testes e Bugs
        * Refatoração
    
 

2. Eu como usuario final gostaria que o jogo descobrisse qual a melhor forma de eu aprender. 

        Criterios de aceitação:
        * A rede neural deve coletar as informações do usuário dentro do jogo
        * As métricas de desemepenho do usuario devem atender os requisistos do modelo de felder e silverman
        * A eficacia da rede neural deve ser superior a 70% em relação a predição de aprendizado
        * 60% dos dados devem usados como conjunto de treinamento e 40% para o conjunto de teste
        DOD:
        * Comparativo entre as diferentes redes neurais testas e sua porcetagem de efetividade
        * Relatório de conclusão do código da rede neural e como foi desenvolvido
        * Teste de unidades
        * Teste de compatibilidade
        * Relatório de bugs e correções

3. Eu como usuario final gostaria que toda vez que retornar ao jogo, minha estratégia de jogo fosse a mesma

        Criterios de aceitação:
        * O banco de dados deve conter informações para identificar cada aluno individualmente
        * Os dados de desempenho do aluno devem ser persistidos no banco de dados 
        * O desempenho em jogo deve estar atrelado a conta do jogo do aluno
        DOD:
        *Codigo em SQL do banco de dados desenvolvido testado e aprovado
        *Testes de unidade
        
        

### Modelo entidade Relacionamento

<div align="center">
  <img src="https://github.com/ruan177/orm-IA/blob/main/ClassModel.png">
</div>

### Modelo de classe

<div align="center">
  <img src="https://github.com/ruan177/orm-IA/blob/main/ERDDiagram1.png">
</div>

