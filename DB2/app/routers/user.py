from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from ..schemas import CreateUser, UpdateUser, UserResponse
from ..models.user import User
from ..models.task import Task
from ..backend.db_depends import get_db

router = APIRouter()


# Создание пользователя
@router.post("/users/", response_model=UserResponse)
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_data = User(**user.dict())
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


# Получение всех пользователей
@router.get("/users/", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# Обновление данных пользователя
@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == user_id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.dict(exclude_unset=True).items():
        setattr(user_data, key, value)

    db.commit()
    db.refresh(user_data)
    return user_data


# Удаление пользователя вместе с его задачами
@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == user_id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    # Удаление всех задач, связанных с этим пользователем
    db.query(Task).filter(Task.user_id == user_id).delete()

    # Удаление пользователя
    db.delete(user_data)
    db.commit()

    return {"status_code": status.HTTP_204_NO_CONTENT, "detail": "User and associated tasks deleted"}


# Получение всех задач пользователя по user_id
@router.get("/users/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == user_id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks
