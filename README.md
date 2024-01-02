# O que é uma API?

APIs são mecanismos que permitem que dois componentes de software se comuniquem usando um conjunto de definições e protocolos. Por exemplo, o sistema de software do instituto meteorológico contém dados meteorológicos diários. A aplicação para a previsão do tempo em seu telefone “fala” com esse sistema por meio de APIs e mostra atualizações meteorológicas diárias no telefone.

ref.: [API - Wiki](https://pt.wikipedia.org/wiki/Interface_de_programa%C3%A7%C3%A3o_de_aplica%C3%A7%C3%B5es#:~:text=A%20API%20permitem%20utilizar%20caracter%C3%ADsticas,aceder%20a%20arquivos%2C%20codificar%20dados.)

![ ](https://github.com/Prog-LucasAlves/API_JupyterNotebook_Deploy/blob/master/image/API_01.png)

## Para que servem as APIs?

A API acelera o **desenvolvimento** de novos aplicativos. Você não precisa criar todas as soluções de software do zero, pois pode usar APIs prontas para funções padrão. As APIs também facilitam a integração de diferentes aplicativos e serviços, melhoram seu desempenho e os adaptam às necessidades do seu público-alvo.

## Como funcionam as APIs?

As funções básicas de uma API são: obter informação, enviá-la, alterá-la e excluí-la. Para fazer isso, o aplicativo do usuário envia uma solicitação para um aplicativo de terceiros, que gera uma resposta. Imagine que você compra um ingresso de cinema online ou pede um táxi por meio de um aplicativo. Durante a transação, o terminal acessa a API do banco emissor do cartão e envia uma solicitação de pagamento. Seu aplicativo, aquele que envia a solicitação, é chamado de **cliente** e aquele que retorna a resposta é conhecido como **servidor**.

## Os tipos de APIs

Existem APIs para aplicativos, sites e sistemas operacionais. Por exemplo, a maioria dos sistemas operacionais (Unix, Windows, MacOS, etc.) conta com APIs que permitem programar serviços para esses sistemas.

As APIs são classificadas por tipo de arquitetura:

- **SOAP** (Simple Object Access Protocol) significa “Protocolo Simples de Acesso a Objetos”. Utiliza XML para transferir dados entre sistemas e é comumente usado em aplicativos corporativos.
- **RPC** (Remote Procedure Call) ou “Chamada de Procedimento Remoto”. O cliente solicita uma ação necessária ao servidor e, como resposta, uma função é executada no aplicativo.
- **REST** (Representational State Transfer) é a ferramenta mais popular na atualidade. Esse tipo de interface opera o protocolo HTTP para troca de dados e é frequentemente usada em aplicações web.
- **WebSocket** ativa a comunicação bidirecional entre cliente e servidor, tornando o programa mais interativo. As informações são enviadas no formato JSON.

... Vamos utilizar **API REST** com o framework **FastAPI**.

Ref.: [FastAPI](https://fastapi.tiangolo.com/)

## Diferença Entre REST e RESTful

**REST** é um conjunto de princípios e restrições de arquitetura de softwares. Uma API **RESTful** é aquela que está em conformidade com os critérios estabelecidos pela Transferência de Estado Representacional (REST).

## Protocolo HTTP - API REST

O protocolo HTTP é a base usada por trás das APIs REST e as "requisita" utilizando diversos "tipos". Os mais comuns são:

- POST: (Create) Criar um recurso
- GET: (Read) Obter um recurso
- PUT: (Update) Atualizar um recurso
- DELETE: Remover um recurso

## *Para realizar esse projeto vou(vamos) utilizar o VSCode e o terminal(PowerShell)*

## Python

- Vou utilizar nesse projeto a versão o python **3.11.3** atraves do *pyenv*

```python
pyenv local 3.11.3
```

Ref.: [pyenv](https://github.com/pyenv/pyenv)

## Criando o ambiente virtual

```python
poetry init
```

Ref.: [poetry](https://python-poetry.org/)

## Ativando nosso ambiente virtual

```python
poetry shell
```

## Instalando o FastAPI

FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.8 ou superior, baseado nos type hints padrões do Python.

```python
poetry add fastapi
```

## Instalando o Uvicorn

Uvicorn é uma implementação de servidor web ASGI para Python.

```python
poetry add uvicorn
```

Ref.: [uvicorn](https://www.uvicorn.org/)

## Criando endpoint

Endpoints são os pontos de acesso de uma API. Eles são definidos por uma URL, um método e um conjunto de parâmetros.

```python
echo > main.py
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Olá": "Mundo"}
```

## Executando o servidor

Para executar o servidor, precisamos usar o Uvicorn e passar o nome do **arquivo(*main*)** e o nome da **variável(*app*)** que contém a instância do FastAPI.

```python
> uvicorn main:app --reload
```

## Testes Unitários

São testes que verificam se uma parte específica do código, costumeiramente a nível de função, está funcionando corretamente.

```python
poetry add pytest
```

Ref.: [pytest](https://docs.pytest.org/en/7.4.x/)

```python
echo > test_api.py
```

```python
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_response():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}
```

## Rodando os testes

```python
pytest -v test_api.py
```

## CI (Continuous Integration)

Integração contínua (CI) é uma prática de automatizar a integração de alterações de código de vários contribuidores em um único projeto de software. É uma prática recomendada primária de DevOps, permitindo que os desenvolvedores mesclem com frequência as alterações de código em um repositório central onde builds e testes são executados. Ferramentas automatizadas são usadas para afirmar a correção do novo código antes da integração.

:construction:

## Colocando nossa aplicação no Ar

Vamos usar o site

https://dashboard.render.com/login

[API NO AR](https://api-produtos-e247.onrender.com/docs)
