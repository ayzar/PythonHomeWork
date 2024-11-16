from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
from fastapi import FastAPI
from app.routers import user, task  # подключаем маршруты для пользователей и задач
from app.backend.db import engine
from app.models import User, Task  # Импортируем модели

app = FastAPI()

# Подключаем маршруты
app.include_router(user.router)
app.include_router(task.router)

# Создаем таблицы в базе данных при запуске приложения
User.metadata.create_all(bind=engine)
Task.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
