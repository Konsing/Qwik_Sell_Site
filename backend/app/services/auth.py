from sqlalchemy.orm import Session
from ..schemas import UserCreate, UserLogin, TokenResponse

def register_user_service(user_create: UserCreate, db: Session) -> TokenResponse:
    """
    Registers a new user, then creates and returns access and refresh tokens.
    Raises EmailAlreadyRegistered or UsernameAlreadyRegistered if conflicts occur.
    """
    pass

def login_user_service(user_login: UserLogin, db: Session) -> TokenResponse:
    """
    Authenticates the user and returns new access and refresh tokens.
    Raises AuthenticationError if credentials are invalid.
    """
    pass

def refresh_tokens_service(refresh_token: str, db: Session) -> TokenResponse:
    """
    Validates the provided refresh token and returns new access and refresh tokens.
    Raises TokenRefreshError if the refresh token is invalid or expired.
    """
    pass

def logout_user_service(db: Session) -> None:
    """
    Logs out the user by invalidating tokens if necessary.
    """
    pass