from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_main():
    return "Главная страница"

@app.get("/user/admin")
def read_admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
def read_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
def get_user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
