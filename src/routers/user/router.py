from typing import Optional, Union

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from starlette import status

from src.controllers.user.controller import UserController
from src.domain.validators.user.validator import VerifyUserCredentialsResponseModel, VerifyUserCredentialsModel
from src.core.interfaces.routers.user.interface import IUserRouter
router = InferringRouter()


@cbv(router)
class UserRouter(IUserRouter):
    def __init__(self):
        self._user_controller = UserController()

    def get_router(self):
        return router

    @router.get("/login", response_model=VerifyUserCredentialsResponseModel, status_code=Union[status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])
    async def login(self, username: str, password: str):
        user_credential = VerifyUserCredentialsModel(username=username,
                                                     password=password)
        result = await self._user_controller.login_user(user_credentials=user_credential)

        return result

    @router.get("/login", response_model=VerifyUserCredentialsResponseModel, status_code=Union[status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])
    async def get_socials(self, user_id: int):
        result = await self._user_controller.verify_user_have_social_networking(user_id=user_id)

        return result
