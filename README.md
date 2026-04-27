# Case-Study
AI Destekli Belge Analiz ve Soru-Cevap Sistemi 
# AI Document QA System

## 📌 Proje Tanımı

Bu proje, kullanıcıların PDF ve görsel formatındaki belgeleri yükleyerek bu belgeler üzerinden doğal dil ile soru sorabildiği bir yapay zeka sistemidir.

Sistem, belge içeriğini analiz eder ve yalnızca belgeye dayalı cevaplar üretir.

---

## 🚀 Özellikler

* PDF ve görsel (JPG, PNG) yükleme
* OCR ile metin çıkarımı (Türkçe + İngilizce)
* Semantik arama (embedding)
* Context tabanlı soru-cevap (RAG)
* Hallucination kontrolü ("Bilmiyorum" mekanizması)

---

## 🧠 Kullanılan Teknolojiler

* Python
* FastAPI
* Streamlit
* Sentence Transformers
* Tesseract OCR
* pdfplumber
* scikit-learn

---

## 🏗️ Proje Yapısı

```bash
ai_doc_qa/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── core/
│   ├── ocr.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── retrieval.py
│   └── answer.py
│
├── services/
│   └── pipeline.py
│
├── utils/
│   └── file_utils.py
│
└── requirements.txt
```

---



## ⚙️ Kurulum

### 1. Repo’yu klonlayın

```bash
git clone https://github.com/Gokcee/Case-Study.git
cd Case-Study
```

---

### 2. Sanal ortam oluşturun, requirements.txt dosyasını referans vererek oluşturmanız önerilir. (opsiyonel)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3. Bağımlılıkları yükleyin (requirements.txt'i referans vererek sanal ortam oluşturulmadıysa)

```bash
pip install -r requirements.txt
```

---

### 4. Tesseract kurulum (OCR için)

#### Ubuntu:

```bash
sudo apt-get install tesseract-ocr
```

#### Windows:

* https://github.com/tesseract-ocr/tesseract

---

## ▶️ Çalıştırma

### Backend başlat

```bash
uvicorn app.main:app --reload
```

---

### Frontend başlat

```bash
streamlit run frontend/streamlit_app.py
```

---

## 💻 Kullanım

1. Web arayüzünden belge yükleyin
2. Soru girin
3. Sistem cevap üretsin

---

## Mimari

- OCR → Text Extraction
- Chunking
- Embedding
- Retrieval
- Answer generation

---

## 🧪 Test

TESTING.md dosyasında test senaryoları ve sonuçlar detaylı olarak verilmiştir.

---

## 📓 Geliştirme Süreci

DEVLOG.md dosyasında geliştirme süreci ve alınan kararlar açıklanmıştır.

---

## ⚠️ Bilinen Sınırlamalar

* OCR düşük kaliteli görsellerde hatalı olabilir
* Tablo içeren PDF’lerde veri kaybı olabilir
* Çok uzun belgelerde retrieval performansı düşebilir

---

## 🔮 Gelecek Geliştirmeler

* FAISS / vector database entegrasyonu
* Daha güçlü OCR (PaddleOCR)
* Tablo parsing
* Source attribution (kaynak gösterimi)

---

## 🎯 Sonuç

Bu proje, belge tabanlı soru-cevap sistemi için çalışan bir MVP sunmaktadır. Sistem modüler olup geliştirmeye açıktır.
