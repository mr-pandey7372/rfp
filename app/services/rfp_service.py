from sqlalchemy.orm import Session
from app.models import RFPSession, Question, Draft


def create_rfp(db: Session, client_name, deadline):

    rfp = RFPSession(
        client_name=client_name,
        deadline=deadline
    )

    db.add(rfp)
    db.commit()
    db.refresh(rfp)

    return rfp


def create_question(db, text, rfp_id):

    question = Question(
        text=text,
        rfp_id=rfp_id
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return question


def create_draft(db, question_id, answer_text, version):

    draft = Draft(
        question_id=question_id,
        answer_text=answer_text,
        version=version
    )

    db.add(draft)
    db.commit()
    db.refresh(draft)

    return draft