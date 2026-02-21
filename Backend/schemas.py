from pydantic import BaseModel, EmailStr

# Data coming FROM frontend
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Data going TO frontend
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
class UserLogin(BaseModel):
    email: EmailStr
    password: str 
class TaskCreate(BaseModel):
    title: str
    description: str      
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str     

    class Config:
        from_attributes = True