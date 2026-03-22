import boto3
import pandas as pd
from io import BytesIO
from botocore.client import Config
from prj02.config import MinioConfig

def read_csv_from_minio():
    s3 = boto3.client(
        "s3",
        endpoint_url=MinioConfig.endpoint,
        aws_access_key_id=MinioConfig.access_key,
        aws_secret_access_key=MinioConfig.secret_key,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )

    obj = s3.get_object(Bucket=MinioConfig.bucket, Key=MinioConfig.file)
    data = obj["Body"].read()

    df = pd.read_csv(BytesIO(data))
    return df
