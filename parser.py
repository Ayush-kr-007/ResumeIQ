# parser.py
import os
import PyPDF2
from docx import Document


def extract_resume_text(file_path: str) -> str:
    """
    Accepts PDF, DOCX, or TXT
    Returns extracted text (lowercased)
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif ext == ".pdf":
        text = ""
        reader = PyPDF2.PdfReader(file_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

    elif ext == ".docx":
        doc = Document(file_path)
        text = " ".join(p.text for p in doc.paragraphs)

    else:
        raise ValueError("Unsupported file format")

    return text.lower()
