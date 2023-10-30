## Documentação da Arquitetura
### Estrutura de pastas do projeto:
```
- src
    - db (Exterior - Mysql)
        - database
    - domain (Classes de domínio, regras de negócio)
        - actions
            - database
            - user
            - card
            - friendship
            - transaction
        - interfaces
            - database
            - user
            - card
            - friendship
            - transaction
        - usecase
            - user
            - card
    - web (Exterior - API Rest)
        - user
        - card
        - friendship
        - transaction
```
## Arquitetura Hexagonal

### Por que o sistema está adotando essa arquitetura?
A arquitetura hexagonal, também conhecida como arquitetura de portas e adaptadores (Ports and Adapters), é um padrão de arquitetura de software que foi projetado para criar sistemas mais flexíveis, testáveis e independentes de detalhes de implementação. Ela está sendo usada neste projeto pois buscamos alcançar alta modularidade e separação de preocupações em um sistema.

### Quais são as portas e adaptadores? Qual o objetivo deles?
Temos portas, implementadas como interfaces, de: user, transaction, friendship, card e database. Interfaces são as interfaces de comunicação entre as camadas, aqui deve conter tanto as classes com a definição da estrutura dos dados quanto os metodos abstratos que são utilizados para realizar a comunicação entre as camadas.

No nosso projeto temos um adaptador de Mysql, por exemplo, responsável por configurar toda a lógica com esse banco de dados. Quem utiliza esta parte são os UseCase do domain, que irão chamar a partir de uma interface.

### Pode-se dar pequenos exemplos de código e diagramas

**Porta: userInterface.py**
```
...
class UserInterface(ABC):
    @abstractmethod
    def getUser(self, id) -> User:   
        pass

    @abstractmethod
    def getUsersList(self) -> List[User]:   
        pass

    @abstractmethod
    def postUser(self, user: User) -> List[User]:
        pass
...
```

**Adaptador: mysql.py**
```
...
class MysqlAdapter(DatabaseInterface):
    def get_user(self, id) -> User: 
        cursor = get_conn().cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE id = {id};"
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        if user == '':
            return None

        else:
            return user
    ...
```

**Injeção de Dependências: configuration.py**
```
def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(DatabaseInterface, MysqlAdapter)
        binder.bind(UserInterface, UserUseCase(DatabaseActions()))
        binder.bind(CardInterface, CardUseCase(DatabaseActions()))

    inject.configure(config)
```

## Principais tecnologias e bibliotecas utilizadas
- Utilizado a linguagem [python](https://www.python.org/) para desenvolver o projeto.
- Consutruido utilizando o [poetry](https://poetry.eustace.io/) para gerenciar as dependências.
- Utilizado o [Flask](https://flask.palletsprojects.com/) para servir a API.
- Utilizado o [Blueprint](https://flask.palletsprojects.com/en/1.1.x/blueprints/) para separar as rotas da API.


## Explicação da arquitetura hexagonal
- No print abaixo tem uma exemplicação de como seria a Arquitetura Hexagonal:<br>
    ![Hexagonal Architecture](https://user-images.githubusercontent.com/36082343/173716095-28cfabae-02aa-4272-ad8f-13ab729c3dbe.png)
- Toda a aplicação pode ser separada em 3 niveis:
    - Web (Lado esquerdo do print acima)
        - Este ponto seria a entrada seria o que o cliente iria chamar para comunicar com a api, esta parte além de receber a requisição por diferentes entradas que podemos ter faria também o pré-processamento, em resumo recebe e entende o que o cliente enviou, para assim montar a comunicação com o "back-end(Domain)" para processar.

    - Domain (Parte do meio do print acima)
        - Este ponto seria o processamento da requisição, esta parte recebe o que o lado esquerdo recebeu do cliente e processa de fato, comunicando com os meios externos(Banco de dados, serviços de email, etc.)

    - Adapters (Parte da direita do print acima)
        - Aqui seria feito a comunicação com aplicações externas do nosso código, ou seja, tudo o que precisa ser solicitado/enviado exterdo da API será responsabilidade desta parte realizar a implementação.
- Com estas separações descritas acima podemos ter uma aplicação muito mais flexivel e aberta para modificações e inclusões.

## Como executar o projeto
- Para poder iniciar é preciso ter instalado as dependências abaixo:
    - [Python](https://www.python.org/)
    - [Pip](https://pip.pypa.io/)
    - [Poetry](https://poetry.eustace.io/)
    - [Git](https://git-scm.com/)
- Após ter instalado as dependências pode ser clonado o repositório do projeto:
  ######
    git clone https://github.com/KaioAlex/PDS-TP.git
- Para executar o projeto é preciso estar dentro da pasta do projeto e rodar o comando abaixo para definir que queremos criar o ambiente virtual dentro da pasta do projeto:
  ######
    poetry config virtualenvs.in-project true
- Após isso pode ser executado a criação e ativação do ambiente virtual:
  ######
    poetry shell
- Após pode ser executado o comando abaixo para instalar as dependências do projeto(O poetry fará todo o trabalho para nós):
  ######
    poetry install
- Precisa ser definido também uma variavel global para que o Flask consiga encontrar quem inicia o projeto:
  ######
    export FLASK_APP=src/main.py; export FLASK_DEBUG=1
- Após isso pode ser executado o comando abaixo para executar o projeto:
  ######
    poe start
  #####
- Após isso se tudo deu certo, deve estar executando o projeto no endereço http://127.0.0.1:5000
