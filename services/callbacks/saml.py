import base64

from http import HTTPStatus

from fastapi import Request, Response, HTTPException
from saml2 import BINDING_HTTP_POST
from saml2.client import Saml2Client

from abstractions.service import IService

from dtos.responses.base import BaseResponseDTO


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

    async def run(
        self,
        request: Request,
        saml_service: Saml2Client
    ) -> Response:

        form_data = await request.form()
        saml_response_data = form_data.get("SAMLResponse")

        if not saml_response_data:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, 
                detail="SAML Response not found"
            )

        # Process SAML response
        authn_response = saml_service.parse_authn_request_response(
            saml_response_data, BINDING_HTTP_POST
        )
        # Extract user attributes
        user_attributes = authn_response.ava
        
        # Handle name_id properly - convert to string for JSON serialization
        try:
            if hasattr(authn_response.name_id, 'text'):
                user_name_id = str(authn_response.name_id.text)
            else:
                # Fallback to string conversion
                user_name_id = str(authn_response.name_id)
        except Exception as e:
            self.logger.error(f"Error processing name_id: {e}")
            # Use a safe fallback
            user_name_id = str(authn_response.name_id)

        # Store user info in session (using Starlette session middleware)
        request.session["saml_attributes"] = user_attributes
        request.session["saml_name_id"] = user_name_id
        request.session["user_info"] = {
            "name": user_attributes.get("displayname", ["Unknown"])[0],
            "email": user_attributes.get("emailaddress", ["Unknown"])[0],
            "userUrn": user_attributes.get("userurn", ["Unknown"])[0]
        }

        return_path = "/api/profile"
        if form_data.get("RelayState"):
            return_path = base64.b64decode(
                s=form_data.get("RelayState")
            ).decode("utf-8")

        return BaseResponseDTO(
            transactionUrn=self.urn,
            status=HTTPStatus.OK,
            responseMessage="User login successful",
            responseKey="success_user_login",
            data={
                "return_path": return_path
            },
            error={}
        )
