import traceback

from fastapi import Request, Response, HTTPException
from http import HTTPStatus
from saml2.client import Saml2Client

from abstractions.service import IService

from constants.api_status import APIStatus

from dtos.responses.base import BaseResponseDTO


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

    async def run(
        self,
        request: Request,
        saml_service: Saml2Client = None
    ) -> Response:

        saml_name_id = request.session.get("saml_name_id")
        self.logger.debug(f"SAML Name ID from session: {saml_name_id}")

        if not saml_name_id:

            self.logger.warning(
                "No active SAML session found, but proceeding with logout."
            )

        try:

            self.logger.debug("Performing local application logout...")

            # Clear all session data for local logout only
            self.logger.debug("Clearing local user session data.")
            request.session.pop("saml_attributes", None)
            request.session.pop("saml_name_id", None)
            request.session.pop("user_info", None)

            # Clear any other application-specific session data
            session_keys_to_clear = [
                "access_token",
                "refresh_token",
                "user_roles",
                "permissions",
                "last_activity"
            ]

            for key in session_keys_to_clear:
                request.session.pop(key, None)

            request.session.clear()

            self.logger.debug(
                "Local application logout completed successfully."
            )

            return BaseResponseDTO(
                transactionUrn=self.urn,
                status=APIStatus.SUCCESS,
                responseMessage="Successfully logged out from application",
                responseKey="success_user_logout",
                data={
                    "message": "logout successfully"
                },
                error={}
            )

        except Exception as e:

            self.logger.error(f"Error during local logout: {e}", exc_info=True)
            self.logger.error(traceback.format_exc())

            try:
                request.session.clear()
                self.logger.debug("Session cleared despite error.")
            except Exception as session_error:
                self.logger.error(f"Error clearing session: {session_error}")

            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=(
                    f"Local logout failed due to an unexpected error: {str(e)}"
                )
            )
