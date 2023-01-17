from src.core.interfaces.infrastructures.http_client.interface import IHTTPClientInfrastructure
from aiohttp import ClientSession


class HTTPClientInfrastructure(IHTTPClientInfrastructure):
    session = None

    @classmethod
    async def get_session(cls) -> ClientSession:
        if cls.session is None:
            cls.session = ClientSession()

        return cls.session

    @classmethod
    async def restart_session(cls):
        cls.session = None

    @classmethod
    async def close_session(cls):
        cls.session.close()
