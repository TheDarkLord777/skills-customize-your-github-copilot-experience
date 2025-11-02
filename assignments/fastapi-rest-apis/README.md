# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and build a small REST API using the FastAPI framework. You'll define request/response models, implement CRUD endpoints, validate input with Pydantic, and run the app locally with uvicorn.

## 📝 Tasks

### 🛠️ Build the API Core

#### Description
Create a small REST API for managing a simple resource (for example, "items"). Implement endpoints to create, read (single + list), update, and delete items. Use Pydantic models for input validation and typed responses.

#### Requirements
Completed project should:

- Include a minimal FastAPI app (example entry: `starter-code.py`) with these endpoints:
  - `GET /items/` — return list of items
  - `GET /items/{id}` — return a single item or 404
  - `POST /items/` — create an item (validate body)
  - `PUT /items/{id}` or `PATCH /items/{id}` — update an item
  - `DELETE /items/{id}` — remove an item
- Use Pydantic models for request and response bodies.
- Validate input and return appropriate HTTP status codes (201 on create, 404 when not found, 400 on validation errors, etc.).
- Keep an in-memory data store (list/dict) for simplicity — persistence is optional.
- Include clear README usage instructions showing how to run the server and call the endpoints (curl or HTTPie examples).

Example flow (HTTP):

```
POST /items/  {"name":"Notebook","description":"A small notebook"}  -> 201 Created
GET /items/  -> [{"id":1,"name":"Notebook","description":"A small notebook"}]
GET /items/1 -> {"id":1,"name":"Notebook","description":"A small notebook"}
```

### 🛠️ Add Enhancements (Optional)

#### Description
Extend the API with practical improvements and document them in this README.

#### Requirements (if implemented)

- Add query parameters for filtering/listing (e.g., ?limit=10, ?q=search).
- Implement basic error handling middleware or custom exception handlers.
- Split app into modules (routers, models, main) and add a simple automated test (pytest) for one endpoint.
- Add OpenAPI examples or use FastAPI's automatic docs (`/docs`) to demonstrate the API.

## 📝 Starter Code / How to run

This folder includes a minimal starter FastAPI app in `starter-code.py` and a `requirements.txt`.

To run locally (recommended with a virtual environment):

```bash
python3 -m pip install -r requirements.txt
uvicorn starter-code:app --reload
```

Then open http://127.0.0.1:8000/docs to explore the API using the automatic Swagger UI.

---

If you implement any optional enhancements, document what you changed and why in this README.
