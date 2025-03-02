from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from .schemas import UserPrivate
from .config.database import get_db
from .config.token import get_current_user

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[UserPrivate, Depends(get_current_user)]