"""
Resume Parser Service
Extracts text from PDF and DOCX files
"""

from PyPDF2 import PdfReader
from docx import Document
import io


def extract_text_from_pdf(file) -> str:
    """Extract text content from a PDF file."""
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")


def extract_text_from_docx(file) -> str:
    """Extract text content from a DOCX file."""
    try:
        doc = Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Error reading DOCX: {str(e)}")


def parse_resume(uploaded_file) -> str:
    """
    Parse resume from uploaded file (PDF or DOCX).
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        Extracted text from the resume
    """
    file_extension = uploaded_file.name.lower().split('.')[-1]
    
    if file_extension == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_extension in ['docx', 'doc']:
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Please upload PDF or DOCX.")
