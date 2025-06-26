from pydantic import BaseModel


class UpdateJobApplicationStatusRequestDTO(BaseModel):

    reference_number: str
    application_urn: str
    stage: str
    status: str