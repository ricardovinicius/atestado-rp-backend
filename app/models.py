from sqlmodel import Field, Relationship, SQLModel
    
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    name: str
    feedback: "Feedback" = Relationship(back_populates="user")
    
class Feedback(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    user_id: int = Field(foreign_key="user.id", nullable=False)
    user: User = Relationship(back_populates="feedback")
    
    questions: list["Question"] = Relationship(back_populates="feedback")

class Question(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    question_text: str
    value: int = Field(ge=1, le=5)
    
    feedback_id: int = Field(foreign_key="feedback.id", nullable=False)
    feedback: Feedback = Relationship(back_populates="questions")

    
    
