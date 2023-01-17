# EXTERNAL IMPORTS


# NATIVE IMPORTS
from abc import abstractstaticmethod, ABC

# INTERNAL IMPORTS


class IMongoBaseRepository(ABC):
    infra = None
    database = None
    collection = None

    @classmethod
    @abstractstaticmethod
    def _get_collection(cls):
        """
        :return:
        """

    @classmethod
    @abstractstaticmethod
    def find_one(cls, *, query: dict, project: dict = None):
        """
        :param query:
        :param project:
        :return:
        """

    @classmethod
    @abstractstaticmethod
    def update_one(cls, *, query: dict, project: dict = None):
        """
        :param query:
        :param project:
        :return:
        """

    @classmethod
    @abstractstaticmethod
    def insert_one(cls, *, payload: dict):
        """
        :param payload:
        :return:
        """

