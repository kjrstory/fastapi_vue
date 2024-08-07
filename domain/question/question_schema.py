import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer
from domain.comment.comment_schema import Comment
from domain.user.user_schema import User
from domain.category.category_schema import Category
from typing import Optional

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
    comments: list[Comment] = []
    user: Optional[User] = None
    modify_date: Optional[datetime.datetime] = None
    voter: list[User] = []
    category: Category

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    subject: str
    content: str
    category_id: int

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []


class QuestionUpdate(QuestionCreate):
    question_id: int


class QuestionDelete(BaseModel):
    question_id: int


class QuestionVote(BaseModel):
    question_id: int    
