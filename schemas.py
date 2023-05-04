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
    
class OrderModel(BaseModel):
    id : Optional[str]
    quantity : int
    order_status : Optional[str]="PENDING"
    pizza_size : Optional[str]="SMALL"
    user_id :Optional [int]
    
    
    class Config:
        orm_model=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }
    