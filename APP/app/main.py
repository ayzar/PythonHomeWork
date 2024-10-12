import sys
import os
from fastapi import FastAPI
from sqlalchemy.schema import CreateTable
from app.models.user import User
from app.models.task import Task
from .routers import task, user

# Добавляем путь к папке backend в sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from app.backend.db import engine, Base


# Вывод SQL-запросов для создания таблиц
print(str(CreateTable(User.__table__)))
print(str(CreateTable(Task.__table__)))

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
