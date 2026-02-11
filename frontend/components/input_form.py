"""사용자 텍스트 입력 → 전송 시 request 접수 (호출측에서 API 호출)."""
import streamlit as st


def render_input_form(on_submit):
    """
    채팅 입력 폼.
    on_submit(user_message: str) 호출되면 백엔드 요청은 app.py에서 처리.
    """
    if prompt := st.chat_input("메시지를 입력하세요"):
        on_submit(prompt)
