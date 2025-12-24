from pydantic import BaseModel,Field
from typing import Annotated
class Student(BaseModel):
    cgpa:Annotated[float,Field(...,title="cgpa of the student",example="7.5")]
    iq:Annotated[int,Field(...,title="iq of the student",)]