# aavo

아파트 실거래가·매물 분석 AI 서비스

## 구조

- **backend**: FastAPI (에이전트, API)
- **frontend**: Streamlit (대화 UI)

## 로컬 실행

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

백엔드가 `http://localhost:8000` 에 떠 있어야 프론트에서 채팅이 동작합니다.

### 최소 동작

- 사용자 메시지 입력 → Backend `/api/chat` → main_agent가 `[main_agent] 요청을 받았습니다: ...` 형태로 응답.
