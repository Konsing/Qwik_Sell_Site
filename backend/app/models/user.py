import uuid
import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from ..config.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import EmailType

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(EmailType, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    
    orders = relationship("Order", back_populates="user", cascade="all, delete")
    products = relationship("Product", back_populates="user", cascade="all, delete")
    cart_items = relationship("Cart", back_populates="user", cascade="all, delete")
    auth_tokens = relationship("AuthToken", back_populates="user", cascade="all, delete")
