# Trabalho Prático - SplitWallet

* Membros e papéis:

    Caio Alexandre Campos Maciel (BackEnd Developer)
  
    Othavio Rudda da Cunha Araújo (FullStack Developer, PO)
  
    João Pedro Braga Ennes (FrontEnd Developer)

    Pedro Luis Costa Mucci (FullStack Developer)
  
*   Escopo:

    Este trabalho tem como objetivo implementar um sistema que gerencie as despesas de forma inteligente.

    *  Pricipais Features:
 
          - Cadastro de despesas individuais

          - Criação de grupos para cadastros de despesas compartilhadas

          - Divisão de despesas antre participantes de grupos

          - Gerenciamento de dívidas entre participantes dos grupos

          - Controle de fluxo de pagamento entre participantes de um grupo

* Tecnologias:

    Front-End: JavaScript com framework Vue JS

    Backend: Python com framework Flask

    BD: MySQL

## Backlog do Produto

1. Como usuário, eu gostaria de fazer cadastro no meu perfil.
2. Como usuário, eu gostaria de editar os dados do meu perfil.
3. Como usuário, eu gostaria de adicionar e deletar cartões da minha carteira.
4. Como usuário, eu gostaria de procurar lista de cartões franquiados.
5. Como usuário, eu gostaria de solicitar o bloqueio (inativação) de um cartão cadastrado na plataforma.
6. Como usuário, eu gostaria de pesquisar outros usuários da plataforma pelo username.
7. Como usuário, eu gostaria de poder adicionar e deletar amigos da minha lista de amizade.
8. Como usuário, eu gostaria de favoritar amigos da plataforma.
9. Como usuário, eu gostaria de enviar e receber dinheiro dos meus amigos.
10. Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
11. Como usuário, eu gostaria de consultar o meu extrato de transações realizadas.
12. Como usuário, eu gostaria de gerar um arquivo CSV com minhas transações desejadas.
13. Como usuário, eu gostaria de consultar perguntas comuns na tela de ajuda.
14. Como usuário, eu gostaria de realizar a conversão da moeda referente a quantia disponível na plataforma (e.g. Real para Dólar).
15. Como usuário, eu gostaria de ganhar pontos para cada transação realizada.

## Backlog da Sprint

**História #1**: Criar e editar conta Tela de Login e Perfil. (BP 1 e 2)
- **Tarefas e responsáveis**:
    - Instalar banco de dados [Caio]
    - Instalar Python Flask [Caio]
    - Criar Tabela usuários [Othávio]
    - CRUD usuário [Othávio]
    - Criar ambiente Vue.js [Pedro]
    - Criar tela de Login [Pedro]
    - Criar tela Perfil [João]

**História #2**: Carteira, cartões e valores. BP (3 a 5, 14)
- **Tarefas e responsáveis**:
    - Criar tabelas de carteira e cartões [Caio]
    - CRUD tabelas de carteira e cartões [Othavio]
    - Tela de carteira [João, Pedro]

**História #3**: Lita de amigos  e favoritos (BP 6 a 8)
- **Tarefas e responsáveis**:
    - CRUD tabela amigos [Caio]
    - Criar tabela de amigos no BD [Othávio]
    - Criar tela de amigos [Pedro]
    - Listar amigos favoritos primeiro com uma estrlinha ao lado [João]
 
**História #4**: Enviar e receber dinheiro. (BP 9)
- **Tarefas e responsáveis**:
    - Update tabela de cartões [Caio]
    - Regras de negócio BACK [Othávio]
    - Telas de enviar e receber valores [João, Pedro]
 
**História #5**: Pagar conta em conjunto. (BP 10)
- **Tarefas e responsáveis**:
    - Gerenciar valores na carteira [Caio]
    - Tela de pagamento  [João, Pedro]
    - Regra de negócio, Verificar valores disponível [Othávio]
 
**História #6**: Extrato de operações. (BP 11 e 12)
- **Tarefas e responsáveis**:
    - Gerar CSV [Othávio]
    - CRUD tabela de histórico [Caio]
    - Tela de Histórico [João, Pedro]
 
**História #7**: Tela de ajuda. (BP 13)
- **Tarefas e responsáveis**:
    - Tabela de Perguntas(BACK) [Othávio]
    - Ler tabela de perguntas [Caio]
    - Tela de Perguntas [João,Pedro]
      
**História #8**: Sistema de pontos. (BP 15)
- **Tarefas e responsáveis**:
    - Atualizar tabela de usuário com pontos [Othávio]
    - Realizar calculo de pontos pela transação [Caio]
    - Mostrar pontos no Perfil [Pedro, João]
 
