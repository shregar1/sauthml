from fastapi import Request, Response, HTTPException

from abstractions.service import IService


class APISExampleService(IService):

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
        request: Request
    ) -> Response:

        if not request.session.get("saml_name_id"):
            raise HTTPException(
                status_code=401,
                detail="Unauthorized: Please log in"
            )

        return {
            "message": "This is a protected endpoint"
        }
