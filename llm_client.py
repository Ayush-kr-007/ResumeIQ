from transformers import pipeline

# Lightweight + more stable than gpt2
_generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

def call_llm(prompt: str) -> str:
    result = _generator(
        prompt,
        max_new_tokens=120,
        do_sample=False,
        truncation=True
    )

    # Remove prompt echo (GPT-2 problem)
    text = result[0]["generated_text"]
    return text.replace(prompt, "").strip()
