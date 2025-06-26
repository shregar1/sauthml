from pydantic import BaseModel


class FetchNotificationRequestDTO(BaseModel):

    reference_number: str
    user_urn: str