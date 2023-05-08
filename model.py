from pydantic import BaseModel, HttpUrl, EmailStr
from typing import Union
from enum import Enum



    
class Roll(str, Enum):
    student ="student"
    educator="educator"
    administrator="administratior"
    staff="staff"
    temp="temp"

    
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

    
class User(BaseModel):
    roll: Roll
    name: str
    user_id: int

        
class Image(BaseModel):
    url: str
    name: str    

    
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    is_offer: Union[bool, None] = None
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None
        
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None
    
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
   
class Uzer(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    
class New_UZer(Uzer):
    password: str
    
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}] 

