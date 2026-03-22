import boto3
import pandas as pd
from io import BytesIO
from botocore.client import Config
from botocore.exceptions import ClientError
from prj02.config import MinioConfig
from prj02.logger import logger


class MinioClient:
    def __init__(self):
        logger.debug("Inicializando MinioClient")

        self.s3 = boto3.client(
            "s3",
            endpoint_url=MinioConfig.endpoint,
            aws_access_key_id=MinioConfig.access_key,
            aws_secret_access_key=MinioConfig.secret_key,
            config=Config(signature_version="s3v4"),
            region_name="us-east-1",
        )

        logger.debug(
            f"Cliente MinIO configurado: endpoint={MinioConfig.endpoint}, "
            f"bucket={MinioConfig.bucket}"
        )

    def read_csv(self, bucket=None, key=None):
        bucket = bucket or MinioConfig.bucket
        key = key or MinioConfig.file

        logger.debug(f"Leyendo CSV desde MinIO: bucket={bucket}, key={key}")

        try:
            obj = self.s3.get_object(Bucket=bucket, Key=key)
            data = obj["Body"].read()
            df = pd.read_csv(BytesIO(data))

            logger.debug(f"CSV leído correctamente. Filas: {len(df)}")
            return df

        except ClientError as e:
            logger.error(f"Error al leer CSV desde MinIO: {e}")
            raise

    def write_csv(self, df, bucket, key):
        logger.debug(f"Escribiendo CSV en MinIO: bucket={bucket}, key={key}")

        try:
            buffer = BytesIO()
            df.to_csv(buffer, index=False)
            buffer.seek(0)

            self.s3.put_object(Bucket=bucket, Key=key, Body=buffer.getvalue())

            logger.debug("CSV escrito correctamente en MinIO")

        except ClientError as e:
            logger.error(f"Error al escribir CSV en MinIO: {e}")
            raise
