from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


from app.database import SessionLocal
from app.schemas.rfp_schema import RFPSessionCreate
from app.services.rfp_service import create_rfp


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/rfp")
def create_rfp_api(data: RFPSessionCreate, db: Session = Depends(get_db)):


    return create_rfp(
        db,
        client_name=data.client_name,
        deadline=data.deadline
    )

# QUESTION
from app.schemas.rfp_schema import QuestionCreate
from app.services.rfp_service import create_question

@app.post("/question")
def add_question(data: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, data.text, data.rfp_id)


# DRAFT 
from app.schemas.rfp_schema import DraftCreate
from app.services.rfp_service import create_draft

@app.post("/draft")
def add_draft(data: DraftCreate, db: Session = Depends(get_db)):
    return create_draft(
        db,
        data.question_id,
        data.answer_text,
        data.version
    )