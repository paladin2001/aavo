"""흐름 제어: 사용자 입력 분석 후 타 agent 호출 또는 종료."""
import logging

logger = logging.getLogger(__name__)


def run(user_message: str) -> str:
    """
    사용자 메시지를 받아 main agent가 처리한 결과 텍스트를 반환.
    (최소 구동: 입력 그대로 확인 응답)
    """
    if not (user_message or user_message.strip()):
        return "메시지가 비어 있습니다. 요청 내용을 입력해 주세요."
    logger.info("main_agent run: %s", user_message[:100])
    return f"[main_agent] 요청을 받았습니다: {user_message.strip()}"
