from pydantic import BaseModel


class CreateMessageRequestDTO(BaseModel):

    reference_number: str
    chat_urn: str
    sender_urn: str
    message: str