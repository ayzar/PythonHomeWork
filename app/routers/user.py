from fastapi import APIRouter
from ..schemas import CreateUser, UpdateUser

router = APIRouter()

users_db = []  # Временная база данных для хранения пользователей

@router.post("/users/")
async def create_user(user: CreateUser):
    user_data = user.dict()
    user_data['id'] = len(users_db) + 1  # Генерация id для пользователя
    users_db.append(user_data)
    return user_data

@router.get("/users/")
async def get_users():
    return users_db

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: UpdateUser):
    for u in users_db:
        if u['id'] == user_id:
            u.update(user.dict())
            return u
    return {"error": "User not found"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    global users_db
    users_db = [u for u in users_db if u['id'] != user_id]
    return {"message": "User deleted"}
