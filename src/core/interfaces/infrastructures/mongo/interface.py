# EXTERNAL IMPORTS

# NATIVE IMPORTS
from abc import abstractstaticmethod, ABC

# INTERNAL IMPORTS


class IMongoDBInfrastructure(ABC):
    client = None
    settings = None

    @classmethod
    @abstractstaticmethod
    def get_client(cls):
        """
        :return:
        """

    @classmethod
    @abstractstaticmethod
    def restart_client(cls):
        """
        :return:
        """
    @classmethod
    @abstractstaticmethod
    def close_connection(cls):
        """
        :return:
        """
