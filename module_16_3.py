from fastapi import FastAPI, HTTPException
from typing import Annotated
from fastapi.params import Path

app = FastAPI()

# Изначальный словарь с пользователями
users = {
    '1': 'Имя: Example, возраст: 18'
}

# Асинхронный GET запрос, возвращающий всех пользователей
@app.get('/users')
async def get_users():
    return users

# Асинхронный POST запрос, добавляющий нового пользователя с валидацией возраста от 18 до 90
@app.post('/user/{username}/{age}')
async def add_user(
    username: str, 
    age: Annotated[int, Path(ge=18, le=90, description="Возраст должен быть от 18 до 90")]
):
    new_user_id = str(max(map(int, users.keys())) + 1)  # Определение нового ключа
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

# Асинхронный PUT запрос, обновляющий данные о пользователе с валидацией возраста от 18 до 90
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: str,
    username: str,
    age: Annotated[int, Path(ge=18, le=90, description="Возраст должен быть от 18 до 90")]
):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Асинхронный DELETE запрос, удаляющий пользователя по его ID
@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="User not found")
