from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
from fastapi.params import Path

app = FastAPI()

# Пустой список для хранения пользователей
users: List['User'] = []

# Модель пользователя с валидацией
class User(BaseModel):
    id: int
    username: str
    age: int

# GET запрос: возвращаем список всех пользователей
@app.get("/users", response_model=List[User])
async def get_users():
    return users

# POST запрос: добавляем нового пользователя с валидацией возраста
@app.post("/user/{username}/{age}", response_model=User)
async def add_user(
    username: str, 
    age: Annotated[int, Path(ge=18, le=90, description="Возраст должен быть от 18 до 90")]
):
    user_id = len(users) + 1  # ID для нового пользователя
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)  # Добавляем пользователя в список
    return new_user

# PUT запрос: обновляем данные пользователя с валидацией возраста
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: int, 
    username: str, 
    age: Annotated[int, Path(ge=18, le=90, description="Возраст должен быть от 18 до 90")]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос: удаляем пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
