# aavo 프로젝트 전체 폴더/파일 구조

> 아파트 실거래가·매물 분석 AI 서비스 — 전체 scope 설계 (부분 개발용 참조)

---

## 루트

```
aavo/
├── .env.example
├── .gitignore
├── README.md
├── STRUCTURE.md                 # 이 문서
├── requirements.txt             # 루트 공통 의존성 (선택)
├── logs/                        # 시간단위 로그 적재 (실행 시 생성)
├── data/                        # 정적·캐시 데이터 (공시 파일, 뉴스 캐시 등)
├── backend/                     # FastAPI 백엔드
├── frontend/                    # Streamlit UI
├── shared/                      # 백엔드·프론트 공통 스키마/상수 (선택)
└── tests/                       # 통합/단위 테스트
```

---

## backend/ (FastAPI)

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI 앱 진입점, 라우터 등록
│   ├── config.py                # 설정 (env, DB URL, 로그 경로 등)
│   ├── logging_config.py        # 시간단위 로그 설정 (logs/ 폴더)
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── chat.py          # 사용자 요청 접수 → main agent 호출
│   │       ├── health.py        # 헬스체크
│   │       ├── conversations.py # 대화 목록/조회 (사이드바용)
│   │       └── ...
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── main_agent.py        # 흐름 제어: 입력 분석 → 타 agent 호출/종료
│   │   ├── realestate_save_agent.py   # 실거래가 수집 → RDB 저장
│   │   ├── realestate_load_agent.py   # RDB → pandas 등 제공
│   │   ├── policy_agent.py      # 부동산 정책 공시 데이터 수집
│   │   ├── news_agent.py        # 부동산/지역 뉴스·사고 뉴스 수집
│   │   ├── calculate_agent.py   # 환산지수, 보정계수, 대표가격, 가격적정성
│   │   └── tools/               # Agent용 도구 (MCP, Langchain tools)
│   │       ├── __init__.py
│   │       ├── mcp_tools.py
│   │       └── ...
│   │
│   ├── services/                # 비즈니스 로직 (Agent와 분리)
│   │   ├── __init__.py
│   │   ├── realestate_service.py
│   │   ├── policy_service.py
│   │   ├── news_service.py
│   │   └── calculate_service.py
│   │
│   ├── models/                  # Pydantic·도메인 모델
│   │   ├── __init__.py
│   │   ├── request.py
│   │   ├── response.py
│   │   └── domain/
│   │       ├── realestate.py
│   │       ├── policy.py
│   │       └── ...
│   │
│   ├── db/                      # PostgreSQL
│   │   ├── __init__.py
│   │   ├── connection.py        # 세션/엔진
│   │   ├── models.py            # SQLAlchemy ORM (실거래가, 대화 등)
│   │   ├── migrations/          # Alembic 마이그레이션 (선택)
│   │   └── repositories/
│   │       ├── __init__.py
│   │       ├── realestate_repo.py
│   │       ├── conversation_repo.py
│   │       └── ...
│   │
│   └── rag/                     # RAG (벡터 저장소, 검색)
│       ├── __init__.py
│       ├── vector_store.py
│       ├── retriever.py
│       └── ...
│
├── requirements.txt
└── ...
```

---

## frontend/ (Streamlit)

```
frontend/
├── app.py                       # Streamlit 진입점 (사이드바 + 중앙 대화)
├── config.py                    # API URL 등 프론트 설정
├── requirements.txt
│
├── components/
│   ├── __init__.py
│   ├── sidebar.py               # 사이드바: 지난 대화 목록, 선택 시 조회
│   ├── chat.py                  # 중앙 대화창 (메시지 표시)
│   └── input_form.py            # 사용자 텍스트 입력 → request 접수
│
├── pages/                       # Streamlit 멀티페이지 (필요 시)
│   └── ...
│
└── ...
```

---

## data/

```
data/
├── policy/                      # 부동산 정책 공시 파일 캐시
├── news_cache/                  # 뉴스 캐시 (선택)
└── ...
```

---

## shared/ (선택)

```
shared/
├── __init__.py
├── schemas.py                   # 요청/응답 스키마 공통
└── constants.py
```

---

## tests/

```
tests/
├── __init__.py
├── conftest.py                  # pytest 픽스처, 테스트 DB 등
├── unit/
│   ├── test_main_agent.py
│   ├── test_realestate_save_agent.py
│   └── ...
└── integration/
    ├── test_chat_api.py
    └── ...
```

---

## logs/

- 실행 시 생성. **시간단위** 로그 파일 적재 (예: `aavo_2025-02-11_14.log`).
- `backend/app/logging_config.py`에서 경로·포맷 설정.

---

## 요약

| 구역        | 역할 |
|------------|------|
| `backend/` | FastAPI, Main/Realestate/Policy/News/Calculate Agent, DB, RAG, API 라우트 |
| `frontend/`| Streamlit: 사이드바(대화 목록) + 중앙(대화창 + 입력) |
| `data/`    | 공시·뉴스 등 캐시 데이터 |
| `logs/`    | 시간단위 로그 파일 |
| `tests/`   | 단위/통합 테스트 |

**원칙:** Single Response — 파일/모듈별 기능 분리.  
**실행:** Local 기준 (PostgreSQL 로컬, FastAPI + Streamlit 각각 실행).

이 구조를 기준으로 부분별로 나누어 개발하면 됩니다.
