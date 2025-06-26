from pydantic import BaseModel


class EmployeeCandidateFetchJobApplicationRequestDTO(BaseModel):

    reference_number: str
    job_urn: str
    offset: int