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
Este projeto consome a API: parallelum.com.br/fipe/api/v1/carros/
que entrega varias respostas Json dependendo do endpoint.

exemplo:
https://parallelum.com.br/fipe/api/v1/carros/marcas
retorna um dicionario Json com os campos ['nome' e 'codigo'] para cada marca

https://parallelum.com.br/fipe/api/v1/carros/marcas/{idMarca}/modelos
retorna um dicionario Json com os campos ['nome' e 'codigo'] para cada modelo de uma determinada marca

parallelum.com.br/fipe/api/v1/carros/marcas/{idMarca}/modelos/{idModelo}/anos
retorna um dicionario Json com os campos ['nome' e 'codigo'] para cada ano de um determinado modelo

https://parallelum.com.br/fipe/api/v1/carros/marcas/{idMarca}/modelos/{idModelo}/anos/{idAno}
retorna o Json do veiculo selecionado

A partir desse Json do veiculo que sao feiras as operaçoes de Create Update Read Delete utilizando os templates do Django


### Models
A model criada foi a Vehicle com os atributos:
codeFipe (PK)
price
brand
model
modelYear
fuel
vehicleType
fuelType

### Rotas disponiveis
listarei cada rota e uma breve descricao do seu comportamento

http://127.0.0.1:8000/fipe/
é a rota da ixdex da aplicaçao

http://127.0.0.1:8000/fipe/marcas/
retorna todas as marcas da API

http://127.0.0.1:8000/fipe/marcas/{idMarca}/modelos/
retorna todos os modelos de uma marca

http://127.0.0.1:8000/fipe/marcas/{idMarca}/modelos/{idModelo}/anos
retorna todos os anos desse modelo

http://127.0.0.1:8000/fipe/marcas/{idMarca}/modelos/{idModelo}/anos/{idAno}
retorna a tabela fipe do veiculo e da a opção de salvar no banco de dados

caso salve, o botao ira enviar um metodo POST para a rota:
http://127.0.0.1:8000/fipe/createOrUptadeVehicle/
isso salvara o veiculo no bd

http://127.0.0.1:8000/fipe/allVehicles/
Lista todos os veiculos salvos

http://127.0.0.1:8000/fipe/getVehicle/{codeFipe}
Lista um veiculo salvo pelo codeFipe que esta definido como id no models

http://127.0.0.1:8000/fipe/deleteVehicle/{codeFipe}
Deleta um veiculo pelo codeFipe

http://127.0.0.1:8000/fipe/updateVehicleForm/{codeFipe}
gera um formulario com os atributos de veiculo preenchidos para substituir e atualizar

clicando em atualizar o botão envia um metodo POST para:

http://127.0.0.1:8000/fipe/updateVehicle/{codeFipe}
que reculpera o Vehicle.object pelo codeFipe e recebe os campos do POST para fazer o update


## Começando

py -m venv .venv

git clone https://github.com/jluca-s/fabrica-api-crud.git

pip install -r requirements.txt

dentro de ProjetoApiCrud\

.\.venv\Scripts\activate

dentro de ProjetoApiCrud\Crud

py .\manage.py runserver