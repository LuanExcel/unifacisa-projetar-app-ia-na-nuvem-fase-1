from fastapi import APIRouter, Form
from app.schemas import SentimentResponse
from app.sentiment_model import analise_sentimento
from app.config_logs import logger

router = APIRouter()


@router.get("/")
def home():
    logger.info("home executado")
    return {"status": "API funcionando"}


@router.post("/sentiment", response_model=SentimentResponse)
def predicao(text: str = Form(...)):

    sentiment = analise_sentimento(text)

    logger.info(f"Texto recebido: {text} | Sentimento: {sentiment}")

    return SentimentResponse(
            text=text,
            sentiment=sentiment
        )