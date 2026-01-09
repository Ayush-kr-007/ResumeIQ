# from llm_client import call_llm

# def explain_result(result: dict) -> str:
#     prompt = (
#         "Explain this ATS result to a student in 4–5 sentences.\n\n"
#         f"{result}\n\n"
#         "Explanation:"
#     )
#     print("🔥 NEW explainer loaded")

#     return call_llm(prompt)

def explain_result(result: dict) -> str:
    role = result["role"]
    score = result["ats_score"]
    fit = result["fit"]
    missing = [s for s, _ in result["missing_core"]][:3]

    explanation = (
        f"Your resume was evaluated for the {role} role and received an ATS score of {score}%. "
        f"This indicates a {fit.lower()} overall alignment with the role. "
    )

    if missing:
        explanation += (
            "Some important skills that could improve your chances include "
            + ", ".join(missing)
            + ". "
        )

    explanation += (
        "Strengthening these areas can significantly improve your profile and increase your role fit."
    )

    return explanation
