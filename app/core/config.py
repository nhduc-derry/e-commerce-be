import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI app")
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres.wglzmgazisgtmifdhxpo:Abcd168%2A%2A%2Aa@aws-1-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require")

settings = Settings()
