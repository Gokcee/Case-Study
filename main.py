from services.pipeline import upload_document, ask_question
from utils.file_utils import read_file
import os

def main():
    print("=== AI Document QA System (Local) ===")

    # Dosya yükleme
    while True:
        path = input("\nDosya path gir (devam etmek için 'q'): ")

        if path.lower() == "q":
            break

        if not os.path.exists(path):
            print("❌ Dosya bulunamadı, tekrar dene bro...")
            continue

        try:
            file_bytes, filename = read_file(path)
            upload_document(file_bytes, filename)
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")

    # Soru-cevap loop
    while True:
        question = input("\nSorunu yaz (çıkmak için 'q'): ")

        if question.lower() == "q":
            print("👋 Çıkılıyor...")
            break

        try:
            answer = ask_question(question)
            print("\n📌 CEVAP:\n", answer)
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")

if __name__ == "__main__":
    main()