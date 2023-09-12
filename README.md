# PII redactor: remove personally identifiable information from text

This app is built using [FastAPI](https://fastapi.tiangolo.com/) and [spaCy](https://github.com/explosion/spacy-llm). It uses named entity recognition to identify various types of PII and then replaces them with `[REDACTED]`. LLMs handle the NER task – you can choose whether you want to use OpenAI or Anthropic.

# Usage
💾 Install requirements
```
pip install -r requirements.txt
```
🦄 Run the app
```
uvicorn main:app --reload
```
🧑‍💻 Call the `/redact` endpoint
```
{
    "text": "Give me a call on 123 356 7890",
    "openai_api_key": "XXXXX"
}
```
or
```
{
    "text": "Give me a call on 123 356 7890",
    "anthropic_api_key": "YYYYY"
}
```
🙌 Get a response
```
"Give me a call on [REDACTED]"
```
