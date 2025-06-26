from pydantic import BaseModel


class FetchMessagesRequestDTO(BaseModel):

    reference_number: str
    chat_urn: str