# EXTERNAL IMPORTS

# NATIVE IMPORTS

# INTERNAL IMPORTS
from src.domain.enums.user.enum import UserStatusEnum
from src.domain.exceptions import UserNotFound
from src.domain.validators.user.validator import VerifyUserCredentialsModel, VerifyUserCredentialsResponseModel, \
    UserSocialRequest
from src.repositories.user.repository import UserRepository
from src.transports.user_social.transport import UserSocial
from src.core.interfaces.services.user.interface import IUserService


class UserService(IUserService):
    def __init__(self):
        self._user_repository = UserRepository
        self._user_transport = UserSocial()

    def verify_user_credentials(self, user_credentials: VerifyUserCredentialsModel) -> VerifyUserCredentialsResponseModel:
        result = self._user_repository.get_user_credentials(user_credentials)

        if result is None:
            raise UserNotFound()

        is_correct_password = result.password == user_credentials.password
        is_active = result.status == UserStatusEnum.active

        return VerifyUserCredentialsResponseModel(
            is_active=is_active,
            is_user=True,
            correct_credentials=is_correct_password,
        )

    async def verify_user_have_social_networking(self, user_id: int) -> UserSocialRequest:
        result = await self._user_transport.get_social_user_data(user_id)

        return result

