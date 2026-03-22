# prj02 — Lectura de CSV desde MinIO con configuración parametrizada

Este proyecto demuestra una arquitectura limpia y modular en Python para leer archivos CSV almacenados en **MinIO**, utilizando credenciales y configuración externas a través de un archivo `.env`.  
El objetivo es disponer de una base sólida para futuros desarrollos de parametrización, orquestación y automatización.

---

## 🚀 Características principales

- Lectura de archivos CSV desde MinIO usando `boto3`
- Configuración desacoplada mediante `.env`
- Código modular y extensible (`config.py`, `minio_reader.py`)
- Compatible con MinIO local, Docker o entornos remotos
- Preparado para evolucionar hacia:
  - logs profesionales
  - clases cliente (`MinioClient`)
  - escritura de datos en MinIO
  - integración con YAML de parametrización

---

## 📂 Estructura del proyecto

´´´
prj02/
├── src/
│   └── prj02/
│       ├── init.py
│       ├── config.py
│       ├── minio_reader.py
│       └── main.py
├── .env
└── .gitignore
´´´

---

## ⚙️ Configuración

El archivo `.env` contiene los parámetros de conexión a MinIO:

´´´
MINIO_ENDPOINT=http://localhost:9000
MINIO_ACCESS_KEY=xxxx
MINIO_SECRET_KEY=XXXX
MINIO_BUCKET=bucket01
MINIO_FILE=datosDPara.csv
´´´

> **Importante:**  
> El archivo `.env` está excluido del repositorio mediante `.gitignore` para evitar exponer credenciales.

---

## 📦 Instalación de dependencias

Crear entorno virtual (opcional pero recomendado):

```bash
python -m venv py312
source py312/bin/activate

▶️ Ejecución
Desde la raíz del proyecto:

bash
python -m prj02.main
Si la conexión es correcta, verás el contenido del CSV cargado desde MinIO.

🧠 Funcionamiento interno
config.py
Carga las variables del archivo .env y expone una clase MinioConfig con:

endpoint

access_key

secret_key

bucket

file

minio_reader.py
Crea un cliente S3 compatible con MinIO y descarga el CSV en memoria usando BytesIO.

main.py
Punto de entrada del proyecto.
Llama a read_csv_from_minio() y muestra el DataFrame resultante.