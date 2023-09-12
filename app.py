from fastapi import FastAPI, HTTPException
from src.detect_pii import redact_pii
from pydantic import BaseModel
import os


class Payload(BaseModel):
    text: str


app = FastAPI()


@app.get("/redact")
def redact(payload: Payload):
    if os.getenv('OPENAI_API_KEY') is None and os.getenv('ANTHROPIC_API_KEY') is None:
        raise HTTPException(status_code=400, detail='Please provide an API key for either OpenAI or Anthropic.')
    payload_dict = payload.model_dump()
    return redact_pii(payload_dict['text'])


@app.get("/healthcheck")
async def healthcheck():
    return "Healthy."
