from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Устанавливаем URL для SQLite базы данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskmanager.db"

# Создаем движок базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()


