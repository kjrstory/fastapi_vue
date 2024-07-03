import datetime

from pydantic import BaseModel, field_validator, validator
from domain.user.user_schema import User
from typing import Optional


class CommentCreate(BaseModel):
    content: str

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Comment(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: Optional[User] = None
    question_id: Optional[int] = None
    answer_id: Optional[int] = None
    modify_date: Optional[datetime.datetime] = None

#    @validator('question_id', 'answer_id', pre=True)
#    def check_question_or_answer(cls, v, values):
#        if values.get('question_id') is None and values.get('answer_id') is None:
#            raise ValueError('question_id 또는 answer_id 중 하나는 필수입니다.')
#        if values.get('question_id') is not None and values.get('answer_id') is not None:
#            raise ValueError('question_id와 answer_id 중 하나만 사용할 수 있습니다.')
#        return v

    class Config:
        orm_mode = True


class CommentList(BaseModel):
    total: int = 0
    comment_list: list[Comment]= []


class CommentUpdate(CommentCreate):
    comment_id: int


class CommentDelete(BaseModel):
    comment_id: int
