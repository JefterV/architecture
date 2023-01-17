from abc import abstractstaticmethod, ABC
from aiohttp import ClientSession


class IHTTPClientInfrastructure(ABC):
    session = None

    @classmethod
    @abstractstaticmethod
    async def get_session(cls) -> ClientSession:
        """
        :return:
        """

    @classmethod
    @abstractstaticmethod
    async def restart_session(cls):
        """
        :return:
        """

    @classmethod
    @abstractstaticmethod
    async def close_session(cls):
        """
        :return:
        """
