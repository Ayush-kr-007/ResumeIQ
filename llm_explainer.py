def explain_result(result: dict) -> str:
    role = result.get("role", "the selected role")
    score = result.get("ats_score", 0)
    fit = result.get("fit", "Needs Upskilling")

    missing = [s for s, _ in result.get("missing_core", [])][:3]

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
        "Strengthening these areas can significantly improve your profile and "
        "increase your role fit."
    )

    return explanation
