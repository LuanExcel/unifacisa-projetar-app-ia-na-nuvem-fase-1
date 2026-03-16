from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    text: str
    sentiment: str