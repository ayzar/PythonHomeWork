from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..backend.db_depends import get_db
from typing import Annotated
from ..models.user import User
from ..schemas import CreateUser, UpdateUser, UserResponse
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from typing import List

router = APIRouter()


# Функция для получения всех пользователей
@router.get("/users", response_model=List[UserResponse])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User)).scalars().all()
    return result


# Функция для получения пользователя по ID
@router.get("/users/{user_id}", response_model=UserResponse)
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    return user


# Функция для создания пользователя
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    user_data = user.dict()
    user_data['slug'] = slugify(user_data['username'])
    stmt = insert(User).values(**user_data)
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Функция для обновления пользователя
@router.put("/update/{user_id}")
async def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    user_db = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    stmt = update(User).where(User.id == user_id).values(**user.dict())
    db.execute(stmt)
    db.commit()

    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


# Функция для удаления пользователя
@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user_db = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    stmt = delete(User).where(User.id == user_id)
    db.execute(stmt)
    db.commit()

    return {"status_code": status.HTTP_200_OK, "transaction": "User deleted successfully"}
