from pydantic import BaseModel


class FetchChatsRequestDTO(BaseModel):

    reference_number: str
    user_urn: str