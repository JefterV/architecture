# EXTERNAL IMPORTS
from pydantic import BaseSettings, Field

# NATIVE IMPORTS

# INTERNAL IMPORTS


class SettingsInfrastructure(BaseSettings):
    _settings = None
    MONGO_DATABASE_URL: str = Field(env="MONGO_DATABASE_URL", default=None)
    MONGO_USER_LOGIN_DATABASE: str = Field(env="MONGO_USER_LOGIN_DATABASE", default=None)
    MONGO_USER_LOGIN_COLLECTION: str = Field(env="MONGO_USER_LOGIN_DATABASE", default=None)
    USER_SOCIAL_BASE_URL: str = Field(env="USER_SOCIAL_BASE_URL", default=None)
    ENVIRONMENT: str = Field(env="USER_SOCIAL_BASE_URL", default="prd")

    @classmethod
    def get_settings(cls):
        if cls._settings is None:
            cls._settings = SettingsInfrastructure()

        return cls._settings



