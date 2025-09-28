from pydantic import BaseModel , EmailStr
from uuid import UUID
from datetime import datetime
from enum import Enum



class UserSchema(BaseModel):
    email : EmailStr
    password : str


class UserLoginSchemaResponse(BaseModel):
    id : UUID
    email : EmailStr
    created_at : datetime
    status : Enum
    access_token : str
    refresh_token : str

    class Config():
        orm_mode= True

class UserRegisterSchemaResponse(BaseModel):
    id : UUID
    email : EmailStr
    created_at : datetime
    status : Enum
   

    class Config():
        orm_mode= True

   

class hash_password(BaseModel):
    password :str   