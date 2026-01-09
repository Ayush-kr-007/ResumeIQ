job_roles_skills = {

    "Data Analyst": {
        "core_skills": {
            "python": 3,
            "sql": 3,
            "pandas": 2,
            "excel": 2,
            "data visualization": 2,
            "power bi": 2,
            "statistics": 2
        },
        "nice_to_have": [
            "tableau", "dashboard", "business understanding"
        ],
        "entry_level": True
    },

    "Data Scientist": {
        "core_skills": {
            "python": 3,
            "machine learning": 3,
            "statistics": 3,
            "sql": 2,
            "pandas": 2,
            "numpy": 2
        },
        "nice_to_have": [
            "scikit-learn", "feature engineering", "model evaluation"
        ],
        "entry_level": True
    },

    "Machine Learning Engineer": {
        "core_skills": {
            "python": 3,
            "machine learning": 3,
            "scikit-learn": 3,
            "statistics": 2
        },
        "nice_to_have": [
            "deep learning", "docker", "mlops"
        ],
        "entry_level": True
    },

    "Business Analyst": {
        "core_skills": {
            "excel": 3,
            "sql": 2,
            "data analysis": 2,
            "reporting": 2,
            "documentation": 1
        },
        "nice_to_have": [
            "power bi", "tableau", "stakeholder management"
        ],
        "entry_level": True
    },

    "Business Intelligence Developer": {
        "core_skills": {
            "sql": 3,
            "power bi": 3,
            "tableau": 2,
            "data modeling": 2,
            "excel": 2
        },
        "nice_to_have": [
            "dax", "dashboard", "report automation"
        ],
        "entry_level": True
    },

    "AI Engineer": {
        "core_skills": {
            "python": 3,
            "machine learning": 3,
            "deep learning": 2
        },
        "nice_to_have": [
            "nlp", "computer vision", "tensorflow"
        ],
        "entry_level": True
    },

    "Software Engineer": {
        "core_skills": {
            "python": 3,
            "java": 2,
            "data structures": 3,
            "algorithms": 3,
            "object oriented programming": 2
        },
        "nice_to_have": [
            "git", "api development", "system design"
        ],
        "entry_level": True
    },

    "Web Developer": {
        "core_skills": {
            "html": 3,
            "css": 3,
            "javascript": 3,
            "frontend development": 2
        },
        "nice_to_have": [
            "react", "node.js", "api integration"
        ],
        "entry_level": True
    },

    "DevOps Engineer": {
        "core_skills": {
            "linux": 3,
            "shell scripting": 2,
            "ci/cd pipelines": 2
        },
        "nice_to_have": [
            "docker", "kubernetes", "cloud services"
        ],
        "entry_level": True
    },

    "Database Administrator": {
        "core_skills": {
            "sql": 3,
            "database design": 2,
            "backup and recovery": 2
        },
        "nice_to_have": [
            "performance tuning", "data security", "postgresql"
        ],
        "entry_level": True
    }
}
for role, data in job_roles_skills.items():
    print(role, type(data["core_skills"]))
