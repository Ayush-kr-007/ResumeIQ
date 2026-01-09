import json
import re
from llm_client import call_llm

def suggest_additional_skills(resume_text: str) -> set[str]:
    resume_text = resume_text[:3000]

    prompt = f"""
You are an assistant that suggests possible skills.

Based on the resume text, list up to 10 skills that
might be implied but not explicitly listed.

Return ONLY JSON:
{{ "skills": [] }}

Resume:
{resume_text}
"""

    output = call_llm(prompt)

    match = re.search(r"\{.*\}", output, re.DOTALL)
    if not match:
        return set()

    try:
        data = json.loads(match.group())
        return set(s.lower() for s in data.get("skills", []))
    except:
        return set()
