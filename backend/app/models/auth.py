# models/auth.py
import uuid
import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.database import Base
from sqlalchemy.dialects.postgresql import UUID

class AuthToken(Base):
    __tablename__ = 'auth_tokens'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    # Access token fields
    access_token = Column(String, unique=True, nullable=False)
    access_expires_at = Column(
        DateTime(timezone=True),
        nullable=False
    )
    
    # Refresh token fields
    refresh_token = Column(String, unique=True, nullable=False)
    refresh_expires_at = Column(
        DateTime(timezone=True),
        nullable=False
    )
    
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    
    user = relationship("User", back_populates="auth_tokens")
