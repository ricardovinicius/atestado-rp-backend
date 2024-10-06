from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, Session, create_engine, StaticPool, select

from app.models import User

from .app import app, get_session

@pytest.fixture(name="session")  
def session_fixture():  
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session 

@pytest.fixture(name="client")  
def client_fixture(session: Session):  
    def get_session_override():  
        return session
    app.dependency_overrides[get_session] = get_session_override  
    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear()
    
def test_get_existent_user(session: Session, client: TestClient):
    existent_username = "test"
    
    user = User(name=existent_username)
    
    session.add(user)
    
    expected_response = {
        "id": 1,
        "name": "test",
        "feedback": None
    }
    
    response = client.get("/user?username=test")
    
    assert response.status_code == 200
    assert response.json() == expected_response
    
def test_get_not_existent_user(session: Session, client: TestClient):
    existent_username = "test"
    
    expected_response = {
        "id": 1,
        "name": "test",
        "feedback": None
    }
    
    response = client.get("/user?username=test")
    
    assert response.status_code == 200
    assert response.json() == expected_response
    
    created_user = session.exec(select(User).where(User.id == 1)).first()
    
    assert created_user is not None

def test_create_feedback(session: Session, client: TestClient):
    user = User(name="test")
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    request_body = {
        "user_id": user.id,
        "questions": [
            {
                "question_text": "test_question",
                "value": 5
            }
        ]
    }
    
    response = client.post("/feedback", json=request_body)
    
    assert response.status_code == 200
    
    assert user.feedback is not None
    
def test_create_feedback_with_not_existent_user(session: Session, client: TestClient):
    request_body = {
        "user_id": 1,
        "questions": [
            {
                "question_text": "test_question",
                "value": 5
            }
        ]
    }
    
    response = client.post("/feedback", json=request_body)
    
    assert response.status_code == 404
    
    
    
    