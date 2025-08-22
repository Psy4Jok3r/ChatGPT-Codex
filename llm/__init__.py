import os
from typing import List

try:
    import openai
except Exception:  # pragma: no cover - optional dependency
    openai = None

MODEL = "openai/gpt-oss-20b:free"

class LLM:
    """Wrapper around OpenRouter LLM access.

    Requires the environment variable `OPENROUTER_API_KEY` to be set.
    """

    def __init__(self) -> None:
        self.client = openai if openai else None

    def chat(self, messages: List[dict]) -> str:
        if not self.client:
            return "(llm unavailable)"
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            return "(missing OPENROUTER_API_KEY)"
        self.client.api_key = api_key
        response = self.client.ChatCompletion.create(model=MODEL, messages=messages)
        return response["choices"][0]["message"]["content"]
