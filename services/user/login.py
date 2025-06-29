from fastapi import Request, Response, HTTPException
from http import HTTPStatus
from saml2.client import Saml2Client

from abstractions.service import IService

from constants.api_status import APIStatus

from dtos.responses.base import BaseResponseDTO


class UserLoginService(IService):

    def __init__(
        self,
        urn: str = None,
        user_urn: str = None,
        api_name: str = None
    ) -> None:

        super().__init__(urn, user_urn, api_name)
        self.urn = urn
        self.user_urn = user_urn
        self.api_name = api_name

    async def run(
        self,
        request: Request,
        saml_service: Saml2Client,
        request_payload: dict
    ) -> Response:

        authn_request_url = saml_service.prepare_for_authenticate(
            redirect_url=request_payload.get("redirect_url")
        )[1]["headers"][0][1]

        if authn_request_url:

            headers = {
                "Cache-Control": "no-cache, no-store",
                "Pragma": "no-cache"
            }

            return BaseResponseDTO(
                transactionUrn=self.urn,
                status=APIStatus.SUCCESS,
                responseMessage="User login successful",
                responseKey="success_user_login",
                data={
                    "url": authn_request_url,
                    "headers": headers
                },
                error={}
            )

        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Unable to initiate login"
        )
