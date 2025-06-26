import os
import sys

from dotenv import load_dotenv
from loguru import logger

from configurations.azure import AzureConfiguration, AzureConfigurationDTO


logger.remove(0)
logger.add(
    sys.stderr,
    colorize=True,
    format="<green>{time:MMMM-D-YYYY}</green> | \
            <black>{time:HH:mm:ss}</black> | \
            <level>{level}</level> | \
            <cyan>{message}</cyan> | \
            <magenta>{name}:{function}:{line}</magenta> | \
            <yellow>{extra}</yellow>"
)

# Load environment variables from .env file
load_dotenv()

logger.info("Loading Configurations")
azure_configuration: AzureConfigurationDTO = AzureConfiguration().get_config()
logger.info("Loaded Configurations")

# Access environment variables
logger.info("Loading environment variables")
APP_NAME: str = os.environ.get('APP_NAME')
SECRET_KEY: str = os.getenv("SECRET_KEY")
ALGORITHM: str = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        1440
    )
)
BASE_URL: str = os.getenv("BASE_URL")
logger.info("Loaded environment variables")

unprotected_routes: set = {
    "/health",
    "/login"
}

common_routes: set = {
}

callback_routes: set = {
}
