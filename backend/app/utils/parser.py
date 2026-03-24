import fitz #PyMuPDF
from docx import Document

def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream = file.file.read(), filetype = "pdf")
    for page in pdf:
        text += page.get_text()
    
    return text

def extract_text_from_docx(file):
    doc = Document(file.file)
    
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def parse_file(file):
    if file.filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.filename.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        raise ValueError('Unsupported file format')