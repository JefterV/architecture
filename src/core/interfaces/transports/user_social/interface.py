# EXTERNAL IMPORTS

# NATIVE IMPORTS
from typing import Optional
from abc import abstractstaticmethod, ABC

# INTERNAL IMPORTS
from src.domain.validators.user.validator import UserSocialRequest


class IUserSocial(ABC):

    @staticmethod
    async def setup_init():
        """
        :return:
        """

    async def get_social_user_data(self, user_id: int) -> Optional[UserSocialRequest]:
        """
        :param user_id:
        :return:
        """

