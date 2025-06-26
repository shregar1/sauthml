from fastapi import Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from http import HTTPStatus
from saml2.client import Saml2Client

from abstractions.controller import IController

from constants.api_lk import APILK
from constants.api_status import APIStatus

from dependencies.saml import get_saml_service

from dtos.responses.base import BaseResponseDTO

from errors.bad_input_error import BadInputError
from errors.unexpected_response_error import UnexpectedResponseError

from services.user.login import UserLoginService

from utilities.dictionary import DictionaryUtility


class UserLoginController(IController):

    def __init__(self, urn: str = None) -> None:
        super().__init__(urn)
        self.api_name = APILK.LOGIN

    async def post(
        self,
        request: Request,
        redirect_url: str,
        saml_service: Saml2Client = Depends(get_saml_service)
    ):

        self.logger.debug("Fetching request URN")
        self.urn = request.state.urn
        self.user_id = getattr(request.state, "user_id", None)
        self.user_urn = getattr(request.state, "user_urn", None)
        self.logger = self.logger.bind(
            urn=self.urn,
            user_urn=self.user_urn,
            api_name=self.api_name
        )
        self.dictionary_utility = DictionaryUtility(urn=self.urn)

        try:

            self.logger.debug("Validating request")
            self.request_payload = {}
            self.request_payload.update({
                "user_id": self.user_id,
                "redirect_url": redirect_url
            })

            await self.validate_request(
                request_payload=self.request_payload,
                request_headers=dict(request.headers.mutablecopy())
            )
            self.logger.debug("Verified request")

            self.logger.debug("Running online user service")
            response_dto: BaseResponseDTO = await UserLoginService(
                urn=self.urn,
                user_urn=self.user_urn,
                api_name=self.api_name
            ).run(
                request=request,
                saml_service=saml_service,
                request_payload=self.request_payload
            )

            self.logger.debug("Preparing response metadata")
            http_status_code = HTTPStatus.PERMANENT_REDIRECT
            self.logger.debug("Prepared response metadata")

            response_payload: dict = response_dto.to_dict()
            return RedirectResponse(
                url=response_payload.get("url"),
                headers=response_payload.get("headers")
            )

        except (BadInputError, UnexpectedResponseError) as err:

            self.logger.error(
                f"{err.__class__} error occured while logging in user: {err}"
            )
            self.logger.debug("Preparing response metadata")
            response_dto: BaseResponseDTO = BaseResponseDTO(
                transactionUrn=self.urn,
                status=APIStatus.FAILED,
                responseMessage=err.responseMessage,
                responseKey=err.responseKey,
                data={},
                error={}
            )
            http_status_code = err.http_status_code
            self.logger.debug("Prepared response metadata")

        except Exception as err:

            self.logger.error(
                f"{err.__class__} error occured while logging in user: {err}"
            )

            self.logger.debug("Preparing response metadata")
            response_dto: BaseResponseDTO = BaseResponseDTO(
                transactionUrn=self.urn,
                status=APIStatus.FAILED,
                responseMessage="Failed to login users.",
                responseKey="error_internal_server_error",
                data={},
                error={}
            )
            http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            self.logger.debug("Prepared response metadata")

        return JSONResponse(
            content=response_dto.to_dict(),
            status_code=http_status_code
        )
