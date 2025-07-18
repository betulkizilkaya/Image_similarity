import sqlite3
import os

from Embedding import get_embeddings
from Similarity import compute_similarity


def create_db():
    conn = sqlite3.connect('image_silo.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS image_files (
            id INTEGER PRIMARY KEY,
            folder_name TEXT,
            image_name TEXT,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_images(image_root_folder):
    conn=sqlite3.connect('image_silo.db')
    cursor = conn.cursor()

    inserted_cnt= 0

    for root,dirs,images in os.walk(image_root_folder): #os.walk(...) ile klasör içindeki tüm görselleri bulur.
        folder_name = os.path.basename(root)
        for image in images:
            if image.lower().endswith(('.png','.jpg','.jpeg')):
                image_path = os.path.join(root, image)
                cursor.execute('''
                    INSERT INTO image_files (folder_name,image_name,image_path) 
                    VALUES (?,?,?)''',
        (folder_name,image,image_path))
                print(f'Inserted: {image} from {folder_name}')
                inserted_cnt+= 1


    conn.commit()
    conn.close()
    print(f"✅ Total images inserted: {inserted_cnt}")

if __name__=="__main__":
    image_folder=(r'C:\Users\betul\OneDrive\Belgeler\GitHub\Image_similarity\Images')

    create_db()
    insert_images(image_folder)
    print("Image insertion completed.")

    print("Extracting image embeddings...")
    image_paths, embeddings = get_embeddings() #Bu fonksiyon başka bir dosyada (Embedding.py) tanımlı.

    print("🔹Calculating image similarity with NearestNeighbors...")
    compute_similarity(image_paths, embeddings)#Bu da başka bir dosyada (Similarity.py) tanımlı.

    print("All steps completed successfully.")