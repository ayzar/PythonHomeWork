from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from slugify import slugify  # Импортируем slugify
from ..backend.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True, nullable=True)  # slug может быть пустым

    # Связь с задачами
    tasks = relationship('Task', back_populates='user')

    # Конфигурация для Pydantic моделей
    class Config:
        orm_mode = True

    # Конструктор для генерации slug
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Генерация slug, если он не был задан
        if not self.slug and hasattr(self, 'username'):
            self.slug = slugify(self.username)
