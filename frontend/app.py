"""Streamlit 진입점: 사이드바(대화 목록) + 중앙(대화창 + 입력)."""
import uuid
import streamlit as st
import httpx

from config import API_CHAT, API_HEALTH
from components.sidebar import render_sidebar
from components.chat import render_chat
from components.input_form import render_input_form


def ensure_session_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "conversations" not in st.session_state:
        st.session_state["conversations"] = []
    if "current_conversation_id" not in st.session_state:
        st.session_state["current_conversation_id"] = None


def send_message(user_message: str) -> str:
    """백엔드 /api/chat 호출 후 응답 텍스트 반환."""
    try:
        with httpx.Client(timeout=30.0) as client:
            r = client.post(
                API_CHAT,
                json={
                    "message": user_message,
                    "conversation_id": st.session_state.get("current_conversation_id"),
                },
            )
            r.raise_for_status()
            data = r.json()
            return data.get("reply", ""), data.get("conversation_id")
    except httpx.ConnectError:
        return "백엔드에 연결할 수 없습니다. backend를 먼저 실행해 주세요 (uvicorn app.main:app --port 8000).", None
    except Exception as e:
        return f"오류: {e}", None


def on_user_submit(user_message: str):
    """사용자 전송 시: 메시지 추가 → API 호출 → 응답 추가 → 대화 목록 갱신."""
    ensure_session_state()
    cid = st.session_state.get("current_conversation_id")
    if not cid:
        cid = str(uuid.uuid4())
        st.session_state["current_conversation_id"] = cid

    st.session_state["messages"].append({"role": "user", "content": user_message})
    reply, new_cid = send_message(user_message)
    if new_cid:
        st.session_state["current_conversation_id"] = new_cid
    st.session_state["messages"].append({"role": "assistant", "content": reply})

    # 대화 목록에 현재 대화 추가/갱신
    convs = st.session_state["conversations"]
    existing = next((c for c in convs if c.get("id") == cid), None)
    title = (user_message[:50] + "…") if len(user_message) > 50 else user_message
    entry = {"id": cid, "title": title or "새 대화", "messages": list(st.session_state["messages"])}
    if existing:
        for i, c in enumerate(convs):
            if c.get("id") == cid:
                convs[i] = entry
                break
    else:
        convs.append(entry)
    st.rerun()


def main():
    st.set_page_config(page_title="aavo", layout="wide")
    ensure_session_state()

    render_sidebar()

    col1, col2 = st.columns([1, 4])
    with col2:
        st.header("대화")
        render_chat()
        render_input_form(on_user_submit)


if __name__ == "__main__":
    main()
