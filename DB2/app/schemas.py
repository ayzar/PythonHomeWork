from pydantic import BaseModel
from typing import Optional

# Схема для создания пользователя
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

# Схема для обновления пользователя
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

# Схема для вывода пользователя с поддержкой ORM
class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str

    class Config:
        orm_mode = True  # Исправлено на orm_mode, который поддерживает SQLAlchemy

# Схема для создания новой задачи
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
    completed: bool = False  # По умолчанию задача не завершена
    user_id: int  # Связь с пользователем


# Схема для обновления задачи с необязательными полями
class UpdateTask(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None  # Поле для обновления статуса выполнения

# Схема для возврата задачи с поддержкой ORM
class TaskResponse(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    completed: bool
    user_id: int

    class Config:
        orm_mode = True  # Включаем поддержку ORM для схемы ответа задачи
