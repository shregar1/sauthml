from fastapi import APIRouter
from http import HTTPMethod

from constants.api_lk import APILK

from config import logger

from controllers.user.login import UserLoginController
from controllers.user.logout import UserLogoutController

router = APIRouter(prefix="/user/")

logger.debug(f"Registering {UserLoginController.__name__} route.")
router.add_api_route(
    path="/login",
    endpoint=UserLoginController().post,
    methods=[HTTPMethod.POST.value],
    name=APILK.EXAMPLE
)
logger.debug(f"Registered {UserLoginController.__name__} route.")

logger.debug(f"Registering {UserLogoutController.__name__} route.")
router.add_api_route(
    path="/logout",
    endpoint=UserLogoutController().post,
    methods=[HTTPMethod.POST.value],
    name=APILK.EXAMPLE
)
logger.debug(f"Registered {UserLogoutController.__name__} route.")