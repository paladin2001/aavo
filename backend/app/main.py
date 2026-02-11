"""FastAPI 앱 진입점."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import API_HOST, API_PORT
from app.logging_config import setup_logging
from app.api.routes import chat, conversations, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield
    # shutdown 정리 (필요 시)


app = FastAPI(title="aavo", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(conversations.router, prefix="/api", tags=["conversations"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=API_HOST, port=API_PORT, reload=True)
