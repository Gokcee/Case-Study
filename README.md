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
ai-doc-qa/
│
├── app/
│   ├── main.py
│   ├── api/routes.py
│   ├── services/
│   │   ├── ocr.py
│   │   ├── embedding.py
│   │   ├── retriever.py
│   │   └── llm.py
│   └── utils/chunking.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
├── vector_store/
│
├── DEVLOG.md
├── TESTING.md
├── README.md
├── requirements.txt
```

---

## ⚙️ Kurulum

### 1. Repo’yu klonlayın

```bash
git clone https://github.com/your-repo/ai-doc-qa.git
cd ai-doc-qa
```

---

### 2. Sanal ortam oluşturun (opsiyonel ama önerilir)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3. Bağımlılıkları yükleyin

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
