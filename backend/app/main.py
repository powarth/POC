# app/main.py
from fastapi import FastAPI
from app.config import settings
from app.routers import students, wishes

app = FastAPI(title="FESUP API", version="1.0")

# Import des routes
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(wishes.router, prefix="/wishes", tags=["Wishes"])

@app.get("/")
def home():
    return {"message": "Bienvenue sur l’API FESUP 2026 🎓"}

@app.get("/config")
def get_config():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "db_url": settings.database_url
    }
