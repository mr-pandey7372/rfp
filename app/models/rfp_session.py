from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime


class RFPSession(Base):
    __tablename__ = "rfp_sessions"

    rfp_id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    deadline = Column(DateTime)
    status = Column(String, default="draft")

    questions = relationship("Question", back_populates="rfp")