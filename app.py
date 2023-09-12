from fastapi import FastAPI, HTTPException
from src.detect_pii import redact_pii
from pydantic import BaseModel, model_validator
import os


class Payload(BaseModel):
    text: str
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    @model_validator(mode='after')
    def check_api_keys(self) -> 'Payload':
        if self.openai_api_key is None and self.anthropic_api_key is None:
            raise HTTPException(status_code=400,
                                detail="At least one API key is required: please provide either 'openai_api_key' or "
                                       "'anthropic_api_key'. To create API keys, go to "
                                       "https://platform.openai.com/account/api-keys for OpenAI or "
                                       "https://console.anthropic.com/account/keys for Anthropic.")
        return self


app = FastAPI()


@app.get("/redact")
def redact(payload: Payload):
    payload_dict = payload.model_dump()
    if key := payload_dict.get('openai_api_key'):  # if both keys are provided, default to OpenAI
        os.environ['OPENAI_API_KEY'] = key
        model = 'openai'
    elif key := payload_dict.get('anthropic_api_key'):
        os.environ['ANTHROPIC_API_KEY'] = key
        model = 'anthropic'
    return redact_pii(payload_dict['text'], model)


@app.get("/healthcheck")
async def healthcheck():
    return "Healthy."
