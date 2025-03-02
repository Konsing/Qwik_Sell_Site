import uuid
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..config.database import Base
from sqlalchemy.dialects.postgresql import UUID

class Cart(Base):
    __tablename__ = 'cart'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey('products.id', ondelete='CASCADE'),
        nullable=False
    )
    quantity = Column(Integer, nullable=False, default=1)
    
    user = relationship("User", back_populates="cart_items")
    product = relationship("Product")
