from pydantic import BaseModel
from pydantic_core.core_schema import FieldValidationInfo


class Category(BaseModel):
    id: int
    subject: str

