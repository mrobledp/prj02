from prj02.minio_client import MinioClient
from prj02.logger import logger

def main():
    logger.debug("Inicio de ejecución de prj02")

    client = MinioClient()
    df = client.read_csv()

    print(df)
    logger.debug("Ejecución finalizada correctamente")

if __name__ == "__main__":
    main()

