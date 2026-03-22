from pydantic import BaseModel
from datetime import datetime


class RFPSessionCreate(BaseModel):
    client_name: str
    deadline: datetime


class QuestionCreate(BaseModel):
    text: str
    rfp_id: int


class DraftCreate(BaseModel):
    question_id: int
    answer_text: str
    version: int