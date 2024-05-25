# Simple Bank - 5 (API RESTful)
![a324d210d9bade9fd920676deb9f37cc-ilustracao-plana-de-banco-de-edificio](https://github.com/vitoriarntrindade/simple-bank-1/assets/139915844/a7d2fce1-0148-4508-84aa-6242610d18e9)

 O objetivo do projeto **Simple Bank** é aplicar a linguagem de programação **Python**,  em uma situação *real*.
 A proposta desse projeto veio a partir de um *bootcamp* da plataforma de cursos **DIO**. 

 Esta é uma API Flask-RESTful com modelagem de dados utilizando SQLAlchemy. A API permite operações CRUD (Create, Read, Update, Delete).
 
 Principais Componentes

* Flask-RESTful: Extensão do Flask para criação de APIs RESTful em Python.
* SQLAlchemy: Biblioteca Python para interação com bancos de dados relacionais.
* Modelagem de Dados: Definição de modelos de dados como classes Python usando SQLAlchemy.
* Operações CRUD: Implementação das operações CRUD para manipulação de recursos.


  # Recursos da API 

# Client Resources :busts_in_silhouette: 


### Criar cliente (POST)


![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/a9852e38-99a9-41a9-b491-6d4ba7713763)

- **Endpoint**: `/clients/`
- **Descrição**: Permite criar um novo cliente.
- **Funcionamento**: Ao acessar o endpoint `/clients/` com o verbo POST, um novo cliente é criado a partir das informações fornecidas no corpo json.

### Cliente pelo ID (GET)
 ![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/1499ecec-d8e1-4b7b-874d-53a3f2cdb733)

- **Endpoint**: `/clients/<int:id>`
- **Descrição**: Permite acessar informações de um cliente específico com base no ID.
- **Funcionamento**: O endpoint `/clients/<int:id>` recebe um ID de cliente como parâmetro na URL. Ao acessar esse endpoint, o sistema retorna as informações do cliente correspondente ao ID fornecido.

### Listar Clientes (GET)
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/e58c8bb0-a1d0-4456-8fd2-e585dee0419d)


- **Endpoint**: `/clients/`
- **Descrição**: Permite acessar uma lista de todos os clientes.
- **Funcionamento**: Ao acessar o endpoint `/clients/`, o sistema retorna uma lista com informações de todos os clientes cadastrados.

  
#### Listar Clientes usando parâmetros para filtrar pela idade
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/f528249a-0495-4100-a785-3c9fd8087da3)




# Address Resources :house_with_garden: :round_pushpin:


## Criar Endereço (POST)
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/6a3ff5c5-075a-4d3d-bb8b-88beb3e8592a)

- **Endpoint**: `/address/`
- **Descrição**: Permite criar um novo endereço, associando ao cliente de ID espeficidado no corpo da requisição..
- **Funcionamento**: O endpoint `/address/` Recebe um ID do cliente no corpo json da requisição e cria um novo endereço fazendo essa associação.

## Endereço pelo ID
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/1ab7ba8c-9738-4ddf-9beb-129fe50439d1)

- **Endpoint**: `/address/<int:id>`
- **Descrição**: Permite acessar informações de um endereço específico com base no ID.
- **Funcionamento**: O endpoint `/address/<int:id>` recebe um ID de endereço como parâmetro na URL. Ao acessar esse endpoint, o sistema retorna as informações do endereço correspondente ao ID fornecido.

## Listar Endereços
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/045ee522-f669-41fd-9951-f0a57d51ff30)

- **Endpoint**: `/address/`
- **Descrição**: Permite acessar uma lista de todos os endereços.
- **Funcionamento**: Ao acessar o endpoint `/address/`, o sistema retorna uma lista com informações de todos os endereços cadastrados.


# Accounts Resources :credit_card: :bank:


## Conta pelo ID
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/96b19db8-1613-403c-8123-44c0000370e1)

- **Endpoint**: `/accounts/<int:id>`
- **Descrição**: Permite acessar informações de uma conta específica com base no ID.
- **Funcionamento**: O endpoint `/accounts/<int:id>` recebe um ID de conta como parâmetro na URL. Ao acessar esse endpoint, o sistema retorna as informações da conta correspondente ao ID fornecido.

## Listar Contas (Com parêmetro opcional de filtragem na url)
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/f2bfe280-1966-4e05-839b-dee47dfedd81)

- **Endpoint**: `/accounts/`
- **Descrição**: Permite acessar uma lista de todas as contas ou fazer filtragem especifíca.
- **Funcionamento**: Ao acessar o endpoint `/accounts/`, o sistema retorna uma lista com informações de todas as contas cadastradas.
 Ao acessar o endpoint '/accounts/' e passar parâmetros na url: Pega todas as contas por regua de balanço passando os seguintes parametros: **operation = 'lt', 'gt' (less then, greater then) balance = (valor desejando para a regua)**


## Depósito em Conta
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/45414ec7-ae16-40db-af37-a99b07f7da6d)

- **Endpoint**: `/accounts/deposit`
- **Descrição**: Realiza um depósito em uma conta específica.
- **Funcionamento**: O endpoint `/accounts/deposit` recebe dados de depósito no corpo da requisição. Ao acessar esse endpoint e fornecer os dados necessários, o sistema realiza o depósito na conta especificada.

## Transação entre Contas
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/de375077-677d-41e7-9c35-9a19e3918b19)

- **Endpoint**: `/accounts/transaction`
- **Descrição**: Realiza uma transação entre duas contas.
- **Funcionamento**: O endpoint `/accounts/transaction` recebe os dados da transação no corpo da requisição. Ao acessar esse endpoint e fornecer os dados necessários, o sistema realiza a transação entre as contas especificadas.

## Saque em Conta
![image](https://github.com/vitoriarntrindade/simple-bank-5/assets/139915844/67d59697-3b90-49e3-8c79-a1cd3e6cd082)

- **Endpoint**: `/accounts/withdrawl`
- **Descrição**: Realiza um saque em uma conta específica.
- **Funcionamento**: O endpoint `/accounts/withdrawl` recebe dados de saque no corpo da requisição. Ao acessar esse endpoint e fornecer os dados necessários, o sistema realiza o saque na conta especificada.


## Próximas Features

O projeto está em constante evolução e há várias melhorias planejadas para o futuro. Algumas das features que desejo incluir são:

   * Autenticação de Usuário: Implementar um sistema de autenticação robusto para garantir que apenas usuários autorizados tenham acesso às funcionalidades do aplicativo.
   * Deixar a validação dos dados de entrada mais robusto. (*Atualmente tem sido feito através de schemas*)
