from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from domain.answer.answer_schema import AnswerCreate, AnswerUpdate
from domain.comment.comment_schema import CommentCreate, CommentUpdate
from models import Question, Answer, User, Comment


def create_comment_question(db: Session, question: Question,
                  comment_create: CommentCreate, user: User):
    db_comment = Comment(question=question,
                       content=comment_create.content,
                       create_date=datetime.now(),
                       user=user
                       )
    db.add(db_comment)
    db.commit()


def create_comment_answer(db: Session, answer: Answer,
                  comment_create: CommentCreate, user: User):
    db_comment = Comment(answer=answer,
                       content=comment_create.content,
                       create_date=datetime.now(),
                       user=user
                       )
    db.add(db_comment)
    db.commit()


def get_comment(db: Session, comment_id: int):
    return db.query(Comment).get(comment_id)


def update_comment(db: Session, db_comment: Comment,
                  comment_update: CommentUpdate):
    db_comment.content = comment_update.content
    db_comment.modify_date = datetime.now()
    db.add(db_comment)
    db.commit()


def delete_comment(db: Session, db_comment: Comment):
    db.delete(db_comment)
    db.commit()
