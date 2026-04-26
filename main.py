# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:19:53 2026

@author: Toshiba-Pc
"""
# =========================
# AI DOCUMENT QA SYSTEM (SPYDER VERSION)
# =========================
import pytesseract

# =========================
# 1. IMPORTS
# =========================
import io
import numpy as np
from PIL import Image
import pytesseract
import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import Tk, filedialog

# =========================
# 2. MODEL & GLOBALS
# =========================
model = SentenceTransformer("all-MiniLM-L6-v2")
documents = []

# =========================
# 3. FILE SELECTION (LOCAL)
# =========================
def select_file():
    Tk().withdraw()  # GUI window gizle
    file_path = filedialog.askopenfilename(
        title="Select a PDF or Image file",
        filetypes=[("PDF files", "*.pdf"), ("Image files", "*.png;*.jpg;*.jpeg")]
    )
    return file_path

# =========================
# 4. OCR & PDF PARSING
# =========================
def extract_text(file_path):
    if file_path.lower().endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        if not text.strip():
            return "PDF okunamadı"
        return text

    # image case
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

# =========================
# 5. CHUNKING
# =========================
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks

# =========================
# 6. EMBEDDING
# =========================
def embed_chunks(chunks):
    return model.encode(chunks)

# =========================
# 7. RETRIEVAL
# =========================
def retrieve_context(question, documents, top_k=3):
    if not documents:
        return ""

    query_embedding = model.encode([question])

    all_chunks = []
    all_embeddings = []

    for doc in documents:
        all_chunks.extend(doc["chunks"])
        all_embeddings.extend(doc["embeddings"])

    if len(all_chunks) == 0:
        return ""

    sims = cosine_similarity(query_embedding, all_embeddings)[0]
    top_indices = np.argsort(sims)[-top_k:][::-1]

    return "\n".join([all_chunks[i] for i in top_indices])

# =========================
# 8. ANSWER GENERATION
# =========================
def generate_answer(question, context):
    if not context.strip():
        return "Bilmiyorum, belgede bu bilgi yok."

    return f"""
Soru: {question}

Cevap (belgeye göre):
{context[:500]}
"""

# =========================
# 9. UPLOAD PIPELINE
# =========================
def upload_document(file_path):
    print("\n📄 Metin çıkarılıyor...")
    text = extract_text(file_path)

    print("✂️ Chunking yapılıyor...")
    chunks = chunk_text(text)

    print("🔢 Embedding oluşturuluyor...")
    embeddings = embed_chunks(chunks)

    documents.append({
        "chunks": chunks,
        "embeddings": embeddings
    })

    print("✅ Doküman yüklendi!")

# =========================
# 10. QUESTION PIPELINE
# =========================
def ask_question(question):
    print("\n🔍 Context aranıyor...")
    context = retrieve_context(question, documents)

    print("\n📌 BULUNAN CONTEXT:\n")
    print(context[:500])

    print("\n🤖 Cevap üretiliyor...\n")
    return generate_answer(question, context)

# =========================
# 11. MAIN LOOP (SPYDER FRIENDLY)
# =========================
if __name__ == "__main__":

    print("=== AI DOCUMENT QA SYSTEM (SPYDER) ===")

    file_path = select_file()

    if not file_path:
        print("❌ Dosya seçilmedi")
        exit()

    upload_document(file_path)

    while True:
        question = input("\n❓ Soru yaz (çıkış: q): ")

        if question.lower() == "q":
            break

        answer = ask_question(question)
        print("\n💬 CEVAP:\n", answer)