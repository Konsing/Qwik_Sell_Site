# schemas/user.py
from .base import BaseModel, ConfigDict, EmailStr, Field, UUID, datetime

# Base model containing common user attributes
class UserBase(BaseModel):
    username: str = Field(..., min_length=5, max_length=18)

    model_config = ConfigDict(from_attributes=True)

# Model for user creation (sign-up)
class UserCreate(UserBase):
    email: EmailStr
    password: str = Field(..., min_length=8)

    model_config = ConfigDict(from_attributes=True)

# Model for user login
class UserLogin(UserCreate):
    pass

# Model representing the user data stored in the database
class UserDB(UserCreate):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Public model for exposing user information without sensitive data
class UserPublic(UserBase):
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Private model for authenticated user details
class UserPrivate(UserPublic):
    id: UUID
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

#
# These models are for error responses raised from your service layer.
#
class EmailAlreadyRegistered(Exception):
    def __init__(self):
        self.message = "Email is already registered"
        super().__init__(self.message)

class UsernameAlreadyRegistered(Exception):
    def __init__(self):
        self.message = "Username is already registered"
        super().__init__(self.message)

class UserNotFound(Exception):
    def __init__(self):
        self.message = "User not found"
        super().__init__(self.message)