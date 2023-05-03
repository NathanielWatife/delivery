from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType




class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    
class Order(Base):
    ORDER_STATUS = (
        ("PENDING", "pending"),
        ("IN-TRANSIT", "int-transit"),
        ("DELIVERED", "delivered")
        
    )
    
    PIZZA_SIZES = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large"),
        ("EXTRA-LARGE", "extra-large")
    )
    
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default="SMALL")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')
    
    
    def __repr__(self):
        return f"< Order {self.id}>"
