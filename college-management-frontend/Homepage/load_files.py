import os
import pathlib
import psycopg2
import mimetypes
import random
from tqdm import tqdm
from dotenv import load_dotenv

DATASET_PATH = r"C:\Users\My Computer\Desktop\College_Management_System-main\college-management-frontend\Homepage\dataset"

# Zambian first names for assigning to students
zambian_names = [
    "Mwansa", "Chileshe", "Mutale", "Luyando", "Mubanga", "Bwalya", "Misozi", "Chanda", "Musonda", "Mulenga",
    "Kunda", "Mumba", "Lombe", "Kangwa", "Tembo", "Phiri", "Zimba", "Sakala", "Muleya", "Mwanza"
]

load_dotenv()

conn = psycopg2.connect(
    dbname=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT')
)

cur = conn.cursor()

for root, _, files in os.walk(DATASET_PATH):
    for file in tqdm(files, desc="Uploading files"):
        fpath = pathlib.Path(root) / file
        ext = fpath.suffix.lower().lstrip('.')

        if ext not in ('pdf', 'docx'):
            continue

        with open(fpath, 'rb') as f:
            file_data = f.read()

        mime_type, _ = mimetypes.guess_type(fpath)
        if not mime_type:
            mime_type = 'application/octet-stream'

        # Assign a random Zambian name to the student
        student_name = random.choice(zambian_names)

        cur.execute("""
            INSERT INTO assignments (student, title, file_ext, mime_type, file_size_bytes, file_data)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            student_name,
            fpath.stem,
            ext,
            mime_type,
            len(file_data),
            psycopg2.Binary(file_data)
        ))

conn.commit()
cur.close()
conn.close()

print("✅ Upload complete.")