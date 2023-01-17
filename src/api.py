# EXTERNAL IMPORTS
import uvicorn
from fastapi import FastAPI

# NATIVE IMPORTS

# INTERNAL IMPORTS
from src.routers.user.router import UserRouter
from src.infrastructures.settings.infrastructure import SettingsInfrastructure


class CreateAPP:
    def __init__(self):
        self.app = FastAPI()
        self.API_VERSION = "v1"

    def get_app(self):
        self.app.router.redirect_slashes = True
        self.app.include_router(
            UserRouter().get_router(), prefix=f"/{self.API_VERSION}/user", tags=["user"], dependencies=[]
        )

        return self.app
