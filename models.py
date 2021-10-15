from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    username: constr(max_length=8)
    email: EmailStr
