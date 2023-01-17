# EXTERNAL IMPORTS

# NATIVE IMPORTS
from abc import  abstractstaticmethod, ABC

# INTERNAL IMPORTS
from src.domain.validators.user.validator import VerifyUserCredentialsModel, VerifyUserCredentialsResponseModel, \
    UserSocialRequest


class IUserService(ABC):

    @abstractstaticmethod
    def verify_user_credentials(self, user_credentials: VerifyUserCredentialsModel) -> VerifyUserCredentialsResponseModel:
        """
        :param user_credentials:
        :return:
        """

    @abstractstaticmethod
    async def verify_user_have_social_networking(self, user_id: int) -> UserSocialRequest:
        """
        :param user_id:
        :return:
        """

