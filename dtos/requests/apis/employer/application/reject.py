from pydantic import BaseModel


class RejectApplicationRequestDTO(BaseModel):

    reference_number: str
    application_urn: str