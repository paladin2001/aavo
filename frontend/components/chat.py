"""중앙 대화창 (메시지 표시)."""
import streamlit as st


def render_chat():
    """st.session_state.messages 를 채팅 UI로 표시."""
    messages = st.session_state.get("messages", [])
    for msg in messages:
        with st.chat_message(msg.get("role", "user")):
            st.markdown(msg.get("content", ""))
