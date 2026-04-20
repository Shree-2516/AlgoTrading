python -m venv .venv
.venv\Scripts\activate  

frontend = npm run dev
backend = uvicorn app.main:app --reload