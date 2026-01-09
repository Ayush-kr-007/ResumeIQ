# from core.resource_db import RESOURCE_DB
from resource_db import RESOURCE_DB


def build_resource_roadmap(role, missing_skills, level="beginner"):
    roadmap = []

    for skill in missing_skills:
        skill_resources = RESOURCE_DB.get(skill.lower(), {}).get(level, [])

        if not skill_resources:
            continue

        roadmap.append({
            "skill": skill,
            "resources": skill_resources,
            "practice": f"Apply {skill} on a small dataset or project",
            "outcome": f"Basic working knowledge of {skill}"
        })

    return roadmap
