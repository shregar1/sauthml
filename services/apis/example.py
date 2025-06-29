from fastapi import Request, Response, HTTPException
from http import HTTPStatus

from abstractions.service import IService

from constants.api_status import APIStatus

from dtos.responses.base import BaseResponseDTO


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
                status_code=HTTPStatus.unprocessable_ENTITY,
                detail="Unauthorized: Please log in"
            )

        return BaseResponseDTO(
            transactionUrn=self.urn,
            status=APIStatus.SUCCESS,
            responseMessage="Successfully fetched example",
            responseKey="success_fetch_example",
            data={
                "message": "This is a protected endpoint"
            },
            error={}
        )
