# 🔍 Görsel Benzerlik Sistemi (Image Similarity Pipeline)

Bu proje, bir klasörde yer alan görsellerin içeriklerine göre birbirine ne kadar benzediğini hesaplayan ve sonuçları bir SQLite veritabanında saklayan bir sistemdir. 🧠📸  
Derin öğrenme tabanlı görsel temsil çıkarımı ve vektörel benzerlik karşılaştırması gerçekleştirilir.

---

## 🚀 Özellikler

- 📂 Görsellerin otomatik taranması ve veritabanına kaydedilmesi  
- 🧠 ResNet50 ile embedding (vektörel temsil) çıkarımı  
- 📐 Cosine similarity ile benzerlik hesaplama  
- 💾 En benzer görsellerin ve skorlarının veritabanında saklanması  

---

## 🛠️ Kullanılan Teknolojiler

- 🐍 Python 3
- 🖥️ ResNet50 (ImageNet pretrained) – Görsel içeriklerden anlamlı özellik çıkarımı
- 🗂️ DeepFashion Dataset – Benzerlik analizine giren görsellerin alındığı veri seti
- 🧮 CPU Optimized – Tüm işlemler CPU üzerinde çalışacak şekilde yapılandırılmıştır
- 📦 Kütüphaneler:
  - `sentence-transformers`
  - `Pillow (PIL.Image) – Görsellerin açılması, yeniden boyutlandırılması ve işlenmesi`
  - `porch & torchvision – Derin öğrenme modeli ve ön işleme işlemleri`
  - `NumPy – Embedding vektörleri üzerinde matematiksel işlemler`
  - `scikit-learn – NearestNeighbors algoritması ile görseller arası benzerlik analizi`
  - `sqlite3 – Veritabanı işlemleri: görsellerin yolları ve benzerlik skorlarının saklanması`
---

## 📂 Dosya Açıklamaları

- `main.py` → Sistemin çalışmasını başlatır; tüm süreci yönetir  
- `Embedding.py` → Görsellerden embedding çıkarır (ResNet50 kullanarak)  
- `Similarity.py` → Görseller arası benzerliği hesaplar ve veritabanına yazar  
- `image_silo.db` → Görsel bilgileri ve benzerlik skorlarını içeren SQLite veritabanı  

---

## 📁 Klasör Yapısı
    project-folder/
    │
    ├── Images/ # Benzerlik analizine girecek görseller
    ├── main.py
    ├── Embedding.py
    ├── Similarity.py
    ├── image_silo.db # Otomatik oluşturulur
    └── README.md


## 🧪 Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install torch torchvision numpy pillow scikit-learn
2. Görselleri Images/ klasörüne yerleştirin.

3. Ana dosyayı çalıştırın:
   ```bash
   python main.py

4. Sonuçları image_silo.db içindeki image_similarity tablosunda inceleyebilirsiniz.

## 📝 Notlar

- Görseller, DeepFashion veri setinden alınmıştır: [https://github.com/yumingj/DeepFashion-MultiModal](https://github.com/yumingj/DeepFashion-MultiModal)
- Model olarak ImageNet üzerinde önceden eğitilmiş **ResNet50** kullanılmıştır.
- Tüm işlemler **CPU üzerinde çalışacak şekilde** optimize edilmiştir.

## 📄 Lisans

MIT Lisansı © 2025 [Betül Kızılkaya](https://github.com/betulkizilkaya)  
Lisans detayları için: [LICENSE](LICENSE)

