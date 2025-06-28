from fastapi import APIRouter
from http import HTTPMethod

from constants.api_lk import APILK

from config import logger

from controllers.callbacks.saml import CallbackSAMLController

router = APIRouter(prefix="/callback")

logger.debug(f"Registering {CallbackSAMLController.__name__} route.")
router.add_api_route(
    path="/saml",
    endpoint=CallbackSAMLController().post,
    methods=[HTTPMethod.POST.value],
    name=APILK.CALLBACK_SAML
)
logger.debug(f"Registered {CallbackSAMLController.__name__} route.")