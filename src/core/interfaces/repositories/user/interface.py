# EXTERNAL IMPORTS

# NATIVE IMPORTS
from abc import abstractstaticmethod, ABC
# INTERNAL IMPORTS
from src.domain.validators.user.validator import VerifyUserCredentialsModel, GetUserResponseModel


class IUserRepository(ABC):
    settings = None
    database = None
    collection = None

    @classmethod
    def get_user_credentials(cls, user_credentials: VerifyUserCredentialsModel) -> GetUserResponseModel:
        """
        :param user_credentials:
        :return:
        """

    @classmethod
    def insert_new_user(cls, user_id: int) -> GetUserResponseModel:
        """
        :param user_id:
        :return:
        """
