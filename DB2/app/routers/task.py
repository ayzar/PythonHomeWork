from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from ..backend.db_depends import get_db
from ..models.task import Task
from ..models.user import User
from ..schemas import CreateTask, UpdateTask, TaskResponse

router = APIRouter()

# Маршрут для создания задачи
@router.post("/tasks/")
async def create_task(task: CreateTask, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == task.user_id).first()  # Используем task.user_id
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    new_task = Task(
        title=task.title,
        content=task.content,
        priority=task.priority,
        completed=task.completed,
        user_id=task.user_id  # Связываем задачу с пользователем
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Маршрут для получения всех задач
@router.get("/tasks/", response_model=list[TaskResponse])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

# Маршрут для обновления задачи
@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: UpdateTask, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")

    existing_task.title = task.title
    existing_task.content = task.content
    existing_task.priority = task.priority
    existing_task.completed = task.completed

    db.commit()
    db.refresh(existing_task)
    return existing_task

# Маршрут для удаления задачи
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "message": "Task deleted successfully"}
