
SKILL_ALIASES = {
    "python": ["python"],
    "sql": ["sql", "mysql", "postgresql"],
    "excel": ["excel", "ms excel", "microsoft excel"],
    "data analysis": ["data analysis"],
    "reporting": ["reporting", "reports"],
    "documentation": ["documentation"],
    "data modeling": ["data modeling", "dimensional modeling"],
    "data structures": ["data structures", "ds"],
    "algorithms": ["algorithms", "algo"],
    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "js"],
    "shell scripting": ["shell scripting", "bash"],
    "ci/cd pipelines": ["ci/cd", "cicd", "pipelines"],
    "pandas": ["pandas"],
    "numpy": ["numpy", "np"],
    "data cleaning": ["data cleaning", "data cleansing"],
    "data preprocessing": ["data preprocessing", "preprocessing"],
    "data wrangling": ["data wrangling", "data munging"],
    "statistics": ["statistics", "statistical analysis"],
    "eda": ["eda", "exploratory data analysis"],
    "hypothesis testing": ["hypothesis testing", "a/b testing"],
    "data visualization": ["data visualization", "visualization", "viz", "data viz"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "dashboard": ["dashboard", "dashboards"],
    "machine learning": ["machine learning", "ml"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "feature engineering": ["feature engineering"],
    "model evaluation": ["model evaluation", "model validation"],
    "regression": ["regression", "linear regression", "logistic regression"],
    "classification": ["classification", "classifier"],
    "django": ["django"],
    "rest api": ["rest api", "api", "restful api"],
    "linux": ["linux", "unix"],
    "git": ["git", "github", "version control"],
    "jupyter notebook": ["jupyter", "jupyter notebook", "ipynb"]
}


def extract_skills(resume_text: str) -> set[str]:
    known_skills = set()

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if alias in resume_text:
                known_skills.add(skill)
                break

    return known_skills
