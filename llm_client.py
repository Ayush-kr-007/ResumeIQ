import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "phi3:mini"

def call_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0}
        }
    )
    response.raise_for_status()
    return response.json()["response"]
