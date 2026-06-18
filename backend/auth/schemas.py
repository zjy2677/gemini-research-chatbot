from pydantic import BaseModel


class RegisterRequest(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    age: int
    gender: str
    email: str


class LoginRequest(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str


class LoginResponse(BaseModel):
    user: UserResponse
