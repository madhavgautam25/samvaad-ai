from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.core.config import settings
from app.database.database import Base, engine

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A multilingual AI voice agent."
)
Base.metadata.create_all(bind=engine)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "model": settings.MODEL_NAME,
        "provider": settings.MODEL_PROVIDER
    }