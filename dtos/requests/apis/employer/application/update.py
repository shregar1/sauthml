from pydantic import BaseModel


class UpdateApplicationProgressRequestDTO(BaseModel):

    reference_number: str
    application_urn: str
    stage: str