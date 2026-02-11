"""시간단위 로그 설정. logs/ 폴더에 aavo_YYYY-MM-DD_HH.log 형식으로 적재."""
import logging
import sys
from datetime import datetime
from pathlib import Path

from app.config import LOG_DIR


def _log_file_path() -> Path:
    now = datetime.now()
    name = f"aavo_{now.strftime('%Y-%m-%d_%H')}.log"
    return LOG_DIR / name


def setup_logging(level: int = logging.INFO) -> None:
    """로그 디렉터리 및 시간단위 파일 핸들러 설정."""
    log_path = _log_file_path()
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
