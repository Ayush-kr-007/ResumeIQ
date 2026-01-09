from llm_client import call_llm

def explain_result(result: dict) -> str:
    prompt = f"""
Explain the ATS evaluation below to a student.

Evaluation data:
{result}

Rules:
- Do NOT change scores
- Do NOT suggest new skills
- Only explain what the system already decided
- Be concise and supportive
"""

    return call_llm(prompt)
