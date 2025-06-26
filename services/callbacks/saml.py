from fastapi import Request, Response
from saml2.client import Saml2Client

from abstractions.service import IService


class CallbackSAMLService(IService):

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
        pass
