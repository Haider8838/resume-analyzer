import docx2txt
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file):
    return extract_text(file)

def extract_text_from_docx(file):
    return docx2txt.process(file)