from pydantic import BaseModel


class EmployerHireApplicationRequestDTO(BaseModel):

    reference_number: str
    application_urn: str