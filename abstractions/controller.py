from abc import ABC

from config import logger

from utilities.dictionary import DictionaryUtility


class IController(ABC):

    def __init__(
        self,
        urn: str = None,
        user_urn: str = None,
        api_name: str = None
    ) -> None:

        super().__init__()
        self.urn = urn
        self.user_urn = user_urn
        self.api_name = api_name
        self.logger = logger.bind(urn=self.urn)
        self.dictionary_utility = DictionaryUtility(urn=self.urn)

    async def validate_request(
        self,
        request_payload: dict,
        request_headers: dict,
    ):
        return
