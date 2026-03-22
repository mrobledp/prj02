from prj02.minio_reader import read_csv_from_minio
from prj02.logger import logger

def main():
    logger.debug("Inicio de ejecución de prj02")
    df = read_csv_from_minio()
    print(df)
    logger.debug("Ejecución finalizada correctamente")

if __name__ == "__main__":
    main()
