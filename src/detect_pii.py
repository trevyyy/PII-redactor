from spacy_llm.util import assemble
from timeit import default_timer
from wasabi import msg
from functools import lru_cache
import os


@lru_cache
def create_openai_pipeline():
    """Load and cache spaCy pipeline using OpenAI gpt-3.5-turbo model"""

    t0 = default_timer()
    pipeline = assemble(f'src/ner_openai.cfg', overrides={"paths.examples": "src/examples.json"})
    msg.good(f'Loaded GPT-3.5 pipeline in {round(default_timer() - t0, 2)}s')
    return pipeline


@lru_cache
def create_anthropic_pipeline():
    """Load and cache spaCy pipeline using Anthropic claude-2 model"""

    t0 = default_timer()
    pipeline = assemble(f'src/ner_anthropic.cfg', overrides={"paths.examples": "src/examples.json"})
    msg.good(f'Loaded Claude-2 pipeline in {round(default_timer() - t0, 2)}s')
    return pipeline


def redact_pii(text: str):
    """Identify and redact PII in string"""

    if os.getenv('OPENAI_API_KEY'):  # if both keys are provided, defaults to OpenAI
        nlp = create_openai_pipeline()
    elif os.getenv('ANTHROPIC_API_KEY'):
        nlp = create_anthropic_pipeline()
    t0 = default_timer()
    doc = nlp(text)
    msg.info(f'Prediction time: {round(default_timer() - t0, 2)}')
    for ent in doc.ents:
        text = text.replace(ent.text, '[REDACTED]')
    return text
