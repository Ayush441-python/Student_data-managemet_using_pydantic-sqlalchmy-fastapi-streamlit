from pydantic import BaseModel, EmailStr
from typing import Literal


class StudentCreate(BaseModel):
    roll_no = int 
    name = str
    email = EmailStr
    branch = Literal["CSE", "IT", "ECE", "EE", "Mech", "Civil"]

