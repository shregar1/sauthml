from fastapi import Request, Response, HTTPException
from http import HTTPStatus

from abstractions.service import IService


class APISProfileService(IService):

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

        user_info = request.session.get("user_info")
        if not user_info:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="User not logged in"
            )

        return user_info
