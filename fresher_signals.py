# fresher_signals.py

def get_project_score(resume_text: str) -> float:
    keywords = [
        "project", "projects", "internship", "intern",
        "capstone", "built", "developed", "implemented"
    ]
    return 1.0 if any(k in resume_text for k in keywords) else 0.0


def get_education_score(resume_text: str) -> float:
    strong = [
        "btech", "b.e", "bachelor",
        "computer science", "data science",
        "statistics", "engineering"
    ]
    medium = ["degree", "graduate", "college", "university"]

    if any(k in resume_text for k in strong):
        return 1.0
    if any(k in resume_text for k in medium):
        return 0.5
    return 0.0


def get_structure_score(resume_text: str) -> float:
    sections = ["skills", "projects", "education", "experience", "certifications"]
    found = sum(1 for s in sections if s in resume_text)

    if found >= 4:
        return 1.0
    elif found >= 2:
        return 0.5
    return 0.0


def get_tool_score(known_skills: set[str]) -> float:
    count = len(known_skills)
    if count >= 6:
        return 1.0
    elif count >= 3:
        return 0.5
    return 0.0
