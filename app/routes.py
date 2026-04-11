from fastapi import APIRouter, HTTPException
from app.schemas import TextRequest, SentimentResponse
from app.sentiment_model import analise_sentimento
from app.config_logs import logger
from tinydb import TinyDB, Query 
from typing import List

# Banco de Dados
file = r'./db.json'

router = APIRouter()


@router.get("/")
def home():
    logger.info("home executado")
    return {"status": "API funcionando"}

# ================================================================


@router.post("/sentiment", response_model=SentimentResponse)
def predicao(request: TextRequest):

    text_content = request.text 

    sentiment = analise_sentimento(text_content)

    # Gerencia o banco de dados
    try:
        db = TinyDB(file)
    except (NameError, ValueError): 

        db = TinyDB('db.json') 

    # Insere e recupera o ID
    temp_id = db.insert({
            "texto": text_content,
            "sentimento": sentiment
        })

    # Atualiza o documento com o próprio ID
    db.update({"id": temp_id}, doc_ids=[temp_id])

    # Retorna seguindo o seu SentimentResponse
    return {
        "id": temp_id,
        "text": text_content,
        "sentiment": sentiment
    }
# ================================================================

@router.get("/sentiments", response_model=List[SentimentResponse])
def listar_sentimentos():
    db = TinyDB(file)
    dados = db.all()

    return [
        SentimentResponse(
            id=item["id"],
            text=item["texto"],
            sentiment=item["sentimento"]
        )
        for item in dados
    ]


@router.get("/sentiments/{id}", response_model=SentimentResponse)
def buscar_por_id(id: int): 

    db = TinyDB('db.json') 
    tabela = db.table('_default')
    
    Busca = Query()

    resultado = tabela.get(Busca.id == id)

    if not resultado:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    
    return SentimentResponse(
        id=resultado['id'],
        text=resultado['texto'],
        sentiment=resultado['sentimento']
    )

@router.put("/sentiments/{id}", response_model=SentimentResponse)
def atualizar(id: int, request: TextRequest):
    db = TinyDB('db.json') 
    tabela = db.table('_default')
    
    Busca = Query()

    resultado = tabela.get(Busca.id == id)

    if not resultado:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    
    text = request.text

    novo_sentimento = analise_sentimento(text)

    db.update({
        "id": id,
        "texto": text,
        "sentimento": novo_sentimento
    }, doc_ids=[id])

    return SentimentResponse(
        id=id,
        text=text,
        sentiment=novo_sentimento
    )

@router.delete("/sentiments/{id}")
def deletar(id: int):
    db = TinyDB('db.json') 
    tabela = db.table('_default')
    
    Busca = Query()

    resultado = tabela.get(Busca.id == id)

    if not resultado:
        raise HTTPException(status_code=404, detail="Registro não encontrado")

    db.remove(Busca.id == id)

    return {"message": "Registro deletado com sucesso"}