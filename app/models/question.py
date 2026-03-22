from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, index=True)

    text = Column(Text, nullable=False)

    rfp_id = Column(Integer, ForeignKey("rfp_sessions.rfp_id"))

    rfp = relationship("RFPSession", back_populates="questions")

    drafts = relationship("Draft", back_populates="question")