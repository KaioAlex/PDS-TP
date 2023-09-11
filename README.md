# Trabalho Prático - SplitWallet

* **Membros e papéis**:

    Caio Alexandre Campos Maciel (BackEnd Developer)
  
    Othavio Rudda da Cunha Araújo (FullStack Developer, PO)
  
    João Pedro Braga Ennes (FrontEnd Developer)

    Pedro Luis Costa Mucci (FullStack Developer)
  
*   **Escopo**:

    Este trabalho tem como objetivo implementar um sistema que gerencie as despesas de forma inteligente. É uma ferramenta prática para ajudar grupos de pessoas a dividir despesas de forma justa e transparente, evitando conflitos e simplificando o gerenciamento financeiro em situações de compartilhamento de despesas. É uma solução interessante para manter o controle das finanças em grupo e garantir que todos estejam quites. Portanto, torna mais fácil o acompanhamento e o equilíbrio de contas em situações como viagens em grupo, compartilhamento de despesas domésticas, jantares entre amigos etc. Sendo útil quando amigos ou colegas compartilham despesas comuns e desejam evitar conflitos sobre quem deve a quem.


    *  **Principais Features**:
 
          - **Registro de despesas individuais**: O usuário pode registrar despesas comuns, como contas de restaurante, aluguel, contas de serviços públicos, compras de supermercado, viagens, entre outras. Ao registrar uma despesa, o usuário especifica o valor, a descrição, a data e quem pagou por ela.

          - **Criação de grupos para cadastros de despesas compartilhadas**: Os usuários podem criar grupos para gerenciar despesas compartilhadas com amigos, familiares ou colegas de trabalho.

          - **Divisão de despesas entre participantes de grupos**: O aplicativo facilita a divisão justa das despesas entre os membros do grupo.
            
          - **Relatórios e histórico**: O usuários pode acessar relatórios detalhados e históricos de despesas, o que ajuda a manter o controle de todas as transações ao longo do tempo.
            
          - **Conversão de moeda**: O aplicativo também oferece a opção de converter despesas em diferentes moedas, o que pode ser útil para usuários que viajam internacionalmente.

          - **Saldo de contas**: O SplitWallet mantém um registro atualizado do saldo de cada membro em relação ao grupo.

* **Tecnologias**:

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
11. Como usuário, eu gostaria de revisar os dados de transação.
12. Como usuário, eu gostaria de consultar o meu extrato de transações realizadas.
13. Como usuário, eu gostaria de gerar um arquivo CSV com minhas transações desejadas.
14. Como usuário, eu gostaria de consultar perguntas comuns na tela de ajuda.
15. Como usuário, eu gostaria de realizar a conversão da moeda referente a quantia disponível na plataforma (e.g. Real para Dólar).
16. Como usuário, eu gostaria de ganhar pontos para cada transação realizada.

## Backlog da Sprint

**História #1**: Como usuário, eu gostaria de fazer cadastro no meu perfil (Criar e editar conta, tela de login e perfil).
- **Tarefas e responsáveis**:
    - Instalar banco de dados [Caio]
    - Instalar Python Flask [Caio]
    - Criar Tabela usuários [Othávio]
    - CRUD usuário [Othávio]
    - Criar ambiente Vue.js [Pedro]
    - Criar tela de Login [Pedro]
    - Criar tela Perfil [João]

**História #2**: Como usuário, eu gostaria de adicionar e deletar cartões da minha carteira (Carteira, cartões e valores).
- **Tarefas e responsáveis**:
    - Criar tabelas de carteira e cartões [Caio]
    - CRUD tabelas de carteira e cartões [Othavio]
    - Tela de carteira [João, Pedro]

**História #3**: Como usuário, eu gostaria de poder adicionar e deletar amigos da minha lista de amizade (Lista de amigos e favoritos)
- **Tarefas e responsáveis**:
    - CRUD tabela amigos [Caio]
    - Criar tabela de amigos no BD [Othávio]
    - Criar tela de amigos [Pedro]
    - Listar amigos favoritos primeiro com uma estrlinha ao lado [João]
 
**História #4**: Como usuário, eu gostaria de enviar e receber dinheiro dos meus amigos.
- **Tarefas e responsáveis**:
    - Update tabela de cartões [Caio]
    - Regras de negócio BACK [Othávio]
    - Telas de enviar e receber valores [João, Pedro]
 
**História #5**: Como usuário, eu gostaria de pagar uma conta em conjunto com meus amigos.
- **Tarefas e responsáveis**:
    - Gerenciar valores na carteira [Caio]
    - Tela de pagamento  [João, Pedro]
    - Regra de negócio, Verificar valores disponível [Othávio]
 
**História #6**: Como usuário, eu gostaria de consultar o meu extrato de transações realizadas (Extrato de operações).
- **Tarefas e responsáveis**:
    - Gerar CSV [Othávio]
    - CRUD tabela de histórico [Caio]
    - Tela de Histórico [João, Pedro]
 
**História #7**: Como usuário, eu gostaria de consultar perguntas comuns na tela de ajuda (Tela de ajuda).
- **Tarefas e responsáveis**:
    - Tabela de Perguntas(BACK) [Othávio]
    - Ler tabela de perguntas [Caio]
    - Tela de Perguntas [João,Pedro]
      
**História #8**: Como usuário, eu gostaria de ganhar pontos para cada transação realizada (Sistema de pontos).
- **Tarefas e responsáveis**:
    - Atualizar tabela de usuário com pontos [Othávio]
    - Realizar calculo de pontos pela transação [Caio]
    - Mostrar pontos no Perfil [Pedro, João]
 
