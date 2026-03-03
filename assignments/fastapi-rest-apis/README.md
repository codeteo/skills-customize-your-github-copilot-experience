# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI. You will practice defining endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI app and implement basic endpoints to verify your API is running and can return data.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Implement a `GET /` endpoint that returns a welcome JSON message.
- Implement a `GET /status` endpoint that returns `{"status": "ok"}`.
- Run locally with Uvicorn and confirm both endpoints respond successfully.

### 🛠️ Build a Task Resource

#### Description
Add a simple in-memory task manager API so users can create and list tasks.

#### Requirements
Completed program should:

- Define a Pydantic model for task input with `title` and optional `completed` fields.
- Implement `POST /tasks` to add a new task.
- Implement `GET /tasks` to return all created tasks.
- Return JSON responses with clear keys and values.

### 🛠️ Add Validation and Error Handling

#### Description
Improve API reliability by validating input and handling common errors.

#### Requirements
Completed program should:

- Reject empty task titles.
- Implement `GET /tasks/{task_id}` to fetch a single task by index.
- Return an appropriate error message when a task is not found.
- Include one short example request/response in a code block.

```text
Request: POST /tasks
Body: {"title": "Finish FastAPI homework"}

Response: 201 Created
{"id": 0, "title": "Finish FastAPI homework", "completed": false}
```
