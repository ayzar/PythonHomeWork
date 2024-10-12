from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///taskmanager.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # echo=True для вывода SQL-запросов в консоль
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
