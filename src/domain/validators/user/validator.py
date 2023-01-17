# EXTERNAL IMPORTS
from pydantic import BaseModel

# NATIVE IMPORTS
from datetime import datetime

# INTERNAL IMPORTS
from src.domain.enums.user.enum import UserStatusEnum


class VerifyUserCredentialsModel(BaseModel):
    username: str
    password: str


class VerifyUserCredentialsResponseModel(BaseModel):
    is_user: bool
    is_active: bool
    correct_credentials: bool


class GetUserResponseModel(BaseModel):
    id: int
    username: str
    password: str
    status: UserStatusEnum
    created_at: datetime


class UserSocialRequest(BaseModel):
    facebook: bool
    instagram: bool
    whatsapp: bool
