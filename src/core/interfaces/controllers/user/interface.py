from abc import abstractstaticmethod, ABC
from typing import Union

from src.domain.validators.user.validator import VerifyUserCredentialsModel, VerifyUserCredentialsResponseModel
from src.utils import generate_error_response


class IUserController(ABC):
    @abstractstaticmethod
    async def login_user(self, user_credentials: VerifyUserCredentialsModel) -> Union[VerifyUserCredentialsResponseModel,
                                                                                      generate_error_response]:
        """
        :param user_credentials: VerifyUserCredentialsModel
        :return: VerifyUserCredentialsResponseModel or generate_error_response if error
        """

    @abstractstaticmethod
    async def verify_user_have_social_networking(self, user_id: int):
        """
        :param user_id: int
        :return:
        """