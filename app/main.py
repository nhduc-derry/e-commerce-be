from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.config import settings
from app.db.database import get_db
from app.controllers.authenController import router as auth_router
from app.controllers.userController import router as user_router


app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def root():
    return {
        "message": "E-commerce backend running",
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "ok 123",
            "database": "connected",
        }
    except Exception as e:
        return {
            "status": "error",
            "database": "failed",
            "detail": str(e),
        }


app.include_router(auth_router)
app.include_router(user_router)
