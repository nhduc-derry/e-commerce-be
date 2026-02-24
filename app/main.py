from fastapi import FastAPI, Depends
from app.core.config import settings

from sqlalchemy.orm import Session
from sqlalchemy import text, inspect
from app.db.database import get_db

app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def root():
    return {
        "message" : "E-commerce backend running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }