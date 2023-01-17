# EXTERNAL IMPORTS

# NATIVE IMPORTS

# INTERNAL IMPORTS
from src.domain.validators.user.validator import VerifyUserCredentialsModel, GetUserResponseModel
from src.repositories.base_repositories.mongo.base import MongoBaseRepository
from src.infrastructures.settings.infrastructure import SettingsInfrastructure
from src.core.interfaces.repositories.user.interface import IUserRepository


class UserRepository(IUserRepository, MongoBaseRepository):
    settings = SettingsInfrastructure.get_settings()
    database = settings.MONGO_USER_LOGIN_DATABASE
    collection = settings.MONGO_USER_LOGIN_COLLECTION

    @classmethod
    def get_user_credentials(cls, user_credentials: VerifyUserCredentialsModel) -> GetUserResponseModel:
        query = {"username": user_credentials.username}
        result = cls.find_one(query=query)

        return result

    @classmethod
    def insert_new_user(cls, user_id: int) -> GetUserResponseModel:
        pass
