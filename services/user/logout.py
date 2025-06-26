from fastapi import Request, Response, HTTPException
from saml2.client import Saml2Client
from starlette.status import HTTP_205_RESET_CONTENT, HTTP_400_BAD_REQUEST

from abstractions.service import IService


class UserLogoutService(IService):

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

    def run(self, request: Request, saml_service: Saml2Client) -> Response:

        saml_name_id = request.session.get("saml_name_id")
        if saml_service.logout(saml_name_id):
            request.session.pop("saml_attributes", None)
            request.session.pop("saml_name_id", None)
            request.session.pop("user_info", None)
            return Response(status_code=HTTP_205_RESET_CONTENT)

        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Logout failed"
        )
