from pydantic import BaseModel


class EmployeeReviewedApplicationRequestDTO(BaseModel):

    reference_number: str
    application_urn: str