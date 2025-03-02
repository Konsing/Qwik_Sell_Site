# schemas/token.py
from .base import BaseModel, Field

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str

# Error response models from token-related operations
class AuthenticationError(BaseModel):
    message: str = "Authentication failed"

class TokenRefreshError(BaseModel):
    message: str = "Token refresh failed"
