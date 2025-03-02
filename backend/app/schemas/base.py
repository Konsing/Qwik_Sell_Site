# schemas/base.py
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

__all__ = ["BaseModel", "EmailStr", "Field", "ConfigDict", "Optional", "UUID", "datetime"]