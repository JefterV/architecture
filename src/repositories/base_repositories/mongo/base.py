# EXTERNAL IMPORTS
from motor.motor_asyncio import AsyncIOMotorClient

# NATIVE IMPORTS

# INTERNAL IMPORTS
from src.domain.exceptions import InvalidMongoConnection
from src.infrastructures.mongo.infrastructure import MongoDBInfrastructure
from src.core.interfaces.repositories.base_repositories.mongo.interface import IMongoBaseRepository


class MongoBaseRepository(IMongoBaseRepository):
    infra = MongoDBInfrastructure
    database = None
    collection = None

    @classmethod
    def _get_collection(cls):
        if not (cls.database and cls.collection):
            raise InvalidMongoConnection()
        mongo_client = cls.infra.get_client()
        database = mongo_client[cls.database]
        collection = database[cls.collection]

        return collection

    @classmethod
    def find_one(cls, *, query: dict, project: dict = None):
        pass

    @classmethod
    def update_one(cls, *, query: dict, project: dict = None):
        pass

    @classmethod
    def insert_one(cls, *, payload: dict):
        pass

