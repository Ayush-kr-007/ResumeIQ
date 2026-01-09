import re


RESUME_SECTIONS = [
    "skills", "education", "experience", "projects",
    "certifications", "internship", "summary"
]


def has_email(text: str) -> bool:
    return bool(re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text))


def has_phone(text: str) -> bool:
    return bool(re.search(r"\b\d{10}\b|\+\d{1,3}\s?\d{8,12}", text))


def has_profile_links(text: str) -> bool:
    return any(x in text for x in ["linkedin", "github"])


def section_score(text: str) -> float:
    found = sum(1 for s in RESUME_SECTIONS if s in text)
    return min(found / 4, 1.0)   # cap at 1.0


def bullet_score(text: str) -> float:
    bullets = sum(text.count(b) for b in ["•", "-", "–"])
    return 1.0 if bullets >= 5 else 0.5 if bullets >= 2 else 0.0


def date_score(text: str) -> float:
    years = re.findall(r"\b(19|20)\d{2}\b", text)
    return 1.0 if len(years) >= 2 else 0.5 if len(years) == 1 else 0.0


def length_score(text: str) -> float:
    length = len(text)
    if length < 150:
        return 0.0
    if length > 10000:
        return 0.5
    return 1.0


def validate_resume(text: str) -> dict:
    text = text.lower()

    sec = section_score(text)
    contact = 1.0 if (has_email(text) or has_phone(text) or has_profile_links(text)) else 0.0
    bullets = bullet_score(text)
    dates = date_score(text)
    length = length_score(text)

    confidence = (
        0.35 * sec +
        0.25 * contact +
        0.15 * bullets +
        0.15 * dates +
        0.10 * length
    )

    return {
        "confidence": round(confidence, 2),
        "section_score": sec,
        "contact_score": contact,
        "bullet_score": bullets,
        "date_score": dates,
        "length_score": length
    }
