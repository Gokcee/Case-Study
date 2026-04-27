from core.ocr import extract_text
from core.chunking import chunk_text
from core.embedding import embed_chunks
from core.retrieval import retrieve_context
from core.answer import generate_answer
from config.settings import documents

def upload_document(file_bytes, filename):
    print(" Metin çıkarılıyor...")
    text = extract_text(file_bytes, filename)

    print(" Chunking yapılıyor...")
    chunks = chunk_text(text)

    print(" Embedding oluşturuluyor...")
    embeddings = embed_chunks(chunks)

    documents.append({
        "chunks": chunks,
        "embeddings": embeddings
    })

    print(" Doküman başarıyla yüklendi!")

def ask_question(question):
    print(" Context aranıyor...")
    context = retrieve_context(question, documents)

    print("\n BULUNAN CONTEXT:\n")
    print(context[:500])

    print("\n Cevap üretiliyor...\n")
    return generate_answer(question, context)