import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI app")
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres.wglzmgazisgtmifdhxpo:Abcd168%2A%2A%2Aa@aws-1-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_ME_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

settings = Settings()
