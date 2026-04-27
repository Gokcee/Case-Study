import io
from PIL import Image
import pytesseract
import pdfplumber

def extract_text(file_bytes, filename):
    if filename.lower().endswith(".pdf"):
        text = ""
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        if not text.strip():
            return "PDF okunamadı"
        return text

    image = Image.open(io.BytesIO(file_bytes))
    return pytesseract.image_to_string(image)