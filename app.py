import base64
import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Request
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, Response
from loguru import logger
from saml2 import BINDING_HTTP_POST
from saml2.client import Saml2Client
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_303_SEE_OTHER,
    HTTP_205_RESET_CONTENT
)

from controllers.user import router as UserRouter
from controllers.apis import router as APISRouter

from dependencies.saml import get_saml_service

from middlewares.request_context import RequestContextMiddleware


app = FastAPI()

load_dotenv()
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
SECRET_KEY: str = os.getenv("SECRET_KEY")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):

    response_payload: dict = {
        "transactionUrn": request.state.urn,
        "responseMessage": "Bad or missing input.",
        "responseKey": "error_bad_input",
        "errors": exc.errors()
    }

    return JSONResponse(
        status_code=400,
        content=response_payload,
    )


@app.get("/health")
async def health_check():
    return {"status": "ok"}


app.add_middleware(
    middleware_class=TrustedHostMiddleware,
    allowed_hosts=["*"]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

logger.info("Initialising middleware stack")
app.add_middleware(RequestContextMiddleware)
logger.info("Initialised middleware stack")


# Login endpoint to initiate SAML authentication
@app.get("/api/login")
async def saml_login(
    redirect_url: str = None,
    saml_service: Saml2Client = Depends(get_saml_service)
):



@app.post("/api/saml/callback")
async def saml_callback(
    request: Request,
    saml_service: Saml2Client = Depends(get_saml_service)
):
    form_data = await request.form()
    saml_response_data = form_data.get("SAMLResponse")
    if not saml_response_data:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, 
            detail="SAML Response not found"
        )

    # Process SAML response
    authn_response = saml_service.parse_authn_request_response(
        saml_response_data, BINDING_HTTP_POST
    )
    user_attributes = authn_response.ava  # Extract user attributes
    user_name_id = str(authn_response.name_id)

    # Store user info in session (using Starlette session middleware)
    request.session["saml_attributes"] = user_attributes
    request.session["saml_name_id"] = user_name_id
    request.session["user_info"] = {
        "name": user_attributes.get("displayName", ["Unknown"])[0],
        "email": user_attributes.get("mail", ["Unknown"])[0],
    }

    # Redirect to the original URL (if provided) or a default page
    if form_data.get("RelayState"):
        return_path = base64.b64decode(
            s=form_data.get("RelayState")
        ).decode("utf-8")
        return RedirectResponse(return_path, status_code=HTTP_303_SEE_OTHER)
    return RedirectResponse("/api/user-info", status_code=HTTP_303_SEE_OTHER)


@app.get("/api/user-info")
async def check_user(request: Request):
    user_info = request.session.get("user_info")
    if not user_info:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User not logged in"
        )
    return user_info


@app.get("/api/logout")
async def logout_user(
    request: Request,
    saml_service: Saml2Client = Depends(get_saml_service)
):
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


@app.get("/api/example")
async def protected_endpoint(request: Request):
    if not request.session.get("saml_name_id"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized: Please log in"
        )

    return {
        "message": "This is a protected endpoint",
        "user": request.session.get("user_info")
    }

logger.info("Initialising routers")
# USER ROUTER
app.include_router(UserRouter)
# APIS ROUTER
app.include_router(APISRouter)
logger.info("Initialised routers")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
