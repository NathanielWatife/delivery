from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id : Optional[int]
    username : str
    email : str
    password : str
    is_staff :Optional[bool]
    is_active : Optional[bool]
    
    
    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                "username":"john wick",
                "email":"johnwick@gmail.com",
                "password":"password",
                "is_staff": False,
                "is_active": True
            }
        }
        
        
        
class Settings(BaseModel):
    authjwt_secret_key: str='2f90394c4ab791dc774b9bd80fd7d8c65a1ae43a026d97b5d41e522219a55256'

class LoginModel(BaseModel):
    username:str
    password:str