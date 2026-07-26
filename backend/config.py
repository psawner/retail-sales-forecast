import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)

MODEL_ACCURACY = float(os.getenv("MODEL_ACCURACY", "92.13"))
USE_S3 = os.getenv("USE_S3", "False") == "True"
