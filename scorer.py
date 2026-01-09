# scorer.py
from ml_model import predict_pass_probability

from fresher_signals import (
    get_project_score,
    get_education_score,
    get_structure_score,
    get_tool_score
)


def get_fit_label(score: float) -> str:
    if score >= 0.75:
        return "Interview Ready"
    elif score >= 0.5:
        return "Needs Upskilling"
    return "Early-Stage Fresher"


def calculate_ats_score(evaluation, resume_text, known_skills):
    core = evaluation["core_score"]
    optional = evaluation["optional_score"]

    project = get_project_score(resume_text)
    education = get_education_score(resume_text)
    structure = get_structure_score(resume_text)
    tools = get_tool_score(known_skills)

    final_score = (
        0.45 * core +
        0.15 * optional +
        0.15 * project +
        0.15 * education +
        0.05 * structure +
        0.05 * tools
    )

    ml_prob = predict_pass_probability(
    core=core,
    optional=optional,
    project=project,
    education=education,
    structure=structure,
    tools=tools
)

    evaluation.update({
        "ats_score": round(final_score * 100, 2),
        "fit": get_fit_label(final_score),
        "ml_pass_probability": ml_prob,
        "signals": {
            "projects": project,
            "education": education,
            "structure": structure,
            "tools": tools
        }
    })

    return evaluation

