from fastapi import APIRouter
from http import HTTPMethod

from constants.api_lk import APILK

from config import logger

from controllers.apis.example import APISExampleController
from controllers.apis.profile import APISProfileController


router = APIRouter(prefix="/api")

logger.debug(f"Registering {APISExampleController.__name__} route.")
router.add_api_route(
    path="/example",
    endpoint=APISExampleController().get,
    methods=[HTTPMethod.GET.value],
    name=APILK.EXAMPLE
)
logger.debug(f"Registered {APISExampleController.__name__} route.")

logger.debug(f"Registering {APISProfileController.__name__} route.")
router.add_api_route(
    path="/profile",
    endpoint=APISProfileController().get,
    methods=[HTTPMethod.GET.value],
    name=APILK.PROFILE
)
logger.debug(f"Registered {APISProfileController.__name__} route.")