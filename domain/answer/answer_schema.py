import datetime

from pydantic import BaseModel, field_validator
from domain.user.user_schema import User
from typing import Optional


class AnswerCreate(BaseModel):
    content: str

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: Optional[User] = None
    question_id: int
    modify_date: Optional[datetime.datetime] = None
    voter: list[User] = []
#    voter_count: int = 0

    class Config:
        orm_mode = True

class AnswerList(BaseModel):
    total: int = 0
    answer_list: list[Answer]= []


class AnswerUpdate(AnswerCreate):
    answer_id: int


class AnswerDelete(BaseModel):
    answer_id: int


class AnswerVote(BaseModel):
    answer_id: int
