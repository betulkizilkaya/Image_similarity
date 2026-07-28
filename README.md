# 🔍 Image Similarity System

This project is an image similarity pipeline that calculates how similar images in a directory are based on their visual content and stores the results in a SQLite database. 🧠📸

It uses a deep learning model to extract vector representations from images and performs similarity comparisons between these vectors.

---

## 🚀 Features

* 📂 Automatically scans images and saves their information to the database
* 🧠 Extracts image embeddings using ResNet50
* 📐 Calculates similarity scores using cosine similarity
* 💾 Stores the most similar images and their similarity scores in a SQLite database
* 🖥️ Designed to run entirely on CPU

---

## 🛠️ Technologies Used

* 🐍 Python 3
* 🧠 ResNet50 pretrained on ImageNet for visual feature extraction
* 🗂️ DeepFashion Dataset as the source of the images used in the similarity analysis
* 🧮 CPU-optimized processing
* 📦 Libraries:

  * `torch` — Deep learning model operations
  * `torchvision` — Image preprocessing and pretrained ResNet50 model
  * `Pillow (PIL)` — Opening, resizing, and processing images
  * `NumPy` — Mathematical operations on embedding vectors
  * `scikit-learn` — Image similarity analysis using the `NearestNeighbors` algorithm
  * `sqlite3` — Storing image paths and similarity scores in a database

---

## 📂 File Descriptions

* `main.py` — Starts and manages the entire image similarity pipeline
* `Embedding.py` — Extracts embeddings from images using ResNet50
* `Similarity.py` — Calculates image similarity scores and saves them to the database
* `image_silo.db` — SQLite database containing image information and similarity scores

---

## 📁 Project Structure

```text
Image_similarity/
│
├── Images/             # Images used in the similarity analysis
├── main.py             # Main application file
├── Embedding.py        # Image embedding extraction
├── Similarity.py       # Similarity calculation and database operations
├── image_silo.db       # Automatically generated SQLite database
└── README.md
```

---

## 🧪 Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/betulkizilkaya/Image_similarity.git
cd Image_similarity
```

### 2. Install the required libraries

```bash
pip install torch torchvision numpy pillow scikit-learn
```

### 3. Add the images

Place the images you want to analyze inside the `Images/` directory.

### 4. Run the application

```bash
python main.py
```

### 5. View the results

The similarity results are stored in the `image_similarity` table inside the automatically generated `image_silo.db` SQLite database.

You can inspect the database using an SQLite database viewer or SQLite commands.

---

## 🧠 How It Works

1. The application scans the images inside the `Images/` directory.
2. Each image is preprocessed according to the input requirements of ResNet50.
3. The pretrained ResNet50 model extracts an embedding vector for each image.
4. The embedding vectors are compared using cosine similarity.
5. The nearest and most similar images are identified using the `NearestNeighbors` algorithm.
6. Image paths and similarity scores are stored in the SQLite database.

---

## 📊 Dataset

The images used in this project were obtained from the DeepFashion-MultiModal dataset:

[DeepFashion-MultiModal](https://github.com/yumingj/DeepFashion-MultiModal)

DeepFashion-MultiModal is used only as the image source for the similarity analysis.

---

## 📝 Notes

* The project uses a ResNet50 model pretrained on ImageNet.
* All operations are configured to run on CPU.
* Processing time may increase depending on the number and size of the images.
* The `image_silo.db` database is automatically created when the application is executed.
* The `Images/` directory must contain supported image formats such as `.jpg`, `.jpeg`, or `.png`.

---

## 📄 License

This project is licensed under the MIT License.

© 2025 [Betül Kızılkaya](https://github.com/betulkizilkaya)

For more information, see the [LICENSE](LICENSE) file.
