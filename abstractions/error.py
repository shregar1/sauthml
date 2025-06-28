from config import logger


class IError(BaseException):

    def __init__(self, urn: str = None) -> None:
        self.urn = urn
        self.logger = logger
