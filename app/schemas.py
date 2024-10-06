from pydantic import BaseModel, Field    

class UserPublicSchema(BaseModel):
    id: int
    name: str
    feedback: "FeedbackPublicSchema | None"
    
class QuestionPublicSchema(BaseModel):
    id: int
    question_name: str
    value: int

class FeedbackPublicSchema(BaseModel):
    id: int
    user_id: int
    questions: list[QuestionPublicSchema]
    
class QuestionCreateSchema(BaseModel):
    question_text: str
    value: int = Field(ge=1, le=5)

class AddQuestionsSchema(BaseModel):
    user_id: int
    questions: list[QuestionCreateSchema]
    
class FeedbackCreateSchema(BaseModel):
    user_id: int
    questions: list[QuestionCreateSchema]


