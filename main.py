from uuid import UUID
from fastapi import FastAPI, HTTPException     # type: ignore
from typing import List
from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()  # Creating instance of the application

# In-memory database with some sample users
db: List[User] = [
    User(id=UUID("3c1ee9e4-b3bd-4133-b379-4eb972c96583"),
         first_name="James",
         last_name="Cameron",
         gender=Gender.male,
         roles=[Role.student]
         ),
    User(id=UUID("3d887719-86a7-449f-8441-6d98d24e50a9"),
         first_name="Cynthia",
         last_name="Rogers",
         gender=Gender.female,
         roles=[Role.student]
         )
]

@app.get("/")  # route for get request and the "/" is the root
async def root():
    return {'Hello': 'World'}

@app.get("/api/v1/users") # Fetch all users
async def fetch_users():
    return db;

@app.post("/api/v1/users") # Register new users
async def register_user(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/{user_id}") # Delete a user by ID
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/api/v1/users/{user_id}") # Update an existing user by ID
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code = 404,
        details = f"User with id {user_id} does not exists"
    )