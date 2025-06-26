from fastapi import Request, Response, HTTPException
from saml2.client import Saml2Client
from starlette.status import HTTP_400_BAD_REQUEST

from abstractions.service import IService


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

    def run(
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

            return {
                "url": authn_request_url,
                "headers": headers
            }

        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Unable to initiate login"
        )
