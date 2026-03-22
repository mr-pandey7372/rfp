from sqlalchemy import Column, Integer, Text, ForeignKey, JSON, String
from sqlalchemy.orm import relationship
from app.database import Base


class Draft(Base):
    __tablename__ = "drafts"

    draft_id = Column(Integer, primary_key=True, index=True)

    question_id = Column(Integer, ForeignKey("questions.question_id"))

    answer_text = Column(Text)

    sources_json = Column(JSON)

    version = Column(Integer)

    edited_by = Column(String)

    question = relationship("Question", back_populates="drafts")