from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    username: str
    email: str
    password: str | None = None

    class Config:
        orm_mode = True
