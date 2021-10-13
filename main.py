from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI()

# Fake DB
users = {}


@app.get("/")
def read_root():
    return {"Hello": "Devies"}


@app.get("/user")
def get_user(username) -> User:
    return {"user": username, "email": users[username]}


@app.get("/users")
def get_all_users():
    return users


@app.delete("/user")
def delete_user(username):
    del users[username]
    return f"{username} deleted"


@app.put("/user")
def add_new_user(username, email):
    users[username] = email
    return {"username": username, "email": email}
