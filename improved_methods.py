from pydantic.networks import EmailStr


@app.put("/user", response_model=User)
def add_new_user(user: User) -> str:
    if user.username in users:
        raise HTTPException(status_code=409, detail=f"{user.username} already exists!")
    users[user.username] = user.email
    return {"username": user.username, "email": user.email}


@app.get("/user", response_model=User)
def get_user(username: str):
    if username not in users:
        raise HTTPException(status_code=404, detail=f"{username} does not exits")
    return {"user": username, "email": users[username]}


@app.delete("/user")
def delete_user(username):
    if username not in users:
        raise HTTPException(status_code=404, detail=f"{username} does not exists!")
    del users[username]
    return f"{username} deleted!"


class User(BaseModel):
    username: constr(max_length=8)
    email: EmailStr
