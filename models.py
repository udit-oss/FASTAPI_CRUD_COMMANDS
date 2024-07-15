# We will be using pydantic library to perform data validation.
# We can declare the shape of our data as classes with attributes
from enum import Enum # Importing Enum for gender and role definitions
from pydantic import BaseModel # type: ignore (Importing BaseModel for data validation)
from uuid import UUID, uuid4
from typing import Optional, List


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel): # User Model: Represents a user with attributes
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel): # User Update Model: Represents data structure for updating a user's attributes 
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
