from abc import abstractstaticmethod, ABC


class IUserRouter(ABC):

    @abstractstaticmethod
    def get_router(self):
        """
        :return:
        """

    @abstractstaticmethod
    async def login(self, username: str, password: str):
        """
        :param username:
        :param password:
        :return:
        """

    @abstractstaticmethod
    async def get_socials(self, user_id: int):
        """
        :param user_id:
        :return:
        """
