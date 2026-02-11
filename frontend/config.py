"""프론트엔드 설정 (API URL 등)."""
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
API_CHAT = f"{BACKEND_URL}/api/chat"
API_HEALTH = f"{BACKEND_URL}/api/health"
API_CONVERSATIONS = f"{BACKEND_URL}/api/conversations"
