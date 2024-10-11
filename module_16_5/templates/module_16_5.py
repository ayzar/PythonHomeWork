from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.params import Path

app = FastAPI()

# Папка для шаблонов
templates = Jinja2Templates(directory="templates")

# Пустой список пользователей
users: List['User'] = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Маршрут для отображения всех пользователей через шаблон
@app.get("/", response_class=HTMLResponse)
async def show_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# POST запрос: добавляем нового пользователя с валидацией возраста (от 18 до 90 лет)
@app.post("/user/{username}/{age}", response_class=HTMLResponse)
async def add_user(
    request: Request,
    username: str,
    age: Annotated[int, Path(ge=18, le=90, description="Возраст должен быть от 18 до 90")]
):
    user_id = len(users) + 1  # ID для нового пользователя
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)  # Добавляем пользователя в список
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# GET запрос: возвращаем одного пользователя по user_id
@app.get("/users/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")

# PUT запрос: обновляем данные пользователя
@app.put("/user/{user_id}/{username}/{age}", response_class=HTMLResponse)
async def update_user(
    request: Request,
    user_id: int,
    username: str,
    age: Annotated[int, Path(ge=18, le=90, description="Возраст должен быть от 18 до 90")]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return templates.TemplateResponse("users.html", {"request": request, "users": users})
    raise HTTPException(status_code=404, detail="User not found")

# DELETE запрос: удаляем пользователя
@app.delete("/user/{user_id}", response_class=HTMLResponse)
async def delete_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return templates.TemplateResponse("users.html", {"request": request, "users": users})
    raise HTTPException(status_code=404, detail="User not found")
