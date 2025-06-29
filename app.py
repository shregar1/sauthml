import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.middleware.sessions import SessionMiddleware

from controllers.apis import router as APISRouter
from controllers.callbacks import router as CallbackRouter
from controllers.user import router as UserRouter

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

logger.info("Initialising routers")
# APIS ROUTER
app.include_router(APISRouter)
# CALLBACK ROUTER
app.include_router(CallbackRouter)
# USER ROUTER
app.include_router(UserRouter)
logger.info("Initialised routers")


if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)
