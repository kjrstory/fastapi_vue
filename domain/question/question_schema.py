import datetime

from pydantic import BaseModel

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
