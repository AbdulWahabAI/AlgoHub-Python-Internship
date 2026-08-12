from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="AlgoHub Task Management API",
    description="A professional REST API built with FastAPI for managing daily tasks.",
    version="1.0.0"
)

# Task ke liye Pydantic Model (Data validation ke liye)
class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=3, max_length=100, description="Title of the task")
    description: Optional[str] = Field(None, max_length=300, description="Detailed description of the task")
    completed: bool = Field(default=False, description="Status of the task")

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    completed: Optional[bool] = False

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    completed: Optional[bool] = None

# Temporary In-Memory Database (List)
fake_db: List[Task] = [
    Task(id=1, title="Learn FastAPI", description="Complete the FastAPI documentation and build a project.", completed=False),
    Task(id=2, title="Submit Internship Task", description="Push the code to GitHub and record a demo video.", completed=True)
]

# 1. Root Endpoint
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the AlgoHub Task Management API! Go to /docs for Swagger UI."}

# 2. Get All Tasks
@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def get_all_tasks():
    return fake_db

# 3. Get Task by ID
@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task_by_id(task_id: int):
    for task in fake_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {task_id} not found.")

# 4. Create a New Task
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task_data: TaskCreate):
    new_id = max([t.id for t in fake_db], default=0) + 1
    new_task = Task(
        id=new_id,
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed
    )
    fake_db.append(new_task)
    return new_task

# 5. Update an Existing Task
@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, task_data: TaskUpdate):
    for task in fake_db:
        if task.id == task_id:
            if task_data.title is not None:
                task.title = task_data.title
            if task_data.description is not None:
                task.description = task_data.description
            if task_data.completed is not None:
                task.completed = task_data.completed
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {task_id} not found.")

# 6. Delete a Task
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int):
    for index, task in enumerate(fake_db):
        if task.id == task_id:
            fake_db.pop(index)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {task_id} not found.")