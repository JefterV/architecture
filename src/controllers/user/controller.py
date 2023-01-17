# EXTERNAL IMPORTS
from fastapi import status

# NATIVE IMPORTS
from typing import Union

# INTERNAL IMPORTS
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from src.domain.exceptions import UserNotFound, InvalidMongoConnection
from src.domain.validators.user.validator import VerifyUserCredentialsModel, VerifyUserCredentialsResponseModel
from src.services.user.service import UserService
from src.utils import generate_error_response
from src.core.interfaces.controllers.user.interface import IUserController


class UserController(IUserController):
    def __init__(self):
        self.user_service = UserService()

    async def login_user(self, user_credentials: VerifyUserCredentialsModel) -> Union[VerifyUserCredentialsResponseModel,
                                                                                      generate_error_response]:
        try:
            result = self.user_service.verify_user_credentials(user_credentials=user_credentials)

            if result.correct_credentials:
                return JSONResponse(jsonable_encoder(result), status_code=status.HTTP_200_OK)

            return JSONResponse(jsonable_encoder(result), status_code=status.HTTP_401_UNAUTHORIZED)

        except UserNotFound:
            # log
            return generate_error_response(
                status=status.HTTP_404_NOT_FOUND,
                message=f"Não foi possivel encontrar o usuario: {user_credentials.username}",
                title="Usuario não encontrado",
            )

        except InvalidMongoConnection:
            # log
            return generate_error_response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Não foi possivel logar o usuario, tente novamnete mais tarde.",
                title="Não foi possivel logar o usuario.",
            )

        except Exception as ex:
            # log
            return generate_error_response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Não foi possivel logar o usuario, tente novamnete mais tarde.",
                title="Não foi possivel logar o usuario.",
            )

    async def verify_user_have_social_networking(self, user_id: int):
        try:
            result = await self.user_service.verify_user_have_social_networking(user_id)

            return JSONResponse(jsonable_encoder(result), status_code=status.HTTP_200_OK)

        except UserNotFound:
            # log
            return generate_error_response(
                status=status.HTTP_404_NOT_FOUND,
                message=f"Não foi possivel encontrar o usuario: {user_id}",
                title="Usuario não encontrado",
            )

        except Exception as ex:
            # log
            return generate_error_response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Não foi possivel logar o usuario, tente novamnete mais tarde.",
                title="Não foi possivel logar o usuario.",
            )