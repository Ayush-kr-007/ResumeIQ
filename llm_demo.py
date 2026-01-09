# import requests
# import json
# import re

# OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
# MODEL = "phi3:mini"


# def parse_resume(resume_text):
#     prompt = f"""
# You are an AI resume parser.

# Extract information from the resume text.
# Return ONLY valid JSON.
# No explanations. No markdown.

# Schema:
# {{
#   "skills": [],
#   "experience_level": "",
#   "domains": [],
#   "tools": [],
#   "education": ""
# }}

# Rules:
# - skills → technical + soft skills
# - experience_level → one of: fresher, junior, mid
# - domains → inferred from projects/experience
# - tools → software, libraries, platforms
# - education → highest degree only

# Resume:
# {resume_text}
# """

#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": MODEL,
#             "prompt": prompt,
#             "stream": False,
#             "options": {
#                 "temperature": 0
#             }
#         }
#     )

#     response.raise_for_status()
#     return response.json()["response"]


# def extract_json(llm_output):
#     match = re.search(r"\{.*\}", llm_output, re.DOTALL)
#     if not match:
#         raise ValueError("No JSON found in LLM output")

#     return json.loads(match.group())


# if __name__ == "__main__":
#     with open("core/resume.txt", encoding="utf-8") as f:
#         resume_text = f.read()

#     llm_output = parse_resume(resume_text)
#     structured_data = extract_json(llm_output)

#     print(json.dumps(structured_data, indent=2))

import json
import re
from transformers import pipeline

# Initialize a free Hugging Face text-generation model
generator = pipeline("text-generation", model="gpt2")  # or try "mistral-mini" for slightly better results

def parse_resume(resume_text):
    """
    Parse a resume using a free Hugging Face model.
    Returns raw LLM output (string) containing JSON.
    """
    prompt = f"""
You are an AI resume parser.

Extract information from the resume text.
Return ONLY valid JSON.
No explanations. No markdown.

Schema:
{{
  "skills": [],
  "experience_level": "",
  "domains": [],
  "tools": [],
  "education": ""
}}

Rules:
- skills → technical + soft skills
- experience_level → one of: fresher, junior, mid
- domains → inferred from projects/experience
- tools → software, libraries, platforms
- education → highest degree only

Resume:
{resume_text}
"""

    # Generate output using Hugging Face model
    result = generator(prompt, max_length=300, do_sample=False)  # deterministic output
    return result[0]["generated_text"]

def extract_json(llm_output):
    """
    Extract JSON from LLM output string.
    """
    match = re.search(r"\{.*\}", llm_output, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in LLM output")
    return json.loads(match.group())

if __name__ == "__main__":
    with open("core/resume.txt", encoding="utf-8") as f:
        resume_text = f.read()

    llm_output = parse_resume(resume_text)
    structured_data = extract_json(llm_output)

    print(json.dumps(structured_data, indent=2))
