from pydantic import BaseModel


class AcceptApplicationRequestDTO(BaseModel):

    reference_number: str
    application_urn: str