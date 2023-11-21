from datetime import datetime

from sqlalchemy.orm import Session

from domain.answer.answer_schema import AnswerCreate, AnswerUpdate
from models import Question, Answer, User


def create_answer(db: Session, question: Question, 
                  answer_create: AnswerCreate, user:User):
    db_answer = Answer(question=question,
                       content=answer_create.content,
                       create_date=datetime.now(),
                       user=user)
    db.add(db_answer)
    db.commit()


def get_answer(db: Session, answer_id: int):
    return db.query(Answer).get(answer_id)    


def update_answer(db: Session, db_answer: Answer,
                  answer_update: AnswerUpdate):
    db_answer.content = answer_update.content
    db_answer.modify_date = datetime.now()
    db.add(db_answer)
    db.commit()


def delete_answer(db: Session, db_answer: Answer):
    db.delete(db_answer)
    db.commit()


def vote_answer(db: Session, db_answer: Answer, db_user: User):
    db_answer.voter.append(db_user)
    db_answer.voter_count = db_answer.voter_count + 1
    db.commit()


def get_answer_list(db: Session, question_id: int,
                    skip: int = 0, limit: int = 10,
                    sort_by: str = 'create_date',
                    desc: bool = True,
                    ):
    sort_column = getattr(Answer, sort_by)
    if desc:
        sort_column = sort_column.desc()
    else:
        sort_column = sort_column.asc()
    _answer_list = db.query(Answer).filter(Answer.question_id == question_id)\
            .order_by(sort_column)
    total = _answer_list.count()
    answer_list = _answer_list.offset(skip).limit(limit).all()
    return total, answer_list
    
