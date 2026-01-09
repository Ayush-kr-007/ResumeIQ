# evaluator.py

def calculate_core_score(core_skills, known_skills):
    matched = sum(
        weight for skill, weight in core_skills.items()
        if skill.lower() in known_skills
    )
    total = sum(core_skills.values())
    return matched / total if total else 0


def calculate_optional_score(optional_skills, known_skills):
    if not optional_skills:
        return 0

    optional_set = set(s.lower() for s in optional_skills)
    return len(optional_set & known_skills) / len(optional_set)


def evaluate_role(role_name, role_data, known_skills):
    core_score = calculate_core_score(
        role_data["core_skills"],
        known_skills
    )

    optional_score = calculate_optional_score(
        role_data.get("nice_to_have", []),
        known_skills
    )

    missing_core = sorted(
        (
            (skill, weight)
            for skill, weight in role_data["core_skills"].items()
            if skill.lower() not in known_skills
        ),
        key=lambda x: x[1],
        reverse=True
    )

    return {
        "role": role_name,
        "core_score": core_score,
        "optional_score": optional_score,
        "missing_core": missing_core
    }
