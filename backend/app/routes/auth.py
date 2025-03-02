from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import db_dependency
from ..schemas import (
    UserCreate,
    UserLogin,
    EmailAlreadyRegistered,
    UsernameAlreadyRegistered,
    TokenResponse, 
    RefreshTokenRequest,
    AuthenticationError,
    TokenRefreshError
)
from ..services.auth import (
    register_user_service,
    login_user_service,
    refresh_tokens_service,
    logout_user_service
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post(
    "/register",
    response_model=TokenResponse,
    description="Creates a new user account and returns access and refresh tokens."
)
def register_user(user_create: UserCreate, db: Session = Depends(db_dependency)):
    try:
        tokens = register_user_service(user_create=user_create, db=db)
    except (EmailAlreadyRegistered, UsernameAlreadyRegistered) as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return tokens

@router.post(
    "/login",
    response_model=TokenResponse,
    description="Authenticates a user and returns new access and refresh tokens."
)
def login_user(user_login: UserLogin, db: Session = Depends(db_dependency)):
    try:
        tokens = login_user_service(user_login, db)
    except AuthenticationError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return tokens

@router.post(
    "/refresh",
    response_model=TokenResponse,
    description="Refreshes tokens using a valid refresh token."
)
def refresh_tokens(token_request: RefreshTokenRequest, db: Session = Depends(db_dependency)):
    try:
        tokens = refresh_tokens_service(token_request.refresh_token, db)
    except TokenRefreshError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return tokens

@router.post(
    "/logout",
    description="Logs out the user."
)
def logout_user(db: Session = Depends(db_dependency)):
    try:
        logout_user_service(db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return {"message": "Successfully logged out"}
