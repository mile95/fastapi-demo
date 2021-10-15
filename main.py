from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI()

# Fake DB
users = {}


@app.get("/user", response_model=User)
def get_user(username: str):
    if username not in users:
        raise HTTPException(status_code=404, detail=f'{username} does not exist')
    return {"username": username, "email": users[username]}


@app.get("/users")
def get_all_users():
    return users


@app.delete("/user")
def delete_user(username: str):
    if username not in users:
        raise HTTPException(status_code=404, detail=f'{username} does not exist')
    del users[username]
    return f"{username} deleted"


@app.put("/user")
def add_new_user(user: User):
    if user.username in users:
        raise HTTPException(status_code=409, detail=f'{user.username} already exist')
    users[user.username] = user.email
    return {"username": user.username, "email": user.email}
