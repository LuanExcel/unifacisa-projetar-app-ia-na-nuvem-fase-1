# API de Análise de Sentimentos

Esta é uma API RESTful construída com FastAPI para realizar análise de sentimentos em textos fornecidos. Ela permite submeter textos para análise, armazenar os resultados em um banco de dados TinyDB e gerenciar esses registros.

## Funcionalidades

A API oferece os seguintes endpoints:

| Método HTTP | Endpoint           | Descrição                                                                 |
|-------------|--------------------|---------------------------------------------------------------------------|
| `GET`       | `/`                | Verifica o status da API.                                                 |
| `POST`      | `/sentiment`       | Analisa o sentimento de um texto e o armazena no banco de dados.         |
| `GET`       | `/sentiments`      | Lista todos os registros de análise de sentimento.                       |
| `GET`       | `/sentiments/{id}` | Busca um registro de análise de sentimento específico pelo seu ID.       |
| `PUT`       | `/sentiments/{id}` | Atualiza o texto e o sentimento de um registro existente pelo seu ID.    |
| `DELETE`    | `/sentiments/{id}` | Remove um registro de análise de sentimento pelo seu ID.                 |

## Tecnologias Utilizadas

*   **FastAPI**: Framework web para construção de APIs com Python.
*   **TinyDB**: Banco de dados NoSQL leve e otimizado para pequenos projetos.
*   **Uvicorn**: Servidor ASGI para rodar aplicações FastAPI.
*   **Python 3.12.1**

## Configuração do Ambiente

Para rodar esta aplicação, você precisará ter Python 3.12.1 e `pip` instalados em seu sistema.

### 1. Clonar o Repositório

O código-fonte deste projeto está disponível no GitHub, na branch `fase2` do repositório `unifacisa-projetar-app-ia-na-nuvem-fase-1`.

```bash
git clone -b fase2 https://github.com/LuanExcel/unifacisa-projetar-app-ia-na-nuvem-fase-1.git
cd unifacisa-projetar-app-ia-na-nuvem-fase-1
```

### 2. Instalar Dependências

É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

```bash
python -m venv venv
venv\Scripts\activate`
pip install -r requirements.txt
```

## Como Rodar a Aplicação

Você pode rodar a aplicação de duas formas principais: localmente com Uvicorn ou usando a imagem Docker.

### Opção 1: Rodar Localmente com Uvicorn

Após instalar as dependências, você pode iniciar a API usando Uvicorn:

```bash
uvicorn main:router --reload --port 8000
```

A API estará disponível em `http://localhost:8080`.

### Opção 2: Rodar com Docker

Você pode puxar a imagem do Docker Hub e rodar a aplicação em um contêiner:

```bash
docker run -p 8080:8080 luanexcel/api-sentimento:v1
```

Este comando irá baixar a imagem `luanexcel/api-sentimento:v1` do Docker Hub e executá-la, mapeando a porta `8080` do contêiner para a porta `8080` da sua máquina local. A API estará acessível em `http://localhost:8080`.

## Acesso à API Publicamente (Deploy no Render)

A API também está disponível publicamente através do deploy no Render. Você pode acessar a documentação interativa (Swagger UI) e testar os endpoints diretamente:

[Documentação da API no Render](https://unifacisa-projetar-app-ia-na-nuvem-fase.onrender.com/docs)

## Automação e CI/CD

Este projeto utiliza **GitHub Actions** para automação de CI/CD, garantindo que o código seja testado e implantado automaticamente a cada nova alteração. O workflow é definido no arquivo `.github/workflows/workflow.yaml`.

## Uso da API

Você pode interagir com a API usando ferramentas como `curl` ou através da documentação interativa do Swagger UI (localmente em `http://localhost:8080/docs` ou no deploy do Render).

### 1. Verificar Status da API

```bash
curl http://localhost:8080/
```

**Resposta esperada:**
```json
{
  "status": "API funcionando"
}
```

### 2. Analisar Sentimento de um Texto (`POST /sentiment`)

```bash
curl -X POST http://localhost:8080/sentiment \
     -H "Content-Type: application/json" \
     -d '{"text": "Eu amo a nova funcionalidade!"}'
```

**Resposta esperada:**
```json
{
  "id": 1, 
  "text": "Eu amo a nova funcionalidade!",
  "sentiment": "positivo"
}
```

### 3. Listar Todos os Sentimentos (`GET /sentiments`)

```bash
curl http://localhost:8080/sentiments
```

**Resposta esperada:**
```json
[
  {
    "id": 1,
    "text": "Eu amo a nova funcionalidade!",
    "sentiment": "positivo"
  },
  {
    "id": 2,
    "text": "O serviço foi terrível.",
    "sentiment": "negativo"
  }
]
```

### 4. Buscar Sentimento por ID (`GET /sentiments/{id}`)

Substitua `{id}` pelo ID do registro que você deseja buscar.

```bash
curl http://localhost:8080/sentiments/1
```

**Resposta esperada:**
```json
{
  "id": 1,
  "text": "Eu amo a nova funcionalidade!",
  "sentiment": "positivo"
}
```

### 5. Atualizar Sentimento por ID (`PUT /sentiments/{id}`)

Substitua `{id}` pelo ID do registro que você deseja atualizar.

```bash
curl -X PUT http://localhost:8080/sentiments/1 \
     -H "Content-Type: application/json" \
     -d '{"text": "Eu realmente gostei da nova funcionalidade!"}'
```

**Resposta esperada:**
```json
{
  "id": 1,
  "text": "Eu realmente gostei da nova funcionalidade!",
  "sentiment": "positivo"
}
```

### 6. Deletar Sentimento por ID (`DELETE /sentiments/{id}`)

Substitua `{id}` pelo ID do registro que você deseja deletar.

```bash
curl -X DELETE http://localhost:8080/sentiments/1
```

**Resposta esperada:**
```json
{
  "message": "Registro deletado com sucesso"
}
```
