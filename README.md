# API FIPE CRUD

este simples programa em django consome a api da tabela fipe e faz um crud com os dados recebidos

## Índice

- [API FIPE CRUD](#api-fipe-crud)
  - [Índice](#índice)
  - [Sobre o Projeto](#sobre-o-projeto)
    - [Models](#models)
    - [Rotas disponiveis](#rotas-disponiveis)
  - [Começando](#começando)

## Sobre o Projeto

### Models
A model criada foi a Vehicle com os atributos:
price
brand
model
modelYear
fuel
codeFipe
vehicleType
fuelType

### Rotas disponiveis
listarei cada rota e uma breve descricao do seu comportamento



## Começando

py -m venv .venv

git clone https://github.com/jluca-s/fabrica-api-crud.git

pip install -r requirements.txt

dentro de ProjetoApiCrud\

.\.venv\Scripts\activate

dentro de ProjetoApiCrud\Crud

py .\manage.py runserver

