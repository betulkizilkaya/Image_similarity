import sqlite3
from sklearn.neighbors import NearestNeighbors
import os

def compute_similarity(image_paths, embeddings, top_k=5):
    conn = sqlite3.connect('image_silo.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS image_similarity (
            id INTEGER PRIMARY KEY,
            image_name1 TEXT,
            image_name2 TEXT,
            score REAL
        )
    ''')
    conn.commit()

    model = NearestNeighbors(n_neighbors=top_k + 1, metric='cosine')# Burada +1 yapılır çünkü kendisi de en benzer olarak geri döner.
    model.fit(embeddings)

    distances, indices = model.kneighbors(embeddings)

    for i, query_path in enumerate(image_paths):
        query_name = os.path.basename(query_path)# Sadece dosya adı

        for idx, dist in zip(indices[i], distances[i]):# dist: İki görsel arasındaki cosine distance değeridir.
            matched_path = image_paths[idx]
            matched_name = os.path.basename(matched_path)

            similarity_score = 1 - dist# Bu formülle mesafeyi benzerliğe çeviririz.

            if matched_name == query_name or query_name > matched_name:# Aynı dosyayla veya tekrar kayıtları engelle
                continue

            cursor.execute('''
                INSERT INTO image_similarity (image_name1, image_name2, score)
                VALUES (?, ?, ?)
            ''', (query_name, matched_name, float(similarity_score)))

    conn.commit()
    conn.close()
    print("✅ Image similarity results inserted into the database.")
