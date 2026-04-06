from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    id: int
    text: str
    sentiment: str