from pydantic import BaseModel


class EmployeeRecommendApplicationRequestDTO(BaseModel):

    reference_number: str
    application_urn: str