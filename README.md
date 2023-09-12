# PII redactor: remove personally identifiable information from text

This app is built using [FastAPI](https://fastapi.tiangolo.com/) and [spaCy](https://github.com/explosion/spacy-llm). It uses named entity recognition to identify various types of PII and then replaces them with `[REDACTED]`. LLMs handle the NER task – you can choose whether you want to use OpenAI or Anthropic. To get your API key, go to [openai.com](https://platform.openai.com/account/api-keys) or [anthropic.com](https://console.anthropic.com/account/keys).

# Usage
💾 Install requirements
```
pip install -r requirements.txt
```
🔐 Set environment variables
```
export OPENAI_API_KEY="sk-..."
```
or
```
export ANTHROPIC_API_KEY="SK-..."
```
🦄 Run the app
```
uvicorn main:app --reload
```
🧑‍💻 Call the `/redact` endpoint
```
{
    "text": "Give me a call on 123 356 7890"
}
```
🙌 Get a response
```
"Give me a call on [REDACTED]"
```
