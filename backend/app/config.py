"""설정 (env, 로그 경로 등)."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# 프로젝트 루트: backend 상위
PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = Path(os.getenv("LOG_DIR", "logs"))
if not LOG_DIR.is_absolute():
    LOG_DIR = PROJECT_ROOT / LOG_DIR
LOG_DIR.mkdir(parents=True, exist_ok=True)

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
