#ResNet50 modeli kullanarak her görselin temsilini çıkaracağız.
import sqlite3
import numpy as np
import torch
from torchvision import models, transforms
from PIL import Image
from torchvision.models import resnet50, ResNet50_Weights

model = resnet50(weights=ResNet50_Weights.DEFAULT)# ResNet50_Weights.DEFAULT:En güncel ImageNet ağırlıkları kullanılır.
model.fc=torch.nn.Identity()# Sınıflandırma katmanı kaldırılıyor, sadece özellik çıkarımı yapılır.
model.eval()# dropout vb. devre dışı kalır.

transforms=transforms.Compose([# ResNet50 modeline uygun hale getiriyor:
    transforms.Resize((224, 224)),
    transforms.ToTensor(),# Tensor'e (çok boyutlu veri yapısı) çevirme
])

def get_embedding(image_path):
    try:
        img=Image.open(image_path).convert('RGB')  # Görseli RGB formatına dönüştürüyoruz
        img=transforms(img).unsqueeze(0)
        with torch.no_grad():
            emb=model(img).squeeze().numpy()
        norm = np.linalg.norm(emb)
        return emb / norm if norm != 0 else emb

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def get_embeddings():
    conn = sqlite3.connect('image_silo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT image_path FROM image_files")
    rows = cursor.fetchall()
    conn.close()

    image_paths = []
    embeddings = []

    for (path,) in rows:# Tuple’dan sadece bir değeri alır.
        emb = get_embedding(path)
        if emb is not None:
            image_paths.append(path)#image_paths listesine o görselin yolu eklenir.
            embeddings.append(emb)#Her görselin embedding’i, embeddings listesine eklenir.

    embeddings = np.array(embeddings).astype('float32')#Listeyi bir NumPy array’ine dönüştürür
    return image_paths, embeddings