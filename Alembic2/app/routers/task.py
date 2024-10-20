from fastapi import APIRouter
from ..schemas import CreateTask, UpdateTask

router = APIRouter()

tasks_db = []  # Временная база данных для хранения задач

@router.post("/tasks/")
async def create_task(task: CreateTask):
    task_data = task.dict()
    task_data['id'] = len(tasks_db) + 1  # Генерация id для задачи
    tasks_db.append(task_data)
    return task_data

@router.get("/tasks/")
async def get_tasks():
    return tasks_db

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: UpdateTask):
    for t in tasks_db:
        if t['id'] == task_id:
            t.update(task.dict())
            return t
    return {"error": "Task not found"}

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    global tasks_db
    tasks_db = [t for t in tasks_db if t['id'] != task_id]
    return {"message": "Task deleted"}
