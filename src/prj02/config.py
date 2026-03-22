import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

class MinioConfig:
    endpoint = os.getenv("MINIO_ENDPOINT")
    access_key = os.getenv("MINIO_ACCESS_KEY")
    secret_key = os.getenv("MINIO_SECRET_KEY")
    bucket = os.getenv("MINIO_BUCKET")
    file = os.getenv("MINIO_FILE")
