from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    username: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
