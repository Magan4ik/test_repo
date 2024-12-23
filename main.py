from fastapi import FastAPI
from db import schemas

app = FastAPI()

users = [
    schemas.User(id=0, username="MMM", email="example1@gmail.com"),
    schemas.User(id=1, username="YYY", email="example2@gmail.com"),
    schemas.User(id=2, username="GGG", email="example3@gmail.com"),
]


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return "Not found"


if __name__ == "__main__":
    import os
    os.system("uvicorn main:app --reload")
