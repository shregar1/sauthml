from pydantic import BaseModel


class CreateChatRequestDTO(BaseModel):

    reference_number: str
    sender_urn: str
    receiver_urn: str