"""사이드바: 지난 대화 목록, 선택 시 해당 대화 조회."""
import streamlit as st


def render_sidebar():
    """사이드바 렌더. st.session_state.conversations 기반 목록 표시."""
    with st.sidebar:
        st.title("aavo")
        st.caption("대화 목록")
        conversations = st.session_state.get("conversations", [])
        if not conversations:
            st.info("아직 대화가 없습니다.")
            return
        for i, conv in enumerate(conversations):
            label = conv.get("title", conv.get("id", "대화"))[:40]
            if st.button(label, key=f"conv_{i}_{conv.get('id', '')}", use_container_width=True):
                st.session_state["current_conversation_id"] = conv.get("id")
                st.session_state["messages"] = conv.get("messages", [])
                st.rerun()
