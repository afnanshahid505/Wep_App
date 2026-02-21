from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from database import engine, SessionLocal
from models import Base, User, Task
from schemas import UserCreate, UserResponse,UserLogin, TaskResponse, TaskCreate
from auth import hash_password,verify_password,create_access_token,decode_access_token

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Frontend Intern Assignment API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    payload = decode_access_token(token)
    user_id = payload.get("user_id")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user        
@app.get("/")
def home():
    return "Home page"        

@app.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    
    # 1️⃣ Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # 2️⃣ Check if username already exists
    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )

    # 3️⃣ Hash the password
    hashed_pwd = hash_password(user.password)

    # 4️⃣ Create user object
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pwd
    )

    # 5️⃣ Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 6️⃣ Return safe response
    return new_user
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    
    # 1️⃣ Check if user exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    # 2️⃣ Verify password
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    # 3️⃣ Create JWT token
    access_token = create_access_token(
        data={"user_id": db_user.id}
    )

    # 4️⃣ Return token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
@app.get("/me", response_model=UserResponse)
def read_profile(current_user: User = Depends(get_current_user)):
    return current_user
@app.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Task).filter(Task.owner_id == current_user.id).all()
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    return db_task
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}