# llm_roadmap.py
from llm_client import call_llm

def explain_roadmap(role, roadmap):
    prompt = f"""
You are a career mentor.

Explain the following learning roadmap for the role of {role}.
Do NOT add new resources.
Do NOT change structure.

Roadmap:
{roadmap}
"""


    return call_llm(prompt)
