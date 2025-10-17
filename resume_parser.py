import pdfplumber
import docx
from io import BytesIO

def extract_text_from_resume(uploaded_file):
    text = ""
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif file_type == "docx":
        doc = docx.Document(BytesIO(uploaded_file.read()))
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        text = "Unsupported file format."

    return text.strip()
