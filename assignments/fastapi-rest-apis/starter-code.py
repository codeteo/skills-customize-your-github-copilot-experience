from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Homework Starter")


class TaskInput(BaseModel):
    title: str = Field(..., min_length=1)
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: List[Task] = []


@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome! Build your FastAPI homework API here."}


@app.get("/status")
def read_status() -> dict:
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def list_tasks() -> List[Task]:
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_input: TaskInput) -> Task:
    task = Task(id=len(tasks), **task_input.model_dump())
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


# Run locally with:
# uvicorn starter-code:app --reload
