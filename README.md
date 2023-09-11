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
4. Como usuário, eu gostaria de personalizar meus cartões (e.g. cores).
5. Como usuário, eu gostaria de solicitar o bloqueio (inativação) de um cartão cadastrado na plataforma.
6. Como usuário, eu gostaria de poder adicionar e deletar amigos da minha lista de amizade.
7. Como usuário, eu gostaria de favoritar amigos da plataforma.
8. Como usuário, eu gostaria de enviar e receber dinheiro dos meus amigos.
9. Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
10. Como usuário, eu gostaria de consultar perguntas comuns na tela de ajuda.
11. Como usuário, eu gostaria de mandar mensagem na tela de ajuda.
12. Como usuário, eu gostaria de consultar o meu extrato de transações realizadas.
13. Como usuário, eu gostaria de gerar um arquivo CSV com minhas transações desejadas.
14. Como usuário, eu gostaria de realizar a conversão da moeda referente a quantia disponível na plataforma (e.g. Real para Dólar).
15. Como usuário, eu gostaria de ganhar pontos para cada transação realizada.


## Backlog da Sprint

**História #1**: Como usuário, eu gostaria de criar uma conta
- **Tarefas e responsáveis**:
    - Instalar banco de dados [Caio]
    - Instalar Python Flask [Caio]
    - Criar Tabela usuários [Othávio]
    - Criar Tela Kanban no github [Othávio]
    - Criar ambiente Vue.js [Pedro]
    - Criar tela de Login [Pedro]
    - Criar tela inicial [João]

**História #2**: Como usuário, eu gostaria de editar os dados do meu perfil.
- **Tarefas e responsáveis**:
    - API - Ler tabela de usuários [Caio]
    - API - UPDATE tabela de usuários [Caio]
    - Tela de perfil [João]
    - Modal de edição de usuário [Pedro]
    - Atualizar BD com informações de usuário [Othávio]

**História #3**: Como usuário, eu gostaria de adicionar e deletar cartões da minha carteira.
- **Tarefas e responsáveis**:
    - CRUD tabela de cartões e carteira [Caio]
    - Criar tabela de carteira e carteira no BD [Othávio]
    - Criar tela de carteiras [Pedro]
    - Criar Botões para adicionar e remover cartões [João]
 
**História #4**: Como usuário, eu gostaria de personalizar meus cartões.
- **Tarefas e responsáveis**:
    - Update tabela de cartões [Caio]
    - Modal para listar cores (FRONT) [Othávio]
    - Criar layout dos cartões [Pedro]
 
**História #5**: Como usuário,  eu gostaria de solicitar o bloqueio (inativação) de um cartão cadastrado na plataforma.
- **Tarefas e responsáveis**:
    - Adicionar campo isValid na tabela de cartões relacionado ao usuário [Caio]
    - Botão para fazer o pedido de bloqueio do cartão [João]
    - Modal genérico (Tem certeza da sua ação?) [Pedro]
 
**História #6**: Como usuário,  eu gostaria de poder adicionar e deletar amigos da minha lista de amizade.
- **Tarefas e responsáveis**:
    - Criar tabela de amizade [Othávio]
    - CRUD tabela de amizade [Caio]
    - Tela de amizade [João]
    - Botões para adicionar e remover amigos [Pedro]
 
**História #7**: Como usuário, eu gostaria de favoritar amigos da plataforma.
- **Tarefas e responsáveis**:
    - Adicionar campo de favorito na tabela de amizade (BACK) [Othávio]
    - Listar primeiro amigos favoritos [João]
    - Adicionar estrela colorida para amigo favorito [Pedro]
    - 
**História #8**: Como usuário, eu gostaria de enviar e receber dinheiro dos meus amigos.
- **Tarefas e responsáveis**:
    - Atualizar carteira do usuário (BACK) [Othávio]
    - Criar tela de transferência [Pedro]
    - Listar amigos [João]
 
**História #9**: Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
- **Tarefas e responsáveis**:

**História #9**: Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
- **Tarefas e responsáveis**:

**História #9**: Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
- **Tarefas e responsáveis**:

**História #9**: Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
- **Tarefas e responsáveis**:

**História #9**: Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
- **Tarefas e responsáveis**:
    - 
