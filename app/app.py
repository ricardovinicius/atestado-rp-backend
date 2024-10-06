from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from app.database import create_db_and_tables, engine, get_session
from app.models import Feedback, Question, User
from app.schemas import FeedbackCreateSchema, UserPublicSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    
app = FastAPI(lifespan=lifespan)    

@app.get("/user",  response_model = UserPublicSchema)
async def get_user(*, session: Session = Depends(get_session), username: str): 
    user = session.exec(select(User).where(User.name == username)).first()
    
    if user is None:
        user = User(name=username)
        session.add(user)
        session.commit()
        session.refresh(user)
    
    return user

@app.post("/feedback")
async def add_feedback(*, session: Session = Depends(get_session), feedback: FeedbackCreateSchema):
    user = session.exec(select(User).where(User.id == feedback.user_id)).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail=f"User id:{feedback.user_id} not found")
    
    user.feedback = Feedback(questions=[Question(question_text=q.question_text, value=q.value) for q in feedback.questions])
    
    session.commit()
    session.refresh(user)
    
