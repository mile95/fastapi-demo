from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    username: str
    email: str
