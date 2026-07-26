import pandas as pd
import boto3
from backend.config import USE_S3

BUCKET = "retail_forecast"

def load_csv(file_name):

    if USE_S3:

        s3 = boto3.client("s3")

        obj = s3.get_object(
            Bucket=BUCKET,
            Key=file_name
        )

        return pd.read_csv(obj["Body"])

    else:

        return pd.read_csv(
            f"{file_name}"
        )