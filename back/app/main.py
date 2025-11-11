from fastapi import FastAPI
from app.core.database import init_db
from app.routers import auth

app = FastAPI(title="BudgetBuddy API")

app.include_router(auth.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {"message": "BudgetBuddy backend running!"}
