# EXTERNAL IMPORTS
from motor.motor_asyncio import AsyncIOMotorClient

# NATIVE IMPORTS

# INTERNAL IMPORTS
from src.infrastructures.settings.infrastructure import SettingsInfrastructure
from src.core.interfaces.infrastructures.mongo.interface import IMongoDBInfrastructure


class MongoDBInfrastructure(IMongoDBInfrastructure):
    client = None
    settings = SettingsInfrastructure().get_settings()

    @classmethod
    def get_client(cls):
        url = cls.settings.MONGO_DATABASE_URL
        if cls.client is None:
            cls.client = AsyncIOMotorClient(url)

        return cls.client

    @classmethod
    def restart_client(cls):
        cls.client = None

    @classmethod
    def close_connection(cls):
        if cls.client is not None:
            cls.client.close()
