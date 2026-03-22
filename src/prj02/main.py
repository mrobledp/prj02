from prj02.minio_reader import read_csv_from_minio

def main():
    df = read_csv_from_minio()
    print("Contenido del CSV:")
    print(df)

if __name__ == "__main__":
    main()
