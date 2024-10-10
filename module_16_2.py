from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Валидация для user_id
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, example=1)]
):
    return f"Вы вошли как пользователь № {user_id}"

# Валидация для username и age
@app.get("/user/{username}/{age}")
def get_user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, example=24)]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
