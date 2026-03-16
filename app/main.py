from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Análise de sentimento para livros",
    description="API para análise de sentimentos de lievros de literatura",
    version="1.0"
)

app.include_router(router)