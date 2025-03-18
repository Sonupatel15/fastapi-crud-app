# FastAPI Users API

A simple CRUD API for managing users using FastAPI.

## Features

- Create, read, update, and delete users
- Search users by name
- Data validation using Pydantic models

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.


## API Endpoints

| Method | Endpoint                   | Description          |
| ------ | -------------------------- | -------------------- |
| POST   | /users/                    | Create a new user    |
| GET    | /users/{id}                | Get user by ID       |
| GET    | /users/                    | List all users       |
| GET    | /users/search/?name={name} | Search users by name |
| PUT    | /users/{id}                | Update user by ID    |
| DELETE | /users/{id}                | Delete user by ID    |

## Testing with Postman

Import the collection from the `postman` directory or create new requests to test the API endpoints.
