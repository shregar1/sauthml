from pydantic import BaseModel


class FetchEmployerProfileRequestDTO(BaseModel):

    reference_number: str
    user_urn: str