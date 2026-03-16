# API para análise de sentimento para livros

## API REST para análise de sentimentos de textos para avaliação de livros

  ----------------------
  Estrutura do Projeto
  ----------------------

sentiment_api/

│ ├── app/ │ ├── main.py │ ├── routes.py │ ├── schemas.py │ ├──
sentiment_model.py │ └── logger.py │ ├── requirements.txt └── README.md

  ---------------------
## 1. Clonar o projeto

```bash
  git clone cd sentiment_api
```

## 2. Criar ambiente virtual (venv)


  Windows:
```bash
python -m venv venv
 ```
Ativar:

```bash
venv/Scripts/activate
```

## 3. Instalar dependências


```bash
pip install -r requirements.txt
```

## 4. Executar a API


Rodar o servidor com:
```bash
uvicorn app.main:app --reload
```
O servidor iniciará em:
```bash
http://127.0.0.1:8000
```

## 5. Documentação automática


O FastAPI gera automaticamente uma interface para testar a API.

Acesse:

http://127.0.0.1:8000/docs

Essa interface permite testar GET e POST diretamente no navegador.


## 6. Endpoint GET

Verifica se a API está funcionando.
```bash
GET /

Resposta:

{ “status”: “API funcionando” }
```

## 7. Endpoint POST

Endpoint responsável por realizar a análise de sentimento do texto
enviado.

```bash
POST /sentiment

Exemplo de requisição:

{ “text”: “Esse produto é ótimo” }

Resposta:

{ “text”: “Esse produto é ótimo”, “sentiment”: “positivo” }
```
  -----------------------------------
  Exemplo no Swagger (FastAPI Docs)
  -----------------------------------
```bash
Na interface /docs clique em:

POST /sentiment

Depois clique em “Try it out” e insira o texto no form:

{ “text”: “Esse produto é maravilhoso” }

```

## Logs da API


As requisições e respostas da API são registradas em logs.

Exemplo de log:
```bash
2026-03-14 10:32:11 | INFO | Texto recebido: Esse produto é ótimo |
Sentimento: positivo
```
  ------------------------
  Tecnologias utilizadas
  ------------------------

FastAPI Uvicorn Pydantic Loguru
