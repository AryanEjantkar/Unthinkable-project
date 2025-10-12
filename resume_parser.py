import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """Extract text from an uploaded PDF resume."""
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text("text")
    return text.strip()
