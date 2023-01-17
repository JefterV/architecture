# EXTERNAL IMPORTS

# NATIVE IMPORTS

# INTERNAL IMPORTS
from typing import Optional

from src.domain.exceptions import UserNotFound
from src.domain.validators.user.validator import UserSocialRequest
from src.infrastructures.settings.infrastructure import SettingsInfrastructure
from src.infrastructures.http_client.infrastructure import HTTPClientInfrastructure
from src.core.interfaces.transports.user_social.interface import IUserSocial


class UserSocial(IUserSocial):
    def __init__(self):
        self.settings = SettingsInfrastructure.get_settings()
        self.user_social_base_url = self.settings.USER_SOCIAL_BASE_URL

    @staticmethod
    async def setup_init():
        return await HTTPClientInfrastructure.get_session()

    async def get_social_user_data(self, user_id: int) -> Optional[UserSocialRequest]:
        session = await self.setup_init()
        params = {"user_id": user_id}

        response = await session.get(
            self.user_social_base_url,
            params=params
        )
        if response.status == 404:
            raise UserNotFound()

        response_to_json = await response.json()
        return UserSocialRequest(**response_to_json)

